from easygui import diropenbox
from json import load, dumps
from os import listdir, getcwd, mkdir
from os.path import isfile, isdir, splitext, join
from shutil import copy

def import_json(filepath):
    """read JSON file (assuming UTF-8 encoding)"""
    json_file = open(filepath, "r", encoding="utf-8")
    data = load(json_file)
    json_file.close()
    return data

def main():
    # ask user for input and output directories
    dir1 = diropenbox(msg="Select first input directory", title="Select first input directory", default=getcwd())
    dir2 = diropenbox(msg="Select second input directory", title="Select second input directory", default=getcwd())
    dir3 = diropenbox(msg="Select output directory", title="Select output directory", default=getcwd())
    if not (dir1 and dir2 and dir3):
        exit()

    # generate list of JSON files that are present in both input directories
    filenames_and = [name for name in listdir(dir1) if name in listdir(dir2) and isfile(join(dir1, name)) and isfile(join(dir2, name)) and splitext(join(dir1, name))[1] == ".json" and splitext(join(dir2, name))[1] == ".json"]

    # generate list of JSON files that are only present in dir1
    filenames_xdir1 = [name for name in listdir(dir1) if not name in listdir(dir2) and isfile(join(dir1, name)) and splitext(join(dir1, name))[1] == ".json"]

    # generate list of JSON files that are only present in dir2
    filenames_xdir2 = [name for name in listdir(dir2) if not name in listdir(dir1) and isfile(join(dir2, name)) and splitext(join(dir2, name))[1] == ".json"]

    # merge each JSON file that is in both directories and write it to the output directory
    for filename in filenames_and:
        data1 = import_json(join(dir1, filename))
        data2 = import_json(join(dir2, filename))
        data1_handles = list(map(lambda x: x[0].get("username", ""), data1))
        data3 = list(filter(lambda x: x[0].get("username", "") not in data1_handles, data2)) + data1
        with open(join(dir3, filename), "w", encoding="utf-8") as outfile:
            outfile.write(dumps(data3, indent=4))

    # copy each JSON file that is only present in dir1 directly to dir3
    for filename in filenames_xdir1:
        copy(join(dir1, filename), join(dir3, filename))

    # copy each JSON file that is only present in dir2 directly to dir3
    for filename in filenames_xdir2:
        copy(join(dir2, filename), join(dir3, filename))

    # copy all avatars from dir2 to dir3
    if isdir(join(dir2, "profile_picture")):
        if not isdir(join(dir3, "profile_picture")):
            mkdir(join(dir3, "profile_picture"))
        for file in listdir(join(dir2, "profile_picture")):
            copy(join(dir2, "profile_picture", file), join(dir3, "profile_picture", file))

    # only copy all avatars from dir1 to dir3 that do not yet exist in dir3
    if isdir(join(dir1, "profile_picture")):
        if not isdir(join(dir3, "profile_picture")):
            mkdir(join(dir3, "profile_picture"))
        for file in listdir(join(dir1, "profile_picture")):
            if not isfile(join(dir3, "profile_picture", file)):
                copy(join(dir1, "profile_picture", file), join(dir3, "profile_picture", file))

main()