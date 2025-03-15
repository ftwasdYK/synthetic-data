import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_volume(volumes:np.array):
    plt.figure(figsize=(10, 5))
    plt.plot(volumes, label="Simulated Trading Volume", color='green')
    plt.xlabel("Days")
    plt.ylabel("Trading Volume")
    plt.show()

def plot_stock_price(prices:np.array):
    plt.figure(figsize=(10, 5))
    plt.plot(prices, label="Stock Price", color='blue')
    plt.xlabel("Days")
    plt.ylabel("Stock Price")
    plt.title("Simulated Stock Price with Student's t-Distributed Returns and a mixture of Poisson-Based Jumps")
    plt.legend()
    plt.show()

def plot_hist(data:np.array, bins:int=100, color:str='blue', alpha:float=0.6):
    # Plot histogram
    plt.figure(figsize=(10, 6))
    sns.histplot(data, bins=100, kde=True, color='blue', alpha=0.6)

    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title("Histogram of Generated Data")
    plt.show()