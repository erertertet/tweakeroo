
temp_file = open("src\main\\resources\\assets\\tweakeroo\lang\working_directory\\temp_working_1.txt", "r", encoding="utf-8")

for i,line in enumerate(temp_file.readlines()):
    
    # literals = line[:-1].split("\t")
    # print(i, line)

    if i % 2 == 0:

        literals = line[:-1].split("\t")

        print(f"\"{literals[0]}\":\"{'testing string'}\",")
        print(f"\"config.name.{literals[0].lower()}\":\"{'testing name'}\",")
        print(f"\"config.comment.{literals[0].lower()}\":\"{'testing comment'}\",")