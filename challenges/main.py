def get_student_grade(students, name):
    lookup = {}
    # TODO: loop through `students` and populate `lookup` with name -> grade
    # TODO: return the grade for `name` from `lookup`, or "Not found" if missing
    for student in students:
        student_name = student['name']
        grade = student['grade']
        
        lookup[student_name] = lookup.get(student_name, grade)
    
        if student_name == name:
            return lookup[name]

    return 'Not found'

print(get_student_grade([{'name': 'Ada', 'grade': 'A'}, {'name': 'Bola', 'grade': 'B'}], 'Ada'))
print(get_student_grade([{'name': 'Ada', 'grade': 'A'}], 'Chidi'))
print(get_student_grade([], 'Ada'))