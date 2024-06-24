import random


def bubble_sort(list_to_sort):
    for i in range(0,len(list_to_sort)-1):
        for j in range(0, len(list_to_sort)-1-i):
            if list_to_sort[j] > list_to_sort[j+1]:
                list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]
    return list_to_sort


def binary_search(elem, lst, start_idx, stop_idx):
    if start_idx == stop_idx and lst[start_idx] != elem:
        return -1
    else:
        center_elem = lst[int((stop_idx+start_idx)/2)]
        center_elem_index = int((stop_idx+start_idx)/2)
        if center_elem == elem:
            return center_elem_index
        elif center_elem > elem:
            return binary_search(elem, lst, 0, center_elem_index)
        else:
            return binary_search(elem, lst, center_elem_index, len(lst))


unsorted_list = random.sample(range(100), 10)
print(unsorted_list)

sorted_list = bubble_sort(unsorted_list)
print(sorted_list)

index = binary_search(sorted_list[8], sorted_list, 0, len(sorted_list))
print(index)

