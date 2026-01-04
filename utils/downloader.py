import requests, os

def download_wdc(years, save_dir="data"):
    """
    Download WDC Kp files for given years.
    years: int or list of ints
    Returns list of saved file paths.
    """
    if isinstance(years, int):
        years = [years]
        
    os.makedirs(save_dir, exist_ok=True)
    file_paths = []
    
    for year in years:
        # INSERT A CHECK FOR IF THE FILE ALREADY EXISTS HERE
        file_name = f"Kp_def{year}.wdc"
        file_path = os.path.join(save_dir, file_name)
        if os.path.exists(file_path):
            print(f"File already exists: {file_path}")
            file_paths.append(file_path)
            continue
        url = f"https://datapub.gfz-potsdam.de/download/10.5880.Kp.0001/Kp_definitive/Kp_def{year}.wdc"
        response = requests.get(url)
        if response.status_code == 200:
            file_path = os.path.join(save_dir, f"Kp_def{year}.wdc")
            with open(file_path, "w") as f:
                f.write(response.text)
            print(f"Downloaded: {file_path}")
            file_paths.append(file_path)
        else:
            print(f"Failed to download {year}: {response.status_code}")
    return file_paths
