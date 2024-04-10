import re

lines = open('src\main\java\\fi\dy\masa\\tweakeroo\config\Hotkeys.java', 'r').read()
pattern = r'public static final [^(]*\(([^)\n]*)\)'
matches = re.findall(pattern, lines)

names = []

for match in matches:
    literal = match.split(", ")
    # print(literal[0], literal[-1])
    names.append((literal[0], literal[-1]))

for name in names:
    ...
    print(f"{name[0]}: \"测试\",")

quit()

lines = open('src\main\java\\fi\dy\masa\\tweakeroo\config\FeatureToggle.java', 'r').read()
pattern = r'[^(]*\(([\"[a-zA-Z]*\",[^\)]*]*)'
matches = re.findall(pattern, lines)

names = []

for match in matches:
    literal = match.split(", ")
    # print(literal[0], literal[-1])
    names.append((literal[0], literal[-1]))

for name in names:
    ...
    # print(f"{name[0]}: \"测试\",")

lines = open('src\main\java\\fi\dy\masa\\tweakeroo\config\FeatureToggle.java', 'r').read()
pattern = r'[^(]*\(([\"[a-zA-Z]*\",[^\)]*]*)'
matches = re.findall(pattern, lines)

names = []

for match in matches:
    literal = match.split(", ")
    # print(literal[0], literal[-1])
    names.append((literal[0], literal[-1]))

for name in names:
    print(f"{name[0]}: \"测试\",")