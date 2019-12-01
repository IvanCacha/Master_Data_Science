#%%

import sys
import os
import numpy as np
import pandas as pd

if len(sys.argv)>=2:
    dir_path=sys.argv[1]
else:
    dir_path=os.path.dirname(os.path.realpath(__file__))

if len(sys.argv)>=3:
    flag_subdirectory=sys.argv[2]
else:
    flag_subdirectory='Y'

print('El directorio establecido es: ' + dir_path)

files = []

for r, d, f in os.walk(dir_path):
    for file in f:
        files.append(os.path.join(r, file))

for i in range(len(files)):
    try:
        with open(files[i], 'r') as f:
            count=0
            print ('analizando fichero: ' + files[i])
            for line in f:
                count += 1
    except Exception:
        count="No se puede contar"
        pass
    files[i] = (files[i], os.path.getsize(files[i]),count)

files.sort(key=lambda filename: filename[1], reverse=True)

files_pd=pd.DataFrame(files)

print(files_pd)


# %%
