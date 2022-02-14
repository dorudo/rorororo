import pyupbit
import numpy as np

#변동성 돌파 전략을 사용하기 위한 k값을 구하는 과정(고가-저가)*k
def get_ror(k=0.5):
    df = pyupbit.get_ohlcv("KRw-XRP", count=30)
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    fee = 0.0032
    df['ror'] = np.where(df['high'] > df['target'],
                         df['close'] / df['target'] ,
                         1)

    ror = df['ror'].cumprod()[-2]
    return ror


for k in np.arange(0.1, 1.0, 0.1):
    ror = get_ror(k)
    print("%.1f %f" % (k, ror))
