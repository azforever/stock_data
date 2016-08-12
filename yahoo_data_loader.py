import pandas_datareader.data as web
import pandas as pd
import sqlite3
import datetime

conn = sqlite3.connect('/home/hwu/dev/trading/data/stock.db')


def last_update_date(symbol):
    today = datetime.datetime.today()
    last_date_table = pd.read_sql_query(
        "SELECT Date from [{}] order by Date DESC limit 1;".format(symbol),
        conn,
        parse_dates=['Date'])
    last_updated_date = last_date_table['Date'][0]
    if last_updated_date < today:
        return last_updated_date
    else:
        return today


def download(symbol):
    start = datetime.datetime(2000, 1, 1)
    end = datetime.datetime.today()
    df = web.DataReader(symbol, 'yahoo', start, end)
    df.to_sql(symbol, conn, flavor='sqlite')
    print("{} downloaded".format(symbol))


def update_table(symbol):
    ld = last_update_date(symbol)
    td = datetime.datetime.today()
    if ld.strftime("%y%m%d") < td.strftime("%y%m%d"):
        start = ld
        end = td
        df = web.DataReader(symbol, 'yahoo', start, end)
        max_date = df.index.max()
        if max_date == ld:
            # no new data is comming,
            print("no new data, {} is already up to date".format(symbol))
        else:
            df.to_sql(symbol, conn, flavor='sqlite', if_exists='append')
            print("{} updated".format(symbol))
    else:
        print("{} is already up to date".format(symbol))


download_symbols = pd.read_sql_query(
    "SELECT name from sqlite_master WHERE type='table';", conn)
download_symbols = list(download_symbols['name'])


def process_symbol(symbol):
    if symbol not in download_symbols:
        download(symbol)
    else:
        update_table(symbol)


symbols = pd.read_csv('/home/hwu/dev/trading/data/symbols.csv')
symbols = list(symbols['symbol'])
for i in symbols:
    process_symbol(i)
