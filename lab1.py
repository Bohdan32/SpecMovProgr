import math

# Історія обчислень
calc_history = []

class CalculatorSettings:
    def __init__(self):
        self.decimal_places = 2  # Кількість десяткових знаків
        self.memory = 0.0  # Значення в пам'яті

    def set_decimal_places(self):
        try:
            self.decimal_places = int(input("Введіть кількість десяткових знаків: "))
        except ValueError:
            print("Помилка введення. Використовується значення за замовчуванням (2).")

    def set_memory(self, value):
        self.memory = value

    def get_memory(self):
        return self.memory

def add_to_history(expression, result):
    calc_history.append((expression, result))

def display_history():
    for i, (expression, result) in enumerate(calc_history, 1):
        print(f"{i}. {expression} = {result}")

def display_settings_menu(settings):
    print("\nНалаштування:")
    print("1. Кількість десяткових знаків")
    print("2. Пам'ять")
    print("3. Вихід з меню налаштувань")

def calculator():
    settings = CalculatorSettings()

    while True:
        try:
            # Введення користувача
            num1 = float(input("Введіть перше число: "))
            operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")
            num2 = float(input("Введіть друге число: "))

            # Перевірка оператора
            if operator not in ('+', '-', '*', '/', '^', '√', '%'):
                print("Помилковий оператор. Будь ласка, введіть дійсний оператор.")
                continue

            # Обчислення
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0 or num1 == 0:
                    raise ZeroDivisionError("Ділення на нуль недопустиме.")
                result = num1 / num2
            elif operator == '^':
                result = num1 ** num2
            elif operator == '√':
                result = math.sqrt(num1)
            elif operator == '%':
                result = num1 % num2

            # Округлення результату
            result = round(result, settings.decimal_places)

            # Збереження в історію
            expression = f"{num1} {operator} {num2}"
            add_to_history(expression, result)

            # Виведення результату
            print(f"Результат: {result}")

            # Повторення обчислень
            another_calculation = input("Виконати ще одне обчислення? (Так/Ні): ").strip().lower()
            if another_calculation != 'так':
                break

        except ValueError:
            print("Помилка введення. Будь ласка, введіть коректні числа.")
        except ZeroDivisionError as e:
            print(f"Помилка: {e}")

def settings_menu(settings):
    while True:
        display_settings_menu(settings)
        choice = input("Виберіть налаштування: ")

        if choice == '1':
            settings.set_decimal_places()
        elif choice == '2':
            try:
                value = float(input("Введіть значення для пам'яті: "))
                settings.set_memory(value)
            except ValueError:
                print("Помилка введення. Будь ласка, введіть коректне число.")
        elif choice == '3':
            break
        else:
            print("Недійсний вибір.")

if __name__ == "__main__":
    settings = CalculatorSettings()
    while True:
        main_menu_choice = input("Обчислення (1) / Налаштування (2) / Історія (3) / Вихід (4): ").strip()
        if main_menu_choice == '1':
            calculator()
        elif main_menu_choice == '2':
            settings_menu(settings)
        elif main_menu_choice == '3':
            display_history()
        elif main_menu_choice == '4':
            break
        else:
            print("Недійсний вибір.")
