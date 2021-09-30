#this script run in liunix system
#
#

import os
import sys
import shutil

root = os.getcwd()
patern = "CVS"

for folder in os.walk(root,topdown=False):
    if folder[0].split('/')[-1] == patern:
        shutil.rmtree(folder[0])


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

