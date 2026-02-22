---
tags:
  - reinforcement_learning
aliases:
  - Deep Reinforcement Learning Doesn't Work Yet (2018)
title: deep reinforcement learning doesn't work yet
description: ""
bot: false
parent nodes:
  - "[[202602192221 - reinforcement learning|Reinforcement Learning]]"
published on:
---

> [Deep Reinforcement Learning Doesn't Work Yet](https://www.alexirpan.com/2018/02/14/rl-hard.html)


- Problems with RL (2018)
	- Deep Reinforcement Learning Can Be Horribly <mark style="background: #ABF7F7A6;">Sample Inefficient</mark> [^4]
	- If You Just Care About Final Performance, <mark style="background: #FFB86CA6;">Many Problems are Better Solved by Other Methods</mark> [^5]
	- Reinforcement Learning Usually Requires a Reward Function [^6]
	- Reward Function Design is Difficult [^7] <mark style="background: #BBFABBA6;">(Reward Hacking)</mark>
	- Even Given a Good Reward, <mark style="background: #D2B3FFA6;">Local Optima Can Be Hard To Escape</mark> [^8]
	- Even When Deep RL Works, It May Just Be Overfitting to Weird Patterns In the Environment [^9]
	- Even Ignoring Generalisation Issues, The Final Results Can be Unstable and Hard to Reproduce [^10]
- Takeaways (2018)
	- <mark style="background: #FF5582A6;">Self-play is an amazing strategy</mark> [^11]
	- <mark style="background: #FFF3A3A6;">Simplify the problem into an easier form</mark> [^12]
- Future Work (2018)
	- Local optima are good enough [^13]
	- More learning signals [^14]
		- Sparse rewards are hard to learn because you get very little information about what thing help you
		- Define auxiliary tasks
		- Hallucinate positive rewards
		- Bootstrap with self-supervised learning to build a good world model
	- Model-based learning unlocks sample efficiency [^15]
	- Use reinforcement learning just as the fine-tuning step [^1]
	- Reward functions could be learnable [^2]
		- <mark style="background: #BBFABBA6;">Imitation learning</mark>
			- <mark style="background: #D2B3FFA6;">Behavioural cloning</mark>
			- <mark style="background: #ABF7F7A6;">Inverse reinforcement learning</mark>
	- Transfer learning saves the day [^3]
		- You can leverage knowledge from previous tasks to speed up learning of new ones


[^1]: https://www.alexirpan.com/2018/02/14/rl-hard.html#:~:text=Use%20reinforcement%20learning%20just%20as%20the%20fine%2Dtuning%20step
[^2]: https://www.alexirpan.com/2018/02/14/rl-hard.html#:~:text=Reward%20functions%20could%20be%20learnable
[^3]: https://www.alexirpan.com/2018/02/14/rl-hard.html#:~:text=Transfer%20learning%20saves%20the%20day
[^4]: https://www.alexirpan.com/2018/02/14/rl-hard.html#:~:text=Deep%20Reinforcement%20Learning%20Can%20Be%20Horribly%20Sample%20Inefficient
[^5]: https://www.alexirpan.com/2018/02/14/rl-hard.html#:~:text=If%20You%20Just%20Care%20About%20Final%20Performance%2C%20Many%20Problems%20are%20Better%20Solved%20by%20Other%20Methods
[^6]: https://www.alexirpan.com/2018/02/14/rl-hard.html#:~:text=Reinforcement%20Learning%20Usually%20Requires%20a%20Reward%20Function
[^7]: https://www.alexirpan.com/2018/02/14/rl-hard.html#:~:text=Reward%20Function%20Design%20is%20Difficult
[^8]: https://www.alexirpan.com/2018/02/14/rl-hard.html#:~:text=Even%20Given%20a%20Good%20Reward%2C%20Local%20Optima%20Can%20Be%20Hard%20To%20Escape
[^9]: https://www.alexirpan.com/2018/02/14/rl-hard.html#:~:text=Even%20When%20Deep%20RL%20Works%2C%20It%20May%20Just%20Be%20Overfitting%20to%20Weird%20Patterns%20In%20the%20Environment
[^10]: https://www.alexirpan.com/2018/02/14/rl-hard.html#:~:text=Even%20Ignoring%20Generalization%20Issues%2C%20The%20Final%20Results%20Can%20be%20Unstable%20and%20Hard%20to%20Reproduce
[^11]: https://www.alexirpan.com/2018/02/14/rl-hard.html#:~:text=There%20is%20a%20way%20to%20introduce%20self%2Dplay%20into%20learning.
[^12]: https://www.alexirpan.com/2018/02/14/rl-hard.html#:~:text=The%20problem%20is%20simplified%20into%20an%20easier%20form.
[^13]: https://www.alexirpan.com/2018/02/14/rl-hard.html#:~:text=Local%20optima%20are%20good%20enough
[^14]: https://www.alexirpan.com/2018/02/14/rl-hard.html#:~:text=Add%20more%20learning%20signal
[^15]: https://www.alexirpan.com/2018/02/14/rl-hard.html#:~:text=Model%2Dbased%20learning%20unlocks%20sample%20efficiency