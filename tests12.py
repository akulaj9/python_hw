print("===============================")
print("Task #7")
print("===============================")

def is_help_teachers(num_task):
    lst = []
    for i in range(2, 9+1):
      for j in range(2, 9+1):
        n = "%s*%s" % (i,j)
        if n[::-1] in lst:
            continue
        lst.append(n)
    import random
    random.shuffle(lst)
    return lst[:num_task]



list_tasks = is_help_teachers(15)
print("Tasks for pupils:")
for i in range(len(list_tasks)):
    print("%s. %s" % (i+1, list_tasks[i]), end=" / ")