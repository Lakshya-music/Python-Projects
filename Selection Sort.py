#Selection Sort

def selection_sort(lst):
    for i in range(len(lst)):
        min = i

        for j in range(i+1, len(lst)):
            if lst[j] < lst[min]:
                min = j

        lst[i], lst[min] = lst[min], lst[i]

lst = [5, 4, 0, 3, 2, 1]
selection_sort(lst)
print(lst)