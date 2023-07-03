string = input("Enter a string: ")
split = string.split()
thisdic = {}
for words in split:
    if words in thisdic:
        thisdic[words] += 1
    else:
        thisdic[words] = 1
for words in thisdic:
    print("{0}:{1}".format(words, thisdic[words]))
print(split)