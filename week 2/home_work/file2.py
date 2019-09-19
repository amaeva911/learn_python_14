"""

Домашнее задание 

Работы с файлами

* Скачайте файл по ссылке
* Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
* Подсчитайте количество слов в тексте
* Замените точки в тексте на восклицательные знаки
* Сохраните результат в файл referat2.txt

"""


def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as referat:
            text = referat.read()
            return text
    except FileNotFoundError:
        print('Файл не был найден, проверьте указанный путь и корректность переданного наименования файла')


def line_len(text):
    try:
        text_length = len(text)
        print(f'Общее количество символов: {text_length}')
    except ValueError:
        print('Невозможно посчитать длину строки, если это не строка :)')


def word_count(text):
    try:
        word_list = text.split()
        count = len(word_list)
        print(f'Количество слов в тексте: {count}')
    except ValueError:
        print('Невозможно посчитать количество слов, если считаешь не слова :)')


def point_to_exclamation_replace(text):
    try:
        final_text = text.replace(".","!")
        print('Символы "." успешно заменены на "!"')
        return final_text
    except ValueError:
        print('Это не похоже на текст, пожалуйста, перепроверьте отправленные данные :)')

def resave(text):
    with open('referat2.txt', 'w', encoding='utf-8') as rw:
        rw.write(text)
        print('Переданные данные были успешно записаны в "referat2.txt"')


file_name = 'referat.txt'

line_len(read_file(file_name))
word_count(read_file(file_name))

resave(point_to_exclamation_replace(read_file(file_name)))

