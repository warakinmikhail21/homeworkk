text1 = ['Dublin\n' 'London\n', 'Munhen\n', 'Krasnodar\n', 'Paris\n']
data = open('text1.txt', 'w')
data.writelines(text1)
data.close()

text2 = []
data = open("text2.txt",'a')
data.close()


user_input = int(input("Enter  line  -> "))

with open('text1.txt', 'r') as copy_word_text1:
    line = copy_word_text1.readlines()
    save_word = (line[user_input])
    
print("Answer is -> ", save_word)

with open("text2.txt", 'a') as add_word:
    add_word.write(save_word)

with open('text2.txt', 'r') as read_text2:
    print("Line add",f'({save_word})',"\n",read_text2.read())







