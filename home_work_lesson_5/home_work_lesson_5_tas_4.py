# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
translate_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
with open('text_4.txt', encoding='utf-8') as f:
    for str_f in f:
        first = str_f.index(' ')
        word = str_f[:first]
        two_pass = str_f[first:]
        translate_word = translate_dict.get(word)
        new_str = translate_word + two_pass
        with open('text_4_2.txt', 'a', encoding='utf-8') as f_2:
            f_2.writelines(new_str)
