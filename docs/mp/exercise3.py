# Objective for Python Ex 2: explore lemmas and POS and named entities in your text blobs
# Try counting the top 10 or 20 of a thing
# Try a basic Python plotting library to create an SVG: We'll try Pygal
# See https://towardsdatascience.com/interactive-data-visualization-in-python-with-pygal-4696fccc8c96

from collections import Counter
import pygal
import spacy
# Need line 8 the first time: Then comment it out after the first time you run it:
# nlp = spacy.cli.download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')
lemmatizer = nlp.get_pipe("lemmatizer")
print(lemmatizer.mode)  # 'rule'

loz = open('Python3.txt', 'r')
# If, when you print the file, it comes out with weird characters in place of apostrophes, quotes, etc.,
# try adapting this alternative version of the line above:
# yourtext = open('yourtext.txt', 'r', encoding="utf8", errors='ignore')
words = loz.read()
lozwords = nlp(words)
# print(words)


def nouncollector(words):
    Nouns = []
    count = 0
    for token in words:
        if token.pos_ == "NOUN":
            count += 1
            # print(count, ": ", token.text, " lemma: ", token.lemma_, " pos: ", token.pos_)
            # don't forget the underscore after token.lemma_ , token.pos_, etc.!
            Nouns.append(token.lemma_)
            # print(count, ": ", token, token.pos_, spacy.explain(token.pos_))
    # print(count, ": ", Verbs)
    return Nouns

listNouns = nouncollector(lozwords)
noun_freq = Counter(listNouns)
topTwenty = noun_freq.most_common(20)
print(topTwenty)
lastTen = noun_freq.most_common()[:-10:-1]
print(lastTen)

# ebb: Okay, let's try out the pygal graphing library!
# Here I am experimenting and creating TWO bar graphs. For homework you only need to create one.
# I made one bar graph called bar_chartOver10, and another that I like much better called bar_chartTopTen
# bar_chartOver10 = pygal.Bar()
bar_chartTopTwenty = pygal.Bar()

# bar_chartOver10.title = 'Verbs Used Over 10 Times in Disney Songs'
bar_chartTopTwenty.title='Top 20 Most Common Nouns in the LoZ Sacred World Timeline'

# for n in noun_freq:
#     # noun_freq is a dictionary structure, so we return its key and its value:
#     print(n, noun_freq[n])
#     if noun_freq[n] > 10:
#     bar_chartOver20.add(n, noun_freq[n])


for t in topTwenty:
    # this is a list of tuples, so we return its values like this:
    print(t[0], t[1])
    bar_chartTopTwenty.add(t[0], t[1])

print(bar_chartTopTwenty)
# print(bar_chartOver10.render(is_unicode=True))
# bar_chartOver10.render_to_file('bar_chartOver10.svg')
bar_chartTopTwenty.render_to_file('bar_chartTopTwentyNames.svg')


# On windows ctrl / comments out blocks.
# On mac command / comments out blocks

# lowercaseList = []
# for l in listNouns:
#     l = str(l).lower()
#     lowercaseList.append(l)
# setNouns = set(lowercaseList)
# count = 0
# for s in setNouns:
#     count += 1
# print(sorted(setNouns))
# print(count)



