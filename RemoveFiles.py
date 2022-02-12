import time
import os
import shutil
def main():
    deletedFoldersCount  = 0
    deletedFilesCount = 0
    files = 0
    path = "C:/Users/gogof/Desktop/coding/hi-main/c99.txt"
    days = 30
    seconds = time.time()-(days*24*3600)
    if os.path.exists(path):
        for root_folder,folder,files in os.walk(path):
            if seconds>=get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                deletedFoldersCount+=1
                break
            else:
                for folder in folders:
                    folder_path = os.path.join(root_folder,folder)
                if seconds>=get_file_or_folder_age(folder_path):
                    remove_folder(folder_path)
                    deletedFoldersCount+=1
        for file in files:
            file_path=os.path.join(root_folder,file)
            if seconds>=get_file_or_folder_age(file_path):
                remove_file(file_path)
                deletedFilesCount+=1
    else:
        if seconds>=get_file_or_folder_age( path):
            remove_file(path)
            deletedFilesCount+=1
            