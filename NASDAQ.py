import pandas as pd
# URL to NASDAQ's official list of listed companies
url = 'ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt'

# Read the CSV file into a pandas DataFrame
nasdaq_df = pd.read_csv(url, sep='|')

# Display the first few rows to verify
print(nasdaq_df.head())

# Extract the 'Symbol' column which contains the ticker symbols
tickers = nasdaq_df['Symbol'].tolist()

# Display the first few ticker symbols
print(tickers)

