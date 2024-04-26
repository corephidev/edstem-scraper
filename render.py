import matplotlib.pyplot as plt
import collections

f = open(input("Filename: "), "r")
data = dict(collections.Counter([line.strip() for line in f.readlines()]))
f.close()

keys = []
values = []

data = sorted(data.items(), key=lambda v: v[1], reverse=True)[:10]

k = [x[0] for x in data]
v = [x[1] for x in data]

fig, ax = plt.subplots()

bar = ax.barh(k, v)

for index, value in enumerate(v):
    plt.text(value, index, str(value))

plt.show()
