import json
import os

FILENAME = "resource/library.json"

def load_books():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as file:
        return json.load(file)

def save_books(books):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)

def show_books(books):
    if not books:
        print("Нет книг в базе.")
        return
    for book in books:
        status = "Доступна" if book.get("available", False) else "Занята"
        print(f"ID: {book['id']} | Название: {book['title']} | Автор: {book['author']} | Год: {book['year']} | Статус: {status}")

def search_books(books, query):
    query = query.lower()
    results = []
    for book in books:
        if query in book['title'].lower() or query in book['author'].lower():
            results.append(book)
    return results

def add_book(books):
    try:
        new_id = max(book["id"] for book in books) + 1 if books else 1
        title = input("Введите название книги: ").strip()
        author = input("Введите автора: ").strip()
        year = int(input("Введите год издания: "))
        available = True

        new_book = {
            "id": new_id,
            "title": title,
            "author": author,
            "year": year,
            "available": available
        }
        books.append(new_book)
        print("Книга добавлена!")
    except ValueError:
        print("Ошибка: год должен быть числом.")

def change_status(books):
    try:
        book_id = int(input("Введите ID книги для изменения статуса: "))
    except ValueError:
        print("Ошибка: ID должен быть числом.")
        return

    for book in books:
        if book["id"] == book_id:
            book["available"] = not book.get("available", True)
            status = "Доступна" if book["available"] else "Занята"
            print(f"Статус книги изменён на: {status}")
            return
    print("Книга с таким ID не найдена.")

def delete_book(books):
    try:
        book_id = int(input("Введите ID книги для удаления: "))
    except ValueError:
        print("Ошибка: ID должен быть числом.")
        return

    for i, book in enumerate(books):
        if book["id"] == book_id:
            del books[i]
            print("Книга удалена.")
            return
    print("Книга с таким ID не найдена.")

def export_available_books(books):
    available_books = [b for b in books if b.get("available", False)]
    if not available_books:
        print("Доступных книг нет для экспорта.")
        return

    with open("available_books.txt", "w", encoding="utf-8") as f:
        for book in available_books:
            f.write(f"{book['id']}: {book['title']} - {book['author']} ({book['year']})\n")
    print("Список доступных книг экспортирован в 'available_books.txt'.")

def main():
    books = load_books()

    while True:
        print("\nМеню:")
        print("1 - Просмотр всех книг")
        print("2 - Поиск по автору или названию")
        print("3 - Добавить новую книгу")
        print("4 - Изменить статус доступности книги (взята/возвращена)")
        print("5 - Удалить книгу по ID")
        print("6 - Экспорт доступных книг в available_books.txt")
        print("7 - Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            show_books(books)
        elif choice == "2":
            q = input("Введите название или автора для поиска: ").strip()
            results = search_books(books, q)
            if results:
                print(f"Найдено {len(results)} книг:")
                show_books(results)
            else:
                print("Книги не найдены.")
        elif choice == "3":
            add_book(books)
            save_books(books)
        elif choice == "4":
            change_status(books)
            save_books(books)
        elif choice == "5":
            delete_book(books)
            save_books(books)
        elif choice == "6":
            export_available_books(books)
        elif choice == "7":
            print("Выход. Пока!")
            break
        else:
            print("Неверный выбор. Повторите попытку.")

if __name__ == "__main__":
    main()