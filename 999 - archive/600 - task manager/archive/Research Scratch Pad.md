---
tags:
  - inbox
  - academic
  - work
description:
due date: 2026-01-10
start date: 2025-12-26
end date: 2026-02-01
status: Archive
importance level: important
urgency level: urgent
task type: plan
story points: 13
parent nodes:
child nodes:
recurrent:
---

## Strategy 

- Read at least one paper a day.
- Read fast. Cover more topics.
- ==Focus on the research question around using RLHF for simulated "humans" when human data is unavailable/hard to get. Especially if you want to use small models, fine-tuning may be important given their limited prompting capabilities. How to then simulate the virtual humans so that the simulation is plausible?==

## DIRECTION

- Direction 
	- [Multi-Step Reasoning with Large Language Models: A Survey](https://arxiv.org/abs/2407.11511)
		- Smaller Language Models
		- Reinforcement Learning with Verifiable Rewards (RLVR)
		- Group Relative Policy Optimisation (GRPO)
		- Self-Reflection
	- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)
		- Reasoning capabilities can be incentivised with RL.
		- Distillation works better with smaller models.
		- Can the model achieve comparable performance through large-scale RL training?
		- [Supplementary information](https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-025-09422-z/MediaObjects/41586_2025_9422_MOESM1_ESM.pdf)
			- Has a lot of background work for post-training paradigms. GOLD MINE.
			- 
		- RLVR in math and coding.
			- ==Can this be expanded into a domain I want?==
		- 

## TODO

