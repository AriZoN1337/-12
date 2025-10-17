import json

filename = 'products.json'

# Считываем существующий файл (если пуст, то создаем пустой список)
try:
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    data = {"products": []}

# Запрашиваем новые данные у пользователя
name = input("Введите название продукта: ")
price = int(input("Введите цену продукта: "))
available = input("Продукт в наличии? (да/нет): ").lower() == 'да'
weight = int(input("Введите вес продукта (в граммах): "))

# Добавляем новый продукт
new_product = {
    "name": name,
    "price": price,
    "available": available,
    "weight": weight
}
data["products"].append(new_product)

# Сохраняем обновленный файл
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Выводим все продукты на экран
for product in data["products"]:
    print(f"\nНазвание: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    print("В наличии" if product['available'] else "Нет в наличии!")
