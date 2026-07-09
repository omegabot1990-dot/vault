
## ReSearch Reward Spec (Exact, Case-Covering)

---

### 1) Which text is actually validated/scored

`solution_str` is first converted to `response` via `_extract_response_text()`:

1. If `"<|im_start|>assistant\n"` exists, use everything **after the first** occurrence.
2. Else if `"Assistant:"` exists, use everything **after the first** occurrence.
3. Else use `solution_str.strip()`.

So scoring may ignore prompt/system parts if those delimiters exist.

---

### 2) Required format checks (`validate_format`)

A response is considered format-valid only if **all** pass:

- `<think>` count equals `</think>` count.
- At least one `<think>` and at least one `</think>` exist.
- Exactly one `<answer>` and exactly one `</answer>` exist.
- For each `<search>` found, the following must all exist **after it**:
	- `</search>`
	- `<result>`
	- `</result>`
- And ordering must satisfy:
	- `<search>` < `</search>` < `<result>` < `</result>`
- In the `<answer>...</answer>` span, text must contain:
	- `\boxed{`
	- and at least one `}` somewhere.

If any check fails: reward is `0.0` with reason `"bad format: ..."`.

---

### 3) EOS check (conditional)

Only if `tokenizer` is provided and has truthy `tokenizer.eos_token`:

- `response` **must end with** that EOS token.
- If not: reward `0.0`, reason `"over length"`.
- If yes: EOS token is stripped before answer extraction.

If tokenizer is `None` (or `eos_token` missing/empty), no EOS constraint is applied.

---

### 4) Ground-truth normalization

`ground_truth` is normalized as:

- If dict with key `"target"` -> use `ground_truth["target"]`.
- If resulting value is list -> cast each item to `str`.
- Else -> cast to `str`.

---

### 5) Answer extraction/parsing

- Extract substring inside `<answer>...</answer>` using regex `re.DOTALL`.
- If not found: reward `0`, reason `"cannot extract answer"` (this path is mostly unreachable if format check already passed, but still present).
- Then parse boxed answer with:
  - `last_boxed_only_string(answer_part)` to select last `\boxed...` (or `\fbox...` fallback),
  - then `remove_boxed(...)` to strip wrapper.

If boxed parsing throws exception: reward `0`, reason `"find box error: ..."`.

---

### 6) F1 scoring behavior

`get_f1_score(prediction, ground_truths)`:

- Normalization on both sides:
  - lowercase
  - remove punctuation
  - remove articles `a|an|the`
  - collapse whitespace
- For each GT candidate:
  - If prediction is one of `yes/no/noanswer` but differs from GT -> skip candidate.
  - If GT is one of `yes/no/noanswer` but differs from prediction -> skip candidate.
  - Compute token-overlap F1 if overlap > 0.
- Final F1 is max over candidates.

---

### 7) Final reward mapping

- If `f1_score > 0`: return `(float(f1_score), "correct answer, get f1 score: ...")`
- Else (format valid, parsed answer, but no overlap): return `(0.1, "wrong answer but good format: ...")`

So `0.1` is a strict format bonus for validly formatted-but-wrong answers.

---

## Practical “all-cases” table

| Case                                            | Reward |
| ----------------------------------------------- | ------ |
| Any format violation (tags/order/boxed)         | `0.0`  |
| EOS required but missing                        | `0.0`  |
| Valid format, parse failure in boxed extraction | `0`    |
| Valid format, parsed answer, F1 > 0             | `F1`   |
| Valid format, parsed answer, F1 = 0             | `0.1`  |

---

## Important edge nuances (exact implementation)

- `<think>` is **mandatory** (not optional).
- Exactly one `<answer>...</answer>` is mandatory.
- The code does **not explicitly forbid** stray `<result>` tags without a `<search>`; it only validates each discovered `<search>`.
- `answer_content` check uses the slice from `<answer>` start to `</answer>` start; it only checks presence of `\boxed{` and `}` anywhere in that span.
- `remove_boxed()` uses assertions; malformed boxed strings can raise and yield reward `0`.
- Return type is annotated as `Tuple[float, str]`, but some branches return integer `0` (Python still treats as numeric reward).