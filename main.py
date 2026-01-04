from utils.downloader import download_wdc
from analysis.parser import wdc_to_dataframe
from analysis.analysis import compute_weekly_average, count_strong_events, monthly_stats
from analysis.plot import plot_weekly_average, plot_strong_events, plot_monthly_stats
import matplotlib.pyplot as plt
import pandas as pd
import os

# if __name__ == "__main__":
#     # Download Kp data for a specific year
#     files = download_wdc([2024])  # returns list of file paths
#     if not files:
#         print("No files downloaded, exiting.")
#         exit()
        
#     file_path = files[0]
#     df_kp = wdc_to_dataframe(file_path)

if __name__ == "__main__":
    files = download_wdc([2015,2016,2017,2018,2019,2020,2021,2022,2023,2024])
    # df = wdc_to_dataframe(files[0])
    df_list = [wdc_to_dataframe(f) for f in files]  # parse each file
    df = pd.concat(df_list)  # merge into one DataFrame
    df.sort_index(inplace=True)  # ensure it's sorted by datetime

    weekly_avg = compute_weekly_average(df)
    plot_weekly_average(weekly_avg)

    events = count_strong_events(df)
    plot_strong_events(events)

    month_stats = monthly_stats(df, month=1)
    plot_monthly_stats(month_stats, month=1)
    plt.show()
