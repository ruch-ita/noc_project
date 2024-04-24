env = NOCEnvironment()
agent = DQNAgent(env.state_size, 4)  # Assuming 4 possible actions

episodes = 1000
for e in range(episodes):
    state = env.reset()
    state = np.reshape(state, [1, env.state_size])
    for time in range(500):
        action = agent.act(state)
        next_state, reward, done = env.step(action)
        next_state = np.reshape(next_state, [1, env.state_size])
        agent.remember(state, action, reward, next_state, done)
        state = next_state
        if done:
            print(f"episode: {e}/{episodes}, score: {time}, e: {agent.epsilon}")
            break
        if len(agent.memory) > 32:
            agent.replay(32)