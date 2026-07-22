# # buble sort
# mylist = [64, 34, 25, 12, 22, 11, 90, 5]

# n = len(mylist)
# for i in range(n-1):
#   for j in range(n-i-1):
#     if mylist[j] > mylist[j+1]:
#       mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

# print(mylist) 

# # selection sort

# list = [64, 34, 25, 5, 22, 11, 90, 12]

# n = len(list)
# for i in range(n-1):
#   min_index = i
#   for j in range(i+1, n):
#      if mylist[j] < list[min_index]:
#        min_index = j
#   min_value = list.pop(min_index)
#   list.insert(i, min_value)

# print(list)


# insertion sort
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
for i in range(1,n):
  insert_index = i
  current_value = mylist[i]
  for j in range(i-1, -1, -1):
     if mylist[j] > current_value:
       mylist[j+1] = mylist[j]
       insert_index = j
     else:
       break
  mylist[insert_index] = current_value

print(mylist)