import re

lines = open('src\main\\resources\\assets\\tweakeroo\lang\working_directory\Configs.java').read()
pattern = r'public static final [^(]*\(([^)\n]*)\)'
matches = re.findall(pattern, lines)

names = []

for match in matches:
    literal = match.split(", ")
    # print(literal[0], literal[-1])
    names.append((literal[0], literal[-1]))

for name in names:
    print(f"{name[0]}: \"测试\",")

