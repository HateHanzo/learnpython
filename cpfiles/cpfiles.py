#
#
#

import os
import shutil

root = os.getcwd()

for curDir,dirs,files in os.walk(root+"\\fsk",topdown=False):
    for dir in dirs:
        shutil.copy(root+"\\my_param.v",root+"\\fsk\\"+dir)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

