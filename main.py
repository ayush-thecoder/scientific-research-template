import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("Loading example data...")
    df = pd.read_csv('../data/example.csv')
    print("Generating plot...")
    plt.plot(df['time'], df['value'], marker='o')
    plt.title('Example Plot')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.savefig('../figures/example-plot.png')
    print("Plot saved to figures/example-plot.png")

if __name__ == '__main__':
    main()
