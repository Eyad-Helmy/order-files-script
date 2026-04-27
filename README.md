# Order Files Tool

A Python command-line tool to numerically order files in a folder based on their modification date.

## Description

This tool renames files in a directory by prefixing them with a sequential number based on their last modification time (oldest files first). It features a persistent configuration system to remember your "active" folder, saving you from re-typing long Windows paths.

## Features

- Rename files numerically based on modification date
- Set a default folder path for repeated use
- Customize the starting number for ordering
- Skip empty files
- Handle common errors (permissions, existing files)

## Installation

1. Clone this reposistor:
```bash
git clone https://github.com/yourusername/order-files-script.git
cd order-files-script
```
2. Install in "Editable" mode using pip 
```bash
pip install -e .
```


## Usage

Run the script from the command line:

```bash
order-files [options]
```

### Options

- `-s, --start <number>`: Number to start the ordering with (default: 1)
- `-p, --path <path>`: Specific folder path to operate on for this run
- `--set-default <path>`: Save a folder path as the default for future runs
- `--delete-default`: Delete the saved default folder path

### Examples

1. **Set a default folder:**
   ```bash
   order-files --set-default "C:\Users\Name\Desktop\TargetFolder"
   ```

2. **Delete the default folder:**
   ```bash
   order-files --delete-default
   ```

3. **Order files in the default folder starting from 1:**
   ```bash
   order-files
   ```

4. **Order files in a specific folder starting from 10:**
   ```bash
   order-files -s 10
   ```

## Output

The tool provides detailed logs for each file operation, including successes and errors.

Example output:
```
[*] Operating on folder: /path/to/folder
[+] Renamed old_file.txt -> 1-old_file.txt
[+] Renamed another_file.pdf -> 2-another_file.pdf
[!] Error: Could Not Rename locked_file.doc | Permission Denied (File may be open elsewhere)
==== End Of Logs ====
```

## Notes

- Empty files (0 bytes) are skipped.
- Files are sorted by modification time (oldest first).
- The tool does not create backups; ensure you have copies of important files.
- Use absolute paths for reliability.

## License

This project is open-source. Feel free to modify and distribute.