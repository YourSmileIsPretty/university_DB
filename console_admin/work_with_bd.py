import sys
import time
import psycopg2
import prettytable
from prettytable import from_csv
from prettytable import PrettyTable
from operator import itemgetter


#BLOCK STANDART FUNCTION: IMPORT ANG CHANGE INFORMATION IN THE BD
def import_from_file (table_name, name_file):
    con = None
    f = None

    try:
        con = psycopg2.connect(
          database="university_db",
          user="university",
          password="123",
          host="127.0.0.1",
          port="5432"
        )

        cur = con.cursor()
        f = open(name_file, 'r')

        cur.copy_from(f, table_name, sep="|")
        con.commit()

    except psycopg2.DatabaseError as e:

        if con:
            con.rollback()

        print(f'Error {e}')
        sys.exit(1)

    except IOError as e:

        if con:
            con.rollback()

        print(f'Error {e}')
        sys.exit(1)

    finally:

        if con:
            con.close()

        if f:
            f.close()
    print('Data inputed successfully')

def change_table (table_name, name_file, id_table, id_semester):
    con = None
    f = None

    try:
        con = psycopg2.connect(
          database="university_db",
          user="university",
          password="123",
          host="127.0.0.1",
          port="5432"
        )

        cur = con.cursor()

        if id_table == ("1"):
            cur.execute ("DELETE from STUDENTS")

        elif id_table == ("2"):
            if id_semester == ("1"):
                cur.execute ("DELETE from TEACHERS_1SEMESTR")
            elif id_semester == ("2"):
                cur.execute ("DELETE from TEACHERS_2SEMESTR")
            else:
                print("SEMESTER is INCORRECT")

        elif id_table == ("3"):
            if id_semester == ("1"):
                cur.execute ("DELETE from SUBJECTS_1SEMESTR")
            elif id_semester == ("2"):
                cur.execute ("DELETE from SUBJECTS_2SEMESTR")
            else:
                print("SEMESTER is INCORRECT")

        elif id_table == ("4"):
            if id_semester == ("1"):
                cur.execute ("DELETE from ASSESSMENTS_1SEMESTR")
            elif id_semester == ("2"):
                cur.execute ("DELETE from ASSESSMENTS_2SEMESTR")
            else:
                print("SEMESTER is INCORRECT")

        else:
            print('ID_TABLE is INCORRECT')


        f = open(name_file, 'r')
        cur.copy_from(f, table_name, sep="|")
        con.commit()

    except psycopg2.DatabaseError as e:

        if con:
            con.rollback()

        print(f'Error {e}')
        sys.exit(1)

    except IOError as e:

        if con:
            con.rollback()

        print(f'Error {e}')
        sys.exit(1)

    finally:

        if con:
            con.close()

        if f:
            f.close()
    print('Data change successfully')


#BLOCK EXPORTS
def export_students ():
    con = None
    fout = None

    try:
        con = psycopg2.connect(
          database="university_db",
          user="university",
          password="123",
          host="127.0.0.1",
          port="5432"
        )


        cur = con.cursor()
        fout = open("list_students.csv", 'w')
        cur.copy_to(fout, 'STUDENTS', sep="|")

    except psycopg2.DatabaseError as e:

        print(f'Error {e}')
        sys.exit(1)

    except IOError as e:

        print(f'Error {e}')
        sys.exit(1)

    finally:

        if con:
            con.close()

        if fout:
            fout.close()

    print("Data export in file 'list_students.csv' successfully")

