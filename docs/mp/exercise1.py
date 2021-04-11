
# objective: Learn to open and read in data from files.
# play with spaCy
# If necessary (probably not?) at Git Bash or terminal do: pip3 install spacy

import spacy
# Need line 8 the first time: Then comment it out after the first time you run it:
nlp = spacy.cli.download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')

tp5 = open('tp1.txt', 'r')
words = tp5.read()
wordstrings = str(words)
print(wordstrings)

# count=0
# for w in words:
#     count += 1
#     print(count, ": ", w)

# start playing with spaCy and nlp:
tpsentences = nlp(wordstrings)
for token in tpsentences:
     # if not token.is_punct:
    print(token.text, "---->", token.pos_, ":::::", token.lemma_)

# On windows ctrl / comments out blocks.
# On mac command / comments out blocks
# grimmFile = open('tp1.txt', 'r')
# doc2 = tp5.read()
# docstring = str(doc2)
# print(doc2)

#nlpTP = nlp(docstring)
# for token in nlpTP:
    #print the token and its part of speech tag from spacy
    # print(token.text, "--->", token.pos_)




