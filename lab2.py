import math

class Calculator:
    def __init__(self, language='ukrainian'):
        self.result = None
        self.history = []
        self.language = language

    def set_language(self, language):
        self.language = language

    def get_language(self):
        return self.language

    def get_operator_prompt(self):
        if self.language == 'english':
            return "Enter an expression (e.g., '2 + 2' or 'exit'): "
        elif self.language == 'ukrainian':
            return "Введіть вираз (наприклад, '2 + 2' або 'вихід'): "
        else:
            return "Enter an expression (e.g., '2 + 2' or 'exit'): "

    def get_continue_prompt(self):
        if self.language == 'english':
            return "Do you want to continue (yes/no)? "
        elif self.language == 'ukrainian':
            return "Бажаєте продовжити (так/ні)? "
        else:
            return "Do you want to continue (yes/no)? "

    def calculate(self, num1, operator, num2):
        try:
            num1 = float(num1)
            num2 = float(num2)
            if operator == '+':
                self.result = num1 + num2
            elif operator == '-':
                self.result = num1 - num2
            elif operator == '*':
                self.result = num1 * num2
            elif operator == '/':
                if num2 == 0 or num1 == 0:
                    return "Помилка: Не можна ділити на нуль!" if self.language == 'ukrainian' else "Error: Cannot divide by zero!"
                self.result = num1 / num2
            elif operator == '^':
                self.result = num1 ** num2
            elif operator == '√':
                if num1 < 0:
                    return "Помилка: Від'ємне число під коренем!" if self.language == 'ukrainian' else "Error: Negative number under the square root!"
                self.result = math.sqrt(num1)
            elif operator == '%':
                if num2 == 0:
                    return "Помилка: Ділення на нуль!" if self.language == 'ukrainian' else "Error: Division by zero!"
                self.result = num1 % num2
            else:
                return "Помилка: Невірний оператор!" if self.language == 'ukrainian' else "Error: Invalid operator!"
            return self.result
        except ValueError:
            return "Помилка: Невірний формат числа!" if self.language == 'ukrainian' else "Error: Invalid number format!"

    def check_operator(self, operator):
        if operator in ('+', '-', '*', '/'):
            return True
        else:
            return False

    def add_to_history(self, expression, result):
        self.history.append((expression, result))

    def show_history(self):
        if not self.history:
            print("Історія обчислень порожня." if self.language == 'ukrainian' else "Calculation history is empty.")
        else:
            print("Історія обчислень:" if self.language == 'ukrainian' else "Calculation history:")
            for idx, (expr, res) in enumerate(self.history, start=1):
                print(f"{idx}. {expr} = {res}")

    def user_input(self):
        expression = input(self.get_operator_prompt())
        return expression

    def perform_calculation(self, expression):
        try:
            num1, operator, num2 = map(str.strip, expression.split())
            if self.check_operator(operator):
                result = self.calculate(num1, operator, num2)
                if isinstance(result, str):
                    print(result)
                else:
                    print(f"Результат: {result}")
                    self.add_to_history(expression, result)
            else:
                print("Помилка: Невірний оператор!" if self.language == 'ukrainian' else "Error: Invalid operator!")
        except ValueError:
            print("Помилка: Невірний формат виразу!" if self.language == 'ukrainian' else "Error: Invalid expression format!")

    def main_loop(self):
        while True:
            expression = self.user_input()
            if expression.lower() == 'вихід' or expression.lower() == 'exit':
                break
            self.perform_calculation(expression)
            self.show_history()
            next_operation = input(self.get_continue_prompt())
            if next_operation.lower() != 'так' and next_operation.lower() != 'yes':
                break
        print("Програма завершена." if self.language == 'ukrainian' else "Program terminated.")

if __name__ == "__main__":
    print("Виберіть мову (українська або англійська):")
    selected_language = input("Choose a language (ukrainian or english): ").lower()
    while selected_language not in ['ukrainian', 'english']:
        print("Неправильно вибрана мова. Будь ласка, виберіть українську або англійську.")
        print("Invalid language selection. Please choose ukrainian or english.")
        selected_language = input("Choose a language (ukrainian or english): ").lower()
    calculator = Calculator(selected_language)
    calculator.main_loop()
