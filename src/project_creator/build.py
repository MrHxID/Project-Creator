"""Create the file and folder structure outlined by this project."""

import os
import re
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
}


def get_help(topic: str) -> None:
    """Returns a description for the given topic."""
    help_topic = f"HELP ({topic.upper()}):"
    print("\n" + help_topic)
    print("=" * len(help_topic) + "\n")
    print(_help_dict[topic], "\n")


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
        parent_dir = Path(input("Enter your projects home directory: "))
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

    proj_folder = " ".join(word.capitalize() for word in proj_name.split("_"))
    print(proj_folder)

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
    
    


if __name__ == "__main__":
    main()
