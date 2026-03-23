lines = [
    "Привет, это первая строка.",
    "Вторая строка чуть длиннее первой.",
    "Третья строка тут.",
    "А вот и четвертая строка.",
    "Пятая и самая длинная строка в этом маленьком файле!"
]

with open("resource/text.txt", "w", encoding="utf-8") as file:
    for line in lines:
        file.write(line + "\n")

with open("resource/text.txt", "r", encoding="utf-8") as file:
    content = file.readlines()

num_lines = len(content)
num_words = sum(len(line.split()) for line in content)
longest_line = max(content, key=len).rstrip("\n")

print(f"Количество строк в файле: {num_lines}")
print(f"Количество слов в файле: {num_words}")
print(f"Самая длинная строка: {longest_line}")
