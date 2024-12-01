lang = input("Выберите язык (ру - русский, en - английский): ")
if lang == "ру":
    ALPHABET = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
elif lang == "en":
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
else:
    print("Выбран неподдерживаемый язык. Используется русский алфавит по умолчанию.")
    ALPHABET = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
message =  input("Введите сообщение: ").lower()
chipher = []
result = ''
ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
step = int(input("Введите шаг кодиовки: "))
for symbol in message:
    chipher.append(ALPHABET.find(symbol) + step)
for index in chipher:
    result += ALPHABET[index - step]
print(chipher)
print(result)