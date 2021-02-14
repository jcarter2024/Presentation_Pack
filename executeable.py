#Script to retrieve relevant files and paths, supply to cx_Freeze to compile into executeable
import os
import cx_Freeze
files_list = []


dir_path = os.path.dirname(os.path.realpath(__file__))+str('/')
print(dir_path)
for root, directories, filenames in os.walk(str(dir_path)):
    for file in filenames: 
        path=os.path.join(root, file)
        if path.find('/.') == -1 and path.find('__pycache__') == -1: #finds the paths where /. doesn't exist 
            files_list.append(path)

executables = [cx_Freeze.Executable(dir_path+"scripts/main.py")]

cx_Freeze.setup(
    name="try1",
    description='A game and a presentation',
    author='J. Carter',
    options={"build_exe": {"packages":["pygame", "sys", "itertools"],
                            "include_files":files_list}},
    executables = executables

    )