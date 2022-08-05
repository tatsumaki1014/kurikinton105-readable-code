input_id = int(input('idを入力してください'))

with open('dictionary-data.txt', 'r', encoding='utf-8') as f:
    word_list = f.readlines()


id_dict = dict()
id = 1
for i in range(len(word_list)):
    id_dict[id] = word_list[i]  
    id += 1 

print(str(input_id) + ": " + str(id_dict[input_id]))