def export_assessments(list_pass, id_semester):

    try:
        con = psycopg2.connect(
          database="university_db",
          user="university",
          password="123",
          host="127.0.0.1",
          port="5432"
        )


        cur = con.cursor()
    #EXPORT LIST ASSESSMENTS ONLY 3
        if list_pass == ("1"):

            if id_semester == ("1"):
                request = ("COPY (SELECT ASSESSMENTS_1SEMESTR.id, ASSESSMENTS_1SEMESTR.ASSESSMENT, STUDENTS.NAME, SUBJECTS_1SEMESTR.TITLE from ASSESSMENTS_1SEMESTR LEFT JOIN STUDENTS on STUDENTS.id = ASSESSMENTS_1SEMESTR.ID_STUDENT LEFT JOIN SUBJECTS_1SEMESTR on SUBJECTS_1SEMESTR.id = ASSESSMENTS_1SEMESTR.ID_SUBJECT_1S WHERE ASSESSMENTS_1SEMESTR.ASSESSMENT = '3' ORDER BY ASSESSMENTS_1SEMESTR.ID_STUDENT) TO STDOUT WITH CSV DELIMITER '|' HEADER")

                with open ("list_assessments_1semestr_only_3.csv", 'w') as file:
                    cur.copy_expert(request, file)

                print("Data export in file 'list_assessments_1semestr_only_3.csv' successfully")

            elif id_semester == ("2"):
                request = ("COPY (SELECT ASSESSMENTS_2SEMESTR.id, ASSESSMENTS_2SEMESTR.ASSESSMENT, STUDENTS.NAME, SUBJECTS_2SEMESTR.TITLE from ASSESSMENTS_2SEMESTR LEFT JOIN STUDENTS on STUDENTS.id = ASSESSMENTS_2SEMESTR.ID_STUDENT LEFT JOIN SUBJECTS_2SEMESTR on SUBJECTS_2SEMESTR.id = ASSESSMENTS_2SEMESTR.ID_SUBJECT_2S WHERE ASSESSMENTS_2SEMESTR.ASSESSMENT = '3' ORDER BY ASSESSMENTS_2SEMESTR.ID_STUDENT) TO STDOUT WITH CSV DELIMITER '|' HEADER")

                with open ("list_assessments_2semestr_only_3.csv", 'w') as file:
                    cur.copy_expert(request, file)

                print("Data export in file 'list_assessments_2semestr_only_3.csv' successfully")

            else:
                print("SEMESTER is INCORRECT")

    #EXPORT LIST ASSESSMENTS 4 and 5
        elif list_pass == ("2"):

            if id_semester == ("1"):
                request = ("COPY (SELECT ASSESSMENTS_1SEMESTR.id, ASSESSMENTS_1SEMESTR.ASSESSMENT, STUDENTS.NAME, SUBJECTS_1SEMESTR.TITLE from ASSESSMENTS_1SEMESTR LEFT JOIN STUDENTS on STUDENTS.id = ASSESSMENTS_1SEMESTR.ID_STUDENT LEFT JOIN SUBJECTS_1SEMESTR on SUBJECTS_1SEMESTR.id = ASSESSMENTS_1SEMESTR.ID_SUBJECT_1S WHERE ASSESSMENTS_1SEMESTR.ASSESSMENT IN ('4', '5') ORDER BY ASSESSMENTS_1SEMESTR.ID_STUDENT) TO STDOUT WITH CSV DELIMITER '|' HEADER")

                with open ("list_assessments_1semestr_only_4or5.csv", 'w') as file:
                    cur.copy_expert(request, file)

                print("Data export in file 'list_assessments_1semestr_only_4or5.csv' successfully")

            elif id_semester == ("2"):
                request = ("COPY (SELECT ASSESSMENTS_2SEMESTR.id, ASSESSMENTS_2SEMESTR.ASSESSMENT, STUDENTS.NAME, SUBJECTS_2SEMESTR.TITLE from ASSESSMENTS_2SEMESTR LEFT JOIN STUDENTS on STUDENTS.id = ASSESSMENTS_2SEMESTR.ID_STUDENT LEFT JOIN SUBJECTS_2SEMESTR on SUBJECTS_2SEMESTR.id = ASSESSMENTS_2SEMESTR.ID_SUBJECT_2S WHERE ASSESSMENTS_2SEMESTR.ASSESSMENT IN ('4', '5') ORDER BY ASSESSMENTS_2SEMESTR.ID_STUDENT) TO STDOUT WITH CSV DELIMITER '|' HEADER")

                with open ("list_assessments_2semestr_only_4or5.csv", 'w') as file:
                    cur.copy_expert(request, file)

                print("Data export in file 'list_assessments_2semestr_only_4or5.csv' successfully")

            else:
                print("SEMESTER is INCORRECT")

    #EXPORT LIST ASSESSMENTS ONLY 5
        elif list_pass == ("3"):
            if id_semester == ("1"):
                request = ("COPY (SELECT ASSESSMENTS_1SEMESTR.id, ASSESSMENTS_1SEMESTR.ASSESSMENT, STUDENTS.NAME, SUBJECTS_1SEMESTR.TITLE from ASSESSMENTS_1SEMESTR LEFT JOIN STUDENTS on STUDENTS.id = ASSESSMENTS_1SEMESTR.ID_STUDENT LEFT JOIN SUBJECTS_1SEMESTR on SUBJECTS_1SEMESTR.id = ASSESSMENTS_1SEMESTR.ID_SUBJECT_1S WHERE ASSESSMENTS_1SEMESTR.ASSESSMENT = '5' ORDER BY ASSESSMENTS_1SEMESTR.ID_STUDENT) TO STDOUT WITH CSV DELIMITER '|' HEADER")

                with open ("list_assessments_1semestr_only_5.csv", 'w') as file:
                    cur.copy_expert(request, file)

                print("Data export in file 'list_assessments_1semestr_only_5.csv' successfully")

            elif id_semester == ("2"):
                request = ("COPY (SELECT ASSESSMENTS_2SEMESTR.id, ASSESSMENTS_2SEMESTR.ASSESSMENT, STUDENTS.NAME, SUBJECTS_2SEMESTR.TITLE from ASSESSMENTS_2SEMESTR LEFT JOIN STUDENTS on STUDENTS.id = ASSESSMENTS_2SEMESTR.ID_STUDENT LEFT JOIN SUBJECTS_2SEMESTR on SUBJECTS_2SEMESTR.id = ASSESSMENTS_2SEMESTR.ID_SUBJECT_2S WHERE ASSESSMENTS_2SEMESTR.ASSESSMENT = '5' ORDER BY ASSESSMENTS_2SEMESTR.ID_STUDENT) TO STDOUT WITH CSV DELIMITER '|' HEADER")

                with open ("list_assessments_2semestr_only_5.csv", 'w') as file:
                    cur.copy_expert(request, file)

                print("Data export in file 'list_assessments_2semestr_only_5.csv' successfully")

            else:
                print("SEMESTER INCORRECT")

    except psycopg2.DatabaseError as e:

        print(f'Error {e}')
        sys.exit(1)

    except IOError as e:

        print(f'Error {e}')
        sys.exit(1)

    finally:

        if con:
            con.close()

