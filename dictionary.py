with open('dictionary-data.txt', 'r', encoding='utf-8') as f:
    word_list = f.readlines()

for i in range(len(word_list)):
    word_list[i] = word_list[i].replace('\n', '')

for word in word_list:
    print(word)
