import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulated monthly returns for 3 assets
returns = {
    'Asset A': np.random.normal(loc=1.5, scale=2.0, size=12),
    'Asset B': np.random.normal(loc=1.0, scale=1.2, size=12),
    'Asset C': np.random.normal(loc=0.6, scale=0.8, size=12),
}

df = pd.DataFrame(returns)
risk_free_rate = 0.25  # monthly risk-free rate in %

# Sharpe Ratio = (Mean Return - Risk-free rate) / Std Dev
sharpe_ratios = {}
for asset in df.columns:
    mean_return = np.mean(df[asset])
    std_dev = np.std(df[asset])
    sharpe = (mean_return - risk_free_rate) / std_dev
    sharpe_ratios[asset] = sharpe

# Plot Sharpe Ratios
plt.figure(figsize=(8, 5))
plt.bar(sharpe_ratios.keys(), sharpe_ratios.values(), color='skyblue')
plt.title('Sharpe Ratios of Simulated Assets')
plt.xlabel('Assets')
plt.ylabel('Sharpe Ratio')
plt.grid(True, axis='y')
plt.savefig("portfolio_returns.png")
plt.show()
