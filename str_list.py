from random_words import RandomWords

str_list = []
w = RandomWords()

for i in range(0, 5000):
   str_list.append(w.random_word())
print("Created list:", str_list)
