import csv
name_list=[]
score_list=[]
grade_list=[]

def grades(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    try:
        with open("grades.csv", "r") as file:
            content = csv.reader(file)
            next(content)
            for row in content:
                name_list.append(row[0])        ### creating 2 lists separiting name and score for easy sorting
                score_list.append(int(row[1]))
    except FileNotFoundError:
        print("No such file found.")
    ### finding the grade
    for score in score_list:
        grade_list.append(grades(score))
    
    ### printing names and their grades
    for i in range(len(name_list)):
        print("Name :", name_list[i], ", Grades:", grade_list[i])

    ### summary
    grade_counts = {
        'A': grade_list.count('A'),
        'B': grade_list.count('B'),
        'C': grade_list.count('C'),
        'D': grade_list.count('D'),
        'F': grade_list.count('F')
    }
    
    print("Grade summary")
    for grade_val,count in grade_counts.items():
        print(f"Grades: {grade_val} ,  Count: {count}")
    ### for average

    average=sum(score_list)/len(score_list)
    print(f"Average Score of the class is {average:.2f}")

    with open("grades_output.csv","w",newline='') as f:
        writing=csv.writer(f)
        writing.writerow(["Name","Score","Grade"])
        for i in range(len(name_list)):
            writing.writerow([name_list[i],score_list[i],grade_list[i]])


if __name__== "__main__":
    main()