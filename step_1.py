# with open()
# f = open('data/karloson.log', 'r', None, 'utf-8')
# f = open( file= 'data/karloson.log', node='r', encoding='utf-8')
# f = open( node='r', file= 'data/karloson.log', encoding='utf-8')
# f = open('data/karloson.log', 'r', encoding='utf-8')

# Ф      И    О
# Иванов Иван Иванович
# key value
# Имя: Иван
# Фамиля: Иванов
# Отчество: Иванович
# kwargs -> keyword args

# Отчество: Иванович
# Фамиля: Иванов
# Имя: Иван

# Ф      И    О
# Иван Иванов Иванович

# f = open('data/karloson.log', 'r', encoding='utf-8')
# content = f.read()
# f.close()

# context managers
with open('data/karloson.log', 'r', encoding='utf-8') as f:
    content = f.read()

# agile
# task -> 6 hours, Id 8h ->
pass
# task 1-> найти в тексте уникальные слова и подсчитать их количество
# task 2-> атсортировать слова в тексте по частоте их появления
# task 3-> найти перевод для TOP-100

text_i tens = content.split()
text_itens_cnt = len(text_itens)
# print ('слов в тексте', text_itens_cnt)
print(f'слов в тексте', {text_itens_cnt}') # python 3.6+

text_itens_counter = dict()
for el in text_itens_:
    if el not in text_itens_counter:
        text_itens_counter[el] = 0
    text_itens_counter[el] = text_itens_counter[el] +1
    # text_itens_counter[el] += 1





