import grade_calculate



def main():
    
    try:
   
        homework_score()
        grade(final_homework)
        nota_letra(result)
    except FileNotFoundError as fe:
        print(fe)
