
# sort the lines so that the program works.

student['name'] = 'Jan Kowalski'

print(student)

print("%s, born %i studies %s."%( \
    student['name'],student['year'],student['curriculum']))

student = {}

student['year'] += 1985

student["curriculum"] = "biology"

assert len(student) == 3

student.setdefault('year', 0)

