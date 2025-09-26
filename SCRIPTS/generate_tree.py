import os

def generate_tree(startpath, output_file="FOLDER_TREE.md"):
    with open(output_file, "w") as f:
        f.write("```plaintext\n")  # Markdown code block
        for root, dirs, files in os.walk(startpath):
            # Calculate indentation
            level = root.replace(startpath, "").count(os.sep)
            indent = "│   " * level
            f.write(f"{indent}{os.path.basename(root)}/\n")
            
            # Write files
            subindent = "│   " * (level + 1)
            for file in files:
                f.write(f"{subindent}{file}\n")
        f.write("```\n")

# Run it on your current folder (".") or adjust path if needed
if __name__ == "__main__":
    generate_tree(".")
    print("✅ Folder tree generated in FOLDER_TREE.md")

