#Bubble Sort

lst = [1, 4, 2, 5, 3, 7 ,10, 9, 8, 6]

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst)-i-1):
            if lst[j]>lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
bubble_sort(lst)
print(lst)