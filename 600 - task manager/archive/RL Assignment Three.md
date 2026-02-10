---
tags:
  - academic
description:
due date:
start date:
end date:
status: Archive
importance level:
urgency level:
task type:
story points:
parent nodes:
child nodes:
recurrent:
---
# ==CONVERT INTO NOTES==


## What is DQN?

It writes this all down in a big table (Q-values), so it always knows the best move.

- Learn a **Q-function** `Q(s, a)` = expected future reward from taking action `a` in state `s`.
- Use a **neural network** to approximate this function: $Q_\theta(s, a)$.
- The agent **selects the action with the highest Q-value**.

The Q-function is updated using the **Bellman equation**:

$Q(s_t, a_t) = r_t + \gamma \max_{a'} Q(s_{t+1}, a')$

Training loss:

$\mathcal{L}(\theta) = \left( Q_\theta(s_t, a_t) - \left[r_t + \gamma \max_{a'} Q_{\theta^-}(s_{t+1}, a')\right] \right)^2$

Where:
- $\theta$ is the current Q-network parameters
- $\theta^-$ is the target network (updated less frequently)

```python
import torch
import torch.nn as nn
import torch.optim as optim
import random
import numpy as np

class DQN(nn.Module):
    def __init__(self, state_dim, action_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, action_dim)
        )

    def forward(self, x):
        return self.net(x)

# Assume you already have: memory buffer, epsilon-greedy, etc.
# For a given (s, a, r, s')
with torch.no_grad():
    target = r + gamma * torch.max(target_net(s_prime))

q_value = policy_net(s)[0, a]
loss = (q_value - target).pow(2).mean()

optimizer.zero_grad()
loss.backward()
optimizer.step()
```

---
## What is REINFORCE

REINFORCE tries random strategies, and if the reward was good, it pushes the network to make those choices more often.

- Learn a **policy function** $\pi_\theta(a|s)$ directly.
- Use the **reward** as a guide to update policy parameters: $\theta \leftarrow \theta + \alpha \nabla_\theta \log \pi_\theta(a|s) \cdot R$

The gradient estimate is:

$\nabla J(\theta) = \mathbb{E}\left[ \nabla_\theta \log \pi_\theta(a|s) \cdot R \right]$

Where $R$ is the total return (sum of rewards from that point onward).

```python
class PolicyNet(nn.Module):
    def __init__(self, state_dim, action_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, action_dim),
            nn.Softmax(dim=-1)
        )

    def forward(self, x):
        return self.net(x)

# Rollout trajectory
log_probs = []
rewards = []

state = env.reset()
done = False
while not done:
    probs = policy_net(torch.tensor(state).float().unsqueeze(0))
    dist = torch.distributions.Categorical(probs)
    action = dist.sample()
    log_probs.append(dist.log_prob(action))
    state, reward, done, _ = env.step(action.item())
    rewards.append(reward)

# Compute return and loss
R = sum(rewards)
loss = -torch.stack(log_probs).sum() * R

optimizer.zero_grad()
loss.backward()
optimizer.step()
```

---
## What is Actor-Critic

The Critic helps the Actor learn faster and more stably.

- Use **Actor** to represent the policy: $\pi_\theta(a|s)$
- Use **Critic** to estimate the value function: $V_w(s)$
- Advantage: $A(s, a) = R - V(s)$
- Update Actor using advantage: $\nabla_\theta J(\theta) = \nabla_\theta \log \pi_\theta(a|s) \cdot A(s, a)$
- Update Critic with MSE: $\mathcal{L}(w) = \left( V_w(s) - R \right)^2$

```python
class Actor(nn.Module):
    def __init__(self, state_dim, action_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, action_dim),
            nn.Softmax(dim=-1)
        )

    def forward(self, x):
        return self.net(x)

class Critic(nn.Module):
    def __init__(self, state_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 1)
        )

    def forward(self, x):
        return self.net(x)

# During rollout
log_probs, values, rewards = [], [], []

state = env.reset()
done = False
while not done:
    state_tensor = torch.tensor(state).float().unsqueeze(0)
    probs = actor(state_tensor)
    dist = torch.distributions.Categorical(probs)
    action = dist.sample()

    value = critic(state_tensor)
    log_probs.append(dist.log_prob(action))
    values.append(value)
    state, reward, done, _ = env.step(action.item())
    rewards.append(reward)

# Compute returns and advantage
returns = sum(rewards)
values = torch.cat(values)
advantage = returns - values.detach()

# Losses
actor_loss = -torch.stack(log_probs).sum() * advantage
critic_loss = (returns - values).pow(2).mean()

loss = actor_loss + critic_loss

optimizer.zero_grad()
loss.backward()
optimizer.step()
```
