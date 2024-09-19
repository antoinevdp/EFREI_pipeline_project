"""
etudiant table:

id,int,NO,PRI,,auto_increment
first_name,varchar(100),YES,"",,""
last_name,varchar(100),YES,"",,""
classroom_number,int,YES,"",,""
phone_number,varchar(100),YES,UNI,,""
email,varchar(100),YES,UNI,,""
graduation_date,year,YES,"",,""


enseignant table:

id,int,NO,PRI,,auto_increment
first_name,varchar(100),YES,"",,""
last_name,varchar(100),YES,"",,""
classroom_number,int,YES,"",,""
phone_number,varchar(100),YES,UNI,,""
email,varchar(100),YES,UNI,,""
department,varchar(100),YES,"",,""
"""
import mysql.connector
cnx = mysql.connector.connect(user='root', password='password',host='127.0.0.1',database='Ecole')

cursor = cnx.cursor()
query = ("SELECT etudiant.first_name, etudiant.last_name, enseignant.first_name, enseignant.last_name FROM etudiant "
         "LEFT JOIN enseignant ON etudiant.classroom_number = enseignant.classroom_number")
cursor.execute(query)

for (first_name, last_name, t_first_name, t_last_name) in cursor:
  print("Etudiant: {} {}, Enseignant: {} {} ".format(
    first_name, last_name, t_first_name,t_last_name))

query = ("SELECT enseignant.last_name, count(etudiant.id) FROM enseignant "
         "LEFT JOIN etudiant ON enseignant.classroom_number = etudiant.classroom_number "
         "GROUP BY enseignant.id")
cursor.execute(query)
dico = dict(cursor.fetchall())

for i in dico:
    print(f"Enseignant: {i}, Nombre d'étudiants: {dico[i]}")
cursor.close()

cnx.close()