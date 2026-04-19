import os
import re

# 设置工作目录
work_dir = r'C:\Users\komal\Desktop\laser-marking-website\(最终)kvlasermarking.com'

# Google 官方代码模板
official_code = '''    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-ENLCTR79P5"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-ENLCTR79P5');
    </script>'''

# 旧代码模式
old_pattern = r'    <!-- Google Analytics -->\s*<script async src="https://www\.googletagmanager\.com/gtag/js\?id=G-ENLCTR79P5"></script>\s*<script>\s*window\.dataLayer = window\.dataLayer \|\| \[\];\s*function gtag\(\)\{dataLayer\.push\(arguments\);\}\s*gtag\('js', new Date\(\)\);\s*gtag\('config', 'G-ENLCTR79P5'\);\s*</script>'

# 处理所有 HTML 文件
for filename in os.listdir(work_dir):
    if filename.endswith('.html'):
        filepath = os.path.join(work_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否包含旧的 Google Analytics 代码
        if '<!-- Google Analytics -->' in content and 'G-ENLCTR79P5' in content:
            # 替换为官方代码
            content = re.sub(old_pattern, official_code, content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f'✅ Updated: {filename}')
        else:
            print(f'⏭️  Skipped: {filename}')

print('\n✅ All files updated!')
