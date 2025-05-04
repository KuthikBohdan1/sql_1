import sqlite3

con = sqlite3.connect("sql_1/uni.db")
cursor = con.cursor()



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
    print("2.список курсів")
    print("3.додати студента")

    quesion = input("виберіть дію: ")


    if quesion == "0":
        break
    elif quesion == '1':
        cursor.execute(
            """
            SELECT * FROM students
            """
        )
        students = cursor.fetchall()
        print(students)


    elif quesion == '2':
        cursor.execute(
            """
            SELECT * FROM courses
            """
        )
        courses = cursor.fetchall()
        for course in courses:

            print(course)

    elif quesion == '3':
        name = input("введіть імя  студента: ")
        age = int(input("введіть вік студента: "))

        major = input("введіть спеціальність студента: ")
        school = input("введіть заклад студента: ")

        cursor.execute(
            '''
            INSERT INTO students(name, age, major, school)
            VALUES(?, ?, ?, ?)
                ''', (name, int(age), major, school)
                )
        print("успішно додано нового студента")
        con.commit()


con.commit()
con.close()