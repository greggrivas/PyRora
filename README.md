# PyRora

A Python school project for analyzing and visualizing geomagnetic Kp index data. PyRora downloads definitive Kp index data from the GFZ Potsdam repository and provides tools for analyzing geomagnetic activity trends, strong events, and monthly statistics.

## Overview

The Kp index is a measure of geomagnetic activity ranging from 0 (quiet) to 9 (extreme). This project:
- **Downloads** WDC (World Data Center) Kp data files for specified years
- **Parses** Kp index data from `.wdc` files into pandas DataFrames
- **Analyzes** geomagnetic activity through multiple metrics
- **Visualizes** trends and patterns in historical Kp data

## Project Structure

```
PyRora/
├── main.py                 # Entry point, orchestrates download and analysis
├── analysis/
│   ├── analysis.py        # Analysis functions (weekly averages, events, monthly stats)
│   ├── parser.py          # WDC file parser
│   └── plot.py            # Visualization functions
├── utils/
│   └── downloader.py      # WDC file download utility
└── data/                  # Kp data files (auto-populated)
    └── Kp_def*.wdc        # Downloaded WDC Kp files by year
```

## Features

### Data Download
- Automatically downloads Kp index data from GFZ Potsdam
- Caches downloaded files to avoid redundant downloads
- Supports downloading data for multiple years

### Data Parsing
- Parses WDC format files into pandas DataFrames
- Converts raw Kp values to 3-hourly time series
- Handles fractional Kp values (e.g., 5+2/3)

### Analysis Functions
- **Weekly Average**: Computes mean Kp index by week
- **Strong Events**: Counts geomagnetic storms (Kp ≥ 6) per year
- **Monthly Statistics**: Calculates mean and standard deviation for a given month across all years

### Visualization
- Line plots for weekly trends
- Bar charts for yearly event counts
- Error bar plots for monthly statistics with standard deviation

## Usage

### Basic Usage

Run the main analysis script:

```bash
python main.py
```

This will:
1. Download Kp data for years 2015-2024
2. Parse all files into a combined DataFrame
3. Generate and display:
   - Weekly average Kp trends
   - Count of strong geomagnetic events per year
   - January monthly statistics with error bars

## Future Enhancements

- CSV export functionality for processed data
- Additional analysis metrics (spectral analysis, forecasting)
- Interactive visualization with plotly
- Database integration for large-scale analysis
