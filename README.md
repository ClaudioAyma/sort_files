# SORT FILES

This python script receive as parameter the `PATH` variable and sort all files inside of this location, making new directories named with its respective extension and put all of them files inside of its respective directory.
### Requirements
To run this script it is not necesary install external package because it works with modules comes under Python's standard utility module.
- os
- shutil

### Usage
To execute this script only replace the `PATH` variable with the path of your directorie's location where you want to order all your files.

```py
PATH = r"C:/FOLDER/PATH/HERE"
```
save it and run the script.
```
python sort_files.py
```
Now all your files inside the path directory that you passed will be sort.

### Warning! ⚠️
All the files inside the `PATH` variable  you set will be moved to another directory, Becareful to set `PATH` variable a directory that you do not to want to make changes.