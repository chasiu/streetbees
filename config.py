import os

DB_URI = os.environ["DB_URI"]

f = open("data/classes.txt", "r")
CLASSES = {}
c = 1
for i in f:
    CLASSES[c] = i.strip("\n")
    c += 1
f.close()
