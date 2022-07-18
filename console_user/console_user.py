import psycopg2
import work_with_bd
import sys

while True:
    print('~~~~~~~~~~~~~~~~~~~')
    LOGIN = input('LOGIN: ')
    PASSWORD = input('PASSWORD: ')
    if (LOGIN == 'university') and (PASSWORD == '123') :
        print("Database opened successfully")
        print('~~~~~~~~~~~~~~~~~~~')
        break
    else:
        print('INCORRECT LOGIN OR PASSWORD')
        print('~~~~~~~~~~~~~~~~~~~')

con = psycopg2.connect(
  database="university_db",
  user=str.strip(LOGIN),
  password=str.strip(PASSWORD),
  host="127.0.0.1",
  port="5432"
)

while True:
    print("1 - Вывод информации из таблиц \n2 - Закончить работу")

    try:
        what_do = input("Введите цифру: ")
    except Exception as error:
        print(f"You made error: {error}")

#REQUESTS
    if what_do == ("1"):
        while True:
            print('\n----------------------------------------------------------------------------------')
            print("1 - СПИСОК СТУДЕНТОВ \n2 - СДАЧА СЕССИЙ \n3 - ВЕДОМОСТЬ ГРУПП \n4 - ОТЧЁТ ОБ УСПЕВАЕОМСТИ \n5 - РЕЙТИНГ УСПЕВАЕМОСТИ \n6 - Выйти")

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
                    print("1 - Список Троечников \n2 - Список Хорошистов \n3 - Список Отличников")
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
    elif what_do == ('2'):
        print('EXIT...')
        input()
        break


#INCORRECT NUMBER
    else:
        print("INCORRECT NUMBER")
        print('----------------------------------------------------------------------------------\n')
