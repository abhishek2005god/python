#Write a python function which accepts a list and returns a new list with unique elements of the first list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def unique_list(lst):
    new_lst = []
    #It Iterates through the list and adds unique elements to the new list
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst

result = unique_list(lst)
print(result)

