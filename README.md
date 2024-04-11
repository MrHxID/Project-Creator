This is a helper program that creates the file structure needed to make a
python package installable.

[File Structure]

This will be the basic file structure:

```
[home dir]
|
+-- src
|   |
|   +-- [proj name]
|       |
|       +-- __init__.py
|       +-- [your code]
|       +-- ...
|
+-- tests
|   |
|   +-- __init__.py
|   +-- [your tests]
|   +-- ...
|
+-- LICENSE
+-- pyproject.toml
+-- setup.cfg
+-- setup.py
```

The LICENSE will default to MIT but can be changed at will. Just make sure
to change the value of "license" in your "setup.cfg".

To use testing or to import it in other projects go to your shell
and cd into your projects home directory. Then run the following command:
"pip install -e ."
Afterwards you can use everything in your "[home dir]/src/[proj name]"
directory as if it was a regular package.

[Naming Convention]

To create the projects structure the following naming convention is used:
- The [home dir] folder is the location of everything belonging to your project.
    Its name will have the form "Hello World", where words are separated
    by spaces and each word is capitalized. This folder can be renamed afterwards
    without any additional constraints.

- The [proj name] folder of your files is located in your "[home dir]/src" folder.
    Its name will have the form "hello_world" with all lower case letters and
    underscores separating words to conform to the package naming convention of PEP 8.
    If you want to rename this folder later, make sure to also rename the value of
    "name" in the "setup.cfg" and all the places where this package is imported
    (e.g. in your tests). Also make sure that your new name is a valid package name.

You can input the projects name using either the convention for [home dir] (spaces, capitalized)
or for [proj name] (underscores, lower case).

Here is an example structure:

```
Test Project
|
+-- src
|   |
|   +-- test_project
|       |
|       +-- __init__.py
|       +-- ...
|
+-- tests
|   |
|   +-- __init__.py
|   +-- ...
|
...
```

