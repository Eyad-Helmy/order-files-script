import argparse
import json
import sys
from pathlib import Path

# 1. setup config file path
#it should be in the same parent folder this file is in

# 2. define a function that loads the default path from the config file, if it does not exist return None

# 3. define a function that saves a new default path by first creating config file if it does not exist and then adds the path to the file

# 4. main function:
#   initiate argumnt parser instance
#   add all arguments
#   parse the incoming arguments
#   if the arg set-default was used, call save default path function
#   if no path was provided throw an error and close script
#   insert original renaming logic

CONFIG_FILE = Path(__file__).parent / "config.json"

def load_default_path():
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, 'r') as file:
            data = json.load(file)
            return data.get("default_path")
    return None

def save_default_path(path_string):
    if not Path(path_string).is_dir():
        print(f"[!] Error: The path '{path_string}' is not a valid Path")
        sys.exit(1)
    
    with open(CONFIG_FILE, 'w') as file:
        json.dump({"default_path" : path_string}, file)
    print(f"[+] Successfully saved '{path_string}' as the default path.")

def main():
    
    parser = argparse.ArgumentParser(description="Order files numerically based on modification date.")

    parser.add_argument("-s", "--start", type=int, default=1, help="Number to start the ordering with. The default value is 1")
    parser.add_argument("-p", "--path", type=str, help="Specific folder path to operate on for this run.")
    parser.add_argument("--set-default", type=str, help="Save a folder path as the default for future runs.")

    args = parser.parse_args()

    if args.set_default:
        save_default_path(args.set_default)
        sys.exit(0)

    folder_path_string = args.path or load_default_path()   # priority is given to one-time path argument

    if not folder_path_string:
        print("[!] Error: No folder path provided and no default folder path set.")
        print("Use '--set-default <path>' to set a default, or '-p <path>' to provide one for this run.")
        sys.exit(1)
    
    folder_path = Path(folder_path_string)
    
    if not folder_path.exists() or not folder_path.is_dir():
        print(f"[!] Error: Folder '{folder_path}' does not exist")
        sys.exit(1)
    
    #original sorting logic:
    print(f"[*] Operating on folder: {folder_path}")

    files = [file for file in folder_path.iterdir() if file.is_file()]
    # print(files) #output is an array of elements each looking like this: WindowsPath('C:/Users/meyad/Downloads/01-1a-intr_Machine_Human_Bridge (1).pdf')

    if not files:
        print("[-] Ordering Folder Is Empty")
    else:
        files.sort(key= lambda x: x.stat().st_mtime)    #sort files by modification date

        for index, file_path in enumerate(files, start=args.start):
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

if __name__ == "__main__":
    main()