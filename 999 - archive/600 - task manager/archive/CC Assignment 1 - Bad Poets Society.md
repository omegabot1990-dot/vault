---
tags:
  - academic
  - cc
description: assignment one for CC - bad poets society
due date: 2024-10-07
start date: 2024-09-30
end date: 2024-10-05
status: Archive
importance level: important
urgency level: urgent
task type: execute
story points: 
parent nodes:
  - "[[computational creativity]]"
child nodes: 
recurrent:
---

[[202409201734 - bad poets society]]

## Objective

Create Haiku using a combination of GPTs, Templates and Grammars.


## Cues

- N/A

## Notes

1. Base model planned to be used Llama 3.1 8B
	1. https://www.llama.com/llama-downloads/
	2. It did not work out; I could not train the model because it was too big.
2. Base model used Google T5-small
3. SSH
	1. https://rel.liacs.nl/general/ssh-access
	2. https://rel.liacs.nl/issc/ssh-access
	3. `ssh -v s4374886@sshgw.leidenuniv.nl`
	4. `ssh -K U0065004`
	5. `ssh -o ProxyCommand='ssh -g -L 6020:localhost:6020 s4374886@sshgw.leidenuniv.nl -q -W U0065000:22' -g -L 6020:localhost:6020 s4374886@U0065000`
	6. `jupyter-notebook --no-browser --port=6020`
	7. Run VS Code server on Remote Host
		1. `~/.vscode-server/bin/38c31bc77e0dd6ae88a4e9cc93428cc27a56ba40/vscode-server-linux-x64/bin/code-server`
4. Downloaded 
	1. `/vol/home/s4374886/.llama/checkpoints/Llama3.1-8B`

## Summary

- Trained a model on a filtered set of 630ish Haikus and generated results.