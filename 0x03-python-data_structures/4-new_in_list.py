  
#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copyList = []
    for i in my_list:
        copyList = my_list[:]
    if idx < 0 or idx > len(my_list) - 1:
            return copyList
    for i in copyList:
        copyList[idx] = element
        return copyList
