import sqlite3

con = sqlite3.connect("uni.db")
cursor =  con.cursor()



cursor.execute(

    """
    SELECT * FROM students


    """

)

students = cursor.fetchall()
print(students)


while True:
    print("0.вихів з програми")
    print("1.список студентів")

    quesion = input("db,: ")


    if quesion == "0":
        break
    elif quesion == '1':
        cursor.execute(
            """
            SELECT FROM students
            """
        )
        students = cursor.fetchall()
        print(students)


    elif quesion == '2':
        cursor.execute(
            """
            SELECT FROM students
            """
        )
        students = cursor.fetchall()
        for course in courses:

            print(course)
    elif quesion == '3':
        name = input("імя ")
        age = input("вік")
        major = input("спц")

        cursor.execute(
            '''
                INSERT INTO students(name, age, major)
                VALUES(?, ?, ?),
                    ''', (name, age, major)
                )
        print("")
        con.commit


con.commit()
con.close()