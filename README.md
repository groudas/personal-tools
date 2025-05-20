# personal-tools
A collection of scripts and tools I did myself to facilitate little chores.

## copy_txt_folder.js
This script is useful if you need to easily feed the content of a complex folder structure into an LLM context. It creates a new folder named `<current_folder_name>copy` in the parent directory. It then recursively copies all files from the current directory and its subdirectories into this new folder. Each copied file is renamed by taking its original relative path, replacing directory separators with underscores, and appending a `.txt` extension (e.g., a file at `src/module/mainprocess.js` becomes `src_module_mainprocess.js.txt`). Finally, it generates a `tree_structure.txt` file in the destination folder, showing the original directory structure.