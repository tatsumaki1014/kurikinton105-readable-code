with open('dictionary-data.txt', 'r', encoding='utf-8') as f:
    read_list = f.readlines()

word_list = []
kana_dict = []

for i in read_list:
    word_list_split = i.split(" ")
    print(word_list_split)
    

id_dict = dict()
id = 1
for i in range(len(word_list)):
    id_dict[id] = word_list[i]  
    id += 1 

#(WIP)
