import os
import shutil


def get_train_validation_folders(BASE_DIR):
    TRAIN_FOLDERS = []
    VALID_FOLDERS = []
    ALZ_TRAIN = []
    NONALZ_TRAIN = []
    ALZ_VALID = []
    NONALZ_VALID = []
    for (root, dirs, files) in os.walk(BASE_DIR, topdown=True):
        for d in dirs:
            if d == 'train':
                TRAIN_FOLDERS.append(os.path.join(root, d))
            if d == 'validation':
                VALID_FOLDERS.append(os.path.join(root, d))
    for folder in TRAIN_FOLDERS:
        for (root, dirs, files) in os.walk(folder):
            for d in dirs:
                if d == 'alzheimers':
                    ALZ_TRAIN.append(os.path.join(root, d))
                elif d == 'nonalzheimers':
                    NONALZ_TRAIN.append(os.path.join(root, d))
    for folder in VALID_FOLDERS:
        for (root, dirs, files) in os.walk(folder):
            for d in dirs:
                if d == 'alzheimers':
                    ALZ_VALID.append(os.path.join(root, d))
                elif d == 'nonalzheimers':
                    NONALZ_VALID.append(os.path.join(root, d))
    return ALZ_TRAIN, NONALZ_TRAIN, ALZ_VALID, NONALZ_VALID


def prepare_data(FOLDERS, DEST):
    count = 0
    for folder in FOLDERS:
        for(root, dirs, files) in os.walk(folder, topdown=True):
            for f in files:
                new_filename = str(count) + '.jpg'
                count = count + 1
                shutil.copy(os.path.join(root, f),
                            os.path.join(DEST, new_filename))
            print("Finished copying from {}".format(root))


if __name__ == "__main__":
    BASE_DIR = "/home/ryan/Desktop/alzheimers-fastai/data"
    DEST_BASE_DIR = "/home/ryan/Desktop/alzheimers-fastai/dataset"
    alz_train, nonalz_train, alz_valid, nonalz_valid = get_train_validation_folders(
        BASE_DIR)
    ALZ_TRAIN_DEST_FOLDER = os.path.join(DEST_BASE_DIR, 'train', 'alzheimers')
    NON_ALZ_TRAIN_DEST_FOLDER = os.path.join(
        DEST_BASE_DIR, 'train', 'non_alzheimers')
    ALZ_VALID_DEST_FOLDER = os.path.join(DEST_BASE_DIR, 'valid', 'alzheimers')
    NON_ALZ_VALID_DEST_FOLDER = os.path.join(
        DEST_BASE_DIR, 'valid', 'non_alzheimers')

    prepare_data(alz_train, ALZ_TRAIN_DEST_FOLDER)
    prepare_data(nonalz_train, NON_ALZ_TRAIN_DEST_FOLDER)
    prepare_data(alz_valid, ALZ_VALID_DEST_FOLDER)
    prepare_data(nonalz_valid, NON_ALZ_VALID_DEST_FOLDER)
