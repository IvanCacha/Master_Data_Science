# %%
import pandas as pd
import numpy as np

directory = "C:\\Users\\ivanc\\OneDrive\\Documents\\Master Data Science\\Amadeus Challenge\\"
searches_file = directory + 'searches.csv.bz2' 
bookings_file = directory + 'bookings.csv.bz2'

# %%
df_booking=pd.read_csv(bookings_file, 
                       compression='bz2',
                       header=0,
                       chunksize=100,
                       sep='^')
df_search = pd.read_csv(searches_file,
                       compression='bz2',
                       header=0,
                       chunksize=100,
                       sep='^')


# %%
