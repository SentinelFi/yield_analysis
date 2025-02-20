import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parameters
π = 20  # Premium per policy ($)
λ = 100  # Payout per claim ($)
M = 10000  # Number of policies sold
C = 100000  # Initial capital ($)
num_simulations = 10000  # Number of Monte Carlo simulations
p_range = (0.01, 0.20)  # Delay probability range (1% to 20%)

# Monte Carlo Simulation
np.random.seed(42)  # For reproducibility
p_simulated = np.random.uniform(p_range[0], p_range[1], num_simulations)
yield_simulated = (M * (π - λ * p_simulated)) / C * 100  # Yield in percentage

# Compute statistics
mean_yield = np.mean(yield_simulated)
percentile_5 = np.percentile(yield_simulated, 5)
percentile_95 = np.percentile(yield_simulated, 95)

# Plot Distribution of Yields
plt.figure(figsize=(10, 6))
plt.hist(yield_simulated, bins=50, alpha=0.7, edgecolor='black')
plt.axvline(mean_yield, color='red', linestyle='dashed', linewidth=2, label=f'Mean Yield: {mean_yield:.2f}%')
plt.axvline(percentile_5, color='blue', linestyle='dashed', linewidth=2, label=f'5th Percentile: {percentile_5:.2f}%')
plt.axvline(percentile_95, color='green', linestyle='dashed', linewidth=2, label=f'95th Percentile: {percentile_95:.2f}%')

plt.xlabel("Yield (%)")
plt.ylabel("Frequency")
plt.title("Monte Carlo Simulation: Distribution of Expected Yields")
plt.legend()
plt.grid(True)
plt.show()

# Display summary statistics
results_df = pd.DataFrame({
    "Statistic": ["Mean Yield", "5th Percentile", "95th Percentile"],
    "Value (%)": [mean_yield, percentile_5, percentile_95]
})

print(results_df)
