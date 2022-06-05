import os
def getallfiles(path):
    allfiles = os.listdir(path)
    filenames = []
    for name in allfiles:
        fullname = os.path.join(path, name)
        if os.path.isfile(fullname):
            filenames.append(fullname)
        elif os.path.isdir(fullname):
            subfiles = getallfiles(fullname)
            for subfile in subfiles:
                filenames.append(subfile)
    return filenames

path = "."
names = getallfiles(path)