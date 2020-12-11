import gym

from stable_baselines3 import PPO
from stable_baselines3.ppo import MlpPolicy
from stable_baselines3.common.env_util import make_vec_env

# Parallel environments
env = make_vec_env('CartPole-v1', n_envs=4)

model = PPO(MlpPolicy, env, verbose=1)
model.learn(total_timesteps=25000)
model.save("weights/ppo_cartpole.zip")

del model # remove to demonstrate saving and loading

model = PPO.load("weights/ppo_cartpole.zip")

obs = env.reset()
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()
    
    
