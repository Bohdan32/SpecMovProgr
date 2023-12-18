from Figures3D import *
from utility import FileProcessor

def get_character_input():
    while True:
        character = input("Введіть символ для представлення у фігурі: ")
        if Figure3D.is_appropriate_character(character) is False:
            print("Повинен бути введений лише один символ!")
        else:
            return character

def get_color_position_input():
    while True:
        try:
            color = int(input("Введіть номер кольору: "))
            if color not in range(len(colors)):
                print("Ви повинні ввести доступну опцію кольору!")
            else:
                return color
        except ValueError:
            print("Ви повинні ввести ціле число!")

def get_length_input():
    while True:
        try:
            length = int(input("Введіть довжину: "))
            if length <= 0:
                print("Ви повинні ввести додатнє число більше 0!")
            else:
                return length
        except ValueError:
            print("Ви повинні ввести ціле число!")

def get_scale_input():
    while True:
        try:
            scale = float(input("Введіть масштаб для фігури: "))
            if scale <= 0:
                print("Ви повинні ввести масштаб більше 0!")
            else:
                return scale
        except ValueError:
            print("Ви повинні ввести десяткове число!")

representation_2d_file = "2d.txt"
representation_3d_file = "3d.txt"

def main():
    is_figure_available: bool = False
    is_2d_representation_available = False
    is_3d_representation_available = False

    while True:
        print("1 - Створити куб")
        print("2 - Показати 2D")
        print("3 - Показати 3D")
        print("4 - Зберегти 2D")
        print("5 - Зберегти 3D")
        print("0 - Вихід")
        option = str(input("Введіть опцію: "))

        match option:
            case "1":
                character = get_character_input()
                print("Доступні кольори:")
                display_colors()
                color_position = get_color_position_input()
                length = get_length_input()
                scale = get_scale_input()
                try:
                    figure = Cube(length, character, color_position)
                    is_figure_available = True
                except ValueError as e:
                    print(e)
                    is_figure_available = False
            case "2":
                if is_figure_available is True:
                    representation_2d = figure.get_2d_representation()
                    [print(item) for item in representation_2d]
                    is_2d_representation_available = True
                else:
                    print("Фігури немає!")
            case "3":
                if is_figure_available is True:
                    representation_3d = figure.get_3d_representation(scale=scale)
                    print(representation_3d)
                    is_3d_representation_available = True
                else:
                    print("Фігури немає!")
            case "4":
                if is_2d_representation_available is True:
                    try:
                        FileProcessor.write_into_file(representation_2d_file, "".join(representation_2d))
                    except PermissionError:
                        print("У вас немає дозволу на запис у файл!")
                    except FileNotFoundError:
                        print("Файл не існує!")
                else:
                    print("Фігури немає!")
            case "5":
                if is_3d_representation_available is True:
                    try:
                        FileProcessor.write_into_file(representation_3d_file, representation_3d)
                    except PermissionError:
                        print("У вас немає дозволу на запис у файл!")
                    except FileNotFoundError:
                        print("Файл не існує!")
                else:
                    print("Фігури немає!")
            case "0":
                break
            case _:
                print("Невірна опція!")

if __name__ == "__main__":
    main()
