#%%

import sys
import os

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
        files[i] = (files[i], os.path.getsize(files[i]))

files.sort(key=lambda filename: filename[1], reverse=True)

print(files)


# %%
