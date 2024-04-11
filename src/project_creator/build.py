"""Create the file and folder structure outlined by this project."""

import os
import re
import sys
from datetime import date
from functools import partial
from pathlib import Path

_help_dict = {
    "name": 'This will be the name of the main folder in your projects "src" directory.\n'
    'Only alphanumeric characters and "_" are permitted. All other characters are escaped with "_".\n\n'
    'Example: Look at the structure of "Project Creator". There is a folder called "src" and inside\n'
    'is a folder called "project_creator". This is what the name refers to.\n'
    'For a more detailed example refer to the section "[Naming Convention]" in "README.md"',
    "directory": "This will be the parent folder for your new project. Upon project initialization\n"
    "a new folder is created here using the naming convention for [home dir] and every file is put\n"
    "into there.\n"
    'For a more detailed example refer to the section "[Naming Convention]" in "README.md"',
    "author": "Your real name or an alias to identify you with. This will only be used for the\n"
    'license and the "setup.cfg" files.',
}

files = {
    "LICENSE": """License MIT

Copyright (c) {year} "{author}"

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in the
Software without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the
following conditions:

The above copyright notice and this permission notice shall be included in all copies
or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.""",
    "pyproject.toml": """[build-system]
requires = ["setuptools>=42.0", "wheel"]
build-backend = "setuptools.build_meta"
""",
    "README.md": "",
    "setup.cfg": """[metadata]
name = {proj_name}
description = 
author = {author}
license = MIT
license_file = LICENSE
version = 1.0.0
platforms = win32
classifiers = 
    Programming Language :: Python :: {python_ver}

[options]
packages = 
    {proj_name}
install_requires =

python_requires = >={python_ver}
package_dir = 
    =src
zip_safe = no""",
    "setup.py": """from setuptools import setup

if __name__ == "__main__":
    setup()
""",
    "main.py": """def main(): ...


if __name__ == "__main__":
    main()
""",
    "__init__.py": "",
}


def get_help(topic: str) -> None:
    """Returns a description for the given topic."""
    help_topic = f"HELP ({topic.upper()}):"
    print("\n" + help_topic)
    print("=" * len(help_topic) + "\n")
    print(_help_dict[topic], "\n")


def create_file(
    file_name: str, directory: Path, format_args: dict[str, str] | None = None
):
    """Create the file and fill it with basic content.

    Args:
    - file_name (str): name of the file including extention (e.g. ".py")
    - directory (Path): Path-like object describing the location to put the file
    - format_args (dict | None): format the file contents before writing, if `None`
        use empty dict

    Returns
    - None
    """

    default = {}
    if format_args is not None:
        default.update(format_args)

    with open(directory / file_name, "w+") as file:
        file.write(files[file_name].format(**default))


def main():
    print(
        "+-------------------------------+\n"
        "|Welcome to the Project Creator.|\n"
        "+-------------------------------+\n"
        "\n"
        'To get help about the current step, type "?help".\n'
        'To quit without creating a project, type "?quit".\n'
    )

    while True:
        # continuously ask for name until a valid name is provided
        proj_name = input("Enter your projects name: ").lower()

        match proj_name:
            case "?help":
                get_help("name")
                continue

            case "?quit":
                exit(0)

            case _:
                # Sanitize the project name just in case
                proj_name = re.sub(r"[^\w_]", "_", proj_name)
                break

    while True:
        # continuously ask for directory until a valid one is provided
        parent_dir = Path(input("Enter your projects parent directory: "))
        str_parent_dir = str(parent_dir)

        match str_parent_dir.lower():
            case "?help":
                get_help("directory")
                continue

            case "?quit":
                exit(0)

            case _:
                # Sanitize the project directory just in case
                # double backslash to prevent clash in regex
                sep = "\\\\" if os.sep == "\\" else os.sep
                pattern = rf"[^\w_. -{sep}]"
                parent_dir = Path(re.sub(pattern, "_", str_parent_dir))
                break

    while True:
        author = input("Enter your name or alias: ")

        match author:
            case "?help":
                get_help("author")
                continue

            case "?quit":
                exit(0)

            case "":
                author = os.getlogin()
                break

            case _:
                break

    proj_folder = " ".join(word.capitalize() for word in proj_name.split("_"))

    proj_dir = parent_dir / proj_folder

    try:
        proj_dir.mkdir()
    except FileExistsError:
        replace_existing = input(
            "The selected project already exists. Continuing may override important\n"
            "data. Do you want to continue anyway? (y/n): "
        )

        match replace_existing.lower():
            case "y" | "yes":
                pass

            case "n" | "no" | _:
                exit(1)

        del replace_existing

    # Start creating the files

    code_dir = proj_dir / "src" / proj_name
    code_dir.mkdir(exist_ok=True)
    tests_dir = proj_dir / "tests"
    tests_dir.mkdir(exist_ok=True)

    format_dict = {
        "proj_name": proj_name,
        "author": author,
        "year": date.today().year,
        "python_ver": "{}.{}".format(*sys.version_info[:2]),
    }

    create_formatted_file = partial(create_file, format_args=format_dict)

    create_formatted_file("LICENSE", proj_dir)
    create_formatted_file("pyproject.toml", proj_dir)
    create_formatted_file("README.md", proj_dir)
    create_formatted_file("setup.cfg", proj_dir)
    create_formatted_file("setup.py", proj_dir)

    create_formatted_file("__init__.py", code_dir)
    create_formatted_file("main.py", code_dir)

    create_formatted_file("__init__.py", tests_dir)


if __name__ == "__main__":
    main()
