
## Progress

#### Infrastructure

- Set up the latest version of VERL for RL
- Set up scripts for training on various settings (lots of trial and error, time-consuming)
	1. Multi-GPU
		1. 4 L4 24g
		2. 2 A100 40g
	2. Single GPU
		1. A1 40g
		2. A100 80g
- [[Reward|Reward Format Original Blue Print]]

#### Experiment Zero

##### Method

1. LR
	1. `1e-6`
2. Rollout Temperature
	1. `1`
3. KL Ratio
	1. `0.001`
4. Clip Ratio
	1. `0.2`
5. [RUN 1](https://wandb.ai/gaurisankarj1996-leiden-university/research/runs/h3ga5d0w?nw=nwusergaurisankarj1996) 
	1. Max Response Length
		1. `8192`
	2. Batch Size
		1. `1`
	3. Num Rollout
		1. `5`
###### Prompt

```
You are a helpful assistant that can solve the given question step by step with the help of the wikipedia search tool. \

Given a question, you need to first think about the reasoning process in the mind and then provide the answer. \

During thinking, you can invoke the wikipedia search tool to search for fact information about specific topics if needed. \

The reasoning process and answer are enclosed within <think> </think> and <answer> </answer> tags respectively, \

and the search query and result are enclosed within <search> </search> and <result> </result> tags respectively. \

For example, <think> This is the reasoning process. </think> <search> search query here </search> <result> search result here </result> \

<think> This is the reasoning process. </think> <answer> The final answer is \\[ \\boxed{answer here} \\] </answer>. \

In the last part of the answer, the final exact answer is enclosed within \\boxed{} with latex format.
```

###### Reward

1. <mark style="background: #BBFABBA6;">Format</mark>: 0.1

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

2. <mark style="background: #FF5582A6;">F1</mark>

| Case                                            | Reward |
| ----------------------------------------------- | ------ |
| Any format violation (tags/order/boxed)         | `0.0`  |
| EOS required but missing                        | `0.0`  |
| Valid format, parse failure in boxed extraction | `0`    |
| Valid format, parsed answer, F1 > 0             | `F1`   |
| Valid format, parsed answer, F1 = 0             | `0.1`  |
##### Results

1. ![[exp_zero_advantage_mean.png]]
2. ![[exp_zero_tool_call_mean.png]]
3. ![[exp_zero_tool_call_max.png]]
4. ![[exp_zero_score_min.png]]
5. ![[exp_zero_score_mean.png]]
6. ![[exp_zero_score_max.png]]
7. ![[exp_zero_response_len_mean.png]]

##### Conclusions

1. Proved that the training setup works (April 3rd) 
2. The base model did not work as expected 
	1. Preliminary analysis of the base model showed that there was a lot of <mark style="background: #FF5582A6;">language mixing</mark>
	2. <mark style="background: #BBFABBA6;">Should circle back to it once the system is more robust for RL</mark>
3. The instruct model showed some promise
4. No reward whatsoever 

#### Experiment One

##### Method

1. LR
	1. `1e-6`
2. Rollout Temperature
	1. `1`
3. KL Ratio
	1. `0.001`
4. Clip Ratio
	1. `0.2`
5. Prompt and reward the same as experiment zero
6. [RUN 2](https://wandb.ai/gaurisankarj1996-leiden-university/research/runs/ec8wvepv?nw=nwusergaurisankarj1996)
	1. A100 40g 
	2. Batch Size 
		1. `8`
	3. Prompt Length
		1. `2048`
	4. Num Rollouts
		1. `5`
7. [RUN 3](https://wandb.ai/gaurisankarj1996-leiden-university/research/runs/wihsirif?nw=nwusergaurisankarj1996)
	1. L4 4x24g
	2. Batch Size
		1. `4`
	3. Prompt Length
		1. `1024`
	4. Num Rollouts
		1. `5`
8. [RUN 4](https://wandb.ai/gaurisankarj1996-leiden-university/research/runs/x1dsrq4x?nw=nwusergaurisankarj1996) 
	1. L4 4x24g
	2. Batch Size
		1. `4`
	3. Prompt Length
		1. `8192`
	4. Num Rollouts
		1. `5`
9. [RUN 5](https://wandb.ai/gaurisankarj1996-leiden-university/research/runs/0wx183ke?nw=nwusergaurisankarj1996) 
	1. A100 80g
	2. Batch Size
		1. `8`
	3. Prompt Length
		1. `8192`
	4. Num Rollouts
		1. `5`

##### Result

1. ![[exp_one_advantage_mean.png]]
2. ![[exp_one_score_mean.png]]
3. ![[exp_one_score_max.png]]
4. ![[exp_one_tool_call_mean.png]]
5. ![[exp_one_tool_call_max.png]]
6. ![[exp_one_response_len_mean.png]]
7. ![[exp_one_response_len_clip.png]]

##### Conclusions

1. Tool Call
	1. Observations
		1. All runs begin with substantial tool use, around roughly 0.8–1.0 mean calls
		2. By about step 40–60, tool use collapses toward near-zero
		3. After the collapse, there are only sparse spikes
	2. This means the model initially explores the search API because the prompt strongly suggests it, but then learns that <mark style="background: #ADCCFFA6;">it can get comparable or better rewards without using the tool consistently</mark>
	3. That is not what you would expect if the learned policy genuinely believed search was necessary
	4. So the system learned (classic degeneracy)
		1. “Search is optional, expensive, noisy, or unnecessary under this reward”
2. Reward Mean
	1. Observations
		1. Reward rises early
		2. Then stabilises around a moderate value
		3. No catastrophic collapse after tool usage disappears
	2. If tool usage vanished and reward also crashed, you would say the model failed, but here, <mark style="background: #FF5582A6;">tool usage vanishes while reward remains decent or improves</mark>
		1. So, from the optimizer’s perspective, dropping search is working
	3. "Policy simplification under reward pressure" or "collapse to a low-search local optimum"
3. Reward Max
	1. Observations
		1. The max reward still reaches high values often
		2. The best samples remain good even late in training
	2. This suggests the policy has not become globally incompetent; instead, <mark style="background: #ADCCFFA6;">it has become selectively efficient</mark>
		1. Usually short / no-tool behaviour
		2. Occasionally produces a high-scoring trajectory
	3. <mark style="background: #D2B3FFA6;">So the issue is not that the model cannot ever search well; the issue is that the expected reward does not keep search attractive on average</mark>
4. Response Length
	1. Observations
		1. Across the runs, response length starts very high, then drops sharply
	2. This is exactly what you’d expect when the model figures out
		1. “I do not need to emit a long chain-of-thought-like structure and tool scaffolding to get a reward”
	3. <mark style="background: #FF5582A6;">So the model is compressing behaviour</mark>
		1. Less search
		2. Less verbose structured reasoning
		3. Shorter outputs
		4. Still acceptable reward
	4. That is a signature of optimization pressure against the explicit scaffold in your prompt
5. Response Clipping
	1. Observations
		1. One of the 4×24GB runs has severe early clipping, up to ~0.5–1.0 (<mark style="background: #BBFABBA6;">max response length is 1024</mark>)
		2. The red 1×40GB run is close to zero clipping almost all the time
	2. So the 40GB run is not mainly explained by truncation
	3. <mark style="background: #ABF7F7A6;">The short outputs are learned preferences, not forced shortening by clipping</mark>
	4. That strengthens the conclusion that the model is voluntarily abandoning the long format/tool behaviour
6. Advantage
	1. Observations
		1. Advantages are centred near zero, noisy, and small across runs
	2. <mark style="background: #FFF3A3A6;">That is normal-ish for PPO/GRPO style training</mark>
	3. No strong ongoing gradient pushing back toward the search behaviour
	4. Once the policy settles into low-search mode, there is no consistent advantage signal to recover it
		1. So in practice, once tool use dies, the training dynamics do not resurrect it
7. Prompt
	1. 

```
llm_judge_metric: 0.112

llm_judge_metric: 0.1574074074074074

em: 0.072
f1: 0.12097142857142859
acc: 0.072
precision: 0.12893333333333334
recall: 0.119


em: 0.08
f1: 0.13977142857142857
acc: 0.088
precision: 0.1486666666666667
recall: 0.1396666666666667
```

8. <mark style="background: #BBFABBA6;">The advantage mean of zero shows that training is stable</mark>
9. Smaller batch sizes of 4 or 8 make no significant difference in score as it progresses, which means training might be possible
10. <mark style="background: #FFB86CA6;">The noisy signal (score) is because of the small batch sizes (2, 3)</mark>
11. Mismatch between the Re-Search prompt interface and Qwen3
	1. The instruct prompt does not work with hybrid models like Qwen3
12. Similar results in score across GPU types mean that the GPU does not affect the training as much at these batch sizes
13. The tool call mean drops after a few steps, which indicates the reward was set up for an instruct model and not a hybrid model (soft prompt reasoning vs instruct) 
	1. This means the prompt has to be updated
	2. <mark style="background: #FF5582A6;">The smaller model is sensitive to the prompt</mark>
14. Max prompt response length effects early exploration, so the minimum response length for experimentation has to account for this (at least 4096)
15. The model learns to avoid search because there is no reward for this and no prior in the prompt
	1. The model has quite a lot of parametric knowledge
