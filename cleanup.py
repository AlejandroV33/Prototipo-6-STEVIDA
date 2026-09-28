import os
import re

dir_path = r'C:\Users\Daniel Alejandro\Desktop\Alejandro\STEVIDA\Prototipos\prototipo 6'
html_files = [f for f in os.listdir(dir_path) if f.endswith('.html')]

# Patterns to remove
cdn_pattern = re.compile(r'<script src="https://cdn\.tailwindcss\.com"></script>\s*')
config_pattern = re.compile(r'<script>\s*tailwind\.config\s*=.*?</script>\s*', re.DOTALL)
stevida_css_pattern = re.compile(r'<link rel="stylesheet" href="stevida\.css">\s*')

for filename in html_files:
    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # Remove CDN and config
    content = cdn_pattern.sub('', content)
    content = config_pattern.sub('', content)
    
    # Replace stevida.css with output.css
    if '<link rel="stylesheet" href="output.css">' not in content:
        content = stevida_css_pattern.sub('<link rel="stylesheet" href="output.css">\n    ', content)
    else:
        content = stevida_css_pattern.sub('', content)
        
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Cleaned {filename}')

print('HTML cleanup complete.')
