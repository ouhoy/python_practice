f_hand = open("text.txt")
counts = {}
for line in f_hand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

ls = []

for key, val in counts.items():
    new_tup = (val, key)
    ls.append(new_tup)

ls = sorted(ls, reverse=True)

for val, key in ls[:10]:
    print(f"{key.capitalize()}: {val}")
