# %%
import pandas as pd
import numpy as np

directory = "C:\\Users\\ivanc\\OneDrive\\Documents\\Master Data Science\\Amadeus Challenge\\"
bookings_file = directory + 'Sample_Bookings.csv.bz2'

# %%
df_booking = pd.read_csv(bookings_file, sep='^', header=0,
                       compression='bz2')


# %%
pd.set_option('display.max_columns', 38)
df_booking.sample(5)

# %%
df_booking.describe(include='all')

# %%
df_booking.info()

# %%
df_booking.isnull().sum()

# %%
df_booking.rename(columns=lambda x: x.strip(), inplace=True)
df_booking.columns

# %%
df_booking.groupby('rloc')['act_date'].count()\
          .sort_values( ascending=False)\
          .head()
# %%
filter = df_booking['rloc']=='ae15bcfc5aec0eb64b2c5204d08201d5'
df_booking[filter]

# %%
df = df_booking[['arr_port','pax', 'year']]
df.head()

# %%
