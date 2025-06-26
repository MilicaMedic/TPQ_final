# Deep Reinforcement Learning for the Multiple Cryptocurrency Trading Using an Ensemble Strategy

The objective of this project is to implement an automated solution for trading multiple cryptocurrencies by using the Ensembled trading strategy that consist of the following Deep Reinforcement Learning (DRL) agents: Proximal Policy Optimization (PPO), Advantage Actor-Critic (A2C), and Deep Deterministic Policy Gradient (DDPG). The Ensembled strategy combines the best features of the three algorithms, aiming to create a robust solution for adjusting to different market conditions, with the goal to maximize the profits (returns). The project trains, and trades, on the same dataset, all three agents, the Ensemble strategy, and the min-variance as baseline, and gives a performance comparison of all strategies.

All three agents in the Ensemble stragegy are trained at the same time, quarterly (3-month period), and after each time the best agent is selected based on their Sharpe ratio and used for trading in the next quarter.

For this project the FinRL, an open source framework for financial reinforcement learning, is used. This work includes 5 crypto tokens that have adequate liquidity, market capitalisation and, also, to how long the coin is listed (how long the data exists, so that it went through a couple of bull/bear cycles).

The following results are achieved in a simulation with the 100000 timesteps:


<img width="1050" alt="Final - 100000 ts" src="https://github.com/user-attachments/assets/c80e8abe-09d5-4482-9a87-ee039bdb588c" />


Parallel testing of strategies, with DDPG and TD3, resulted with TD3 perform much better as a standalone model, and DDPG usually having the worst standalone performance. However, in the Ensemble strategy, when the TD3 model was used the Ensemble strategy had the lower performance, than when using the DDPG model.

Furthermore, the unstable behaviour of standalone models (specifically A2C and DDPG, where PPO showed to be the most stable) using the same data and same hyperparameters, made them sometimes overperform the Ensemble strategy, but in other cases with the same setting (same parameters and environment) have suboptimal outcome.

The number of timesteps for agents is one the parameters that has the biggest influence on how the agents behave and perform. Also, all models and strategies have low performance when prices are declining, which can be seen on a plot in April 2025., when all five cryptocurrencies had a significant price drop. Similarily, in December 2024., all five cryptocurrencies had a significant surge in prices which reflected on the agents and strategies performance.

The most capable in following trends and volatile market, even with the small number of timesteps (tested on 5000 timesteps) is the PPO model, where it outperformed all other strategies, as it can explore early, and then exploit policies with clipped updates.

The A2C model shows fastest reactions to price changes, but doesn't have a good performance in a bear market, thereforet it would be a good choice in a flat market, or a stable or sideways markets. This behaviour is probably because of the liability of the A2C algorithm toward overfitting, which would make it a bad choice to use alone in the real-world crypto trading.

The worst performance was shown by the DDPG agent, because of its buy/hold early strategy where its performance deprecates when the prices are in down.

Good performance of a single agent does not guarantee the best performance of the Ensemble strategy. Therefore, the Ensemble strategy is a good strategy to combine the three models utilising the best properties of each DRL algorithm.

<img width="445" alt="Perf final - 100000 ts" src="https://github.com/user-attachments/assets/c333fee0-abe8-4740-8b2c-4d77b72dfd51" />

From the performance table we can see that the Ensemble strategy performed the best in all categories. This result shows that even if the individual agents didn't perform superior, the Ensemble strategy managed to exploit the strenghts the inividual agents to achieve the best performance in all categories, which was the goal of the project.

The idea for this project is based on the following work:

Yang, Hongyang and Liu, Xiao-Yang and Zhong, Shan and Walid, Anwar, Deep Reinforcement Learning for Automated Stock Trading: An Ensemble Strategy (September 11, 2020). Available at SSRN: https://ssrn.com/abstract=3690996 or http://dx.doi.org/10.2139/ssrn.3690996

