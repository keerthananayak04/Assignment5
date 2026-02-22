#task2 of Assignment5
numlist=[]
for i in range(1,11):
    numlist.append(i)
print(f"Original list:{numlist}")
extracted_list=numlist[0:5]
print(f"Extracted first five elements:{extracted_list}")
extracted_list.reverse()
print("Reversed extracted elements:",extracted_list)

