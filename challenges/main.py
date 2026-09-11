def group_by_grade(students):
    # TODO: determine each student's letter grade and group their names by grade band
    grade_band = {}

    for student in students:

        name = student['name']
        score = student['score']

        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'

        # grade_band[grade] = grade_band.get(grade, []) + [name]
        if grade not in grade_band:
            grade_band[grade] = [name]
        else:
            grade_band[grade].append(name)
    
    return grade_band

print(group_by_grade([{'name': 'Ada', 'score': 95}, {'name': 'Bola', 'score': 82}]))
print(group_by_grade([{'name': 'Chidi', 'score': 55}]))
print(group_by_grade([]))
print(group_by_grade([{'name': 'Ada', 'score': 92}, {'name': 'Bola', 'score': 95}]))