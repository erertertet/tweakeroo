import re
from typing import List, Tuple

temp_file = open("src\main\\resources\\assets\\tweakeroo\lang\working_directory\\temp_working.txt", "w", encoding="utf-8")

def name_desc_identify(file_path: str) -> List[Tuple[str, str]]:
    lines = open(file_path, "r").read()
    matches = re.findall(r"[^(]*\(([\"[a-zA-Z0-9]*\",[^\)]*]*)", lines)

    names = []

    for match in matches:
        literal = match.split(",")
        names.append((literal[0].strip(), literal[-1].strip()))

    for name in names:
        temp_file.write(f'{name[0][1:-1]}\t{name[0][1:-1]}\t{name[1][1:-1]}\n')
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
