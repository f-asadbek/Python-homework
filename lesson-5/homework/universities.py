universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(universities):
    numberOfStudents = [i[1] for i in universities]
    tuitionFees = [i[2] for i in universities]
    return numberOfStudents, tuitionFees

def mean(value):
    return sum(value) / len(value)

def median(value):
        medianValue = sorted(value)
        length = len(medianValue)
        if length % 2 == 0:
             return (medianValue[length // 2 - 1] + medianValue[length // 2]) / 2
        else:
             return medianValue[length // 2]
        
numberOfStudents, tuitionFees = enrollment_stats(universities)

print(f"Total students: {sum(numberOfStudents)}")
print(f"Total tuition: ${sum(tuitionFees)}")
print(f"Student mean: {mean(numberOfStudents):.2f}")
print(f"Student median: {median(numberOfStudents)}")
print(f"Tuition mean: ${mean(tuitionFees):.2f}")
print(f"Tuition median: ${median(tuitionFees)}")