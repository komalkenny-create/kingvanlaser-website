@echo off
chcp 65001 >nul
echo ===============================================
echo     视频压缩工具 - KINGVAN
echo ===============================================
echo.

cd /d "%~dp0"

REM 检查视频文件
if not exist "video.mp4" (
    echo [!] 视频文件不存在
    pause
    exit /b 1
)

REM 显示原始文件大小
for %%A in (video.mp4) do set ORIGINAL_SIZE=%%~zA
set /a ORIGINAL_MB=ORIGINAL_SIZE/1024/1024
echo [i] 原始文件大小：%ORIGINAL_MB% MB
echo.

echo [✓] 开始压缩视频...
echo      质量：720p 高清
echo      编码：H.264
echo      音频：AAC 128k
echo.

REM 使用 ffmpeg 压缩
"C:\Program Files\FFmpeg\bin\ffmpeg.exe" -i "video.mp4" -c:v libx264 -crf 28 -preset slow -c:a aac -b:a 128k -vf scale=-1:720 -movflags +faststart -y "video-compressed.mp4"

if errorlevel 1 (
    echo.
    echo [!] 压缩失败
    pause
    exit /b 1
)

REM 显示压缩后文件大小
if exist "video-compressed.mp4" (
    for %%A in (video-compressed.mp4) do set COMPRESSED_SIZE=%%~zA
    set /a COMPRESSED_MB=COMPRESSED_SIZE/1024/1024
    set /a SAVED_MB=ORIGINAL_MB-COMPRESSED_MB
    set /a RATIO=SAVED_MB*100/ORIGINAL_MB
    
    echo.
    echo ===============================================
    echo [✓] 压缩完成!
    echo ===============================================
    echo [✓] 压缩后文件大小：%COMPRESSED_MB% MB
    echo [✓] 节省空间：%SAVED_MB% MB (%RATIO%%)
    echo ===============================================
    echo.
    echo 下一步:
    echo 1. 测试压缩后的视频
    echo 2. 如果满意，替换原视频
    echo 3. 更新字幕文件引用
    echo 4. 推送到 GitHub
    echo.
) else (
    echo [!] 压缩失败，输出文件未生成
)

pause
