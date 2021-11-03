#
#
#

import os

dirs = os.listdir('fsk')
for f in dirs:
    file_path = os.path.join('fsk',f)
    for k in os.listdir(file_path):
        if k.endswith('my_param.v'):
            os.remove(file_path+'/'+k)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

