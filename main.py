from stable_baselines3.ppo import CnnPolicy
from stable_baselines3 import PPO
from pettingzoo.butterfly import prison_v3
import supersuit as ss

env = prison_v3.env(vector_observation=False, continuous=False, synchronized_start=False,
                    identical_aliens=False, max_cycles=150, num_floors=4, random_aliens=False)






