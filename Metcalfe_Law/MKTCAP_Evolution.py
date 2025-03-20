import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load data
file_path = "/Users/tedig/Downloads/CoinGecko-GlobalCryptoMktCap-2025-03-15.csv"
df = pd.read_csv(file_path)

# Convert timestamp to datetime
df.iloc[:, 0] = pd.to_datetime(df.iloc[:, 0], unit='ms')

# Calculate rolling standard deviation (volatility)
window_size = 7  # Adjust the window size as needed
df["Volatility"] = df.iloc[:, 1].rolling(window=window_size).std()

# Create plot with transparency
fig, ax = plt.subplots(figsize=(10, 5))
fig.patch.set_alpha(0)
ax.patch.set_alpha(0)

# Plot Market Cap
ax.plot(df.iloc[:, 0], df.iloc[:, 1], marker=".", linestyle="-", color="blue", label="Market Cap")


# Format x-axis
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.xaxis.set_major_locator(mdates.AutoDateLocator())
plt.xticks(rotation=45, fontsize=7)

# Labels
ax.set_xlabel(df.columns[0], color='black')
ax.set_ylabel("Market Cap", color='black')

# Add legend
ax.legend()

# Show plot
plt.show()
