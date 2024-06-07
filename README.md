# file-organizer

Since my ~/Downloads was filled with unorganized file types i had to make thisSince my ~/Downloads directory was cluttered with various unorganized file types, I decided to create this script to tidy it up.


## Features

- **Organizes Files by Extension:** Automatically sorts files into folders named after their extensions.
- **Excludes Directories:** Skips directories while organizing files.
- **Retains Script File:** Ensures the organizing script itself is not moved.

## Prerequisites

- Python 3.x

## How to Use
  
  1. **Clone or Download the Repository:**
      ```sh
      git clone https://github.com/abidzzz/file-organizer.git
      cd file-organizer
      ```
  
  2. **Save the Script:**
     Save the script to a file, for example, `organize_files.py`.
  
  3. **Run the Script:**
     Open a terminal or command prompt, navigate to the directory where the script is saved, and run:
     ```sh
     python organize_files.py```

## Example

Before running the script:
```
current_directory/
├── file1.txt
├── file2.jpg
├── file3.txt
└── organize_files.py
```
After running the script:
```
current_directory/
├── JPG/
│   └── file2.jpg
├── TXT/
│   ├── file1.txt
│   └── file3.txt
└── organize_files.py
```
