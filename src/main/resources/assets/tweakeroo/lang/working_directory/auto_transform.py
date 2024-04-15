import re
from typing import List, Tuple

temp_file = open("src\main\\resources\\assets\\tweakeroo\lang\working_directory\\temp_working_1.txt", "w", encoding="utf-8")

def parentheses_pairing(line: str) -> str | None:
    start = line.find("(")

    if start == -1:
        return None
    
    counter = 0
    ptr = start
    while ptr < len(line):
        if line[ptr] == "(":
            counter += 1
        elif line[ptr] == ")":
            counter -= 1
        
        if counter == 0:
            return line[start + 1 : ptr]
        
        ptr += 1
    
    return None


def name_desc_extract(line: str) -> Tuple[str, str]:

    ptr = 0
    start = None

    temp = []

    while ptr < len(line):
        if line[ptr] == "\"":
            if start != None:
                temp.append(line[start + 1:ptr])
                start = None
            else:
                start = ptr
        
        elif line[ptr] == "\\":
            ptr += 1
        
        ptr += 1
    
    if len(temp) >= 2:
        return (temp[0], temp[-1])
    return None
    



def name_desc_identify(file_path: str) -> List[Tuple[str, str]]:
    lines = open(file_path, "r").readlines()

    names = []

    for line in lines:
        res = parentheses_pairing(line)
        if res and res[0] == "\"":
            names.append(name_desc_extract(res))

    for name in names:
        if name:
            temp_file.write(f'{name[0]}\t{name[1]}\n\n')
        # temp_file.write(f'{name[0][1:-1]}\t测试\t测试文本\n')
    return names


name_desc_identify(
    "src\main\java\\fi\dy\masa\\tweakeroo\config\Configs.java",
)

name_desc_identify(
    "src\main\java\\fi\dy\masa\\tweakeroo\config\FeatureToggle.java",
)

name_desc_identify(
    "src\main\java\\fi\dy\masa\\tweakeroo\config\Hotkeys.java",
)

# Notice: there are two pair of exact same entries of freeCameraPlayerInputs/Movements
