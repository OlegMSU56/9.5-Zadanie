first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(eng_word) - len(rus_word) for eng_word, rus_word in zip(first, second) if
                len(eng_word) != len(rus_word))

second_result = (first[i] == False if len(first[i]) != len(second[i]) else True
                 for i in range(len(first)))

print(list(first_result))
print(list(second_result))