
## Previous Plan

- Build Qwen3 0.6B and load the model
- Implement a GRPO training pipeline
- Build a query system with FlashRag (for a search tool)
- Train on MuSiQue 
- Evaluate the below for baseline:
	- HotpotQA
	- Bamboogle
	- 2WikiMultiHopQA

## Current Status

- <mark style="background: #BBFABBA6;">Build Qwen3 0.6B and load the model</mark> 
- <mark style="background: #BBFABBA6;">Implement a GRPO training pipeline</mark>
	- Single turn
	- Reused reward setup from Re-Search
- <mark style="background: #BBFABBA6;">Build a query system with FlashRag (for a search tool)</mark>
	- The original paper uses a multi-GPU setup where the index (65GB) is loaded in one of the GPUs
	- Updated the setup to work with FlashRag on CPU memory
- <mark style="background: #FF5582A6;">Train on MuSiQue</mark>
	- Tried the Re-Search code base, but the setup is pinned to Qwen2.5
	- Verl version does not support Qwen3
	- Tried to port the code, but was not able to do so
	- Created a GRPO pipeline from scratch
		- Problems
			- Sequential rollout (can try batched rollout)
				- Underutilised GPU (only 5GB)
			- Reference model loaded only once
			- Old model for rollout loaded every time (not optimised)
	- <mark style="background: #BBFABBA6;">Try starting from a new version of Verl that supports Qwen3</mark>
- Evaluate the below for baseline:
	- <mark style="background: #BBFABBA6;">Bamboogle</mark>
		- Base
			- EM
		- Instruct
			- EM
			- LLM-Judge based (Qwen3.5 9B)
		- Reasoning
			- EM
			- LLM-Judge based (Qwen3.5 9B)
- <mark style="background: #FF5582A6;">Build an SFT pipeline</mark>

## Results

![ReSearch|700](https://paper-assets.alphaxiv.org/figures/2503.19470v3/img-0.jpeg)

- Evaluation of the base model showed below-par performance
	- Less than 1%

```
Instruct (Qwen2.5 7B - 10.4EM)
em: 0.008
f1: 0.024152380952380953
acc: 0.008
precision: 0.028
recall: 0.022333333333333334
```

```
Reasoning
em: 0.0
f1: 0.005333333333333333
acc: 0.0
precision: 0.006
recall: 0.005
```

