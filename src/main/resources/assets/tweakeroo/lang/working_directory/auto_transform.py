import re

lines = open('src\main\\resources\\assets\\tweakeroo\lang\working_directory\Configs.java').read()

pattern = r'public static final [^(]*\(([^)\n]*)\)'

matches = re.findall(pattern, lines)

for match in matches:
    literal = match.split(",")
    print(literal[0], literal[-1])
