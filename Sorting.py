#list = [4,2,6,5,1,3]
#Bubble sort
for i in range(len(list)-1,0,-1):
    for j in range(i):
        if list[j]>list[j+1]:
            temp = list[j+1]
            list[j+1] = list[j]
            list[j] = temp
        print(list)
    print('\n')


#Selection Sort
list1 = [4,2,6,5,1,3]
for i in range(len(list1)-1):
    min_index = i
    for j in range(i+1,len(list1)):
        if list1[j]<list1[min_index]:
            min_index = j
    temp = list1[i]
    list1[i]= list1[min_index]
    list1[min_index] = temp
    print(list1)


#Insertion sort
for i in range(1,len(list)):
    for j in range(len(list)):
        if list[i]<list[j]:
            temp = list[j]
            list[j]= list[i]
            list[i]= temp
    print(list)

#Merge sort
'''
def merge(list1, list2):
    list_merge = []

    while list1:
        list1.index()

        if list2[i] < list1[i]:
            list_merge.append(list2[i])
        else:
            list_merge.append(list1[i])
    print(list_merge)
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] < list2[j]:
                print(list1[i], list2[j])
                list_merge.append(list1[i])
                break
            else:
                list_merge.append(list2[j])
        print(list_merge)

list1 = [0,1,3,7,8]
list2 = [2,4,5,6]
list_merge = []
merge(list1,list2)'''