def export_all_assessments(id_semester):
    try:
        con = psycopg2.connect(
          database="university_db",
          user="university",
          password="123",
          host="127.0.0.1",
          port="5432"
        )

        cur = con.cursor()

        if id_semester == ("1"):
            request = ("COPY (SELECT ASSESSMENTS_1SEMESTR.id, ASSESSMENTS_1SEMESTR.ASSESSMENT, STUDENTS.NAME, SUBJECTS_1SEMESTR.TITLE from ASSESSMENTS_1SEMESTR LEFT JOIN STUDENTS on STUDENTS.id = ASSESSMENTS_1SEMESTR.ID_STUDENT LEFT JOIN SUBJECTS_1SEMESTR on SUBJECTS_1SEMESTR.id = ASSESSMENTS_1SEMESTR.ID_SUBJECT_1S ORDER BY ASSESSMENTS_1SEMESTR.ID_STUDENT) TO STDOUT WITH CSV DELIMITER '|' HEADER")

            with open ("ALL_assessments_1semestr.csv", 'w') as file:
                cur.copy_expert(request, file)

            print("Data export in file 'ALL_assessments_1semestr.csv' successfully")

        elif id_semester == ("2"):
            request = ("COPY (SELECT ASSESSMENTS_2SEMESTR.id, ASSESSMENTS_2SEMESTR.ASSESSMENT, STUDENTS.NAME, SUBJECTS_2SEMESTR.TITLE from ASSESSMENTS_2SEMESTR LEFT JOIN STUDENTS on STUDENTS.id = ASSESSMENTS_2SEMESTR.ID_STUDENT LEFT JOIN SUBJECTS_2SEMESTR on SUBJECTS_2SEMESTR.id = ASSESSMENTS_2SEMESTR.ID_SUBJECT_2S ORDER BY ASSESSMENTS_2SEMESTR.ID_STUDENT) TO STDOUT WITH CSV DELIMITER '|' HEADER")

            with open ("ALL_assessments_2semestr.csv", 'w') as file:
                cur.copy_expert(request, file)

            print("Data export in file 'ALL_assessments_2semestr.csv' successfully")

        else:
            print("SEMESTER is INCORRECT")



    except psycopg2.DatabaseError as e:

        print(f'Error {e}')
        sys.exit(1)

    except IOError as e:

        print(f'Error {e}')
        sys.exit(1)

    finally:

        if con:
            con.close()

