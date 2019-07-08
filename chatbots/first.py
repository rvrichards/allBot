# first.py

import spacy

nlp=spacy.load('en')

data=nlp(u'It was the best of times, it was the worst of times.')
print ("\n",data)
for token in data:
     print (token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)


data=nlp(u'He laughed at the start, he the fastest runner.')
print ("\n",data)
for token in data:
     print (token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
