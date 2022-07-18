import sys

'''
Project Luminous
Dummy K-Chorus Ripper (EVE) Ver 1
2021/03/24
'''

def eve(inputdir):
    fileopen=open(inputdir,"rb")
    fileread = fileopen.read()
    fileopen.close()
    count=1
    while True:
        filefind=fileread.find(b'FORM')
        if filefind == -1:
            break
        else :
            kcsizebyte=fileread[filefind+4:filefind+8]
            kcsizeint=int.from_bytes(kcsizebyte, byteorder='big')
            print(kcsizeint)
            kcdata=fileread[filefind:filefind+8+kcsizeint]
            savekc=open(inputdir+str(count)+'.ICM','wb')
            savekc.write(kcdata)
            savekc.close()
            count=count+1
            fileread=fileread[filefind+8+kcsizeint:]
        
    
dir=sys.argv[1]    
eve(dir)