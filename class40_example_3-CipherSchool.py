# practice for loop 
# ask user name and count each character 
# "Sumit Goswami"
# S : 1
# u : 1
# m : 2
# i : 2
# t : 1
#   : 1
# G : 1
# o : 1
# w : 1
# a : 2
name = input("")
temp = ""
for i in range(0,len(name)):
    if name[i] not in temp:
        print(name[i] ,"=",name.count(name[i]))
        temp += name[i]


