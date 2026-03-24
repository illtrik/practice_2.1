import csv

FILENAME = 'resource/products.csv'

def load_products(filename):
    products = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')  # delimiter=';' для Excel CSV
        for row in reader:
            row['Цена'] = int(row['Цена'])
            row['Количество'] = int(row['Количество'])
            products.append(row)
    return products

def save_products(filename, products):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Название', 'Цена', 'Количество']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')  # тоже delimiter=';'
        writer.writeheader()
        for product in products:
            writer.writerow(product)

def add_product(products):
    name = input('Введите название товара: ').strip()
    price = int(input('Введите цену товара: '))
    quantity = int(input('Введите количество товара: '))
    products.append({'Название': name, 'Цена': price, 'Количество': quantity})
    print(f'Товар "{name}" добавлен.')

def find_product(products, name):
    for product in products:
        if product['Название'].lower() == name.lower():
            return product
    return None

def calculate_total_cost(products):
    total = 0
    for product in products:
        total += product['Цена'] * product['Количество']
    return total

def main():
    products = load_products(FILENAME)
    while True:
        print('\nВыберите действие:')
        print('1 - Добавить товар')
        print('2 - Найти товар')
        print('3 - Показать общую стоимость всех товаров')
        print('4 - Сохранить и выйти')
        choice = input('Ваш выбор: ').strip()

        if choice == '1':
            add_product(products)
        elif choice == '2':
            name = input('Введите название товара для поиска: ')
            product = find_product(products, name)
            if product:
                print(f'Найден товар: {product}')
            else:
                print('Товар не найден.')
        elif choice == '3':
            total_cost = calculate_total_cost(products)
            print(f'Общая стоимость всех товаров: {total_cost}')
        elif choice == '4':
            save_products(FILENAME, products)
            print('Данные сохранены. Выход.')
            break
        else:
            print('Некорректный ввод, попробуйте снова.')

if __name__ == '__main__':
    main()