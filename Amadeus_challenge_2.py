# %%
import pandas as pd
import numpy as np

directory = "C:\\Users\\ivanc\\OneDrive\\Documents\\Master Data Science\\Amadeus Challenge\\"
bookings_sample = directory + 'Sample_Bookings.csv.bz2'

# %%
df_booking = pd.read_csv(bookings_sample, sep='^', header=0,
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
year_filter = df['year'] == 2013
result = df[year_filter][['arr_port','pax']].groupby('arr_port').sum().sort_values('pax',ascending=False)
result
top10 = result.iloc[:10]
top10
# %%
bookings_file = directory + 'bookings.csv.bz2'
df_booking = pd.read_csv(bookings_file,
                         sep='^',
                         usecols=['arr_port','pax', 'year'],
                         chunksize=200000
                         )
# %%
all_bookings=pd.DataFrame()
for i, chunks in enumerate(df_booking):
    print(i)
    year_filter = chunks['year'] == 2013
    result_chunks = chunks[year_filter][['arr_port','pax']].groupby('arr_port').sum()
    result_chunks.reset_index(inplace=True)
    all_bookings = all_bookings.append(result_chunks)
all_bookings.shape      

# %%
result= all_bookings.groupby('arr_port').sum().sort_values('pax',ascending=False)
top10 = result.iloc[:10]
top10
# %%


