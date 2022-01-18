from binance import Client 
import pandas as pd 
import time 

api_key = 'KID05KbYWa3LrNphKcKAb0WMUB0yxvxvAmFUl8hKbizG1OsDx0yfgdO5W1sGftMU'
api_secret_key = 'UrIjVv3LdQsbEEBSC34NeHt9FO12nA9YNjiPsqGWDI8077bRR7tlc7Ssd0ELtQfh'
client = Client(api_key, api_secret_key)

def get_minute_data(symbol, interval, lookback):
    df = pd.DataFrame(client.get_historical_klines(symbol,
                                                   interval,
                                                   lookback + ' min ago UTC' ))

    df = df.iloc[:,:6]
    df.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    df = df.set_index('Time')
    df.index = pd.to_datetime(df.index, unit = 'ms')
    df = df.astype(float)
    df['Date'] = df.index
    df.reset_index(drop=True, inplace= True)
    df.dropna(axis=1, inplace=True)
    df['Adj Close'] = df['Close']
    df['Volume'] = df['Volume'].astype(int)
    df = df[['Date', 'Open','High','Low','Close','Adj Close','Volume']]
    return df 

df = get_minute_data('DOGEUSDT', '1d', '200000')
print(df.head())
df.to_csv('ada.csv')



