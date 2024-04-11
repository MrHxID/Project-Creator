This is a helper program that creates the file structure needed to make a
python package installable.

This will be the basic file structure:

[home dir]
          \
           - src
           |    \
           |     - [proj name]
           |                  \
           |                   - __init__.py

To use testing or to import it in other projects go to your shell
and cd into your projects home directory. Then run the following command:
"pip install -e ."
Afterwards you can use everything in your "[home dir]/src/[proj name]"
directory as if it was a regular package.

[Naming Convention]
To create the projects structure the following naming convention is used:
- The home directory is the location of everything belonging to your project.
    Its name will have the form "Hello World", where words are separated
    by spaces and each word is capitalized. This folder can be renamed afterwards
    without any additional constraints

- The source directory of your files is located in your "[home dir]/src" folder.
    Its name will have the form "hello_world" with all lower case letters and
    underscores separating words to conform to the package naming convention of PEP 8.
    If you want to rename this folder later, make sure to also rename the value of
    "name" in the "setup.cfg" and all the places where this package is imported
    (e.g. in your tests).

