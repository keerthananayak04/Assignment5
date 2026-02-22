#task1 of Assignment5
Student={'Alice':89,'john':79,'Amar':45,'Ram':90,'Afzal':66}
name=input("Enter the Student's name:")
if name in Student:
    print(f"{name}'s marks:{Student[name]}")
else:
    print('Student not found.')