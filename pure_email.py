import os
import chardet
import sys
import codecs



def eachfile(filepath):
    workfile=[]
    pathdir=os.listdir(filepath)

    for s in pathdir:
        newdir = os.path.join(filepath, s) # 将文件命加入到当前文件路径后面
        if os.path.isfile(newdir):        #如果是文件
            workfile.append(newdir)

    return workfile



def findEncoding(s):
    file = open(s, mode='rb')
    buf = file.read()
    result = chardet.detect(buf)
    file.close()
    return result['encoding']


def convertEncoding(s):
    encoding = findEncoding(s)
    if encoding != 'ascii':
        # print("convert %s%s to utf-8" % (s, encoding))
        contents = ''
        with codecs.open(s, "r", encoding) as sourceFile:
            contents = sourceFile.read()

        with codecs.open(s, "w", "utf-8") as targetFile:
            targetFile.write(contents)


def pure_email(fp):
    pure_email = []
    f = eachfile(fp)
    fail_file = []
    for i in range(len(f)):
        # convertEncoding('C:\\Users\Tommy\\Desktop\\2018\\spam_2\\'+f[i].split('\\')[-1])
        try:
            fr = open(fp + '\\' + f[i].split('\\')[-1], encoding='utf-8')
            fr_file = fr.readlines()
        except Exception as e:
            #print(e)
            fail_file.append(fp + '\\' + f[i].split('\\')[-1])
            # print('已排除{}'.format('C:\\Users\Tommy\\Desktop\\2018\\spam_2\\'+f[i].split('\\')[-1]))
        else:
            email = []
            pure_email1 = []
            for line in fr_file:
                email.append(line)
            for item in email:
                item = item.strip()
                pure_email1.append(item)
            while "" in pure_email1:
                pure_email1.remove('')
            pure_email.append(pure_email1)

    return pure_email, fail_file

