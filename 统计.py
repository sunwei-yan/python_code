import jieba
from collections import Counter
# 读取 TXT 文件
k=open('gpc.txt','a+')
with open('pl.txt', 'r', encoding='UTF-8') as f:
    text = f.read()
# 对文本进行分词
text_list = jieba.lcut_for_search(text)
# 对分词结果进行统计
counter = Counter(text_list)

# 输出关键词及出现次数
for word, count in counter.most_common(100):
    s=word+str(count)+'\n'
    k.write(s)

    
    print(word, count)
f.close()