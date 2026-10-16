from PIL import Image
import os

# 原始 product2 图片（用户上传的）
input_path = r'C:\Users\komal\Desktop\laser-marking-website\(最终)kvlasermarking.com\product2-backup.png'

# 直接复制作为详情页主图（不裁剪不压缩）
output_large = r'C:\Users\komal\Desktop\laser-marking-website\(最终)kvlasermarking.com\product2-large.png'
output_thumb = r'C:\Users\komal\Desktop\laser-marking-website\(最终)kvlasermarking.com\product2.png'

print(f'正在处理：{input_path}')

if os.path.exists(input_path):
    img = Image.open(input_path)
    print(f'原始尺寸：{img.size}')
    
    # 直接保存，不裁剪不压缩
    img.save(output_large, quality=100)
    print(f'✅ 详情页主图已保存：product2-large.png {img.size}')
    
    # 缩略图也使用原图（让 CSS 来处理缩放）
    img.save(output_thumb, quality=100)
    print(f'✅ 首页缩略图已保存：product2.png {img.size}')
    
    print('\n完成！图片未裁剪未压缩，保持原始质量。')
else:
    print(f'错误：文件不存在 - {input_path}')
