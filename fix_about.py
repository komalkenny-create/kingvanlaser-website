import os
import re

work_dir = r'C:\Users\komal\Desktop\laser-marking-website\(最终)kvlasermarking.com'

# 更新 about.html 的导航条
about_file = os.path.join(work_dir, 'about.html')
with open(about_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 替换导航条
content = content.replace(
    '<li><a href="index.html">Home</a></li>                    <li><a href="index.html#products">Products</a></li>',
    '<li><a href="index.html">Home</a></li>                    <li><a href="about.html">About Us</a></li>                    <li><a href="index.html#products">Products</a></li>'
)

# 替换 CSS 样式
content = content.replace(
    '.mv-card {            background: white;            padding: 40px 30px;',
    '.mv-card {            background: white;            padding: 30px 25px;'
)
content = content.replace(
    '.mv-icon {            width: 60px;            height: 60px;            margin: 0 auto 20px;',
    '.mv-icon {            width: 50px;            height: 50px;            margin: 0 auto 15px;'
)
content = content.replace(
    '.mv-icon svg { width: 30px; height: 30px; }',
    '.mv-icon svg { width: 24px; height: 24px; }'
)
content = content.replace(
    '.mv-card h3 {            font-size: 1.5rem;',
    '.mv-card h3 {            font-size: 1.3rem;'
)
content = content.replace(
    '.mv-card h3 {            margin-bottom: 12px;        }',
    '.mv-card h3 {            margin-bottom: 10px;        }'
)

with open(about_file, 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ Updated about.html')
print('  - Added About Us link to navigation')
print('  - Reduced icon size: 60px → 50px')
print('  - Reduced icon margin: 20px → 15px')
print('  - Reduced SVG size: 30px → 24px')
print('  - Reduced h3 size: 1.5rem → 1.3rem')
print('  - Reduced h3 margin: 12px → 10px')
print('  - Reduced card padding: 40px 30px → 30px 25px')
