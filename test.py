import os

original_folder = r"C:\Users\dibij\Downloads"

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