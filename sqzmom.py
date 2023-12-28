import pandas_ta as ta

def sqzmom(df, length=20, lengthKC=20, multKC=1.5):
    """
    A Python implementation of Squeeze Momentum
    https://pastebin.com/UCpcX8d7
    """
    # Calculate Bollinger Bands
    indicator_bb = ta.bbands(close=df["close"], length=length, std=multKC)
    df["bb_upper"] = indicator_bb[indicator_bb.columns[2]]
    df["bb_lower"] = indicator_bb[indicator_bb.columns[0]]

    # Calculate Keltner Channel
    indicator_kc = ta.kc(high=df["high"], low=df["low"], close=df["close"], length=lengthKC, scalar=multKC)
    df["kc_upper"] = indicator_kc[indicator_kc.columns[2]]
    df["kc_lower"] = indicator_kc[indicator_kc.columns[0]]

    # Squeeze conditions
    df["squeeze_on"] = (df["bb_lower"] > df["kc_lower"]) & (df["bb_upper"] < df["kc_upper"])
    df["squeeze_off"] = (df["bb_lower"] < df["kc_lower"]) & (df["bb_upper"] > df["kc_upper"])
    df["no_squeeze"] = (df["squeeze_on"] == False) & (df["squeeze_off"] == False)

    # Squeeze Momentum
    # linear_regression = ta.LinearRegression(close=df["close"], length=lengthKC, offset=0)
    # df["squeeze_mom"] = linear_regression.slope

    return df
