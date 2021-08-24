"""
This part of code is the Q learning brain, which is a brain of the agent.
All decisions are made in here.

View more on my tutorial page: https://morvanzhou.github.io/tutorials/
"""

import numpy as np
import pandas as pd

# greedy 10%  this is different from the tradition 0.9
class QLearningTable:
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.1):
        self.actions = actions  # a list
        self.lr = learning_rate
        self.gamma = reward_decay
        self.epsilon = e_greedy
        self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)

    # In our situation, action space is Real-time changing
    # After choosing one action (one attribute), this action will be removed from action space.
    def choose_action(self, observation, action_space):
        choose_flag = 0
        choose_flag = self.check_state_exist(observation, choose_flag)

        if choose_flag == 1:        #(if this is a new created state, we will randomnly choose a action)
            action = np.random.choice(action_space)
            if action in action_space:
                action_space.remove(action)
        else:
            # action selection
            if np.random.uniform() < self.epsilon:
                # choose best action
                state_action = self.q_table.loc[observation, :]
                # some actions may have the same value, randomly choose on in these actions
                action = np.random.choice(state_action[state_action == np.max(state_action)].index)

                if action in action_space:
                    action_space.remove(action)
            else:
                # choose random action
                action = np.random.choice(action_space)
                if action in action_space:
                    action_space.remove(action)

        # if action space is empty, this means we will finish this episode after the following join
        if action_space:     #the empty list is false
            done = False
        else:
            done = True

        return action, action_space, done

    # def learn(self, s, a, r, s_, done):
    #     self.check_whether_state_exist(s_)
    #     q_predict = self.q_table.loc[s, a]   #inintial 0
    #     if done == False:
    #         maxExpectedValue = self.q_table.loc[s_, :].max()
    #         q_target = r + self.gamma * maxExpectedValue  # next state is not terminal
    #     else:
    #         q_target = r  # next state is terminal
    #     self.q_table.loc[s, a] += self.lr * (q_target - q_predict)  # update
    #
    #     return maxExpectedValue      #for second Qtable calculatiing max expected value going forward


    def learn(self, s, a, r, s_):
        self.check_whether_state_exist(s_)
        q_predict = self.q_table.loc[s, a]   #inintial 0

        maxExpectedValue = self.q_table.loc[s_, :].max()
        q_target = r + self.gamma * maxExpectedValue  # next state is not terminal

        self.q_table.loc[s, a] += self.lr * (q_target - q_predict)  # update

        return maxExpectedValue      #for second Qtable calculatiing max expected value going forward


    def secondTableLearn(self, s, a, r,maxExpect):
        q_predict = self.q_table.loc[s, a]  # inintial 0
        q_target = r + self.gamma * maxExpect  # next state is not terminal
        self.q_table.loc[s, a] += self.lr * (q_target - q_predict)  # update




    def check_state_exist(self, state, flag):
        if state not in self.q_table.index:
            # append new state to q table
            self.q_table = self.q_table.append(
                pd.Series(
                    [0] * len(self.actions),    # (column dimension is same as the size of initial action space)
                    index=self.q_table.columns,
                    name=state,
                )
            )
            flag = 1
        return flag

    def check_whether_state_exist(self, state):
        if state not in self.q_table.index:
            # append new state to q table
            self.q_table = self.q_table.append(
                pd.Series(
                    [0] * len(self.actions),
                    index=self.q_table.columns,
                    name=state,
                )
            )




    # In our situation, action space is Real-time changing
    # After choosing one action (one attribute), this action will be removed from action space.
    def secondTable_choose_action(self, observation, action_space):
        self.check_whether_state_exist(observation)      #observation: 1, 2, 3, 4, ... (single table name id)

        # action selection
        if np.random.uniform() < self.epsilon:
            # choose best action
            state_action = self.q_table.loc[observation, :]
            # some actions may have the same value, randomly choose on in these actions
            action = np.random.choice(state_action[state_action == np.max(state_action)].index)

        else:
            # choose random action
            action = np.random.choice(action_space)



        return action
