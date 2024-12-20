import pandas as pd
import sqlite3

import logging
logger = logging.getLogger()

logging.basicConfig(
    filename=r'C:\Users\Max\.vscode\Kunskapskontroll\log.log',
    format='[%(asctime)s][%(levelname)s]%(message)s',
    level=logging.DEBUG,
    datefmt= '%y-%m-%d %H:%M')

logger.info('Hello')

logging.debug('This is a debug-level log record')
logging.info('This is a info-level log record')
logging.warning('This is a warning-level log record')
logging.error('This is a error-level log record')
logging.critical('This is a critical-level log record')


con = sqlite3.connect('Nvidia_stock.db')

df = pd.read_csv('C:/Users/Max/.vscode/kunskapskontroll/NVIDIA_STOCK.csv')

df['Date'] = df['Price'] 

new_df = df.drop(columns=['Price']) 

try:   
    df['Date'] = pd.to_datetime(df['Date'])
except Exception as e:
    logging.critical(e)
    pass

    
start_date = '2023-01-01'
end_date = '2023-07-01'

new_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

selected_colums = ['Date','Open', 'Close']
new_df = new_df[selected_colums]

new_df.to_sql('NVIDIA_STOCK.csv', con, if_exists='replace')

def validate_open_close(df):
    """
    Kontrollera att kolumnerna "Open" och "Close" innehåller numeriska värden.

    >>> data = {'Open': [15, 41 ], 'Close': [14, 42]}
    >>> test_df = pd.DataFrame(data)
    >>> validate_open_close(test_df)
    True

    >>> invalid_data = {'Open': [14, 'text'], 'Close': [100, 41]}
    >>> invalid_df = pd.DataFrame(invalid_data)
    >>> validate_open_close(invalid_data)
    False
    """
    try:
        # Kontrollerar att "Open" och "Close" är numeriska
        pd.to_numeric(df['Open'])
        pd.to_numeric(df['Close'])
        return True
    except Exception:
        return False
    
import doctest
doctest.testmod()

data = {'Open': [14, 30], 'Close': [14, 42]}
df = pd.DataFrame(data)

print(validate_open_close(data))  # Förväntat resultat: True

invalid_data = {'Open': [14, 'text'], 'Close': [14, 30]}
invalid_df = pd.DataFrame(invalid_data)

print(validate_open_close(invalid_data))  # Förväntat resultat: False


def Price_risen_over_period(df, start_date, end_date):
    """
    Kontrollerar om värdena i kolumnerna "Open" och "Close" har stigit
    från det första datumet till det sista datumet inom en angiven period.

    Exempel:
    >>> data = {'Date': [start_date, end_date]}
    >>> test_df = pd.df(data)
    True
    """
   
    # Hämta värden för det första och sista datumet
    first_row = df.iloc[0] 
    last_row = df.iloc[-1]
    
     # Kontrollera om "öppning" och "stängning" har stigit
    return (last_row['Open'] > first_row['Close']) and (last_row['Open'] > first_row['Close'])

print(Price_risen_over_period(df, start_date, end_date))  # Förväntat resultat: True







