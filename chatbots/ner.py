#NER - ner.py
# first.py

import spacy

nlp=spacy.load('en')

data=nlp(u'Fred Flintstone was born February 29, 15,000 BC in Bedrock, BC Canada. He is best known for saying "Yabba Dabba DO!"')
print ("\n",data)

for ent in data.ents:
     print (ent.text, ent.label_)

