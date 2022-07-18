import psycopg2
import work_with_bd
import sys

con = psycopg2.connect(
  database="university_db",
  user="university",
  password="123",
  host="127.0.0.1",
  port="5432"
)
print("Доступ предоставлен")
print('----------------------------------------------------------------------------------')

#MAIN CODE
while True:
    print("1 - Заполнение Таблиц \n2 - Измененеи Таблиц\n3 - Запросы к таблицам \n4 - Закончить работу")

    try:
        what_do = input("Введите цифру: ")
    except Exception as error:
        print(f"You made error: {error}")

#IMPORT DATA IN THE TABLES
    if what_do == ("1"):
        while True:
            print('\n----------------------------------------------------------------------------------')
            print("1 - Таблица Студенты \n2 - Таблицы Преподователи\n3 - Таблицы Предметы \n4 - Таблицы Оценки \n5 - Выйти")

            try:
                id_table = input("Введите цифру: ")
            except Exception as error:
                print(f"You made error: {error}")

            print('----------------------------------------------------------------------------------\n')
        #TABLE STUDENTS
            if id_table == ("1"):
                print("Предполагается, что файл находится в той же дерриктории, что и программа. \nЕсли файл находит в другой дерриктории, пропишите полный путь до неё. \nПри том заменяя значки слэшей на '/' ")
                name_file = input("Название файла: ")
                work_with_bd.import_from_file ('STUDENTS', name_file)

        #TABLES TEACHERS FIRST AND SECOND SEMESTRES
            elif id_table == ("2"):

                try:
                    id_semester = input("1 - 1 Semester | 2 - 2 Semester\nВведите цифру: ")
                except Exception as error:
                    print(f"You made error: {error}")

                if id_semester == ("1"):
                    print("Предполагается, что файл находится в той же дерриктории, что и программа. \nЕсли файл находит в другой дерриктории, пропишите полный путь до неё. \nПри том заменяя значки слэшей на '/' ")
                    name_file = input("Название файла: ")
                    work_with_bd.import_from_file ('TEACHERS_1SEMESTR', name_file)

                elif id_semester == ("2"):
                    print("Предполагается, что файл находится в той же дерриктории, что и программа. \nЕсли файл находит в другой дерриктории, пропишите полный путь до неё. \nПри том заменяя значки слэшей на '/' ")
                    name_file = input("Название файла: ")
                    work_with_bd.import_from_file ('TEACHERS_2SEMESTR', name_file)

        #TABLES SUBJECTS FIRST AND SECOND SEMESTERS
            elif id_table == ("3"):

                try:
                    id_semester = input("1 - 1 Semester | 2 - 2 Semester\nВведите цифру: ")
                except Exception as error:
                    print(f"You made error: {error}")

                if id_semester == ("1"):
                    print("Предполагается, что файл находится в той же дерриктории, что и программа. \nЕсли файл находит в другой дерриктории, пропишите полный путь до неё. \nПри том заменяя значки слэшей на '/' ")
                    name_file = input("Название файла: ")
                    work_with_bd.import_from_file ('SUBJECTS_1SEMESTR', name_file)

                elif id_semester == ("2"):
                    print("Предполагается, что файл находится в той же дерриктории, что и программа. \nЕсли файл находит в другой дерриктории, пропишите полный путь до неё. \nПри том заменяя значки слэшей на '/' ")
                    name_file = input("Название файла: ")
                    work_with_bd.import_from_file ('SUBJECTS_2SEMESTR', name_file)

        #TABLES ASSESSMENTS FIRST AND SECOND SEMESTRES
            elif id_table == ("4"):

                try:
                    id_semester = input("1 - 1 Semester | 2 - 2 Semester\nВведите цифру: ")
                except Exception as error:
                    print(f"You made error: {error}")

                if id_semester == ("1"):
                    print("Предполагается, что файл находится в той же дерриктории, что и программа. \nЕсли файл находит в другой дерриктории, пропишите полный путь до неё. \nПри том заменяя значки слэшей на '/' ")
                    name_file = input("Название файла: ")
                    work_with_bd.import_from_file ('ASSESSMENTS_1SEMESTR', name_file)

                elif id_semester == ("2"):
                    print("Предполагается, что файл находится в той же дерриктории, что и программа. \nЕсли файл находит в другой дерриктории, пропишите полный путь до неё. \nПри том заменяя значки слэшей на '/' ")
                    name_file = input("Название файла: ")
                    work_with_bd.import_from_file ('ASSESSMENTS_2SEMESTR', name_file)

        #EXIT TO MAIN MENUE
            elif id_table == ("5"):
                print("EXIT TO MAIN MENUE")
                break

        #INCORRECT NUMBER
            else:
                print("INCORRECT NUMBER")


