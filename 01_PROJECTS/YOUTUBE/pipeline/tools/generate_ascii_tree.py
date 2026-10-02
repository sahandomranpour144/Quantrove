import os

ROOT = r"E:\Agentic Workspaces\ClaudeCode\01_PROJECTS\YOUTUBE"

def generate_ascii_tree(startpath, max_files_per_dir=10):
    lines = []
    lines.append(f"YouTube Project/ ({os.path.basename(startpath)})")
    
    total_files = 0
    total_dirs = 0

    for root, dirs, files in os.walk(startpath):
        dirs.sort()
        files.sort()
        
        # Don't recurse into internal or heavy cache directories
        for ignore_dir in ["__pycache__", ".git", "node_modules", ".agents"]:
            if ignore_dir in dirs:
                dirs.remove(ignore_dir)
            
        rel_path = os.path.relpath(root, startpath)
        if rel_path == ".":
            level = 0
        else:
            level = rel_path.count(os.sep) + 1
            dir_name = os.path.basename(root)
            indent = "│   " * (level - 1) + "├── "
            lines.append(f"{indent}{dir_name}/")
            total_dirs += 1

        file_indent = "│   " * level + "├── "
        file_count = len(files)
        total_files += file_count
        
        for i, f in enumerate(files):
            if i < max_files_per_dir or file_count <= max_files_per_dir + 2:
                lines.append(f"{file_indent}{f}")
            elif i == max_files_per_dir:
                lines.append(f"{file_indent}... and {file_count - max_files_per_dir} more files")
                break

    return "\n".join(lines), total_dirs, total_files

def main():
    tree_str, total_dirs, total_files = generate_ascii_tree(ROOT, max_files_per_dir=12)
    print("\n=======================================================")
    print("VERIFIED WORKSPACE ARCHITECTURE TREE")
    print("=======================================================\n")
    print(tree_str)
    print("\n-------------------------------------------------------")
    print(f"Summary: {total_dirs} directories, {total_files} files verified across workspace.")
    print("-------------------------------------------------------\n")

if __name__ == "__main__":
    main()
