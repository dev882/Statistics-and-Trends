"""
This is the template file for the statistics and trends assignment.
You will be expected to complete all the sections and
make this a fully working, documented file.
You should NOT change any function, file or variable names,
 if they are given to you here.
Make use of the functions presented in the lectures
and ensure your code is PEP-8 compliant, including docstrings.
"""
from corner import corner
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
import seaborn as sns

  def plot_relational_plot(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=df, x='aon', y='arpu_9', s=60, alpha=0.7, color='steelblue', ax=ax)
    ax.set_title("Scatter Plot: AON vs ARPU_9", fontsize=14, fontweight='bold')
    ax.set_xlabel("Age on Network (Days)")
    ax.set_ylabel("ARPU (Month 9)")
    plt.tight_layout()
    plt.savefig("relational_plot.png", dpi=300, bbox_inches='tight')
    plt.show()
    return

plot_relational_plot(df)


def plot_categorical_plot(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(df['aon'], bins=30, kde=True, color='skyblue', ax=ax)
    ax.set_title("Histogram: Distribution of AON", fontsize=14, fontweight='bold')
    ax.set_xlabel("Age on Network (Days)")
    ax.set_ylabel("Count")
    plt.tight_layout()
    plt.savefig("categorical_plot.png", dpi=300, bbox_inches='tight')
    plt.show()
    return

plot_categorical_plot(df)

def plot_statistical_plot(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    
    arpu_means = {
        'ARPU_6': df['arpu_6'].mean(),
        'ARPU_7': df['arpu_7'].mean(),
        'ARPU_8': df['arpu_8'].mean(),
        'ARPU_9': df['arpu_9'].mean()
    }
    sns.barplot(x=list(arpu_means.keys()), y=list(arpu_means.values()), palette="viridis", ax=ax)
    ax.set_title("Average ARPU by Month", fontsize=14, fontweight='bold')
    ax.set_xlabel("Month")
    ax.set_ylabel("Average ARPU")
    plt.tight_layout()
    plt.savefig("statistical_plot.png", dpi=300, bbox_inches='tight')
    plt.show()
    return

plot_statistical_plot(df)

def statistical_analysis(df, col: str):
    data = df[col].dropna()
    mean = data.mean()
    stddev = data.std()
    skew = ss.skew(data)
    excess_kurtosis = ss.kurtosis(data)
    return mean, stddev, skew, excess_kurtosis

moments = statistical_analysis(df, 'arpu_9')
print("Statistical Moments for arpu_9:")
print(f"Mean = {moments[0]:.2f}")
print(f"Std Dev = {moments[1]:.2f}")
print(f"Skewness = {moments[2]:.2f}")
print(f"Excess Kurtosis = {moments[3]:.2f}")


def writing(moments, col):
    print(f'For the attribute {col}:')
    print(f'Mean = {moments[0]:.2f}, '

          f'Standard Deviation = {moments[1]:.2f}, '
          f'Skewness = {moments[2]:.2f}, and '
          f'Excess Kurtosis = {moments[3]:.2f}.')
    print('The data was right/left/not skewed and platy/meso/leptokurtic.')
    return

writing(moments, df['arpu_9'] )



def preprocessing(df):
    _ = df.head()
    _ = df.describe()
    _ = df.tail()
    _ = df.corr(numeric_only=True)
    cleaned_df = df.dropna()
    print("Data cleaned. Remaining rows:", cleaned_df.shape[0])
    return cleaned_df



def main():
    df = pd.read_csv('/content/telecom_churn_data.csv')
    df = preprocessing(df)
    col = 'arpu_9'
    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)
    moments = statistical_analysis(df, col)
    writing(moments, col)
    return


if __name__ == '__main__':
    main()
