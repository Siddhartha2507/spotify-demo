#build a simple script to manage tasks using dictionary
a = {"task1" : input("enter task1 name:"),
"task2" : input("enter task2 name:"),
"task3" : input("enter task3 name:")}

a["task2"] = input("update task2:")
del a["task3"]
print(a)


