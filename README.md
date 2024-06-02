# Stock-market
This project aims at emulating a small portion of the real world stock market by offering one company's stock(Tata Steel) and providing the computer 3 options namely,buying,selling and holding based on historical stock price and EPS (Earnings Per Share) data. The goal is to maximize the return on investment by learning optimal trading strategies through interaction with the stock market environment.




### Methodology

The project follows these steps to implement the trading bot:

1. **Data Loading**: Load historical EPS and stock price data from CSV files.
2. **Feature Engineering**: Extract features such as EPS growth, stock price change over six months, stock price movement in the last fifteen days, and stock price movement in the last two days.
3. **Environment Setup**: Define the states and actions for the Q-learning algorithm. Actions include buying, selling, and holding stocks.
4. **Reward Mechanism**: Implement a reward system based on the increase or decrease in portfolio value after taking an action.
5. **Q-Learning Implementation**: Use the Q-learning algorithm to update the Q-values, which represent the expected rewards for taking specific actions in given states.
6. **Training the Bot**: Train the bot over multiple episodes to learn the optimal policy for trading stocks.
7. **Execution and Evaluation**: Execute the trading strategy and evaluate the performance based on the final portfolio value.

### Approach

1. **Data Loading**
   - Load historical EPS data from `eps.csv`.
   - Load historical stock prices from `prices.csv`.

2. **Feature Engineering**
   - `six_months_price(date)`: Calculate the price change over six months.
   - `eps_growth(a, b)`: Calculate the EPS growth between two dates.
   - `last_two_quarters_eps(date)`: Determine EPS growth for the last two quarters.
   - `stock_decrease_fifteen(a)`: Check if the stock price has decreased over the last fifteen days.
   - `stock_growth(a, b)`: Compare stock prices between two dates.
   - `getstockprice(a)`: Retrieve the stock price for a given date.
   - `last_two_days(date)`: Compare stock prices for the last two days.
   - `get_last_fifteen_days_stock(date)`: Retrieve stock prices for the last fifteen days.

3. **Environment Setup**
   - Define the initial investment and the number of stocks in hand.
   - Create a Q-table to store Q-values for each state-action pair.
   - Initialize an environment matrix to store rewards for each action in each state.

4. **Reward Mechanism**
   - Define rewards for buying and selling based on the increase or decrease in portfolio value.
   - Implement functions `buy(date)` and `sell(date)` to execute trades and update rewards.

5. **Q-Learning Implementation**
   - Define parameters such as learning rate and discount factor.
   - Update Q-values using the Q-learning formula:
     ```
     Q(state, action) = Q(state, action) + learning_rate * (reward + discount * max(Q(next_state)) - Q(state, action))
     ```
   - Iterate through the environment and update Q-values based on the rewards received from actions taken.

6. **Training the Bot**
   - Randomly select actions (buy, sell, hold) during the training phase.
   - Update the Q-table based on the rewards received from the environment.
   - Train the bot over multiple episodes to learn the optimal policy.

7. **Execution and Evaluation**
   - Evaluate the performance of the bot by calculating the final portfolio value.
   - Print the final amount of money in hand and the number of stocks held.
   - Display the Q-table and environment matrix to analyze the learning process.

### Files

- `eps.csv`: Contains historical EPS data.
- `prices.csv`: Contains historical stock prices.
- `trading_bot.py`: Main script implementing the trading bot.

