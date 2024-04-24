def test_agent(env, agent, test_episodes):
    total_rewards = 0
    for e in range(test_episodes):
        state = env.reset()
        state = np.reshape(state, [1, env.state_size])
        episode_rewards = 0
        while True:
            action = agent.act(state)  # Choose the best action based on learned policy
            next_state, reward, done = env.step(action)
            episode_rewards += reward
            next_state = np.reshape(next_state, [1, env.state_size])
            state = next_state
            if done:
                break
        total_rewards += episode_rewards
        print(f"Test Episode {e+1}/{test_episodes}: Reward: {episode_rewards}")
    average_reward = total_rewards / test_episodes
    print(f"Average Reward over {test_episodes} test episodes: {average_reward}")
    return average_reward

# Set the epsilon to a low value to use the learned policy
agent.epsilon = 0.01

# Test the agent
test_episodes = 100
average_reward = test_agent(env, agent, test_episodes)