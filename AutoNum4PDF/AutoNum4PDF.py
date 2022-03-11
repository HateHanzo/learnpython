#coding=utf-8
import os
import struct
import shutil

#��ȡ�ļ��м������ļ����µ������ļ���
def GetFileName(path):
    ret = []
    for root,dirs,files in os.walk(path):
        for filespath in files:
            ret.append(os.path.join(root,filespath))
    return ret

  
if __name__ == '__main__':
    dirpath = 'test_paper' 
    files = GetFileName(dirpath)
    paper_path = files[0].rsplit('\\',1)
    #print(paper_path)
    
    for i in range(0,len(files)):
        paper_name = files[i].split('\\')[-1]
        new_paper_name = '[' + str(i) + ']' + '_' + paper_name
        print(new_paper_name)
        ori = files[i]
        new = paper_path[0] + '\\' + new_paper_name
        shutil.move(ori,new)

    

    

    
    

    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

