s = input()
words = s.replace(","," ").split()
count = {}
for word in words:
    if word in count:
        count[word] +=1
    else:
        count[word] = 1
most = words[0]
for word in words:
    if count[word]>count[most]:
        most = word
print(f"The most frequent word is '{most}' with a count of {count[most]}")