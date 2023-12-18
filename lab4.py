import random

# Символи ASCII-арту
characters = {
    'a': [
        "  AA  ",
        " A  A ",
        " AAAAA",
        " A  A ",
        " A  A "
    ],
    'b': [
        " BBB  ",
        " B  B ",
        " BBBB ",
        " B  B ",
        " BBB  "
    ],
    'c': [
        " CCCC ",
        " C    ",
        " C    ",
        " C    ",
        " CCCC "
    ],
    'e': [
        " EEEE ",
        " E    ",
        " EEEE ",
        " E    ",
        " EEEE "
    ],
    'g': [
        " GGGG ",
        " G    ",
        " G GG ",
        " G  G ",
        " GGGG "
    ],
    'i': [
        " III ",
        "  I  ",
        "  I  ",
        "  I  ",
        " III "
    ],
    'r': [
        " RRR  ",
        " R  R ",
        " RRR  ",
        " R R  ",
        " R  R "
    ],
    's': [
        " SSSS ",
        " S    ",
        " SSSS ",
        "    S ",
        " SSSS "
    ],
    'y': [
        " Y  Y ",
        "  YY  ",
        "   Y  ",
        "   Y  ",
        "   Y  "
    ],
    'k': [
        " k  k ",
        " kkk  ",
        " k  k ",
        " k   k",
        " k    k"
    ],
    'l': [
        "L     ",
        "L     ",
        "L     ",
        "L     ",
        "LLLLLL"
    ]
}

# Завдання 8: Варіанти кольорів
color_option = input("Виберіть опцію кольорів (чорно-білий/відтінки сірого): ").lower()

# Завдання 1: Введення користувача
input_text = input("Введіть слово або фразу для ASCII-арту: ")

# Завдання 5: Вирівнювання тексту
alignment = input("Виберіть вирівнювання (ліво, центр, право): ").lower()
if alignment not in ['ліво', 'центр', 'право']:
    alignment = 'ліво'

# Завдання 3: Розміри Art-у
width = int(input("Введіть ширину ASCII-арту: "))
height = int(input("Введіть висоту ASCII-арту: "))

# Завдання 4: Функція генерації Art-у
def generate_ascii_art(input_text, characters, alignment, width, height, color_option):
    lines = []

    if alignment == 'центр':
        lines.append(input_text.center(width))
    elif alignment == 'право':
        lines.append(input_text.rjust(width))
    else:
        lines.append(input_text.ljust(width))

    for i in range(5):
        line = ""
        for char in input_text:
            if char.lower() in characters:
                line += characters[char.lower()][i]
            else:
                line += " " * 6  # Пробіли, якщо символ не знайдено
            line += " "  # Додатковий пробіл між буквами

        if color_option == 'чорно-білий':
            line = "\033[30m" + line + "\033[0m"  # Чорний колір тексту
        elif color_option == 'відтінки сірого':
            line = "\033[90m" + line + "\033[0m"  # Сірий колір тексту

        lines.append(line)

    return lines

# Генерація ASCII-арту
art = generate_ascii_art(input_text, characters, alignment, width, height, color_option)

# Завдання 6: Відображення мистецтва
for line in art:
    print(line)

# Завдання 7: Збереження у файл
save_option = input("Бажаєте зберегти ASCII-арт у файл? (так/ні): ").lower()
if save_option == 'так':
    filename = input("Введіть ім'я файлу: ")
    with open(filename, 'w') as file:
        for line in art:
            file.write(line + '\n')

# Завдання 9: Функція попереднього перегляду
def preview_ascii_art(art):
    print("Попередній перегляд ASCII-арту:")
    for line in art:
        print(line)

# Попередній перегляд ASCII-арту
preview_option = input("Бажаєте побачити попередній перегляд ASCII-арту? (так/ні): ").lower()
if preview_option == 'так':
    preview_ascii_art(art)
