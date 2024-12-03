
print("""El programa llegeix com a entrada les
qualificacions d'un estudiant en els treballs i tres exàmens i les utilitza per calcular la nota final
del curs de l’estudiant.""")


def homework_score():
    try:
        homework_1 = float(input("Enter H1 grade:"))
        if homework_1 > 15:
            print("homework 1 grade cannot be higher than 15 ")
            homework_1 = float(input("Enter H1 grade:"))
        homework_2 = float(input("Enter H2 grade:"))
        if homework_2 > 20:
            print("Homework 2 grade cannot be higher than 20")
            homework_2 = float(input("Enter H2 grade:"))

        homework_3 = float(input("Enter H3 grade:"))
        if homework_3 > 25:
            print("Homework 3 grade cannot be higher than 25")
            homework_3 = float(input("Enter H3 grade:"))
        peso_homework = float(input("Enter homework weighing:"))


        homework = (((homework_1 + homework_2 + homework_3)/60)*peso_homework)
    except ZeroDivisionError as ze:
        print(ze)
    return homework

final_homework = homework_score()



def grade(final_homework):
    try:
        
        exam_1 = float(input("Enter grade of exam 1(0~100): "))
        if exam_1 > 100:
            print("Maximo 100")
            exam_1 = float(input("Enter grade of exam 1(0~100): "))

        peso_e1 = float(input("Enter weighing of exam 1: "))
        exam_1_final = (((exam_1)/100)*peso_e1)
        print(f"Nota examen 1 : {exam_1_final}")

        exam_2 = float(input("Enter grade of exam 2: "))
        if exam_2 > 100:
            print("Maximo 100")
            exam_2 = float(input("Enter grade of exam 2(0~100): "))
        peso_e2 = float(input("Enter weighing of exam 2: "))
        exam_2_final = (((exam_2)/100)*peso_e2)
        print(f"Nota examen 2:{exam_2_final}")

        final_exam = float(input(f"Enter grade of final exam: "))
        if final_exam > 100:
            print("Maximo 100")
            final_exam = float(input("Enter grade of exam 1(0~100): "))
        peso_final = float(input(f"Enter weighing final': ") )
        final_final = (((final_exam)/100)*peso_final)
        print(f"Nota Examen Final: {final_final}")

        final_grade = exam_1_final + exam_2_final + final_final + final_homework

        
    except ZeroDivisionError as ze:
        print(ze)
    return final_grade

result = grade(final_homework)


def nota_letra (result):
    if result > 90:
        return "A, Molt bé vaya maquina"
    elif 80 < result < 89.99:
        return "B, Bé pero se puede mejorar"
    elif 70 < result < 79.99:
        return "C, Pelado"
    elif 60 < result < 69.99:
        return "D, Casi pero no, te falta calle"
    elif result < 60:
        return "F, Suspendido que pringao"

letra = nota_letra(result)

print(f"Tu nota final es : {round(result,2)}% equivalente a la letra : {letra}")



