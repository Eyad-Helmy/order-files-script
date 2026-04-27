from pathlib import Path


folder_path = Path(r"C:\Users\meyad\Desktop\filtering_placeholder")

files = [file for file in folder_path.iterdir() if file.is_file()]
# print(files) #output is an array of elements each looking like this: WindowsPath('C:/Users/meyad/Downloads/01-1a-intr_Machine_Human_Bridge (1).pdf')

if not files:
    print("[-] Ordering Folder Is Empty")
else:
    files.sort(key= lambda x: x.stat().st_mtime)    #sort files by modification date

    for index, file_path in enumerate(files, start=1):
        if file_path.stat().st_size == 0:
            print(f"[-] Skipped: '{file_path.name}' (File is empty - 0 bytes)")
            continue    #skip this loop iteration 

        new_name = f"{index}-{file_path.name}"
        new_file_path = file_path.with_name(new_name)   #change the address name(last part of an address of a file) in memory to a new name given as an argument 

        try:
            file_path.rename(new_file_path)     #take this new full path and rename the old key in the file table into that path string
            print(f"[+] Renamed {file_path.name} -> {new_name}")    #file_path name doesn't change in memory only changed in the actual SSD

        except PermissionError:
            print(f"[!] Error: Could Not Rename {file_path.name} | Permission Denied (File may be open elsewhere)")

        except FileExistsError:
            print(f"[!] Error: Could Not Rename {file_path.name} | {new_name} already exists")
        
        except OSError as e:
            print(f"[!] System Error on {file_path.name}: {e}")

    print("==== End Of Logs ====")
