import gym
import numpy as np
import pandas as pd

reward_list = []
player_0_hands = []
player_2_hands = []
NUM_EPISODES = 100000

env = gym.make('coinche.gym.env:coinche-v0')
env.__init__()

for i_episode in range(NUM_EPISODES):
    env.reset()
    total_round_reward = 0

    if i_episode % 500 == 0:
        print(i_episode)

    while True:
        # try:
        action = env.action_space.sample()  # Use a random action
        observation, reward, done, info = env.step(action)  # to take a single step in the environment
        total_round_reward += reward
        if done:
            reward_list.append(total_round_reward)
            player_0_hands.append(info["player0-hand"])
            player_2_hands.append(info["player2-hand"])
            break

    env.close()  # Close the environment

player_0_hands = np.array(player_0_hands)
player_2_hands = np.array(player_2_hands)
reward_list = np.array(reward_list).reshape((len(reward_list), 1))

data = np.concatenate([player_0_hands, player_2_hands, reward_list], axis=1)

df = pd.DataFrame(data)
df.to_csv("hands_and_reward.csv")