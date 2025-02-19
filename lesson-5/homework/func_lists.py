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
        students = [university[1] for university in universities]
        tuitions = [university[2] for university in universities]
        return students, tuitions


def mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def median(numbers):
    numbers = list(numbers)
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    if length == 0:
        return 0
    mid = length // 2
    if length % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]


students, tuitions = enrollment_stats(universities)
total_students = sum(students)
total_tuition = sum(tuitions)
mean_students = mean(students)
median_students = median(students)
mean_tuition = mean(tuitions)
median_tuition = median(tuitions)
print("*" * 30)
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}")
print("")
print(f"Student mean: {mean_students:,.2f}")
print(f"Student median: {median_students:,}")
print("")
print(f"Tuition mean: $ {mean_tuition:,.2f}")
print(f"Tuition median: $ {median_tuition:,}")
print("*" * 30)


