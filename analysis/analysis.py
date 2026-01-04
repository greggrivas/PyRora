def compute_weekly_average(df):
    """
    Computes the weekly average Kp index.
    Returns a pandas Series indexed by the week starting date.
    """
    return df['Kp'].resample('W-MON').mean()


def monthly_stats(df, month=1):
    """
    Compute the monthly average Kp and standard deviation for a given month over all years.
    Returns a DataFrame indexed by year.
    """
    df_filtered = df[df.index.month == month]
    stats = df_filtered.groupby(df_filtered.index.year)['Kp'].agg(['mean', 'std'])
    return stats


def count_strong_events(df, threshold=6):
    """
    Count the number of strong Kp events per year.
    Returns a dictionary {year: event_count}.
    """
    df_sorted = df.sort_index()
    df_sorted['strong'] = df_sorted['Kp'] >= threshold #creates a new column strong (boolean)

    events_per_year = {}
    for year, group in df_sorted.groupby(df_sorted.index.year): #split the data in different years
        strong = group['strong'].values #create an array of the strong column 
        # Count changes from False -> True as new events
        events = 0
        in_event = False
        for val in strong:
            if val and not in_event:
                events += 1
                in_event = True
            elif not val:
                in_event = False
        events_per_year[year] = events
    return events_per_year

# CREATE LOGIC TO SAVE A CSV FILE JUST TO THE LOLZ