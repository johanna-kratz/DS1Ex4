def assigment(new_list, position_new_list, old_list, position_old_list):
    new_list[position_new_list] = old_list[position_old_list]


def merge_sort(list_to_sort):
    # base case: list of length 1 are sorted
    if len(list_to_sort) == 1:  # this is shorter and better readable than having a long if statement for case >1
        return list_to_sort

    # split list into two smaller list and sort them
    mid = len(list_to_sort) // 2
    left_list = list_to_sort[:mid]
    right_list = list_to_sort[mid:]

    merge_sort(left_list)
    merge_sort(right_list)

    # initialize positions
    position_right = 0
    position_left = 0
    position_sort = 0 

    # merge the two lists back together into one list till one list is completely merged back
    while position_left < len(left_list) and position_right < len(right_list):
        if left_list[position_left] <= right_list[position_right]:
            assigment(new_list=list_to_sort, position_new_list= position_sort, old_list=left_list, position_old_list=position_left)
            position_left += 1
        else:
            assigment(new_list=list_to_sort, position_new_list= position_sort, old_list=right_list, position_old_list=position_right)
            position_right += 1
        position_sort += 1

    # then add the remaining list
    while position_left < len(left_list):
        list_to_sort[position_sort] = left_list[position_left]
        position_left += 1
        position_sort += 1

    while position_right < len(right_list):
        list_to_sort[position_sort] = right_list[position_right]
        position_right += 1
        position_sort += 1

import matplotlib.pyplot as plt

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
merge_sort(my_list)
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
