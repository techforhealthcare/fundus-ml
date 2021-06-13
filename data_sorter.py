from pathlib import Path
import shutil
import os

def create_folders(folder_list):
    for i in folder_list:
        if not os.path.exists(i):
            os.makedirs(i)
            
            print("folder is created: " + i)
        else:
            print("folder already exists: " + i)

def create_left_right_folder(DIR_LEFT,DIR_RIGHT):
    #Create data raw/clean output folder
    # parent_dir = os.getcwd()
    folder= [str(DIR_LEFT),str(DIR_RIGHT)]
    create_folders(folder)


def file_list_sort(source_dir):
    image_paths = list(source_dir.glob("*.jpeg"))
    substring_left = "left"
    substring_right = "right"
    left_list=[]
    right_list =[]
    for file in image_paths:
        if substring_left in file.name:
            left_list.append(file)
        elif substring_right in file.name:
            right_list.append(file)
    
    return left_list , right_list
    

def left_right_image_mover (source_dir , dest_dir_left, dest_dir_right):
    left_list , right_list = file_list_sort(source_dir)

    for path_left in left_list:
        shutil.move(str(path_left),str(dest_dir_left))

    for path_right in right_list:
        shutil.move(str(path_right),str(dest_dir_right))
    return 

def data_sort_and_mover_wrapper(source_dir , dest_dir_left, dest_dir_right):
    create_left_right_folder(dest_dir_left,dest_dir_right)
    left_right_image_mover(source_dir,dest_dir_left,dest_dir_right )
    return


if __name__ == "__main__":

    source_dir = Path("data")
    dest_dir_left = Path("data/left")
    dest_dir_right = Path("data/right")
    data_sort_and_mover_wrapper(source_dir,dest_dir_left,dest_dir_right)