#CHANGE INFORMATION IN TABLES
    elif what_do == ("2"):
        while True:
            print('\n----------------------------------------------------------------------------------')
            print("1 - Таблица Студенты \n2 - Таблицы Преподователи\n3 - Таблицы Предметы \n4 - Таблицы Оценки \n5 - Выйти")

            try:
                id_table = input("Введите цифру: ")

            except Exception as error:
                print(f"You made error: {error}")

            print('----------------------------------------------------------------------------------\n')
        #TABLE STUDENTS
            if id_table == ("1"):
                print("Предполагается, что файл находится в той же дерриктории, что и программа. \nЕсли файл находит в другой дерриктории, пропишите полный путь до неё. \nПри том заменяя значки слэшей на '/' ")
                name_file = input("Название файла: ")
                work_with_bd.change_table ('STUDENTS', name_file, id_table, 0)

        #TABLES TEACHERS
            elif id_table == ("2"):

                try:
                    id_semester = input("1 - 1 Semester | 2 - 2 Semester\nВведите цифру: ")
                except Exception as error:
                    print(f"You made error: {error}")

                if id_semester == ("1"):
                    print("Предполагается, что файл находится в той же дерриктории, что и программа. \nЕсли файл находит в другой дерриктории, пропишите полный путь до неё. \nПри том заменяя значки слэшей на '/' ")
                    name_file = input("Название файла: ")
                    work_with_bd.change_table ('TEACHERS_1SEMESTR', name_file, id_table, id_semester)

                elif id_semester == ("2"):
                    print("Предполагается, что файл находится в той же дерриктории, что и программа. \nЕсли файл находит в другой дерриктории, пропишите полный путь до неё. \nПри том заменяя значки слэшей на '/' ")
                    name_file = input("Название файла: ")
                    work_with_bd.change_table ('TEACHERS_2SEMESTR', name_file, id_table, id_semester)

        #TABLES SUBJECTS
            elif id_table == ("3"):

                try:
                    id_semester = input("1 - 1 Semester | 2 - 2 Semester\nВведите цифру: ")
                except Exception as error:
                    print(f"You made error: {error}")

                if id_semester == ("1"):
                    print("Предполагается, что файл находится в той же дерриктории, что и программа. \nЕсли файл находит в другой дерриктории, пропишите полный путь до неё. \nПри том заменяя значки слэшей на '/' ")
                    name_file = input("Название файла: ")
                    work_with_bd.change_table ('SUBJECTS_1SEMESTR', name_file, id_table, id_semester)

                elif id_semester == ("2"):
                    print("Предполагается, что файл находится в той же дерриктории, что и программа. \nЕсли файл находит в другой дерриктории, пропишите полный путь до неё. \nПри том заменяя значки слэшей на '/' ")
                    name_file = input("Название файла: ")
                    work_with_bd.change_table ('SUBJECTS_2SEMESTR', name_file, id_table, id_semester)

        #TABLES ASSESSMENTS
            elif id_table == ("4"):

                try:
                    id_semester = input("1 - 1 Semester | 2 - 2 Semester\nВведите цифру: ")
                except Exception as error:
                    print(f"You made error: {error}")

                if id_semester == ("1"):
                    print("Предполагается, что файл находится в той же дерриктории, что и программа. \nЕсли файл находит в другой дерриктории, пропишите полный путь до неё. \nПри том заменяя значки слэшей на '/' ")
                    name_file = input("Название файла: ")
                    work_with_bd.change_table ('ASSESSMENTS_1SEMESTR', name_file, id_table, id_semester)

                elif id_semester == ("2"):
                    print("Предполагается, что файл находится в той же дерриктории, что и программа. \nЕсли файл находит в другой дерриктории, пропишите полный путь до неё. \nПри том заменяя значки слэшей на '/' ")
                    name_file = input("Название файла: ")
                    work_with_bd.change_table ('ASSESSMENTS_2SEMESTR', name_file, id_table, id_semester)

        #EXIT TO MAIN MENUE
            elif id_table == ("5"):
                print("EXIT")
                break

        #INCORRECT NUMBER
            else:
                print("INCORRECT NUMBER")


