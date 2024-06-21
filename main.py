from Tasks.Task1 import smallest_number
from Tasks.Task2 import biggest_number
from Tasks.Task3 import array_sum
from Tasks.Task4 import array_avg
from Tasks.Task5 import array_median
from Tasks.Task6 import minisort
# Main Py file, tasks should not be performed here

array = [4, 23, 8, 13, 7, 9, 42, 11, 6, 80, 3]

print("Smallest Number: ", smallest_number(array))
print("Biggest Number: ", biggest_number(array))
print("Array Sum: ", array_sum(array))
print("Array Average: ", array_avg(array))
print("Array Median: ", array_median(array))
print("Array Sort: ", minisort(array))


