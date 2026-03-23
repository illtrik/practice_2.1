def write_lines_to_file(file_name, lines):
    with open(file_name, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

def read_lines_from_file(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return f.readlines()

def analyze_text(lines):
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    longest_line = max(lines, key=len).rstrip("\n")
    return num_lines, num_words, longest_line

def main():
    file_name = "resource/text.txt"
    lines = [
        "Первая строка для анализа.",
        "Здесь немного текста.",
        "Это третья строка.",
        "Четвертая строчка длиннее всех предыдущих.",
        "И наконец, пятая строка."
    ]

    write_lines_to_file(file_name, lines)
    lines_read = read_lines_from_file(file_name)
    num_lines, num_words, longest_line = analyze_text(lines_read)

    print(f"Количество строк в файле: {num_lines}")
    print(f"Количество слов в файле: {num_words}")
    print(f"Самая длинная строка: {longest_line}")

if __name__ == "__main__":
    main()
