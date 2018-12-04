import requests
import pandas as pd
import plotly.plotly as py
import plotly
import plotly.graph_objs as go
from plotly.graph_objs import Scatter, Layout
import pandas as pd
from scipy import stats

proxyDict = {
    # "http": "http://proxy.intra.bt.com:8080",
    "https": "http://proxy.intra.bt.com:8080"
    # "ftp": ftp_proxy
}
# Create URL to JSON file (alternatively this can be a filepath)
url = 'https://api.coindesk.com/v1/bpi/historical/close.json?start=2011-01-01&end=2018-11-23'

r = requests.get(url, proxies=proxyDict)

j = r.json()
print(plotly.__version__)  # version >1.9.4 required

# print(j['bpi'])
# df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")
# df = j['bpi']
df = pd.DataFrame(list(j['bpi'].items()), columns=['Date', 'DateValue'])
print(df.Date)
# data = [go.Scatter(
#     x=df.Date,
#     y=df['DateValue'])]

# py.iplot(data)
x = df.index
y = df.DateValue
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
r = df.index*(r_value**2)
# print(r)

print(slope, intercept, r_value, p_value, std_err)
plotly.offline.plot({
    "data": [
        Scatter(x=df.Date, y=df.DateValue),
        Scatter(x=df.Date, y=r)
    ],
    "layout": Layout(
        title="BTC/USD R^2 = "+str(r_value**2),
        yaxis=dict(
            type='log',
            autorange=True
        )
    )
})
