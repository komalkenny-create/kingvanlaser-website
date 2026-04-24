file_path = r'C:\Users\komal\Desktop\07_项目网站\laser-marking-website\(最终)kingvanlaser.com\about.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('2014company satrt.jpg', '2014.jpg')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('修改完成')
