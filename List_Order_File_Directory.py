#%%

import sys
import os

if len(sys.argv)>=2:
    dir_path=sys.argv[1]
else:
    dir_path=os.path.dirname(os.path.realpath(__file__))
    
print('El directorio establecido es: ' + dir_path)






# %%
