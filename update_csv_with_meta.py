# Step 1: Read the CSV file into a DataFrame
import random
from pathlib import Path

import pandas as pd

csv_inputs = Path(Path.cwd() / "csv_inputs").glob('*')
for file in csv_inputs:
    print(file.absolute())
    try:
        df = pd.read_csv(file.absolute())
        # add logic adding locations based on coordinates from some geo-api
        df['region'] = random.choice(["Garda", "Boka-Kotorska", "San-Francisco", "Lake Michigan"])
        df['class'] = "29er"
        df['measurement'] = "boat_telemetry"
        df.to_csv(Path.cwd() / "csv_with_meta" / f"{file.name}", index=False)
    except:
        pass

