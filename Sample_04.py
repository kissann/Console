# Модуль OS

# Перегляд вмісту каталогів

import os
# Повертає список файлів та каталогів поточної папки
print(os.listdir())

# Доступ до всіх її підкаталогам і файлів
print(os.walk(os.getcwd()))

for root, ct, fls in os.walk(os.getcwd()):
    print(root)
    for dir in ct:
        print(dir)

    for file in fls:
        print(file)
