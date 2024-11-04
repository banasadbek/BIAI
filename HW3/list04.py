import statistics

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(list):
    total_students = 0 
    total_tuition = 0
    students = []
    tuition = []
    for index in list:
        total_students+=index[1]
        total_tuition+=index[2]
        students.append(index[1])
        tuition.append(index[2])
    print(f'Total students: {total_students}')
    print(f'Total tuition: ${total_tuition}')
    student_mean = round(statistics.mean(students),2)
    student_median = round(statistics.median(students),2)
    tuition_mean = round(statistics.mean(tuition),2)
    tuition_median = round(statistics.median(tuition),2)
    print(f'\nStudent mean: {student_mean}')
    print(f'Student median: {student_median}')
    print(f'\nTuition mean: ${tuition_mean}')
    print(f'Tuition median: ${tuition_median}')

enrollment_stats(universities)