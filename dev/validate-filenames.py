#!/usr/bin/env python3

import re
import sys
from pathlib import Path
from typing import Final


ROOT_DIR: Final = Path(__file__).parent.parent
NAME_RE: Final = re.compile(r"^[a-z-]+\.json5$")


def main():
    found_invalid = False
    for file in ROOT_DIR.glob("*.json*"):
        if not NAME_RE.match(file.name):
            if not found_invalid:
                found_invalid = True
                print("Disallowed preset filenames detected:")
            print(file.name)

    if found_invalid:
        sys.exit(1)


if __name__ == "__main__":
    main()
