from textblob.classifiers import NaiveBayesClassifier
from nltk.corpus import movie_reviews

train = [('I like this new tv show.', 'pos'), ('I do not enjoy my job', 'neg'),
         # similar train sentences with sentiments goes here
         ]


test = [
    ('mission impossible three is awesome btw', 'pos'),
    ('brokeback mountain was beautiful', 'pos'),
    ('that and teh da vinci code is awesome so far', 'pos'),
    ('10 things i hate about you = ', 'neg'),
    ('brokeback mountain is a spectacularly beautiful movie', 'pos'),
    ('mission impossible 3 is amazing', 'pos'),
    ('the actor who plays harry potter sucks', 'neg'),
    ('harry potter = gorgeous', 'pos'),
    ('the beer was good.', 'pos'),
    ('I do not enjoy my job', 'neg'),
    ("I ain't feeling very good today.", 'neg'),
    ('I feel amazing!', 'pos'),
    ('I feel amazing!', 'pos'),
    ('Gary is a friend of mine', 'pos'),
    ("I can't believe I'm done this.", 'pos'),
    ('I went to see brokeback mountain, which is beautiful(', 'pos'),
    ('and i love brokeback mountain too: ]', 'pos'),
]

cl = NaiveBayesClassifier(train)
print("Accuracy: {0}".format(cl.accuracy(test)))

reviews = [(movie_reviews.raw(fileid), category)
           for category in movie_reviews.categories()
           for fileid in movie_reviews.fileids(category)
           ]

# reviews = [(list(movie_reviews.words(fileid)), category)
#            for category in movie_reviews.categories()
#            for fileid in movie_reviews.fileids(category)
#            ]

# print(reviews[0])

new_train, new_test = reviews[0:100], reviews[101:200]
cl.update(new_train)
accuracy = cl.accuracy(test+new_test)
print("Accuracy: {0}".format(cl.accuracy(test)))

# show 5 most informative features
cl.show_informative_features(4)

