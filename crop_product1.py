from PIL import Image

# 打开原始图片
img = Image.open(r'C:\Users\komal\Desktop\laser-marking-website\(最终)kvlasermarking.com\product-1gengxin.png')
print(f'原始尺寸: {img.size}')
width, height = img.size

# 裁切图片，聚焦机器主体
left = int(width * 0.08)
top = int(height * 0.05)
right = int(width * 0.92)
bottom = int(height * 0.82)

cropped = img.crop((left, top, right, bottom))
print(f'裁切后尺寸: {cropped.size}')

# 调整到800x800
resized = cropped.resize((800, 800), Image.LANCZOS)
output_path = r'C:\Users\komal\Desktop\laser-marking-website\(最终)kvlasermarking.com\product1.png'
resized.save(output_path, quality=95, optimize=True)
print(f'✅ 保存成功！最终尺寸: {resized.size}')
print(f'输出路径: {output_path}')
