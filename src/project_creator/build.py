"""Create the file and folder structure outlined by this project."""

from pathlib import Path
import re
import os

_help_dict = {
    "name": 'This will be the name of the main folder in your projects "src"-directory.\n'
    'Only alphanumeric characters and "_" are permitted. All other characters are escaped with "_".\n\n'
    'Example: Look at the structure of "Project Creator". There is a folder called "src" and inside\n'
    'is a folder called "project_creator". This is what the name refers to.',
    "directory": "",
}


def get_help(topic: str) -> None:
    """Returns a description for the given topic."""
    print(f"\nHELP ({topic.upper()}):")
    print("=" * len(f"HELP ({topic.upper()}):"), "\n")
    print(_help_dict[topic], "\n")


def main():
    print(
        "+-------------------------------+\n"
        "|Welcome to the Project Creator.|\n"
        "+-------------------------------+\n"
        "\n"
        'To get help about the current step, type "?help".\n'
        'To quit without creating a project, type "?quit".'
    )

    print(rf"[^\w_. -{os.sep}]")

    while True:
        # continuously ask for name until a valid name is provided
        proj_name = input("Enter your projects name: ")

        match proj_name.lower():
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
        proj_dir = Path(input("Enter your projects home directory: "))
        str_proj_dir = str(proj_dir)

        match str_proj_dir.lower():
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
                proj_dir = Path(re.sub(pattern, "_", str_proj_dir))
                break

    proj_dir.mkdir(exist_ok=True)


if __name__ == "__main__":
    main()
