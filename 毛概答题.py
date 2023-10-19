import json
import codecs
import random
with codecs.open('output6.json', 'r', 'gbk') as f:
        json_str = f.read()
        
f2=open('pdt2.txt', 'a+')
x=''  
yt=''   
# 将JSON格式字符串反序列化为Python对象
data = json.loads(json_str)
f2.write('-------------------------------------------NEW ALL--------------------------------------------'+'\n')
# 使用Python对象进行操作
for j in range(0,50):
        yt=''
        i =random.randint(0,352)
        if(len(data[i]['dn'][6:])>=2):
            yt='多选'
        s=str(data[i]['bt'])+data[i]['tm']+'\n'+data[i]['xx']+yt+'\n'
        print(s)
        an=input()
        if(an==data[i]['dn'][6:]):
            print("答对了")
        else:
            print("答案是"+data[i]['dn'])
            f2.write(s+data[i]['dn']+'\n')
        # if(len(data[j]['xx'])<=10):
        #     s=str(data[j]['bt'])+data[j]['tm']+'\n'+data[j]['xx']+yt+'\n'+data[j]['dn']+'\n'
        #     print(s)    
f2.write(x)
