import pandas as pd

def wdc_to_dataframe(file_path):
    """
    Parse a WDC Kp .wdc file into a pandas DataFrame with 3-hourly datetime index.
    """
    records = []
    kp_fraction = {'0':0.0, '3':1/3, '7':2/3}
    
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        line = line.rstrip("\n")
        if not line.strip() or line.startswith("#"):
            continue
        
        year = int(line[0:2]) + 2000
        month = int(line[2:4])
        day = int(line[4:6])
        kp_raw = line[12:28]  # Kp columns: 13-28 (8 values, 2 digits each) (from pdf documentation columns [n-1, pdf col])
        
        for i in range(8):
            kp_pair = kp_raw[i*2:i*2+2]
            if len(kp_pair.strip()) < 2:
                continue
            int_part = int(kp_pair[0])
            frac_part = kp_fraction.get(kp_pair[1], 0.0)  # Project the 2nd digit of kppair against the dictionary to decide on the decimal
            kp_value = int_part + frac_part
            timestamp = pd.Timestamp(year=year, month=month, day=day, hour=i*3)
            records.append({'datetime': timestamp, 'Kp': kp_value}) #append to records list each column as a dictionary (I literally append a dictionary)
            
    df = pd.DataFrame(records)
    df.set_index('datetime', inplace=True)
    return df
