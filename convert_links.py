import os
import re

def convert_wikilinks(folder='docs'):
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # [[Название страницы]] → [Название страницы](Название страницы.md)
                new_content = re.sub(r'\[\[([^\]]+)\]\]', r'[\1](\1.md)', content)

                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

convert_wikilinks()
