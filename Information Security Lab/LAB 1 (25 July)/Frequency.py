# Program to count frequency of words in a sentence.
text = "hi hello how are you hi hi hi hello you"
splitted_text = text.split(" ")
no_of_words = len(text)
result = {}

for i in splitted_text:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1

print(result)


# Program to count frequency of letters in a sentence.
text = "hi hello how are you hi hi hi hello you"
splitted_text = [*text]
no_of_words = len(text)
result = {}

for i in splitted_text:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1

print(result)