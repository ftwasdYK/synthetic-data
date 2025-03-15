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
```python 
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
```python 
python main.py --dir_save 'data/synthetic_data.csv' --initial_price 100 --rows 10000 --df 5 --num_events 4
```


# Synthetic data generation