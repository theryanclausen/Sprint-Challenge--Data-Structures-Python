import time

start_time = time.time()

f = open('./names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('./names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

names_1.sort()
names_2.sort()

duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
pointer_1 = 0
pointer_2 = 0
counter = 0
while pointer_1 < len(names_1) - 1 and pointer_2 < len(names_2) - 1:
    if names_1[pointer_1] > names_2[pointer_2]:
        pointer_2 += 1
    if names_1[pointer_1] < names_2[pointer_2]:
        pointer_1 += 1
    if names_1[pointer_1] == names_2[pointer_2]:
        duplicates.append(names_1[pointer_1])
        pointer_1 += 1
        pointer_2 += 1

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

