import stanfordnlp
import csv
from itertools import combinations

file = open('data/XCAQ/text.txt')
out = open('data/XCAQ/temp/test.txt', 'w')
out_csv = open('data/XCAQ/temp/pair.csv','w')

sentence = file.read().split('。')
sentence.pop()

nlp = stanfordnlp.Pipeline(lang="zh")
for text in sentence:
    text = text.replace('\n', '')
    text = text.replace('　', '')
    text = text.replace(' ', '')
    word = nlp(text).sentences[0].words
    entity=[]
    pre=0
    for w in word:
        if (w.dependency_relation == 'nmod' and w.upos == "PROPN"):
            if(len(w.text)==1):
                entity.append(w.text+word[int(w.index)].text)
            else:
                entity.append(w.text)
    
    for (a, b) in combinations(entity, 2):
        out.write(a + " " + b + " " + "unknown ")
        out.write(text + '\n')
        writer=csv.writer(out_csv)
        writer.writerow([a,b])

out.close()
out_csv.close()
