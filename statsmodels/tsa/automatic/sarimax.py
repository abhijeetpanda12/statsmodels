"""automatic forecasting for SARIMAX models."""
import numpy as np
import pandas as pd
import statsmodels.api as sm

def auto_order(endog, criteria='aic', d=0, max_order=(3, 3), spec=None):
    """Auto order function for SARIMAX models."""
    aic_matrix = np.zeros(p, q)
    for p in range(max_order[0]):
        for q in range(max_order[1]):
            if p == 0 and q == 0:
                continue
            # fit  the model
            mod = sm.tsa.statespace.SARIMAX(endog, order=(p, d, q), **spec)
            res = mod.fit(disp=False)
            aic_matrix[p, q] = res.aic
    min_aic = aic_matrix.min()
    p, q = np.where(aic_matrix == min_aic)
