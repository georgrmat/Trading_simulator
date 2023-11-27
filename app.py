import numpy as np
import matplotlib.pyplot as plt
from random import random
import streamlit as st

# Title
st.title("Optimizing Trading Strategies: Evaluate Profitability, Risk, and Rewards")

# Introductory Text
st.write(
    "Welcome to this trading simulator !\n\n"
    "Explore different trading scenarios by adjusting the number of trades, win rate, risk, and reward.\n"
    "Assess the potential long-term profitability of your trading strategy."
)

money = st.number_input("**Initial capital of investment**", min_value=0, max_value=1000000, value=100)
N = st.slider("**Number of trades**", min_value=0, max_value=500, value=100)
win_rate = st.slider("**Win rate**: percentage of trades that hit take profit", min_value=0, max_value=100, value=50)
risk = st.slider("**Risk per trade**: percentage of your account that you are prepared to allocate for risk in each trade (for a long term strategy and if you're a beginner, don't risk more that 1% per trade)", min_value=0, max_value=100, value=1)
reward = st.slider("**Profit per trade**: targeted percentage of your account that you aim to achieve as profit (an excessively ambitious target is less likely to be consistently achieved)", min_value=0, max_value=100, value=3)

trades = []
for i in range(N):
    if random() < win_rate/100:
        money *= 1 + reward/100
    else:
        money *= 1 - risk/100
    trades.append(money)

fig, ax = plt.subplots()
ax.plot(list(range(N)), trades)
ax.set_xlabel('Trade number (can be seen as time)')
ax.set_ylabel('Portfolio ($)')
st.pyplot(fig)
