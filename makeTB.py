import psycopg2

con = psycopg2.connect(
  database="check_database",
  user="admin",
  password="123",
  host="127.0.0.1",
  port="5432"
)

print("Database opened successfully")
cur = con.cursor()

cur.execute ('''CREATE TABLE DOCTORS (
    id SERIAL PRIMARY KEY NOT NULL,
    NAME_DOCTOR TEXT NOT NULL);''')

cur.execute ('''CREATE TABLE HEAL (
    id SERIAL PRIMARY KEY NOT NULL,
    TIITLE_HEAL TEXT NOT NULL,
    TIMES_INPUT_PER_DAY INT NOT NULL); ''')

cur.execute ('''CREATE TABLE TYPE_PLAGUE (
    id SERIAL PRIMARY KEY NOT NULL,
    TITLE_PLAGUE TEXT NOT NULL,
    ID_HEAL REFERENCES HEAL(ID);''')


cur.execute ('''CREATE TABLE PATIENTS (
    id SERIAL PRIMARY KEY NOT NULL,
    NAME_PATIENT TEXT NOT NULL,
    id_doctor INT REFERENCES DOCTORS(ID),
    id_plague INT REFERENCES PLAGUE(ID)
) ''')



cur.execute('''CREATE TABLE STUDENTS
     (id SERIAL PRIMARY KEY NOT NULL,
     NAME TEXT NOT NULL);'''
     )

cur.execute('''CREATE TABLE SUBJECTS_1SEMESTR
    (id SERIAL PRIMARY KEY NOT NULL,
    TITLE TEXT NOT NULL);'''
    )

cur.execute('''CREATE TABLE SUBJECTS_2SEMESTR
    (id SERIAL PRIMARY KEY NOT NULL,
    TITLE TEXT NOT NULL);'''
    )

cur.execute('''CREATE TABLE TEACHERS_1SEMESTR
     (id SERIAL PRIMARY KEY NOT NULL,
     NAME TEXT NOT NULL,
     ID_SUBJECT_1S INT REFERENCES SUBJECTS_1SEMESTR(ID));'''
     )

cur.execute('''CREATE TABLE TEACHERS_2SEMESTR
     (id SERIAL PRIMARY KEY NOT NULL,
     NAME TEXT NOT NULL,
     ID_SUBJECT_2S INT REFERENCES SUBJECTS_2SEMESTR(ID));'''
     )

cur.execute('''CREATE TABLE ASSESSMENTS_1SEMESTR
    (id SERIAL PRIMARY KEY NOT NULL,
    ASSESSMENT INT NOT NULL,
    ID_STUDENT INT REFERENCES STUDENTS(ID),
    ID_SUBJECT_1S INT REFERENCES SUBJECTS_1SEMESTR(ID));'''
    )

cur.execute('''CREATE TABLE ASSESSMENTS_2SEMESTR
    (id SERIAL PRIMARY KEY NOT NULL,
    ASSESSMENT INT NOT NULL,
    ID_STUDENT INT REFERENCES STUDENTS(ID),
    ID_SUBJECT_2S INT REFERENCES SUBJECTS_2SEMESTR(ID));'''
    )

print("Table created successfully")
input()
con.commit()
con.close()