- [ ] Checkout [Sebastian Raschka Blog](https://magazine.sebastianraschka.com/).
	- [ ] Focus on RLVR
- [ ] Evaluation of LLMs - https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches
- [ ] Reasoning LLMs - https://magazine.sebastianraschka.com/p/understanding-reasoning-llms
- [ ] RL for Reasoning - https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training
- [ ] R1 paper -  https://arxiv.org/abs/2501.12948
	- [ ] https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-025-09422-z/MediaObjects/41586_2025_9422_MOESM1_ESM.pdf - Supplementary Material R1
	- [ ] Read and add notes for the proposal. I think it could be a great starting point.

## BACKLOG

- Checkout [Sebastian Raschka Blog](https://magazine.sebastianraschka.com/).
- Checkout for Evaluation: 
	- https://github.com/EleutherAI/lm-evaluation-harness
	- https://crfm.stanford.edu/helm
- ==Create a graph view of papers read.== - DONE
	- THIS WAS AN AMAZING IDEA
- ==Organise Google Scholar Library.==
- ==Organise Semantic Scholar Library.==
- A Survey on Knowledge Distillation of Large Language Models
	- Check what Knowledge Elicitation is
	- Check what Distillation Algorithms are
- RAG is used with a small model, with reasoning and tool use enforced with GRPO/RLVR.
	- Could be a good idea to explore.
- [DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning](https://arxiv.org/abs/2511.22570v1)
- [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)
- [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290)
- [Olmo 3](https://arxiv.org/abs/2512.13961)
- [gpt-oss-120b & gpt-oss-20b Model Card][https://arxiv.org/abs/2508.10925]
- [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314)
	- We find that on problems where a smaller base model attains somewhat non-trivial success rates, test-time compute can be used to outperform a 14x larger model.
	- Inference scaling can be better than parameter scaling?
- [How Difficulty-Aware Staged Reinforcement Learning Enhances LLMs' Reasoning Capabilities: A Preliminary Experimental Study](https://arxiv.org/abs/2504.00829v1)
	- Works with a 1.5B model.
	- Difficulty-graded RL, difficulty-aware staged reinforcement learning.
	- ==CHECK THIS OUT 29th January==
- [O1 Replication Journey: A Strategic Progress Report -- Part 1](https://arxiv.org/abs/2410.18982)
	- By exposing the model to incorrect reasoning paths and their corrections, journey learning may also reinforce self-correction abilities, potentially making reasoning models more reliable this way.
	- Shortcut learning refers to the traditional approach in instruction fine-tuning, where models are trained using only correct solution paths.
	- Journey learning, on the other hand, also includes incorrect solution paths, allowing the model to learn from mistakes.
	- The paper has a lot of background work done. Can be used as a reference for:
		- PRM
		- Inference Scaling
		- CoT Theory
		- Internal Thought
		- Self-improvement
- [Rethinking Bradley-Terry Models in Preference-Based Reward Modeling: Foundations, Theory, and Alternatives](https://arxiv.org/abs/2411.04991)
	- BT style reward modelling, alternatives
- Extra Reading:
	- https://magazine.sebastianraschka.com/p/beyond-standard-llms
	- https://www.atomproject.ai/ | https://substack.com/@natolambert
	- https://modelcontextprotocol.io/docs/getting-started/intro
		- MCP, more for engineering
	- https://magazine.sebastianraschka.com/p/from-gpt-2-to-gpt-oss-analyzing-the - GPT2-GPT-OSS
	- Research Papers (might make sense later)
		- https://magazine.sebastianraschka.com/p/llm-research-papers-2025-list-one
		- https://magazine.sebastianraschka.com/p/llm-research-papers-2025-part2
- https://www.emergentmind.com/
	- Looks like it might be a cool website.
	- Has an Open Problems section.
	- Is pretty cool.
- ==IMPORTANT READING==
	- [LLM Evaluation](https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches) - DONE
	- [Reasoning](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) - DONE
	- [LLM Architecture Comparison](https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison)
	- [Pre, Post-Training Paradigms](https://magazine.sebastianraschka.com/p/new-llm-pre-training-and-post-training)
	- [Encoder and Decoder](https://magazine.sebastianraschka.com/p/understanding-encoder-and-decoder)
	- [RLHF Alternatives](https://magazine.sebastianraschka.com/p/llm-training-rlhf-and-its-alternatives)
		- Good content for a historical view; it starts from InstructGPT, which is where we want to start.
	- [CPT](https://www.emergentmind.com/topics/continued-pre-training-cpt)
	- [Dropouts](https://www.jmlr.org/papers/volume15/srivastava14a/srivastava14a.pdf?utm_content=buffer79b4)
	- [Language Models are Unsupervised Multi-Task Learners](https://ia601409.us.archive.org/3/items/language-models-are-unsupervised-multitask-learners/language_models_are_unsupervised_multitask_learners.pdf)
- RANDOM
	- [Youtu-LLM: Unlocking the Native Agentic Potential for Lightweight Large Language Models](https://arxiv.org/abs/2512.24618)
	- [mHC: Manifold-Constrained Hyper-Connections](https://www.arxiv.org/abs/2512.24880) - MUST READ LATEST SHIT
	- Checkout
		- Grouped-query attention, sliding-window attention, or multi-head latent attention.
		- Gated DeltaNets in Qwen3-Next and Kimi Linear, as well as the Mamba-2 layers in NVIDIA’s Nemotron 3
	- [NovaSky](https://novasky-ai.github.io/posts/sky-t1/)
		- Distillation of 17k samples @450$
		- Has code 
	- [TinyZero](https://github.com/Jiayi-Pan/TinyZero/) exhibits some emergent self-verification abilities, which supports the idea that reasoning can emerge through pure RL, even in small models.
	- [PERSONA: Dynamic and Compositional Inference-Time Personality Control via Activation Vector Algebra](https://openreview.net/forum?id=QZvGqaNBlU)
		- Activation probing
		- Manipulating vectors in activation space
		- Contrastive activation analysis

## Done

- Read Prompting a Smaller-Scale LLM for Goal-Oriented Emotional Support Dialogue Generation. - DONE
	- Methodology is elaborately written, mostly prompt engineering.
	- Results were analysed in depth, with many graphs. 
	- No significant contribution, but very long and verbose. Maybe that's the expectation.
- Look into https://theses.liacs.nl/cs/2024-2025. - DONE
	- Checked out a few promising papers.
	- Some are super long.
	- Some don't seem that cool.
	- Some are super simple. Or it seems simple.
- Check "Multi-Step Reasoning with Large Language Models, a Survey" for possible future directions. - DONE
- [The Optimal Architecture for Small Language Models](https://huggingface.co/blog/codelion/optimal-model-architecture) - DONE
	- Compares a lot of architectures.
	- Diffusion is good for factuality and throughput.
	- Does work along with pre-training and not alignment. 
	- ==Could be revisited.==
- A Survey on Knowledge Distillation of Large Language Models - DONE
	- Overview
- [LLM Evaluation](https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches) - DONE
	- Overview
	- https://github.com/rasbt/reasoning-from-scratch/tree/main/chF/02_mmlu - CODE
	- LLM as Judge - [PHUDGE: Phi-3 as Scalable Judge](https://arxiv.org/abs/2405.08029)
	- LLM as Judge - https://github.com/rasbt/reasoning-from-scratch/tree/main/chF/04_llm-judge - CODE
	- Basic idea about evaluating LLMs. 
	- Has some code, a pretty good place to start
- [Reasoning](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms)
	- How R1 works
		- The DeepSeek R1 technical report categorizes common inference-time scaling methods (such as Process Reward Model-based and Monte Carlo Tree Search-based approaches) under "unsuccessful attempts." This suggests that DeepSeek did not explicitly use these techniques beyond the R1 model's natural tendency to generate longer responses, which serves as an implicit form of inference-time scaling compared to the V3 base model.
	- Inference Scaling
	- RL
	- SFT + RL
	- Distillation
		- A case study in pure SFT. These distilled models serve as an interesting benchmark, showing how far pure supervised fine-tuning (SFT) can take a model without reinforcement learning.
	- Cold Start data collection for R1 zero

## Code

- [LLM from Scratch](https://github.com/rasbt/LLMs-from-scratch)

## References

- [[domain_specialization_as_the_key_to_make_large_language_models_disruptive_a_comprehensive_survey.pdf|Domain Specialization as the Key to Make Large Language Models Disruptive: A Comprehensive Survey]]
	- Covers a wide range of topics.
	- Should definitely take a deeper look at some topics.
	- IS USEFUL

## Alignment 

- [Anthropic Research](https://www.anthropic.com/research/team/alignment)

## Compute

- [VastAI](https://vast.ai/pricing)

## Papers

- [[Reading List#Research|Research]]


---
## Ideation

%% 
(resources:: Resources - 202512260006)
%%
> [!info] 2025-12-26
> > [!example] **Resources:**
> > - [Chat Research](https://chatgpt.com/g/g-p-694d3776c93c81918e324c42ecbd3585-research/project)
> > - [LLM to Conversational Agent](https://chatgpt.com/share/694ef41a-8924-800c-8043-61b0f312cc4d)
> > - [Reward Function Strategy](https://chatgpt.com/share/694ef99a-e000-800c-9b93-318abb541d43) - DIG DEEP
> > - [Evaluation Paradigms](https://chatgpt.com/share/694efa6c-7784-800c-91a7-62ace3c896d5)


---
%% 
(resources:: Resources - 202511072154)
%%
> [!info] 2025-11-07
> > [!example] **Resources:**
> > - [Mendeley](https://www.mendeley.com/)
> > - [Sci-Hub](https://sci-hub.ru/)
> > - [Ebsco](https://www.ebsco.com/)
> > - [Google Scholar](https://scholar.google.com/)
