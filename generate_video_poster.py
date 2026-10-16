# -*- coding: utf-8 -*-
"""
从视频生成封面图片
"""

try:
    import cv2
    from pathlib import Path
    
    video_path = Path(r'C:\Users\komal\Desktop\laser-marking-website\(最终)kvlasermarking.com\video.mp4')
    output_path = Path(r'C:\Users\komal\Desktop\laser-marking-website\(最终)kvlasermarking.com\video-poster.jpg')
    
    if not video_path.exists():
        print(f"❌ 视频文件不存在：{video_path}")
        exit(1)
    
    # 打开视频
    cap = cv2.VideoCapture(str(video_path))
    
    # 读取第一帧
    ret, frame = cap.read()
    
    if ret:
        # 保存为 JPG
        cv2.imwrite(str(output_path), frame, [cv2.IMWRITE_JPEG_QUALITY, 85])
        print(f"✅ 封面图片已生成：{output_path}")
        print(f"   尺寸：{frame.shape[1]}x{frame.shape[0]}")
    else:
        print("❌ 无法读取视频帧")
    
    cap.release()
    
except ImportError:
    print("OpenCV 未安装，创建备用封面图片...")
    
    # 创建简单的占位封面
    from PIL import Image, ImageDraw, ImageFont
    
    output_path = Path(r'C:\Users\komal\Desktop\laser-marking-website\(最终)kvlasermarking.com\video-poster.jpg')
    
    # 创建 1280x720 的图片
    img = Image.new('RGB', (1280, 720), color=(30, 30, 50))
    draw = ImageDraw.Draw(img)
    
    # 添加文字
    try:
        font = ImageFont.truetype("arial.ttf", 48)
    except:
        font = ImageFont.load_default()
    
    text = "KINGVAN Laser Marking Machine"
    # 计算文字位置（居中）
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (1280 - text_width) // 2
    y = (720 - text_height) // 2
    
    draw.text((x, y), text, fill=(255, 255, 255), font=font)
    
    # 添加播放按钮图标
    play_size = 80
    play_x = 1280 // 2 - play_size // 2
    play_y = 720 // 2 - play_size // 2 + 60
    
    # 绘制三角形播放按钮
    play_points = [
        (play_x + 30, play_y),
        (play_x + 30, play_y + play_size),
        (play_x + play_size - 10, play_y + play_size // 2)
    ]
    draw.polygon(play_points, fill=(255, 0, 0))
    
    # 保存
    img.save(output_path, 'JPEG', quality=85)
    print(f"✅ 备用封面图片已生成：{output_path}")
    print(f"   尺寸：1280x720")
