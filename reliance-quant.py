import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import datetime

TICKER = "RELIANCE.NS"
START_DATE = (
    datetime.date.today() - datetime.timedelta(days=5 * 365 + 10)
).strftime('%Y-%m-%d')

DAYS_TO_PLOT = 252
EMA_PERIODS = [10, 50, 200]
BB_PERIOD = 20
BB_STD = 2
RSI_PERIOD = 14

def calculate_indicators(data):
    for p in EMA_PERIODS:
        data[f'EMA_{p}'] = data['Close'].ewm(span=p, adjust=False).mean()

    mid = data['Close'].rolling(BB_PERIOD).mean()
    std = data['Close'].rolling(BB_PERIOD).std()
    data['BB_Upper'] = mid + BB_STD * std
    data['BB_Lower'] = mid - BB_STD * std
    data['BB_Middle'] = mid

    delta = data['Close'].diff()
    gain = delta.where(delta > 0, 0).rolling(RSI_PERIOD).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(RSI_PERIOD).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))

    return data

df = yf.download(TICKER, start=START_DATE)

if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)

df.dropna(inplace=True)
df = calculate_indicators(df)
plot_df = df.tail(DAYS_TO_PLOT)

addplots = []

addplots.append(mpf.make_addplot(plot_df['EMA_10'], label='EMA 10'))
addplots.append(mpf.make_addplot(plot_df['EMA_50'], label='EMA 50'))
addplots.append(mpf.make_addplot(plot_df['EMA_200'], label='EMA 200'))

addplots.append(mpf.make_addplot(plot_df['BB_Upper'], label='BB Upper'))
addplots.append(mpf.make_addplot(plot_df['BB_Lower'], label='BB Lower'))
addplots.append(
    mpf.make_addplot(plot_df['BB_Middle'], linestyle='dashed', label='BB Middle')
)

addplots.append(mpf.make_addplot(plot_df['RSI'], panel=2, label='RSI'))
addplots.append(mpf.make_addplot([70]*len(plot_df), panel=2, label='Overbought (70)'))
addplots.append(mpf.make_addplot([30]*len(plot_df), panel=2, label='Oversold (30)'))

mc = mpf.make_marketcolors(up='g', down='r', inherit=True)
style = mpf.make_mpf_style(base_mpf_style='yahoo', marketcolors=mc)

fig, axes = mpf.plot(
    plot_df,
    type='candle',
    style=style,
    title=f'{TICKER} – Technical Analysis (Last {DAYS_TO_PLOT} Days)',
    volume=True,
    addplot=addplots,
    panel_ratios=(7, 3, 3),
    figratio=(18, 14),
    figscale=2.2,
    returnfig=True
)

axes[0].legend(loc='upper left', fontsize=9)
axes[4].legend(loc='upper left', fontsize=9)

axes[0].set_ylabel("Price (INR)")
axes[2].set_ylabel("Volume")
axes[4].set_ylabel("RSI")

plt.savefig('Reliance.jpeg')
plt.show()