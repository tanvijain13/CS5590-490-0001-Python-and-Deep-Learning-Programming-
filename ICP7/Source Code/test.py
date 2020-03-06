import nltk
nltk.download("brown")
from nltk.corpus import brown
print(brown.categories())
print(brown.words(categories ='news'))