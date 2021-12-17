word_to_count = {}
user_input = input("Text: ")
text = user_input.split()

for word in text:
    word_to_count[word] = word_to_count.get(word, 0) + 1

result = [(word, count) for word, count in word_to_count.items()]
result.sort()

for word in result:
    print(f"{word[0]:13} : {word[1]}")
