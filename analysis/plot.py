import matplotlib.pyplot as plt

def plot_weekly_average(weekly_series):
    plt.figure(figsize=(10,4))
    weekly_series.plot(kind='line', figsize=(10,4))
    plt.title("Weekly Average Kp")
    plt.ylabel("Kp")
    plt.xlabel("Week Start")
    plt.ylim(0, 11) 
    # plt.show(block=False)

# def plot_strong_events(events_dict):
#     plt.figure(figsize=(10,4))
#     years = list(events_dict.keys())
#     counts = list(events_dict.values())
#     plt.bar(years, counts)
#     plt.title("Strong Kp Events per Year")
#     plt.ylabel("Number of Events")
#     plt.xlabel("Year")
#     # plt.show(block=False)
    
def plot_strong_events(events_dict):
    years = sorted(events_dict.keys())  # numeric
    counts = [events_dict[y] for y in years]
    plt.figure(figsize=(10,4))
    plt.bar(years, counts)
    plt.title("Strong Kp Events per Year")
    plt.ylabel("Number of Events")
    plt.xlabel("Year")
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)


def plot_monthly_stats(stats_df, month):
    """
    Plot monthly average Kp with standard deviation as error bars.
    
    stats_df: DataFrame with 'mean' and 'std' columns
    month: integer
    """
    x = stats_df.index.values  # numeric years
    y = stats_df['mean']
    yerr = stats_df['std']

    plt.figure(figsize=(10, 4))  # separate window
    plt.errorbar(x, y, yerr=yerr, fmt='-o', capsize=4, ecolor='red', elinewidth=1.5)
    plt.title(f"Monthly Average Kp for Month {month}")
    plt.xlabel("Year")
    plt.ylabel("Kp")
    plt.grid(True)
    # plt.show(block=False)  # allows multiple figures to pop up simultaneously


