import re
from typing import List, Tuple


def name_desc_identify(file_path: str) -> List[Tuple[str, str]]:
    lines = open(file_path, "r").read()
    matches = re.findall(r"[^(]*\(([\"[a-zA-Z0-9]*\",[^\)]*]*)", lines)

    names = []

    for match in matches:
        literal = match.split(",")
        names.append((literal[0].strip(), literal[-1].strip()))

    for name in names:
        print(f'{name[0]}: "测试",')
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
