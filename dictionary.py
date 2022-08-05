with open('dictionary-data.txt', 'r', encoding='utf-8') as f:
    word_list = f.readlines()


id_dict = dict()
id = 1
for i in range(len(word_list)):
    id_dict[word_list[i]] =  id
    id += 1 

for word in word_list:
    print(str(id_dict[word]) + ": " + word.replace("\n", "")) #replace関数で単語末尾の改行を削除(上手/n →　上手)
