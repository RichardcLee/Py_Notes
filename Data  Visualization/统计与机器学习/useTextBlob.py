from textblob.classifiers import NaiveBayesClassifier
from textblob.blob import TextBlob


# 训练数据也可以使用文件如json，读入
train = [('I like this new tv show.', 'pos'),
         # similar train sentences with sentiments goes here
         ]
test = [('I do not enjoy my job', 'neg'),
        # similar test sentences with sentiments goes here
        ]


cl = NaiveBayesClassifier(train)    # 朴素贝叶斯分类器
res = cl.classify("The new movie was amazing!")   # shows if pos or neg
print(res+'\n')

cl.update(test)    # retrain

# Classify a TextBlob
blob = TextBlob("The food was good. But the service was horrible. My father was not pleased.", classifier=cl)
print(blob)
print(blob.classify(), '\n')

for sentence in blob.sentences:
    print(sentence)
    print(sentence.classify())