def export_one_student(id_student, id_semester):
    try:
        con = psycopg2.connect(
          database="university_db",
          user="university",
          password="123",
          host="127.0.0.1",
          port="5432"
        )

        cur = con.cursor()

        if id_semester == ('1'):
            request = ("COPY (SELECT ASSESSMENTS_1SEMESTR.id, ASSESSMENTS_1SEMESTR.ASSESSMENT, STUDENTS.NAME, SUBJECTS_1SEMESTR.TITLE from ASSESSMENTS_1SEMESTR LEFT JOIN STUDENTS on STUDENTS.id = ASSESSMENTS_1SEMESTR.ID_STUDENT LEFT JOIN SUBJECTS_1SEMESTR on SUBJECTS_1SEMESTR.id = ASSESSMENTS_1SEMESTR.ID_SUBJECT_1S WHERE STUDENTS.id = {0} ORDER BY ASSESSMENTS_1SEMESTR.ID_STUDENT) TO STDOUT WITH CSV DELIMITER '|' HEADER".format(id_student))

            name_file = id_student + '_list_with_assessments_1semestr.csv'

            with open (name_file, 'w') as file:
                cur.copy_expert(request, file)

            print(f"Data export in file '{name_file}' successfully")

        elif id_semester == ('2'):
            request = ("COPY (SELECT ASSESSMENTS_2SEMESTR.id, ASSESSMENTS_2SEMESTR.ASSESSMENT, STUDENTS.NAME, SUBJECTS_2SEMESTR.TITLE from ASSESSMENTS_2SEMESTR LEFT JOIN STUDENTS on STUDENTS.id = ASSESSMENTS_2SEMESTR.ID_STUDENT LEFT JOIN SUBJECTS_2SEMESTR on SUBJECTS_2SEMESTR.id = ASSESSMENTS_2SEMESTR.ID_SUBJECT_2S WHERE STUDENTS.id = {0} ORDER BY ASSESSMENTS_2SEMESTR.ID_STUDENT) TO STDOUT WITH CSV DELIMITER '|' HEADER".format(id_student))

            name_file = id_student + '_list_with_assessments_2semestr.csv'

            with open (name_file, 'w') as file:
                cur.copy_expert(request, file)

            print(f"Data export in file '{name_file}' successfully")

        else:
            print("SEMESTER is INCORRECT")

    except psycopg2.DatabaseError as e:

        print(f'Error {e}')
        sys.exit(1)

    except IOError as e:

        print(f'Error {e}')
        sys.exit(1)

    finally:

        if con:
            con.close()

