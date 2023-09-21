# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.
numbers = [78, 55, 36, 90, 2]
def sort_list_imperative(numbers):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(numbers) - 1):
            if numbers[i] < numbers[i + 1]:
                # Меняем элементы
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True
    return numbers
print(sort_list_imperative(numbers))

# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле
numbers = [78, 55, 36, 90, 2]
def sort_list_declarative(numbers):
    numbers.sort(reverse=True)
    return numbers
print(sort_list_declarative(numbers))
