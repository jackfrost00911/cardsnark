import os
import re

# Path to your posts folder
POSTS_DIR = '_posts'

def fix_front_matter(content):
    # 1. Fix double-double quotes in Title and Description
    # Matches: title: ""Something"" -> title: "Something"
    content = re.sub(r'title:\s*""(.*?)""', r'title: "\1"', content)
    content = re.sub(r'description:\s*""(.*?)""', r'description: "\1"', content)
    
    # Also catch cases where it's just one extra quote at the start/end
    # title: ""Something" -> title: "Something"
    content = re.sub(r'title:\s*""(.*?)"', r'title: "\1"', content)
    content = re.sub(r'description:\s*""(.*?)"', r'description: "\1"', content)

    # 2. Fix Duplicate Categories
    # If we see 'categories: [reviews]' twice, remove the second one.
    lines = content.split('\n')
    new_lines = []
    seen_categories = False
    
    in_front_matter = False
    dash_count = 0

    for line in lines:
        stripped = line.strip()
        
        # Track if we are inside the Front Matter (---) block
        if stripped == '---':
            dash_count += 1
        
        # Only clean inside the first block
        if dash_count < 2:
            if stripped.startswith('categories:'):
                if seen_categories:
                    continue # Skip this line (it's a duplicate)
                seen_categories = True
        
        new_lines.append(line)
        
    return '\n'.join(new_lines)

def main():
    if not os.path.exists(POSTS_DIR):
        print(f"Error: Could not find folder '{POSTS_DIR}'. Make sure you run this script in your root folder.")
        return

    count = 0
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".md") or filename.endswith(".markdown"):
            filepath = os.path.join(POSTS_DIR, filename)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            fixed_content = fix_front_matter(original_content)
            
            if original_content != fixed_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)
                print(f"Fixed: {filename}")
                count += 1
    
    print(f"\nSuccess! Repaired {count} files.")

if __name__ == "__main__":
    main()

