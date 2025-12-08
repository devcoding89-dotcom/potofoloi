import re

file_path = r'c:\Users\pelew\Documents\CYBER DEV POTOTFOLOIO\INDEX.HTML'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<p>📱 <strong>08075793311</strong></p>', '')
content = content.replace('<p>📱 08075793311</p>', '')
content = re.sub(r'<button type="button" class="btn whatsapp-btn".*?</button>', '', content, flags=re.DOTALL)
content = content.replace('2348075793311', '')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Phone numbers removed successfully!")
