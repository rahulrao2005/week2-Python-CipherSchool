## function
# print how many list exists in list
# [1,2,3 , [1,2],[3,4]] , input
# 2 ---answer
def sublist_counter(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count 
mixed = [1,2,3, [1,2]]         
print(sublist_counter())    