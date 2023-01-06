import os

def write_dir_structure(root_dir, output_file):
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(root_dir):
            level = root.replace(root_dir, '').count(os.sep)
            indent = ' ' * 4 * level
            f.write(f'{indent}|--- {os.path.basename(root)}/\n')
            subindent = ' ' * 4 * (level + 1)
            for file in files:
                f.write(f'{subindent}|--- {file}\n')
            if not files:
                f.write(f'{subindent}--- \n')

# Write the directory structure for the current directory to a file
write_dir_structure('.', 'dir_structure.txt')