def export_avg_assessments(id_semester):
    try:
        con = psycopg2.connect(
          database="university_db",
          user="university",
          password="123",
          host="127.0.0.1",
          port="5432"
        )

        cur = con.cursor()

        if id_semester == ("1"):
            request = ("COPY (SELECT STUDENTS.NAME, round(avg(ASSESSMENTS_1SEMESTR.ASSESSMENT),2) as avg_assessments from ASSESSMENTS_1SEMESTR LEFT JOIN STUDENTS on STUDENTS.id = ASSESSMENTS_1SEMESTR.ID_STUDENT LEFT JOIN SUBJECTS_1SEMESTR on SUBJECTS_1SEMESTR.id = ASSESSMENTS_1SEMESTR.ID_SUBJECT_1S GROUP BY STUDENTS.NAME ORDER BY avg_assessments desc) TO STDOUT WITH CSV DELIMITER '|' HEADER")

            with open ("AVG_assessments_1semestr.csv", 'w') as file:
                cur.copy_expert(request, file)
            print("Data export in file 'AVG_assessments_1semestr.csv' successfully")

        elif id_semester == ("2"):
            request = ("COPY (SELECT STUDENTS.NAME, round(avg(ASSESSMENTS_2SEMESTR.ASSESSMENT),2) as avg_assessments from ASSESSMENTS_2SEMESTR LEFT JOIN STUDENTS on STUDENTS.id = ASSESSMENTS_2SEMESTR.ID_STUDENT LEFT JOIN SUBJECTS_2SEMESTR on SUBJECTS_2SEMESTR.id = ASSESSMENTS_2SEMESTR.ID_SUBJECT_2S GROUP BY STUDENTS.NAME ORDER BY avg_assessments desc) TO STDOUT WITH CSV DELIMITER '|' HEADER")

            with open ("AVG_assessments_2semestr.csv", 'w') as file:
                cur.copy_expert(request, file)
            print("Data export in file 'AVG_assessments_2semestr.csv' successfully")

        else:
            print("SEMESTER is INCORRECT")



    except psycopg2.DatabaseError as e:

        print(f'Error {e}')
        sys.exit(1)

    except IOError as e:

        print(f'Error {e}')
        sys.exit(1)

    finally:

        if con:
            con.close()


#BLOCK SHOW INFORMATION IN CONSOLE
def show_students ():
    try:
        con = psycopg2.connect(
         database="university_db",
         user="university",
         password="123",
         host="127.0.0.1",
         port="5432"
        )


        cur = con.cursor()
        cur.execute("SELECT students.id, students.name from students")
        rows = sorted(cur.fetchall(), key=itemgetter(0))
        th = ['ID', 'Name']
        td = []

        for row in rows:
            td.append(row[0])
            td.append(row[1])

        columns = len(th)
        table = PrettyTable(th)
        td_data = td[:]

        while td_data:
            table.add_row(td_data[:columns])
            td_data = td_data[columns:]

        print('Подождите пару секунд...')
        time.sleep(2)
        print(table)


    except psycopg2.DatabaseError as e:

        print(f'Error {e}')
        sys.exit(1)

    except IOError as e:

        print(f'Error {e}')
        sys.exit(1)

    finally:

        if con:
            con.close()

