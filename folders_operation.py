import os


def mkdir(path):
    path = path.strip()
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False


def file_name(file_dir):
    filenames = []
    for root, dirs, files in os.walk(file_dir):
        folder = str(root) + str(dirs)[:-2] + '/'
        for file in files:
            file_type = file[-4:]
            if file_type == '.png' or file_type == '.tif':
                filenames.append(folder+str(file))
    return filenames
