import os,sys,re,time


def dir_list(path):
    fileList = []
    dirList = []

    for x in os.listdir(path):
        content_path=os.path.join(path, x)
        stat=os.stat(content_path)

        stime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stat.st_mtime)) 

        stime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stat.st_mtime)) 
        info={'name':x,'size':'-','mtime':stime}

        if os.path.isfile(content_path):
            info['size']=fileSize(stat.st_size)

            fileList.append(info)
        else:
            dirList.append(info)

    return fileList, dirList

def fileSize(size):
    if size <= 1024:
        return str(size)+"B"
    elif size <= 1024*1024:
        fsize = size/float(1024)
        fsize=str(round(fsize,2))
        return fsize+"KB"
    elif size <= 1024*1024*1024:
        fsize = size/float(1024*1024)
        fsize=str(round(fsize,2))
        return fsize+"MB"
    else :
        fsize = size/float(1024*1024*1024)
        fsize=str(round(fsize,2))
        return fsize+"GB"