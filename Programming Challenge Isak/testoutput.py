
with open("output.txt", "r") as f:
    lines = f.readlines()

with open(".txt", "r") as f:
    lines1 = f.readlines()

for i in range(len(lines)):
    if lines[i] != lines1[i]:
        print(i, lines[i], lines1[i])