# Quick Sort

def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp
        
        print(elements)

def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)
        
        print(elements)

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start+=1

        while elements[end] > pivot:
            end-=1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)
    print(elements)
    
    return end

elements = [31, 18, 14, 53, 54, 98, 93, 92, 74, 69]
quick_sort(elements, 0, len(elements)-1)
print(elements)

# Reference: https://youtu.be/5iSZ7mh_RAk