def show_assessments (list_pass, id_semester):
    try:
        con = psycopg2.connect(
         database="university_db",
         user="university",
         password="123",
         host="127.0.0.1",
         port="5432"
        )


    #SHOW LIST ASSESSMENTS ONLY 3
        cur = con.cursor()
        if list_pass == ("1"):

            if id_semester == ("1"):
                cur.execute("SELECT ASSESSMENTS_1SEMESTR.id, STUDENTS.NAME, ASSESSMENTS_1SEMESTR.ASSESSMENT, SUBJECTS_1SEMESTR.TITLE from ASSESSMENTS_1SEMESTR LEFT JOIN STUDENTS on STUDENTS.id = ASSESSMENTS_1SEMESTR.ID_STUDENT LEFT JOIN SUBJECTS_1SEMESTR on SUBJECTS_1SEMESTR.id = ASSESSMENTS_1SEMESTR.ID_SUBJECT_1S WHERE ASSESSMENTS_1SEMESTR.ASSESSMENT = '3' ")


            elif id_semester == ("2"):
                cur.execute("SELECT ASSESSMENTS_2SEMESTR.id, STUDENTS.NAME, ASSESSMENTS_2SEMESTR.ASSESSMENT, SUBJECTS_2SEMESTR.TITLE from ASSESSMENTS_2SEMESTR LEFT JOIN STUDENTS on STUDENTS.id = ASSESSMENTS_2SEMESTR.ID_STUDENT LEFT JOIN SUBJECTS_2SEMESTR on SUBJECTS_2SEMESTR.id = ASSESSMENTS_2SEMESTR.ID_SUBJECT_2S WHERE ASSESSMENTS_2SEMESTR.ASSESSMENT = '3' ")

            else:
                print("SEMESTER is INCORRECT")

    #SHOW LIST ASSESSMENTS 4 and 5
        elif list_pass == ("2"):

            if id_semester == ("1"):
                cur.execute("SELECT ASSESSMENTS_1SEMESTR.id, STUDENTS.NAME, ASSESSMENTS_1SEMESTR.ASSESSMENT, SUBJECTS_1SEMESTR.TITLE from ASSESSMENTS_1SEMESTR LEFT JOIN STUDENTS on STUDENTS.id = ASSESSMENTS_1SEMESTR.ID_STUDENT LEFT JOIN SUBJECTS_1SEMESTR on SUBJECTS_1SEMESTR.id = ASSESSMENTS_1SEMESTR.ID_SUBJECT_1S WHERE ASSESSMENTS_1SEMESTR.ASSESSMENT IN ('4', '5')")

            elif id_semester == ("2"):
                cur.execute("SELECT ASSESSMENTS_2SEMESTR.id, STUDENTS.NAME, ASSESSMENTS_2SEMESTR.ASSESSMENT, SUBJECTS_2SEMESTR.TITLE from ASSESSMENTS_2SEMESTR LEFT JOIN STUDENTS on STUDENTS.id = ASSESSMENTS_2SEMESTR.ID_STUDENT LEFT JOIN SUBJECTS_2SEMESTR on SUBJECTS_2SEMESTR.id = ASSESSMENTS_2SEMESTR.ID_SUBJECT_2S WHERE ASSESSMENTS_2SEMESTR.ASSESSMENT IN ('4', '5')")

            else:
                print("SEMESTER is INCORRECT")

    #SHOW LIST ASSESSMENTS ONLY 5
        elif list_pass == ("3"):
            if id_semester == ("1"):
                cur.execute("SELECT ASSESSMENTS_1SEMESTR.id, STUDENTS.NAME, ASSESSMENTS_1SEMESTR.ASSESSMENT, SUBJECTS_1SEMESTR.TITLE from ASSESSMENTS_1SEMESTR LEFT JOIN STUDENTS on STUDENTS.id = ASSESSMENTS_1SEMESTR.ID_STUDENT LEFT JOIN SUBJECTS_1SEMESTR on SUBJECTS_1SEMESTR.id = ASSESSMENTS_1SEMESTR.ID_SUBJECT_1S WHERE ASSESSMENTS_1SEMESTR.ASSESSMENT = '5'")

            elif id_semester == ("2"):
                cur.execute("SELECT ASSESSMENTS_2SEMESTR.id, STUDENTS.NAME, ASSESSMENTS_2SEMESTR.ASSESSMENT, SUBJECTS_2SEMESTR.TITLE from ASSESSMENTS_2SEMESTR LEFT JOIN STUDENTS on STUDENTS.id = ASSESSMENTS_2SEMESTR.ID_STUDENT LEFT JOIN SUBJECTS_2SEMESTR on SUBJECTS_2SEMESTR.id = ASSESSMENTS_2SEMESTR.ID_SUBJECT_2S WHERE ASSESSMENTS_2SEMESTR.ASSESSMENT = '5'")

            else:
                print("SEMESTER INCORRECT")


        rows = sorted(cur.fetchall(), key=itemgetter(0))
        th = ['ID', 'Name', 'Assessment', 'Title Subject']
        td = []

        for row in rows:
            td.append(row[0])
            td.append(row[1])
            td.append(row[2])
            td.append(str(row[3]))

        columns = len(th)
        table = PrettyTable(th)
        td_data = td[:]

        while td_data:
            table.add_row(td_data[:columns])
            td_data = td_data[columns:]

        print('Подождите пару секунд...')
        print(f'Table from {id_semester}')
        time.sleep(2)
        print(table)


    except psycopg2.DatabaseError as e:

        print(f'Error {e}')
        sys.exit(1)

    except IOError as e:

        print(f'Error {e}')
        sys.exit(1)

    finally:

        if con:
            con.close()

