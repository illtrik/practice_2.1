import logging
from datetime import datetime
import os

LOG_FILE = "calculator.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='[%(asctime)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def read_last_operations(n=5):
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return lines[-n:]

def clear_log():
    open(LOG_FILE, "w", encoding="utf-8").close()
    print("Лог файл очищен.")

def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '_':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise ZeroDivisionError("Деление на ноль запрещено!")
        return num1 / num2
    else:
        raise ValueError("Неверная операция!")

def main():
    print("Последние 5 операций в логе:")
    last_ops = read_last_operations()
    if last_ops:
        for op in last_ops:
            print(op.strip())
    else:
        print("Лог пустой.")

    while True:
        print("\nВведите 'clear' для очистки лога, 'exit' для выхода.")
        inp = input("Жми Enter чтобы продолжить или команда: ").strip().lower()
        if inp == "clear":
            clear_log()
            continue
        elif inp == "exit":
            print("Пока!")
            break

        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            operation = input("Введите операцию (+, -, _, /): ").strip()
            result = calculate(num1, num2, operation)
        except ValueError as ve:
            print(f"Ошибка: {ve}")
            continue
        except ZeroDivisionError as zde:
            print(f"Ошибка: {zde}")
            continue

        print(f"Результат: {result}")

        log_message = f"{num1} {operation} {num2} = {result}"
        logging.info(log_message)

if __name__ == "__main__":
    main()