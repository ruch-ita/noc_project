
# Optimised Noc design using RL algorithm

Project Overview:

This project focuses on optimizing a Network on Chip (NOC) using a Reinforcement Learning (RL) approach, specifically employing a Deep Q-Network (DQN). The NOC system involves complex interactions between CPU and IO peripherals, which communicate through a weighted round-robin arbiter. The primary challenge is to manage varying traffic patterns efficiently to achieve optimal performance in terms of latency, bandwidth, buffer occupancy, and power consumption.


## Implementation Details
1. Environment Setup: A simulated NOC environment that includes components like CPU, IO peripherals, and system memory. The environment provides the RL agent with the ability to observe the state of the system and the impact of its actions.

2. DQN Agent: A neural network-based agent that approximates the optimal action-value function. The agent decides on actions to take based on the current state of the NOC, aiming to improve or maintain system performance.
3. Training and Testing: The agent is trained over multiple episodes where it explores and exploits the environment to learn the best actions. After training, the agent is tested to ensure it consistently makes decisions that lead to optimal NOC performance.
4. Performance Metrics: The system's performance is evaluated based on latency, bandwidth, buffer occupancy, and power consumption. The agent receives rewards based on how well it meets these metrics, guiding its learning process.
## Complexity Analysis

- Time Complexity: The time complexity of the DQN algorithm is primarily dependent on the number of weights in the neural network and the size of the replay buffer. Training involves multiple forward and backward passes through the network for each mini-batch of experiences.

- Space Complexity: The space complexity includes the storage for the neural network's weights and the replay buffer, which holds a fixed number of state transitions.
## Testing
- Setup: Install required libraries and dependencies.
- Training: Run the training script to train the DQN agent.
- Testing: Evaluate the agent's performance using the testing script.
- Adjustments: Modify parameters and settings as needed based on specific requirements or to explore different configurations.