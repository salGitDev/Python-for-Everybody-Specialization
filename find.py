file = open("findfile.txt", "r")
frq_word = ""
how_freq = 0
words = []

for line in file:
    line_word = line.lower().replace(",", "").replace(".", "").split(" ")

for word in line_word:
    words.append(word)

for i in range(0, len(words)):
    count = 1

    for j in range(i + 1, len(words)):
        if words[i] == words[j]:
            count = count + 1

    if count > how_freq:
        how_freq = count
        frq_word = words[i]

print("Most repeated word: " + frq_word)
print("Frequency: " + str(how_freq))
file.close()
