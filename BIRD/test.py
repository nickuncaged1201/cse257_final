# from dm_control import suite
# from dm_control import _render

# from dm_control.mujoco.wrapper.mjbindings import functions
# from dm_control.mujoco.wrapper import util
# mjlib = util.get_mjlib()


# from dm_control._render.pyopengl import egl_ext as EGL

# 1. It renders instance for 500 timesteps, perform random actions
# import gym
# env = gym.make('Acrobot-v1')
# env.reset()
# for _ in range(500):
#     env.render()
#     env.step(env.action_space.sample())
# # 2. To check all env available, uninstalled ones are also shown
# from gym import envs 
# print(envs.registry.all())
# env.close()

# import gym
# env = gym.make('CartPole-v0')
# print(env.action_space) #[Output: ] Discrete(2)
# print(env.observation_space) # [Output: ] Box(4,)
# env = gym.make('MountainCarContinuous-v0')
# print(env.action_space) #[Output: ] Box(1,)
# print(env.observation_space) #[Output: ] Box(2,)

import gym
env = gym.make('AlienNoFrameskip-v0')

env.reset()
action = env.action_space.sample()
obs, reward, done, info = env.step(action)

# print(obs.items())
print(len(env))
