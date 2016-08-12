change the path:


```
conn = sqlite3.connect('/home/hwu/dev/trading/data/stock.db')
```


```
symbols = pd.read_csv('/home/hwu/dev/trading/data/symbols.csv')
```


run 

```
python ./yahoo_data_loader.py


the data will be stored in the sqlite db


```
sqlite3 stock.db
sqlite> select * from BABA limit 5;
2014-09-19 00:00:00|92.699997|99.699997|89.949997|93.889999|271879400|93.889999
2014-09-22 00:00:00|92.699997|92.949997|89.5|89.889999|66657800|89.889999
2014-09-23 00:00:00|88.940002|90.480003|86.620003|87.169998|39009800|87.169998
2014-09-24 00:00:00|88.470001|90.57|87.220001|90.57|32088000|90.57
2014-09-25 00:00:00|91.089996|91.5|88.5|88.919998|28598000|88.919998

```

each symbol in symbols.csv will have a table in sqlite db
