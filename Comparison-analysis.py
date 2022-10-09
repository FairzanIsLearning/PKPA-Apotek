#%%
# we are gonna installing the required package first
import matplotlib.pyplot as plt
import numpy as py
import pandas as pd

# next, we import the csv file
aug_raw = pd.read_csv("Training-aug.csv", encoding='windows-1252')
# aug_raw.head()
aug_process = aug_raw[['Nama Obat', 'Indikasi', 'Komposisi', 'Populasi', 'Jumlah Terjual', 'Frekuensi', 'Satuan']]
# use comma: 'Harga Beli','Total Nominal'
# the selling and buying value can not be processed because the contain commas within their value (?)


#%%
# setting index
index_indication = aug_process['Indikasi']
aug_process = aug_process.set_index(index_indication)
# del aug_process['Indikasi']
aug_process = aug_process.sort_index()
aug_process.head()


#%%
# visualize selling times vs indication
plt.plot(aug_process['Indikasi'], aug_process['Jumlah Terjual'])

#%%
# now we are adding the data for profit
# aug_process['Harga Beli'] = aug_process['Harga Beli'].astype(str)
# org_string = aug_process['Harga Beli']
# size = len(org_string)
# Slice string to remove last 3 characters from string
# aug_process['Harga Beli'] = org_string[:size - 2]
# aug_process.head()
# aug_process['Jumlah Terjual'] = aug_process['Jumlah Terjual'] .astype(int)
# aug_process['Harga Beli'] = aug_process['Harga Beli'] .astype(int)
# aug_process['Jumlah Terjual'] = aug_process['Jumlah Terjual'].str.replace(',', '')
# profit = aug_process['Jumlah Terjual'] * aug_process['Harga Beli']
# aug_process.assign(Keuntungan=profit)


# %%
