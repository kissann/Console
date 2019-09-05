# підмодуль os.path
import os

# Повернення файла за вказаним шляхом
print(os.path.basename(os.getcwd() + "\\Sample_1.py"))

# Повертає тільки частину каталогу шляху
print(os.path.dirname(os.getcwd() + "\\Sample_1.py"))

# Перевіряє чи існує файл, чи ні
print(os.path.exists(os.getcwd() + "\\Sample_1.py"))

# isdir перевіряє тільки шлях до папок, а isfile, відповідно, до файлів
print(os.path.isfile(os.getcwd() + "\\Sample_1.py"))
print(os.path.isdir(os.getcwd()))

# Об'єднати шлях із файлом
print(os.path.join(os.getcwd(), 'Sample_1.py'))

# Розбити шлях на кортеж
print(os.path.split(os.path.join(os.getcwd(), 'Sample_1.py')))
