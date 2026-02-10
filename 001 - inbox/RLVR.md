---
tags:
  - inbox
  - work
  - academic
description:
due date:
start date:
end date:
status: In Progress
importance level: important
urgency level: urgent
task type: capture
story points:
parent nodes:
recurrent:
---

## Open Problems

- Process Reward Models
	- How to add rewards for each reasoning step?
	- The next logical step is to not only use the final answer’s correctness as a reward signal but also judge the LLM’s explanations during RLVR training. 
	- This has been done before, for many years in the past, under the research label “process reward models” (PRMs).
- Monte Carlo Tree Search
	- How to incorporate MCTS in the RLVR training phase?
	- [DeepSearch: Overcome the Bottleneck of Reinforcement Learning with Verifiable Rewards via Monte Carlo Tree Search](https://www.alphaxiv.org/overview/2509.25454)
- Curriculum Learning
	- Can curriculum learning make a difference? NEED TO VERIFY
- Rhetoric
	- Can games like Werewolf improve rhetoric?

## Questions

- Reward modelling for non-deterministic domains?
	- Rule-based
		- Unit tests, math checker
	- Semantic matching, encoder to compute similarity
		- [Shaping Explanations: Semantic Reward Modeling with Encoder-Only Transformers for GRPO](https://www.alphaxiv.org/overview/2509.13081)
	- Latent state comparison
	- Keyword matching
	- Evidence grounded with RAG
	- Constraints (predefined rules or on-the-fly generation of rules)
	- Schema compliance (format compliance)
		- Regex
	- Pair-wise ranking (Bradley-Terry style)
		- In PRM?
	- Hybrid setup?
- Can a small 1B model post-trained using RLVR and hybrid keyword, semantic reward modelling be used as a research assistant?
	- [Facebook Research Plan Generation](https://huggingface.co/datasets/facebook/research-plan-gen)
		- Has Rubrics (may be useful)
		- Has reference solutions
- Can RLVR with PRM using semantic reward modelling be used to improve reasoning in a smaller model?
- Does negative sampling with SFT for cold-start help?
- ==NAIVE==
	- How can we bridge the gap between RLVR and non-verifiable domains?
	- Can we use Process Reward Modelling as a bridge between RLVR and non-verifiable domains?
	- How can we extend RLVR into non-verifiable domains?

## Examples

- [TinyZero](https://github.com/Jiayi-Pan/TinyZero/) 
	- Exhibits some emergent self-verification abilities, which supports the idea that reasoning can emerge through pure RL, even in small models
	- Replicates the DeepSeek-R1-Zero approach 
	- Costs less than $30 to train
	- 3B base LM develops self-verification and search abilities all on its own
- https://www.connectedpapers.com/main/f3ec0ee1538796c8d5e5633958106fbe394a32ad/Spurious-Rewards%3A-Rethinking-Training-Signals-in-RLVR/graph
	- <mark style="background: #FF5582A6;">CHECKOUT LATER</mark>

## Notes

- R1 showed that reasoning can be learned with RL. 
	- Emergent Reasoning.
	- Self Distillation.
- [RLVR #1](https://www.emergentmind.com/topics/reinforcement-learning-with-verifiable-rewards-rlvr)
	- Deterministic and Model-based ==Reward Functions==
	- Requires Verifiable Outcomes.
	- Roots in,
		- Mathematics
		- Code-based Tasks
	- The reward function can be,
		- Binary
		- Soft
		- It can be rule-based, model-based (LLM verifier) or a hybrid
	- Policy optimisation can be,
		- PPO
		- GRPO
		- Reward works as the advantage signal
		- KL-divergence penalty for regularisation and against reward hacking
	- Optimises the selection and frequency of already present reasoning patterns
		- Distillation, on the other hand, can introduce novelty
	- Efficacy is tightly coupled with initialisation (SFT)
		- Rapid convergence with a strong SFT base
	- Challenges
		- Reward hacking
		- Model dependence 
			- Works well with models that have good upstream SFT (distillation)
		- Has a base model upper bound (distillation breaks this bound)
		- Metric limitation
			- pass@k may not be enough, could be lucky guesses
			- Proposes ideas like CoT-pass@k, where both the answer and the reasoning are right
	- Future direction
		- Advanced reward modelling
			- Soft, step-wise, process-oriented
		- Implicit and intrinsic rewards
			- Self-certainty, confidence
		- Curriculum learning
		- Data mixture modelling
		- Process reward modelling
		- Incorporation of more subtle similarity metrics (e.g., sentence embedding cosine similarity)
		- Transfer learning?
- [Reward Models](https://cameronrwolfe.substack.com/p/reward-models)


## Papers

- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://www.alphaxiv.org/overview/2501.12948) - Jan 4, 2025
	- [DeepSeek-R1 (Supplementary)](https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-025-09422-z/MediaObjects/41586_2025_9422_MOESM1_ESM.pdf)
	- Foundational for RL and RLVR
	- Showed that reasoning-like behaviour can be developed with RL
		- Reasoning leads to better accuracy
	- Why RLVR?
		- Post-training (bottlenecked by requiring expensive written responses or preference labels) for SFT and RLHF
	- Reward model
		- The **accuracy reward** uses the LeetCode compiler to verify coding answers and a deterministic system to evaluate mathematical responses.
		- The **format reward** relies on an LLM judge to ensure responses follow the expected format, such as placing reasoning steps inside \<think> tags
	- PRM
		- PRM demonstrates a good ability to rerank the top-N responses generated by the model or assist in guided search (Snell et al., 2024); its advantages are limited compared to the additional computational overhead it introduces during the large-scale reinforcement learning process in our experiments.
- [DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning](https://www.alphaxiv.org/abs/2511.22570) - Nov 27, 2025
	- ==READ==
	- Explanation scoring
		- The way the explanations are currently being scored involves a second LLM. This leads to the other direction I am seeing for RLVR: an extension into other domains beyond math and code.​
- [MedRLVR](https://www.emergentmind.com/papers/2502.19655) - Feb 27, 2025
	- RLVR with MCQ medical data as verifiable labels
	- 3B base model
	- Reward signals for,
		- Correctness 
		- Format compliance
	- Future direction?
		- Penalise short CoT
- [Crossing The Reward Bridge](https://www.emergentmind.com/papers/2503.23829) - Mar 31, 2025
	- Generative soft model-based reward signals in unstructured free-form scenarios
		- z-score normalisation
	- Uses objective reference answers
	- Cross-domain reward model - ==CAN WE USE AN ENCODER AND SEMANTIC SIMILARITY?==
		- Created with SFT from data collected during RL exploration
	- RL
		- Uses REINFORCE, REINFORCE++, RLOO
	- Future direction?
		- PRM
		- How to evaluate individual steps?
- [On the Mechanism of Reasoning Pattern Selection in Reinforcement Learning for Language Models](https://www.emergentmind.com/papers/2506.04695) - Jun 5, 2025
	- Optimises the selection of existing reasoning patterns, not creating new ones (distillation is better for new patterns)
	- Slower optimisation of weaker models can be mitigated by SFT
	- SFT + RLVR is amazing
- [Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](https://www.emergentmind.com/papers/2504.13837) - Apr 18, 2025
	- Does not elicit new reasoning patterns
	- Reasoning abilities originate from and are bounded by the base model 
	- Distillation can introduce new reasoning patterns
	- Future direction?
		- Improve RL paradigms
			- Continual scaling
			- ==Multi-turn agent-environment interaction==
- [Adaptive Guidance Accelerates Reinforcement Learning of Reasoning Models](https://www.emergentmind.com/papers/2506.13923) - Jun 16, 2025
	- ==LOOK INTO THIS==
	- Adaptive guidance accelerates learning in RLVR, self-distillation and capability gain
	- The guide-algorithm provides in-context guidance when all roll-outs fail, i.e. adaptive hints in prompts
	- Off-policy importance-ratio correction (sampling) for stable training
	- Guide-GRPO
	- Future direction?
		- Personalised guidance strategies
- [VerIF](https://www.emergentmind.com/papers/2506.09942) - June 11, 2025
	- Combines rule-based and LLM-based semantic verification
	- ==Has an instruction-following dataset with signals==
- [Trust, But Verify: A Self-Verification Approach to Reinforcement Learning with Verifiable Rewards](https://www.emergentmind.com/papers/2505.13445) - May 19, 2025
	- Mathematics domain
	- Simultaneously improves both problem-solving and self-verification
		- Integrated RL for both
	- Online-RL
	- Uses PPO
	- Does problem-solving and self-verification in two steps
		- ==Why not combine both into one?==
			- Add a planning step too
	- Future direction?
		- Expand to other domains
		- Use other policy-gradient algorithms
		- RAG or external-tool use for verification
- [Agent RLVR](https://www.emergentmind.com/papers/2506.11425) - Jun 13, 2025
	- Inspired by human pedagogy
	- The agent creates initial trajectories that are graded by code, and guidance is added 
	- Policy is updated based on RLVR on the rewards of guided trajectories
	- Offline update with SFT, DPO
- ==[ReSearch](https://www.alphaxiv.org/abs/2503.19470) - Sep 23, 2025== | AMAZING PLACE TO START
	- ==EXACTLY WHAT I WANTED TO DO==
	- Uses GRPO and something similar to RLVR
	- Rule-based rewards,
		- Answer reward
		- Format reward
	- Uses instruction-tuned models
	- Future directions?
		- More reward signals other than F1 or exact match
		- More specialised databases
		- ==Not just search but tool-use?==
		- ==Maybe combine soft-rewards too?==
	- [RC-GRPO: Reward-Conditioned Group Relative Policy Optimization for Multi-Turn Tool Calling Agents](https://alphaxiv.org/abs/2602.03025)
	- [Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors](https://alphaxiv.org/abs/2601.15625)
	- [ToolRL: Reward is All Tool Learning Needs](https://alphaxiv.org/abs/2504.13958)
	- [Advancing SLM Tool-Use Capability using Reinforcement Learning](https://alphaxiv.org/abs/2509.04518)
	- [Empowering Multi-Turn Tool-Integrated Reasoning with Group Turn Policy Optimization](https://alphaxiv.org/abs/2511.14846)
	- [Acting Less is Reasoning More! Teaching Model to Act Efficiently](https://alphaxiv.org/abs/2504.14870)
	- [On Group Relative Policy Optimization Collapse in Agent Search: The Lazy Likelihood-Displacement](https://alphaxiv.org/abs/2512.04220)
- [REASONING GYM](https://www.emergentmind.com/papers/2505.24760) - May 30, 2025
	- Provides data generators and verifiers (over 100)
	- Adjustable difficulty
	- Curriculum learning is good
- [Learning to Reason without External Feedback](https://www.alphaxiv.org/abs/2505.19590) - May 26, 2025
	- Uses internal self-certainty as a reward, uses the model's confidence (distributional verification)
	- Self-certainty is the KL-divergence between the uniform distribution over the vocabulary and the predicted next token distribution
		- Metric is mode-seeking, encouraging concentrated probability distributions that indicate higher confidence, while being less biased toward longer sequences compared to perplexity-based measures
	- Uses GRPO
	- Future direction?
		- ==A combination of internal and external rewards==
- [Writing Zero](https://www.alphaxiv.org/overview/2506.00103) - Jun 11, 2025
	- Self-principled critique pairs (phase-dependent rewards)
		- Creates its own rules to judge the output
	- For the creative writing domain
	- GenRM
		- Made from SFT and rule-based RL to act as a judge
	- Bootstrapped Relative Policy Optimisation (BRPO)
		- Pairwise comparison vs pointwise in GPRO, it bootstraps a reference (randomly) and compares all the group responses to this
	- Future direction?
		- Try expanding to new domains
- [Spurious Rewards: Rethinking Training Signals in RLVR](https://www.alphaxiv.org/overview/2506.10947) - Jun 12, 2025
	- RLVR gains are dependent on the base model; even spurious rewards work with some models but not others
	- High dependence on pre-training
	- Code-reasoning may be the reason - ==maybe try a base code model==
- [Generalization of RLVR Using Causal Reasoning as a Testbed](https://www.alphaxiv.org/overview/2512.20760) - Dec 23, 2025
	- ==Says RLVR does not work for smaller models==
	- Heavily dependent on the model capabilities
	- Building strong reasoning foundations through pre-training or initial supervised fine-tuning may be essential before applying reinforcement learning techniques 

## Todos

- [The Era of Agentic Organization: Learning to Organize with Language Models](https://www.alphaxiv.org/overview/2510.26658)
- [Autonomous Agents for Scientific Discovery: Orchestrating Scientists, Language, Code, and Physics](https://www.alphaxiv.org/abs/2510.09901)
- Introduction
	- History
		- [RLHF Alternatives](https://magazine.sebastianraschka.com/p/llm-training-rlhf-and-its-alternatives)
		- Contains step-wise alternatives, starts with InstructGPT.
	- RLHF
		- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)
		- Outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3.
		- This is how alignment started.
	- DPO
		- [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290)
		- Works like an upgrade from RLHF, easier to work with and more stable.
		- This is the next step into alignment.
	- LoRA
		- [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)
		- This is how we are going to fine-tune the model here.
		- Why is pre-training so costly? Find more citations for why LoRA is used.
	- DAPO - ==GRPO==
		- [DAPO: An Open-Source LLM Reinforcement Learning System at Scale](https://arxiv.org/abs/2503.14476)
		- RL at scale framework with data and training code.
		- Maybe a reference I can use.
	- R1-Zero RL recipe, Dr.GRPO
		- [Understanding R1-Zero-Like Training: A Critical Perspective](https://arxiv.org/abs/2503.20783)
		- Has code for basic recipe.
	- DeepSeek-V3.2 - ==GRPO==
		- [DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models](https://arxiv.org/abs/2512.02556)
		- This shit seems to be sota. NEED TO CHECK OUT THE PAPER.
		- Scalable Reinforcement Learning Framework
		- Large-Scale Agentic Task Synthesis Pipeline: To integrate reasoning into tool-use scenarios, we developed a novel synthesis pipeline that systematically generates training data at scale.
	- Olmo
		- [Olmo 3](https://arxiv.org/abs/2512.13961)
		- May have GRPO pipelines explained.
		- This release includes the entire model flow, i.e., the full lifecycle of the family of models, including every stage, checkpoint, data point, and dependency used to build it.
	- Code Sample for RLVR - GRPO Raschka
		- https://github.com/rasbt/reasoning-from-scratch/tree/main/ch06/02_rlvr_grpo_scripts_original

---

- Domain Adaptation? 
	- We do DAPT with LoRA for language understanding the jargon
	- We do SFT for understanding behaviour (we can do distillation based on a large model and domain data to create synthetic QA pairs, maybe an encoder that finds the answer in data)
	- Can we elicit domain-specific reasoning by RL?

Who? Industry
What? Specialised LLMs
Where? Domain-specific tasks
Why? Domain adaptation is crucial for private industries that can't use ChatGPT due to proprietary data and to avoid data leaks. 
- [Domain Specialization as the Key to Make Large Language Models Disruptive: A Comprehensive Survey](https://arxiv.org/abs/2305.18703)
- Check this to cite this information
Pre-training is a bottleneck; find a way to cite.
DAPT will help 
- [Don’t Stop Pretraining: Adapt Language Models to Domains and Tasks](https://www.semanticscholar.org/paper/Don%E2%80%99t-Stop-Pretraining%3A-Adapt-Language-Models-to-Gururangan-Marasovi%C4%87/e816f788767eec6a8ef0ea9eddd0e902435d4271)
- https://www.emergentmind.com/topics/domain-adaptive-pre-training-dapt-f56bf1f4-9ff0-4fb6-af76-587677db57c5
We then do SFT with synthetic data created from unstructured text. To understand expected behaviour.
How? We propose a method to elicit domain-specific reasoning through RL based on RLVR and GRPO on a small 3B foundational model (maybe instruction-tuned) by exploring how to create a hybrid verifier model from domain data.

> Domain Adaptation is not "Domain adaptation means the model must internalize the domain." but is "Domain adaptation means the model must learn how to _interact with_ the domain."

> Domain adaptation = policy adaptation over tools
> Can we get domain-based reasoning by enabling tool use? Tool use + MCTS to learn domain reasoning

---