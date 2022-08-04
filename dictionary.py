with open('dictionary-data.txt', 'r', encoding='utf-8') as f:
    word_list = f.readlines()
for word in word_list:
    print(word)