def show_all_assessments(id_semester):
    try:
        con = psycopg2.connect(
          database="university_db",
          user="university",
          password="123",
          host="127.0.0.1",
          port="5432"
        )

        cur = con.cursor()
        if id_semester == ("1"):
            cur.execute("SELECT ASSESSMENTS_1SEMESTR.id, STUDENTS.NAME, ASSESSMENTS_1SEMESTR.ASSESSMENT, SUBJECTS_1SEMESTR.TITLE from ASSESSMENTS_1SEMESTR LEFT JOIN STUDENTS on STUDENTS.id = ASSESSMENTS_1SEMESTR.ID_STUDENT LEFT JOIN SUBJECTS_1SEMESTR on SUBJECTS_1SEMESTR.id = ASSESSMENTS_1SEMESTR.ID_SUBJECT_1S")

        elif id_semester == ("2"):
            cur.execute("SELECT ASSESSMENTS_2SEMESTR.id, STUDENTS.NAME, ASSESSMENTS_2SEMESTR.ASSESSMENT, SUBJECTS_2SEMESTR.TITLE from ASSESSMENTS_2SEMESTR LEFT JOIN STUDENTS on STUDENTS.id = ASSESSMENTS_2SEMESTR.ID_STUDENT LEFT JOIN SUBJECTS_2SEMESTR on SUBJECTS_2SEMESTR.id = ASSESSMENTS_2SEMESTR.ID_SUBJECT_2S")

        else:
            print("SEMESTER is INCORRECT")

        rows = sorted(cur.fetchall(), key=itemgetter(0))
        th = ['ID_ASSESS', 'Name', 'Assessment', 'Title Subject']
        td = []

        for row in rows:
            td.append(row[0])
            td.append(row[1])
            td.append(row[2])
            td.append(str(row[3]))

        columns = len(th)
        table = PrettyTable(th)
        td_data = td[:]

        while td_data:
            table.add_row(td_data[:columns])
            td_data = td_data[columns:]

        print('Подождите пару секунд...')
        print(f'Table from {id_semester}')
        time.sleep(2)
        print(table)



    except psycopg2.DatabaseError as e:

        print(f'Error {e}')
        sys.exit(1)

    except IOError as e:

        print(f'Error {e}')
        sys.exit(1)

    finally:

        if con:
            con.close()

