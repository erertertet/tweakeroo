
temp_file = open("src\main\\resources\\assets\\tweakeroo\lang\working_directory\\temp_working.txt", "r", encoding="utf-8")

names = []

for i,line in enumerate(temp_file.readlines()):
    
    # literals = line[:-1].split("\t")
    # print(i, line)

    if i % 2 == 0:
        literals = []
    literals.extend(line[:-1].split("\t"))

    if i % 2 == 1:
        print(f"\"config.name.{literals[0].lower()}\":\"{literals[2]}\",")
        # if len(literals) == 3:
            # print(literals)
        # names.append(literals[2])

# print(sorted(names, key=len))