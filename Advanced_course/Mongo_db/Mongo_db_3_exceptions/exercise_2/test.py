import random
import pandas as pd


def random_date(start_date="2020-01-01", end_date="2023-12-31"):
    start_timestamp = pd.to_datetime(start_date).timestamp()
    end_timestamp = pd.to_datetime(end_date).timestamp()
    random_timestamp = random.uniform(start_timestamp, end_timestamp)
    return pd.to_datetime(random_timestamp, unit="s")


# User
print(random_date())  # Generates a random date between "2020-01-01" and "2023-12-31"


