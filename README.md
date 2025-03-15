# Project description

The aim of the project is to generate realistic synthetic data for stock prices and volumes.

The synthetic data is composed of the following columns:

* Stock Price: The stock price at the end of the trading day
* Volume: The volume of the stock traded during the trading day
* SMA_10: The simple moving average of the stock price over the last 10 trading days
* EMA_10: The exponential moving average of the stock price over the last 10 trading days
* RSI: The relative strength index of the stock price over the last 14 trading days
* MACD: The moving average convergence divergence of the stock price
* Signal Line: The signal line of the stock price
* Bollinger Bands: The upper and lower Bollinger Bands of the stock price over the last 20 trading days
generated using the following steps:

# Synthetic data generation

## Stock Price
For the generation of the returns of a stock price a t-distribution is used with a given number of degrees of freedom (df) and a given number of trading days (days).
Also some jumps are added to the returns of the stock price using a Poisson distribution with a given number of events per year (num_events) and scaling it with a normal distribution. 
This simulates some events that can affect the stock price. After generating the returns, the stock price is calculated by multiplying the returns with the previous stock price, starting from the initial stock price.

## Volume

The volume is generated using a log-normal distribution with a given mean (mu_volume) and standard deviation (sigma_volume). 
Also the volume has an autocorrelation factor (rho) that makes the volume of the next day dependent on the volume of the previous day.

## Exponential and Simple Moving Averages

The SMA_10 is calculated as the simple moving average of the stock price over the last 10 trading days. 
The EMA_10 is calculated as the exponential moving average of the stock price over the last 10 trading days. 

## Relative Strength Index

The RSI is calculated as the relative strength index of the stock price over the last 14 trading days.
The RSI is a momentum oscillator that measures the speed and change of price movements.
The RSI oscillates between 0 and 100, with values above 70 indicating that the stock is overbought and values below 30 indicating that the stock is oversold.
The RSI is calculated using the following formula:

$$ RSI = 100 - (100 / (1 + RS)) $$

Where RS is the relative strength, which is the average gain over the last 14 days divided by the average loss over the last 14 days.

The RSI is calculated using the following steps:
1. Calculate the price change from the previous day
2. Calculate the gain and loss from the previous day
3. Calculate the average gain and loss over the last 14 days
4. Calculate the relative strength (RS) as the ratio of the average gain to the average loss
5. Calculate the RSI as $100 - (100 / (1 + RS))$

## Moving Average Convergence Divergence 

The MACD is a trend-following momentum indicator that shows the relationship between two moving averages of the stock price.
The MACD is calculated as the difference between the 12-day and 26-day exponential moving averages of the stock price.

## Signal Line

The signal line is an indicator used in technical analysis to generate buy and sell signals.
The Signal Line is calculated as the 9-day exponential moving average of the MACD.
 

## Bollinger Bands

The Bollinger Bands are a volatility indicator that consists of a simple moving average (SMA) and two standard deviations (bands) above and below the SMA.
The Bollinger Bands are used to identify overbought and oversold conditions in the stock price.

The Bollinger Bands are calculated as follows:
1. Calculate the 20-day simple moving average of the stock price
2. Calculate the standard deviation of the stock price over the last 20 days
3. Calculate the upper Bollinger Band as the SMA plus two standard deviations
4. Calculate the lower Bollinger Band as the SMA minus two standard deviations

# Installation and package management

First we need to initialize the virtual environment. This is done by running the following command in the terminal:

```bash
python3 -m venv myvenv
```

Next, we need to activate the virtual environment. This is done by running the following command in the terminal:

```bash
source myvenv/bin/activate
```

Now we need to install the required packages. This is done by running the following command in the terminal:
```bash
pip install -r requirements.txt
```

# Running the application
```bash 
python main.py
```

This script will generate synthetic data with default parameters and create a .csv file with the data in the default directory 'data/synthetic_data.csv'.

The arguements for the script are as follows:
* dir_save: directory to save the synthetic data (default = 'data/synthetic_data.csv')
* initial_price: Initial stock price (default=100)
* rows: number of samples (rows) in the dataset (default = 10000). 
* df: Degrees of freedom for t-distribution, bigger values are closer to normal distribution (default = 5)
* num_events: Number of events per year on average for 252 days of trading (default = 4)

So in order to change the default parameters, the script can be run as follows:
```bash 
python main.py --dir_save 'data/synthetic_data.csv' --initial_price 100 --rows 10000 --df 5 --num_events 4
```

**Note**: ***The default value for rows (samples) is equivalent to ~40 years of trading.*** 