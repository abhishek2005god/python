#Write a python function to print all even numbers from the given list
def even_numbers(li):
    for i in li:
        if i%2 ==0:
            print(i,end =" ")

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers(lst)