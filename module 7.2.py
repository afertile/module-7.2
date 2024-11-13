file_name = 'test.txt'
def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    strings_positions = {}
    k = 0
    for i in strings:
        k += 1
        strings_positions[(k, file.tell())] = i
        file.write(f'{i}\n')
    file.close()
    return strings_positions
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)