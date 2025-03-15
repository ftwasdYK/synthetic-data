import numpy as np
import scipy.stats as stats
import pandas as pd
import os
import argparse

from utils.plots import plot_volume, plot_stock_price, plot_hist

def generate_stock_price(initial_price:float=100, days:int=10000, df:int=5, num_events:int=4):
    print(f'{days} days is equivalent to ~ {days/252:.2f} years of trading.')
    
    # sigma = # Daily volatility
    dist_t = stats.t.rvs(df, size=days) 
    returns = 0.01 * dist_t # Expected daily return
    # num of events per year on average for 252 days of trading
    dist_p = np.random.poisson(num_events/252, days)
    # Add Poisson-Based Jumps and scale them with a normal distribution in order to have jumps lower than 1.
    jumps = dist_p * np.random.normal(0, 0.09, days)
    returns += jumps  # Add jump effect to returns
    plot_hist(returns)

    prices = [initial_price]
    for r in returns:
        prices.append(prices[-1] * np.exp(r))  # pseudo GBM formula
    plot_stock_price(prices)

    return prices

def generate_volume(days:int=10000):
    # Parameters
    days += 1
    mu_volume = 12  # Mean of log-volume
    sigma_volume = 1  # Std dev of log-volume
    rho = 0.7  # Autocorrelation factor (0 = no memory, 1 = full memory)

    # Generate Log-Normal Volume
    log_volumes = np.random.normal(mu_volume, sigma_volume, days)
    volumes = np.exp(log_volumes)  # Convert to real-world volume

    # Add Autocorrelation
    for days in range(1, days):
        volumes[days] = rho * volumes[days-1] + (1 - rho) * volumes[days]
    
    plot_volume(volumes)
    return volumes

    
def create_synthetic_data(dir_save:str='data/synthetic_data.csv', initial_price:float=100, rows:int=10000, df:int=5, num_events:int=4):
    days = rows
    stock_price = generate_stock_price(initial_price, days, df=df, num_events=num_events)
    volumes = generate_volume()

    # make it a dataframe
    df = pd.DataFrame({'stock_price': stock_price, 'volume': volumes})

    ## Add some additional synthetic data ##
    # Moving Averages
    df['SMA_10'] = df['stock_price'].rolling(window=10).mean()
    df['EMA_10'] = df['stock_price'].ewm(span=10, adjust=True).mean()
    
    # MACD
    df['MACD'] = df['stock_price'].ewm(span=12, adjust=True).mean() - df['stock_price'].ewm(span=26, adjust=True).mean()
    df['Signal_Line'] = df['MACD'].ewm(span=9, adjust=True).mean()
    
    # RSI
    delta = df['stock_price'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))

    # Bollinger Bands
    df['Middle_Band'] = df['stock_price'].rolling(window=20).mean()
    df['Upper_Band'] = df['Middle_Band'] + (df['stock_price'].rolling(window=20).std() * 2)
    df['Lower_Band'] = df['Middle_Band'] - (df['stock_price'].rolling(window=20).std() * 2)
    ##
    df.dropna(inplace=True)
    
    if not os.path.exists(os.path.dirname(dir_save)):
        os.makedirs(os.path.dirname(dir_save))  # Creates the directory if it doesn't exist

    # save to csv
    df.to_csv(dir_save, index=False)

if __name__ == "__main__":
    # parse arguments
    parser = argparse.ArgumentParser(description='Create synthetic data')
    parser.add_argument('--dir_save', type=str, default='data/synthetic_data.csv', help='Directory to save the synthetic data')
    parser.add_argument('--initial_price', type=float, default=100, help='Initial stock price')
    parser.add_argument('--rows', type=int, default=10000, help='Number of rows to generate')
    parser.add_argument('--df', type=int, default=5, help='Degrees of freedom for t-distribution, bigger values are closer to normal distribution')
    parser.add_argument('--num_events', type=int, default=4, help='Number of events per year on average for 252 days of trading')
    args = parser.parse_args()
    create_synthetic_data(args.dir_save, args.initial_price, args.rows, args.df, args.num_events)
    print(f'Synthetic data saved to {args.dir_save}')