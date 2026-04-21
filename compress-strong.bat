@echo off
chcp 65001 >nul
echo ===============================================
echo     视频强力压缩工具 - KINGVAN
echo     目标：37MB → 5-8MB
echo ===============================================
echo.

cd /d "%~dp0"

REM 检查视频文件
if not exist "video.mp4" (
    echo [!] 视频文件不存在
    pause
    exit /b 1
)

if exist "video-compressed.mp4" (
    echo [!] 发现之前的压缩版本
    echo     重命名为 video-compressed-old.mp4
    move /y "video-compressed.mp4" "video-compressed-old.mp4"
    echo.
)

REM 显示原始文件大小
for %%A in (video.mp4) do set ORIGINAL_SIZE=%%~zA
set /a ORIGINAL_MB=ORIGINAL_SIZE/1024/1024
echo [i] 原始文件大小：%ORIGINAL_MB% MB
echo.

echo [✓] 开始强力压缩...
echo      分辨率：480p (标清)
echo      视频码率：600k
echo      音频码率：64k
echo      CRF: 30 (高压缩)
echo.

REM 使用更强力的压缩参数
ffmpeg -i "video.mp4" ^
    -c:v libx264 ^
    -crf 30 ^
    -preset veryslow ^
    -b:v 600k ^
    -vf "scale=-1:480,fps=24" ^
    -c:a aac ^
    -b:a 64k ^
    -movflags +faststart ^
    -y "video-compressed.mp4"

if errorlevel 1 (
    echo.
    echo [!] 压缩失败
    echo     请确保已安装 ffmpeg
    pause
    exit /b 1
)

REM 显示压缩后文件大小
if exist "video-compressed.mp4" (
    for %%A in (video-compressed.mp4) do set COMPRESSED_SIZE=%%~zA
    set /a COMPRESSED_MB=COMPRESSED_SIZE/1024/1024
    set /a SAVED_MB=ORIGINAL_MB-COMPRESSED_MB
    
    echo.
    echo ===============================================
    echo [✓] 压缩完成!
    echo ===============================================
    echo [✓] 压缩后文件大小：%COMPRESSED_MB% MB
    echo [✓] 节省空间：%SAVED_MB% MB
    echo ===============================================
    echo.
    
    if %COMPRESSED_MB% LEQ 10 (
        echo [✓] 完美！视频已压缩到 10MB 以下
    ) else if %COMPRESSED_MB% LEQ 20 (
        echo [✓] 不错！视频已压缩到 20MB 以下
    ) else (
        echo [!] 文件仍然较大，可以尝试：
        echo     1. 降低分辨率到 360p
        echo     2. 降低视频码率到 400k
        echo     3. 提高 CRF 到 32
    )
    echo.
    echo 下一步:
    echo 1. 测试压缩后的视频播放效果
    echo 2. 如果满意，备份原视频
    echo 3. 替换原视频文件
    echo 4. 推送到 GitHub
    echo.
) else (
    echo [!] 压缩失败，输出文件未生成
)

pause
