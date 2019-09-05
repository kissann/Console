#Задача 1
#Написати функцію, яка створює наступну ієрархію файлів та папок.
import os
import shutil
path=os.getcwd()+"/MainFolder"
def createDir():
    if os.path.exists(path):
        print("Директорія існує")
    else:
        os.mkdir("MainFolder")
        dd=os.getcwd()
        os.chdir(dd+'/MainFolder')
        print('Поточна директорія :', os.getcwd())
        for i in range(1,5):
            name="Folder"+str(i)
            os.mkdir(name)
            dd1 = os.getcwd()
            os.chdir(dd1 + '/'+name)
            os.mkdir("SubFolder"+str(i))
            open("File_0"+str(i)+".txt","w")
            os.chdir(dd1)
def menu():
    print("Меню")
    n = input("Пошук файла або директорії- Search\nВидалення файлу - DelFile\n Видалення каталогу - Del"
              "\nПерейменування визначеного файлу або папки - Ren\n Для переходу в папку використовуйте - cd \nВийти з консолі - ^")
    return n

createDir()

flag=True
f=False
while flag:
    n = menu()
    if n=="^":
        flag=False
        break
    elif n=="Search":
        find=input("Введіть ім'я файлу або директорії, або ^ - для виходу в верхнє меню")
        if find=="^":
            break
        else:
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.endswith(find):
                        print("МИ ЗНАЙШЛИ ФАЙЛ\n")
                        f=True
                        path_file = os.path.join(root, file)
                        print(path_file)
                for dir in dirs:
                    if dir.endswith(find):
                        print("МИ ЗНАЙШЛИ Директорію\n")
                        f=True
                        path_file = os.path.join(root, dir)
                        print(path_file)
        if f==False:
                print("Тут немає такого файлу")
    elif n=="Del":
        del1 = input("Введіть ім'я директорії")
        path1 = os.getcwd()+"/MainFolder/"+del1
        if os.path.exists(path1):
            if not os.listdir(path1):
                os.rmdir(path1)
            else:
                y=input("Папка не пуста. Чи видаляти її? Yes, No")
                if y=='Yes':
                    shutil.rmtree(path1)
                    print("Папку видалено")

        print("Ви в каталозі"+path+"\nВміст каталогу")
        print(os.listdir(path))
    elif n=="DelFile":
        del1 = input("Введіть ім'я файлу")
        path1 = os.getcwd() + "/MainFolder/"+del1
        if os.path.exists(path1):
            os.remove(path1)
        else:
            print("В цій директорії такого файлу немає")
            print(os.listdir(path))
    elif n=="Ren":
        ren = input("Введіть ім'я файлу або папки для перейменування")
        new_r=input("Введіть нове ім'я")

        if ren.find(".") == -1:
            path1 = os.getcwd() + "/MainFolder/" + ren
            path2=os.getcwd() + "/MainFolder/" + new_r
        else:
            path1 = os.getcwd() + "/MainFolder/" + ren
            path2 = os.getcwd() + "/MainFolder/" + new_r
        if os.path.exists(path1):
            os.rename(path1,path2)
        else:
            print("В цій директорії такого файлу немає")
            print(path1)
    elif n=="cd":
        path3 = os.getcwd()
        print(path3)
        print(os.listdir(path3))
        cd = input("Введіть папку для переходу")

        os.chdir(path3 + '/'+cd)
        path4=os.getcwd()
        print(path4)




