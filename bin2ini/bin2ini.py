import os
import struct

def Mkdir(path):
    path=path.strip() #去除首位空格
    path=path.rstrip("\\") #去除尾部 \ 符号
    isExists=os.path.exists(path) #判断路径是否存在
    if not isExists:
        os.makedirs(path) #如果不存在则创建目录
        print path+' make dir successfully'
        return True
    else:
        print path+' dir existed' #如果目录存在则不创建，并提示目录已存在
        return False

def GetFileName(path):
    ret = []
    for root,dirs,files in os.walk(path):
        for filespath in files:
            ret.append(os.path.join(root,filespath))
    return ret

def GenIni(bin_name,ini_dir):
    ini_name = ( ((bin_name.split('.')[0]).split('\\')[-1]) + '.ini' )
    mem_word = 1024

    binfile = open(bin_name,'rb')
    inifile = open(ini_dir + '\\' + ini_name,'w')
    size = os.path.getsize(bin_name)
    word_data = ['00','00','00','00']
    k = 0
    addr = 0
    ###main byte write###
    for i in range(0,size):
        data = binfile.read(1)
        num = struct.unpack('B',data)
        byte_data = "%02x" % int(num[0])
        k = k + 1
        word_data[k-1] = byte_data
        if(k == 4):
            inifile.write('@')
            inifile.write(str("%08x" % addr) + ' ')
            inifile.write(word_data[3])
            inifile.write(word_data[2])
            inifile.write(word_data[1])
            inifile.write(word_data[0])
            inifile.write('\n')
            k = 0
            word_data = ['00','00','00','00']
            addr = addr + 1
    #####################
    ###remain byte write###
    if((k != 4) and (k != 0)):
        inifile.write('@')
        inifile.write(str("%08x" % addr) + ' ')
        inifile.write(word_data[3])
        inifile.write(word_data[2])
        inifile.write(word_data[1])
        inifile.write(word_data[0])
        inifile.write('\n')        
        addr = addr + 1
    #####################
    ###empty byte write###
    for i in range(0,mem_word-addr):
        inifile.write('@')
        inifile.write(str("%08x" % addr) + ' ')
        inifile.write('ffffffff')
        inifile.write('\n')        
        addr = addr + 1
    #####################
    binfile.close()
    inifile.close()
    
if __name__ == '__main__':
    bin_path = 'G:\\git-project\\learnpython\\bin2ini\\num1003_sd_bin' #need to change your absolute path
    files = GetFileName(bin_path)
    ini_dir_name = bin_path.split('\\')[-1] + '2ini'
    Mkdir(ini_dir_name)
    for file in files:
        if file.split('.')[1] == 'bin':
            GenIni(file,ini_dir_name)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

