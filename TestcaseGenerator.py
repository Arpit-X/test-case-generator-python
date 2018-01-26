import random
import os
import string
def gen_rand_integer(start,end):
    x=int((random.random()*end) +start-1)
    yield x

def gen_rand_str(start,end):
    length=int((random.random()*end) +start-1)
    res=""
    for i in range(length):
         ind=int(random.random()*26)
         res+=string.ascii_lowercase[ind]
    yield res
while True:
    typ=input("Enter the data type (str/int) :")
    while(typ != 'int' and typ !='str'):
        typ=input("type ca only be a str or int, enter again :")
    start=int(input('enter the minimum digits/stringLenght value : '))
    end=int(input('enter the maximum digits/stringLenght value : '))
    size= int(input('enter how many values you want : '))
    fileName=input('enter thr file name you want to put them in : ')
    ans=input('do you want to specify the location [y/n] : ')
    if ans.lower()=='y':
        path=input('enter the path where you want to put this file : ')
    else:
        path=os.getcwd()
    location =path+'\\'+fileName+'.txt'

    while os.path.isfile(location):
            tmp=fileName
            fileName=input('file name already exists , enter another name : ')
            if tmp==fileName:
                print('rewriting the file !!!')
                break
            location =path+'\\'+fileName+'.txt'
    try:
        
        fp=open(location,'w')
    except Exception as e:
        print("\n\n\tError opening the file")
        print(e)

    else:
        try:
            fp.write(str(size)+'\n')
            if typ=='int':
                for i in range(size):
                    fp.write(str(next(gen_rand_integer(start,end)))+" ")
            else:
                for i in range(size):
                    fp.write(next(gen_rand_str(start,end))+" ")
            fp.close()
            print('the file\'s location is '+location)
        except Exception as e:
            print(e)
    print('\n\npress any key to exit')
    input()