def show_one_student(id_student, id_semester):
    try:
        con = psycopg2.connect(
          database="university_db",
          user="university",
          password="123",
          host="127.0.0.1",
          port="5432"
        )

        cur = con.cursor()
        if id_semester == ('1'):
            cur.execute("SELECT ASSESSMENTS_1SEMESTR.id, STUDENTS.NAME, ASSESSMENTS_1SEMESTR.ASSESSMENT, SUBJECTS_1SEMESTR.TITLE from ASSESSMENTS_1SEMESTR LEFT JOIN STUDENTS on STUDENTS.id = ASSESSMENTS_1SEMESTR.ID_STUDENT LEFT JOIN SUBJECTS_1SEMESTR on SUBJECTS_1SEMESTR.id = ASSESSMENTS_1SEMESTR.ID_SUBJECT_1S WHERE STUDENTS.id = {0}".format(id_student))


        elif id_semester == ('2'):
            cur.execute("SELECT ASSESSMENTS_2SEMESTR.id, STUDENTS.NAME, ASSESSMENTS_2SEMESTR.ASSESSMENT,  SUBJECTS_2SEMESTR.TITLE from ASSESSMENTS_2SEMESTR LEFT JOIN STUDENTS on STUDENTS.id = ASSESSMENTS_2SEMESTR.ID_STUDENT LEFT JOIN SUBJECTS_2SEMESTR on SUBJECTS_2SEMESTR.id = ASSESSMENTS_2SEMESTR.ID_SUBJECT_2S WHERE STUDENTS.id = {0}".format(id_student))

        else:
            print("SEMESTER is INCORRECT")


        rows = sorted(cur.fetchall(), key=itemgetter(0))
        th = ['ID_ASSESS', 'Name', 'Assessment', 'Title Subject']
        td = []

        for row in rows:
            td.append(row[0])
            td.append(row[1])
            td.append(row[2])
            td.append(str(row[3]))

        columns = len(th)
        table = PrettyTable(th)
        td_data = td[:]

        while td_data:
            table.add_row(td_data[:columns])
            td_data = td_data[columns:]

        print('Подождите пару секунд...')
        print(f'Table from {id_semester} SEMESTER ID student: {id_student}')
        time.sleep(2)
        print(table)


    except psycopg2.DatabaseError as e:

        print(f'Error {e}')
        sys.exit(1)

    except IOError as e:

        print(f'Error {e}')
        sys.exit(1)

    finally:

        if con:
            con.close()

def show_avg_assessments(id_semester):
    try:
        con = psycopg2.connect(
          database="university_db",
          user="university",
          password="123",
          host="127.0.0.1",
          port="5432"
        )

        cur = con.cursor()
        if id_semester == ("1"):
            cur.execute("SELECT STUDENTS.NAME, round(avg(ASSESSMENTS_1SEMESTR.ASSESSMENT),2) as avg_assessments from ASSESSMENTS_1SEMESTR LEFT JOIN STUDENTS on STUDENTS.id = ASSESSMENTS_1SEMESTR.ID_STUDENT LEFT JOIN SUBJECTS_1SEMESTR on SUBJECTS_1SEMESTR.id = ASSESSMENTS_1SEMESTR.ID_SUBJECT_1S GROUP BY STUDENTS.NAME ORDER BY avg_assessments DESC")

        elif id_semester == ("2"):
            cur.execute("SELECT STUDENTS.NAME, round(avg(ASSESSMENTS_2SEMESTR.ASSESSMENT),2) as avg_assessments from ASSESSMENTS_2SEMESTR LEFT JOIN STUDENTS on STUDENTS.id = ASSESSMENTS_2SEMESTR.ID_STUDENT LEFT JOIN SUBJECTS_2SEMESTR on SUBJECTS_2SEMESTR.id = ASSESSMENTS_2SEMESTR.ID_SUBJECT_2S GROUP BY STUDENTS.NAME ORDER BY avg_assessments DESC")

        else:
            print("SEMESTER is INCORRECT")

        rows = sorted(cur.fetchall(), key=itemgetter(1))
        th = ['Name', 'Average score']
        td = []

        for row in rows:
            td.append(row[0])
            td.append(row[1])


        columns = len(th)
        table = PrettyTable(th)
        td_data = td[:]

        while td_data:
            table.add_row(td_data[:columns])
            td_data = td_data[columns:]

        print('Подождите пару секунд...')
        print(f'Table from {id_semester} semester')
        time.sleep(2)
        print(table)

    except psycopg2.DatabaseError as e:

        print(f'Error {e}')
        sys.exit(1)

    except IOError as e:

        print(f'Error {e}')
        sys.exit(1)

    finally:

        if con:
            con.close()
