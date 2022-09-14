#Insertion Sort

def insertion_sort(lst):
    for i in range(1, len(lst)):
        a = lst[i]
        b = i - 1

        while b>=0 and a<lst[b]:
            lst[b+1] = lst[b]
            b -= 1

        lst[b+1] = a

lst = [7, 10, 77, 3, 46, 0, 9, 1]
insertion_sort(lst)
print(lst)