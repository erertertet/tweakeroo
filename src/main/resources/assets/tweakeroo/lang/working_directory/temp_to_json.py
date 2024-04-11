
temp_file = open("src\main\\resources\\assets\\tweakeroo\lang\working_directory\\temp_working.txt", "r", encoding="utf-8")

for line in temp_file.readlines():
    literals = line[:-1].split("\t")

    print(f"\"{literals[0]}\":\"{literals[1]}\",")
    print(f"\"config.comment.{literals[0].lower()}\":\"{literals[2]}\",")