import numpy as np
import matplotlib.pyplot as plt
from random import random
import streamlit as st

money = st.number_input("Enter your initial amount of money", min_value=0, max_value=1000000, value=25)
N = st.slider("Select the number of trades", min_value=0, max_value=1000, value=100)
win_rate = st.slider("Select your percentage of wins (of taking profit)", min_value=0, max_value=100, value=50)
risk = st.slider("Select the percentage of you account you're willing to risk at each trade", min_value=0, max_value=100, value=50)
reward = st.slider("Select the percentage of profit at which you close your trades", min_value=0, max_value=100, value=50)

trades = []
for i in range(N):
    if random() < win_rate:
        money *= 1 + reward/100
        print(i, "  ", "Take Profit", "  ", np.round(money, 2))
    else:
        money *= 1 - risk/100
        print(i, "  ", "Stop Loss", "  ", np.round(money, 2))
    trades.append(money)

fig, ax = plt.subplots()
ax.plot(list(range(N)), trades)
ax.set_xlabel('X-axis label')
ax.set_ylabel('Y-axis label')
st.pyplot(fig)
