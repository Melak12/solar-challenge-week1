import pandas as pd
from scipy.stats import zscore
import numpy as np
import matplotlib.pyplot as plt

def load_data(filename, base_dir="../data"):
    """Load CSV data from the base data directory and parse Timestamp column."""
    filepath = f"{base_dir}/{filename}"
    df = pd.read_csv(filepath)
    if 'Timestamp' in df.columns:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    return df

def clean_data(df, key_columns):
    """Impute missing values and remove outliers using Z-score."""
    for col in key_columns:
        if df[col].isna().any():
            median_val = df[col].median()
            df[col].fillna(median_val, inplace=True)
    z_scores = df[key_columns].apply(zscore)
    outlier_mask = (np.abs(z_scores) > 3).any(axis=1)
    return df[~outlier_mask].copy()

def plot_time_series(df, cols, title):
    fig, ax = plt.subplots(figsize=(16, 6))
    df.set_index('Timestamp')[cols].plot(ax=ax)
    ax.set_ylabel('Value')
    ax.set_title(title)
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.show()

def plot_monthly_boxplots(df, cols):
    df['Month'] = df['Timestamp'].dt.month
    fig, axes = plt.subplots(2, 2, figsize=(16, 10))
    for i, col in enumerate(cols):
        ax = axes[i//2, i%2]
        df.boxplot(column=col, by='Month', ax=ax)
        ax.set_title(f'{col} by Month')
        ax.set_xlabel('Month')
        ax.set_ylabel(col)
    plt.suptitle('Monthly Patterns')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

def plot_hourly_trends(df, cols):
    df['Hour'] = df['Timestamp'].dt.hour
    hourly_means = df.groupby('Hour')[cols].mean()
    hourly_means.plot(figsize=(14, 6))
    plt.title('Average by Hour of Day')
    plt.xlabel('Hour')
    plt.ylabel('Mean Value')
    plt.grid(True)
    plt.show()

def save_clean_data(df, filename, base_dir="../data"):
    filepath = f"{base_dir}/{filename}"
    df.to_csv(filepath, index=False)
    print(f"Cleaned data exported to '{filepath}'.")