#REQUESTS
    elif what_do == ("3"):
        while True:
            print('\n----------------------------------------------------------------------------------')
            print("1 - СПИСОК СТУДЕНТОВ \n2 - ЗДАЧА СЕССИЙ \n3 - ВЕДОМОСТЬ ГРУПП \n4 - ОТЧЁТ ОБ УСПЕВАЕОМСТИ \n5 - РЕЙТИНГ УСПЕВАЕМОСТИ \n6 - Выйти")

            try:
                id_request = input("Введите цифру: ")
            except Exception as error:
                print(f"You made error: {error}")

            if id_request == ("6"):
                print("Exit to main menu")
                print('----------------------------------------------------------------------------------\n')
                break

            print("1 - Вывод в файл | 2 - Вывод на экран")
            try:
                id_print = input("Ввдеите цифру: ")
            except Exception as error:
                print(f"You made error: {error}")


        #EXPORT IN FILE
            if id_print == ("1"):

            #EXPORT LIST STUDENTS
                if id_request == ("1"):
                    print('---------------------------------------------------------------------------------\n')
                    work_with_bd.export_students ()

            #EXPORT LIST ASSESSMENTS WITH SORT (only 3, only 4 and 5, only 5)
                elif id_request == ("2"):
                    print('\n----------------------------------------------------------------------------------')
                    print("1 - Список Тройшников \n2 - Список Хорошистов \n3 - Список Отличников")
                    try:
                        list_pass = input("Введите цифру: ")
                        id_semester = input("\n1 - 1 Semester | 2 - 2 Semester\nВведите цифру: ")
                    except Exception as error:
                        print(f"You made error {error}")

                    print('---------------------------------------------------------------------------------\n')
                    work_with_bd.export_assessments(list_pass, id_semester)


            #EXPORT LIST ALL ASSESSMENTS WITH SORT (from 5 to 3)
                elif id_request == ("3"):
                    try:
                        id_semester = input("\n1 - 1 Semester | 2 - 2 Semester\nВведите цифру: ")
                    except Exception as error:
                        print(f"You made error {error}")

                    print('---------------------------------------------------------------------------------\n')
                    work_with_bd.export_all_assessments(id_semester)

            #EXPORT LIST FOR ONE STUDENT
                elif id_request == ("4"):
                    try:
                        id_student = input("\nВведите идентификатор 'ID' студента:")
                        id_semester = input("\n1 - 1 Semester | 2 - 2 Semester\nВведите цифру: ")
                    except Exception as error:
                        print(f"You made error {error}")

                    print('---------------------------------------------------------------------------------\n')
                    work_with_bd.export_one_student(id_student, id_semester)

            #EXPORT LIST WITH AVG ASSESSMENTS
                elif id_request == ("5"):
                    try:
                        id_semester = input("\n1 - 1 Semester | 2 - 2 Semester\nВведите цифру: ")
                    except Exception as error:
                        print(f"You made error {error}")

                    print('----------------------------------------------------------------------------------\n')
                    work_with_bd.export_avg_assessments(id_semester)

                else:
                    print("INCORRECT NUMBER")


        #SHOW IN CONSOLE
            if id_print == ("2"):

            #SHOW LIST STUDENTS
                if id_request == ("1"):
                    print('---------------------------------------------------------------------------------\n')
                    work_with_bd.show_students ()

            #SHOW LIST ASSESSMENTS WITH SORT (only 3, only 4 and 5, only 5)
                elif id_request == ("2"):
                    print('\n----------------------------------------------------------------------------------')
                    print("1 - Список Тройшников \n2 - Список Хорошистов \n3 - Список Отличников")
                    try:
                        list_pass = input("Введите цифру: ")
                        id_semester = input("\n1 - 1 Semester | 2 - 2 Semester\nВведите цифру: ")
                    except Exception as error:
                        print(f"You made error {error}")

                    print('---------------------------------------------------------------------------------\n')
                    work_with_bd.show_assessments(list_pass, id_semester)

            #SHOW LIST ALL ASSESSMENTS WITH SORT (from 5 to 3)
                elif id_request == ("3"):
                    try:
                        id_semester = input("\n1 - 1 Semester | 2 - 2 Semester\nВведите цифру: ")
                    except Exception as error:
                        print(f"You made error {error}")

                    print('---------------------------------------------------------------------------------\n')
                    work_with_bd.show_all_assessments(id_semester)

            #SHOW LIST FOR ONE STUDENT
                elif id_request == ("4"):
                    try:
                        id_student = input("\nВведите идентификатор 'ID' студента:")
                        id_semester = input("\n1 - 1 Semester | 2 - 2 Semester\nВведите цифру: ")
                    except Exception as error:
                        print(f"You made error {error}")

                    print('---------------------------------------------------------------------------------\n')
                    work_with_bd.show_one_student(id_student, id_semester)

            #SHOW LIST WITH AVG ASSESSMENTS
                elif id_request == ("5"):
                    try:
                        id_semester = input("\n1 - 1 Semester | 2 - 2 Semester\nВведите цифру: ")
                    except Exception as error:
                        print(f"You made error {error}")

                    print('----------------------------------------------------------------------------------\n')
                    work_with_bd.show_avg_assessments(id_semester)

                else:
                    print("INCORRECT NUMBER")
#EXIT
    elif what_do == ('4'):
        print('EXIT...')
        input()
        break


#INCORRECT NUMBER
    else:
        print("INCORRECT NUMBER")
        print('----------------------------------------------------------------------------------\n')
