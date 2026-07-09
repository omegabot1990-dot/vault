# Vault Instructions

This is Sankar's research vault for an AI Master's at Leiden University. The focus is machine learning, reinforcement learning, LLM training, and related math foundations. Use this file as the working agreement for any task inside this folder.

## Me

- Sankar (full name: Gaurisankar J), AI Master's student at Leiden University
- Email: gaurisankarj1996@gmail.com
- Research focus: reinforcement learning, LLM training, and the math foundations that sit underneath them

## People

| Who | Role |
|---|---|
| **Aske Plaat** | Supervisor |
| **Álvaro Serra-Gómez** | Co-supervisor |

Other collaborators / lab mates haven't been named yet. Add them here as they come up.

## Projects

| Name | What |
|---|---|
| **omega_bot** | A temporary OpenClaw helper bot built with Codex, running on a Google VM. Used for ad-hoc help; planned for shutdown soon. The folder this vault lives in is named after it — once it's torn down, the vault will be cleaned up and possibly re-rooted. |
| **Master's research** | Active research focus: reinforcement learning + LLM training. See `002 - research/` for the live zettelkasten. |

## Terms

| Term | Meaning |
|---|---|
| LIACS | Leiden Institute of Advanced Computer Science (Leiden's CS department) |
| MOC | Map of Content — a topic hub note that links related zettels |
| Zettel | An atomic note in the zettelkasten (one idea per note) |

Add new acronyms / shorthand here as they come up.

## Preferences

- Bullets, not prose. Reading speed > completeness.
- Keep my voice in existing zettels — propose changes, don't bulk-rewrite.
- Real citations only. If a source can't be found, mark it `TODO: cite`.

## Folder layout

- `000 - daily notes/` — one file per day, named `YYYY-MM-DD.md`. Drop ad-hoc thoughts, reading notes, and todos here.
- `002 - research/` — the main zettelkasten. Two kinds of notes live here:
  - **Atomic zettels** named `YYYYMMDDHHMM - <topic>.md` (e.g. `202602062040 - probability.md`). One idea per note.
  - **Topic / hub notes** named `<topic>.md` (e.g. `probability.md`, `machine learning.md`). These collect and link related zettels — use them like Maps of Content.
- `008 - templates/` — templates used by the Templater plugin. Don't edit these unless asked.
- `009 - help/` — vault's own help docs and hotkey notes.

## Note conventions

Every note starts with YAML frontmatter. Match the relevant template:

- New atomic zettel → copy `008 - templates/node - zettel.md`. Frontmatter must include: `tags`, `aliases`, `title` (lowercase), `description`, `bot`, `parent nodes` (a wikilink to a parent MOC or zettel), `published on`.
- New MOC / topic hub → copy `008 - templates/node - moc.md`. Sections: Topics, Blogs, Papers, Videos, Code.
- New task → copy `008 - templates/node - inbox.md`.
- New daily note → copy `008 - templates/node - daily notes.md`.

Body style:

- Bulleted, concise, no trailing full stops on bullets.
- Use `[[wikilinks]]` to connect notes. Prefer `[[202602062040 - probability|probability]]` (alias form) over bare titles, so the note ID is preserved if the title changes.
- Math in LaTeX inside callouts: `> [!MATH]` for formulas, `> [!info]` for asides, `> [!example]` for examples.
- Cite sources with footnote refs `[^1]` and deep-link URLs at the bottom (use the `#:~:text=` fragment when possible to point at the exact sentence).
- Highlight emphasis with marks — keep this consistent:
  - Green `#BBFABBA6` → core definitions
  - Orange `#FFB86CA6` → tentative / "for use later"
  - Red `#FF5582A6` → important / decided / warning

When creating a new atomic zettel, generate the timestamp prefix from the current local time as `YYYYMMDDHHMM` and confirm the proposed filename before writing.

## What Claude should help with

Ranked roughly by frequency:

- **Drafting new zettels** from a paper, blog, or my rough notes — match the template and writing style above. Always link to a `parent nodes` value; if I don't tell you what it is, ask.
- **Synthesizing across notes** — summarize what I've already written on a topic, find contradictions, suggest missing links between zettels.
- **Literature digestion** — read a paper (PDF, link, or pasted text) and produce a zettel-shaped summary plus a list of follow-up questions.
- **Refactoring** — split a long note into atomic zettels, promote a topic hub to a proper MOC, or fix dangling wikilinks. Always show the diff and wait for approval before bulk edits.
- **Research planning** — turn the `todo.md` and `highlights.md` files in `002 - research/` into a prioritized weekly plan.

## What Claude should not do

- Don't bulk-rewrite existing zettels without asking. My voice is in those bullets.
- Don't delete files. If a note is obsolete, propose archiving (move to a new `099 - archive/` folder) and wait for confirmation.
- Don't edit the templates in `008 - templates/`.
- Don't invent citations. Every footnote must be a real URL I can click; if you can't find a source, say so and leave a `TODO: cite` marker.
- Don't add fluff prose. Keep notes bullet-first. Reading speed matters more than completeness.

## Useful skills for this vault

- `/engineering:documentation` — write a README, runbook, or longer-form doc into the vault.
- `/engineering:debug` — pasted training error or stack trace, get a structured debug session.
- `/engineering:code-review` — review code I've pasted or pointed at.
- `/productivity:task-management` — manage `TASKS.md` (will live alongside this file).
- `/productivity:memory-management` — keep this file accurate as my work shifts.

## Open questions / TODOs for Claude

- [ ] Reconcile `002 - research/todo.md` with any tasks tracked elsewhere when I ask.
- [ ] Periodically scan for orphan zettels (no `parent nodes` link) and surface them.
- [ ] Watch for duplicate topic hubs (e.g. two notes titled `information theory`) and propose a merge.
