import random
import os

num_list = []

print("Generating Dummy Data")
for i in range(10):
    num_list.append(random.random())
print("> Done.")

# print("\nSorting Numbers")
# num_list.sort()
# print("> Done.")

# file writer
print("\nWriting Numbers to File.")
f = open("data.txt", "w")
f.write(str(num_list))
print("> Done. (" + os.path.realpath(f.name) + ")")
f.close()