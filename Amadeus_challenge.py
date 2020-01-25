# %%
import pandas as pd
import numpy as np

directory = "C:\\Users\\ivanc\\OneDrive\\Documents\\Master Data Science\\Amadeus Challenge\\"
searches_file = directory + 'searches.csv.bz2' 
bookings_file = directory + 'bookings.csv.bz2'

# %%
df_booking=pd.read_csv(bookings_file, 
                       compression='bz2',
                       header=None,
                       chunksize=500000)
df_search = pd.read_csv(searches_file,
                       compression='bz2',
                       header=None,
                       chunksize=500000)


# %%
sample_bookings=df_booking.get_chunk(10000)
sample_bookings.to_csv(directory+ 'Sample_Bookings.csv.bz2',compression='bz2')
sample_searches=df_search.get_chunk(10000)
sample_searches.to_csv(directory+ 'Sample_Searches.csv.bz2',compression='bz2')

# %%
sample_bookings

# %%
