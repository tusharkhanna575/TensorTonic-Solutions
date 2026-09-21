def lag_features(series: list, lags: list) -> list:
    """
    Returns the lag feature matrix.
    """
    # Write code here
    maxi=max(lags)
    res=[]

    for i in range(maxi, len(series)):
        res.append([series[i-j] for j in lags])

    return res