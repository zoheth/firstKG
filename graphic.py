import numpy as np
import csv

r = np.load('data/XCAQ/temp/relation.npy')
file = open("data/GOT-relation/relation2id.txt")
id_r = {}
for line in file.readlines():
    id_r[int(line.split()[1])] = line.split()[0]

with open("data/XCAQ/temp/pair.csv")as csc_f:
    rows = csv.reader(csc_f)
    with open("XCAQ_out.csv", "w")as out_f:
        writer = csv.writer(out_f)
        i = 0
        j=0
        for row in rows:
            if(j==len(r[i])):
                i+=1
                j=0
            if(i==len(r)):
                break
            row.append(id_r[r[i][j]])
            writer.writerow(row)
            j+=1
