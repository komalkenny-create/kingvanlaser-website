# -*- coding: utf-8 -*-
"""
视频压缩脚本
使用 ffmpeg 压缩视频，减小文件大小同时保持较好画质
目标：60MB → 5-10MB
"""

import subprocess
from pathlib import Path

# 文件路径
INPUT_VIDEO = Path(r'C:\Users\komal\Desktop\laser-marking-website\(最终)kvlasermarking.com\video.mp4')
OUTPUT_VIDEO = Path(r'C:\Users\komal\Desktop\laser-marking-website\(最终)kvlasermarking.com\video-compressed.mp4')

# 压缩参数配置
# 方法 1: 使用 CRF (Constant Rate Factor) - 推荐
# CRF 值：18-28 (越小质量越高，文件越大)
# 18 = 几乎无损
# 23 = 默认
# 28 = 较低质量

def compress_video():
    """压缩视频"""
    
    if not INPUT_VIDEO.exists():
        print(f"❌ 视频文件不存在：{INPUT_VIDEO}")
        return False
    
    # 显示原始文件信息
    original_size = INPUT_VIDEO.stat().st_size / 1024 / 1024
    print(f"📊 原始文件信息:")
    print(f"   大小：{original_size:.2f} MB")
    print(f"   路径：{INPUT_VIDEO}")
    print()
    
    # ffmpeg 压缩命令
    # -c:v libx264: 使用 H.264 编码器
    # -crf 28: 质量因子 (28 = 较小文件，可接受质量)
    # -preset slow: 编码速度慢但压缩效率高
    # -c:v libx264 -movflags +faststart: 优化网络播放
    # -vf scale=-1:720: 缩放到 720p 高度（保持宽高比）
    
    cmd = [
        'ffmpeg',
        '-i', str(INPUT_VIDEO),
        '-c:v', 'libx264',
        '-crf', '28',  # 质量因子，可调整为 23-30
        '-preset', 'slow',  # 编码速度，可选：ultrafast, fast, medium, slow, veryslow
        '-c:a', 'aac',
        '-b:a', '128k',  # 音频比特率
        '-vf', 'scale=-1:720',  # 缩放到 720p
        '-movflags', '+faststart',  # 优化网络流式播放
        '-y',  # 覆盖输出文件
        str(OUTPUT_VIDEO)
    ]
    
    print("🎬 开始压缩视频...")
    print(f"   质量因子 (CRF): 28")
    print(f"   分辨率：720p (高清)")
    print(f"   音频：AAC 128k")
    print()
    
    try:
        # 执行 ffmpeg 命令
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        
        if result.returncode != 0:
            print(f"❌ 压缩失败：{result.stderr}")
            return False
        
        # 显示压缩后文件信息
        if OUTPUT_VIDEO.exists():
            compressed_size = OUTPUT_VIDEO.stat().st_size / 1024 / 1024
            compression_ratio = (1 - compressed_size / original_size) * 100
            
            print("✅ 压缩完成!")
            print(f"📊 压缩后文件信息:")
            print(f"   大小：{compressed_size:.2f} MB")
            print(f"   压缩比：{compression_ratio:.1f}%")
            print(f"   节省：{original_size - compressed_size:.2f} MB")
            print(f"   路径：{OUTPUT_VIDEO}")
            print()
            
            # 判断是否达到目标
            if compressed_size < 10:
                print("🎉 完美！视频已压缩到 10MB 以下")
            elif compressed_size < 20:
                print("✅ 不错！视频已压缩到 20MB 以下")
            else:
                print("⚠️ 文件仍然较大，可以尝试更高的 CRF 值（如 30）")
            
            return True
        else:
            print("❌ 输出文件未生成")
            return False
            
    except FileNotFoundError:
        print("❌ ffmpeg 未安装或未添加到系统 PATH")
        print()
        print("📦 如何安装 ffmpeg:")
        print("   方法 1: 使用 winget")
        print("         winget install ffmpeg")
        print()
        print("   方法 2: 使用 choco")
        print("         choco install ffmpeg")
        print()
        print("   方法 3: 从官网下载")
        print("         https://ffmpeg.org/download.html")
        return False
    except Exception as e:
        print(f"❌ 发生错误：{e}")
        return False


def compress_video_alternative():
    """备选方案：使用更激进的压缩参数"""
    
    OUTPUT_VIDEO_2 = Path(r'C:\Users\komal\Desktop\laser-marking-website\(最终)kvlasermarking.com\video-compressed-hq.mp4')
    
    # 使用 2 次编码，获得更好的质量和大小平衡
    cmd = [
        'ffmpeg',
        '-i', str(INPUT_VIDEO),
        '-c:v', 'libx264',
        '-crf', '26',  # 稍微高质量
        '-preset', 'veryslow',  # 最慢但压缩效率最高
        '-c:a', 'aac',
        '-b:a', '96k',  # 更低音频比特率
        '-vf', 'scale=-1:720',
        '-movflags', '+faststart',
        '-y',
        str(OUTPUT_VIDEO_2)
    ]
    
    print("\n🎬 开始高质量压缩...")
    result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    
    if OUTPUT_VIDEO_2.exists():
        size = OUTPUT_VIDEO_2.stat().st_size / 1024 / 1024
        print(f"✅ 高质量版本：{size:.2f} MB")


if __name__ == "__main__":
    print("=" * 70)
    print("🎬 视频压缩工具 - KINGVAN")
    print("=" * 70)
    print()
    
    success = compress_video()
    
    if success:
        print()
        print("=" * 70)
        print("✅ 压缩完成！")
        print()
        print("下一步:")
        print("1. 测试压缩后的视频播放效果")
        print("2. 如果满意，将原视频备份后替换")
        print("3. 更新 HTML 中的视频引用")
        print("4. 推送到 GitHub")
        print("=" * 70)
    else:
        print()
        print("=" * 70)
        print("❌ 压缩失败或 ffmpeg 未安装")
        print()
        print("替代方案:")
        print("1. 使用在线工具：https://www.freeconvert.com/video-compressor")
        print("2. 使用 HandBrake: https://handbrake.fr/")
        print("3. 使用 剪映/必剪 等视频编辑软件导出压缩版本")
        print("=" * 70)
