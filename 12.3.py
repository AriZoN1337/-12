# Читаем английско-русский словарь и формируем русско-английский
en_ru = {}

with open('en-ru.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if ' - ' in line:
            eng, rus = line.strip().split(' - ', 1)
            rus_words = [word.strip() for word in rus.split(',')]
            for r in rus_words:
                if r not in en_ru:
                    en_ru[r] = []
                en_ru[r].append(eng)

# Сортируем по русским словам
ru_en_sorted = dict(sorted(en_ru.items()))

# Записываем в файл ru-en.txt
with open('ru-en.txt', 'w', encoding='utf-8') as f:
    for rus_word, eng_list in ru_en_sorted.items():
        f.write(f"{rus_word} – {', '.join(sorted(set(eng_list)))}\n")

print("Русско-английский словарь создан и сохранён в ru-en.txt")
