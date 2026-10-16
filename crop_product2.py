from PIL import Image
import os

# 打开原始图片
input_path = r'C:\Users\komal\Desktop\laser-marking-website\(最终)kvlasermarking.com\product2.png'
output_large = r'C:\Users\komal\Desktop\laser-marking-website\(最终)kvlasermarking.com\product2-large.png'
output_thumb = r'C:\Users\komal\Desktop\laser-marking-website\(最终)kvlasermarking.com\product2.png'

print(f'正在处理：{input_path}')

# 检查文件是否存在
if not os.path.exists(input_path):
    print(f'错误：文件不存在 - {input_path}')
else:
    img = Image.open(input_path)
    print(f'原始尺寸：{img.size}')
    width, height = img.size

    # 裁剪图片，聚焦机器主体
    left = int(width * 0.05)
    top = int(height * 0.03)
    right = int(width * 0.95)
    bottom = int(height * 0.88)

    cropped = img.crop((left, top, right, bottom))
    print(f'裁剪后尺寸：{cropped.size}')

    # 调整到 400x500（详情页主图）
    resized_large = cropped.resize((400, 500), Image.LANCZOS)
    resized_large.save(output_large, quality=95, optimize=True)
    print(f'✅ 详情页主图已保存：product2-large.png (400x500)')

    # 调整到 400x300（首页缩略图）
    resized_thumb = cropped.resize((400, 300), Image.LANCZOS)
    resized_thumb.save(output_thumb, quality=95, optimize=True)
    print(f'✅ 首页缩略图已保存：product2.png (400x300)')

    print('处理完成！')
