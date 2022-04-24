print('Щас найдем огурец')
text = input('Введите фразу со словом "cucumber": ')
text1 = text[0]
if 'cucumber' in text:
    print(text[text.find('cucumber') + 0:])
else:
    print('cucumber не найден')