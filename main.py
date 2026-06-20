import os
import shutil

original_folder = r"C:\Users\dibij\Downloads"
target_folder = r"D:/doujinshi"
def check_folder():
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        print(f"Directory Created at {target_folder}")
    else:
        print("Directory already exists")   

def list_files():
    for file in os.listdir(original_folder):
        print(file)
def list_origin():    
    for file_name in os.listdir(original_folder):
        if not file_name.endswith(".pdf"):
            continue
        
        full_path = os.path.join(original_folder, file_name)
        url = None
        
        try:
            with open(full_path + ":Zone.Identifier", 'r') as f:
                for line in f:
                    if line.startswith("HostUrl="):
                        url = line.split("=", 1)[1].strip()
                        
                        break
        except FileNotFoundError:
            pass
        
        if url:
            print(f"{file_name} -> {url}")
        else:
            print(f"{file_name} -> No HostUrl found")
            
def move_files():
    for file_name in os.listdir(original_folder):     
        if url and "https://archiveofourown.org/" in url:    
            shutil.move(full_path, target_folder)
            print(f"File moved to {target_folder}")
            
        else:
            print(f"File not moved to {target_folder}")
            