from PIL import Image
import os

# 原始图片路径（用户上传的）
# 由于原始图片已被覆盖，我们使用现有的 product2-large.png 作为源
# 但这样质量会损失，最好用户重新提供原始图片

# 打开 product2-large.png (400x500)
large_path = r'C:\Users\komal\Desktop\laser-marking-website\(最终)kvlasermarking.com\product2-large.png'

if os.path.exists(large_path):
    img = Image.open(large_path)
    print(f'当前 product2-large.png 尺寸：{img.size}')
    
    # 从 400x500 缩放到 400x300（首页缩略图）
    # 使用 crop 保持比例
    width, height = img.size
    
    # 计算裁剪区域（从 500 高度中取 300，居中裁剪）
    left = 0
    top = int((height - 300) / 2)  # 从中间开始
    right = width
    bottom = top + 300
    
    cropped = img.crop((left, top, right, bottom))
    print(f'裁剪后尺寸：{cropped.size}')
    
    # 保存为 product2.png（首页缩略图）
    output_path = r'C:\Users\komal\Desktop\laser-marking-website\(最终)kvlasermarking.com\product2.png'
    cropped.save(output_path, quality=95, optimize=True)
    print(f'✅ 首页缩略图已保存：product2.png (400x300)')
else:
    print('错误：找不到 product2-large.png')
