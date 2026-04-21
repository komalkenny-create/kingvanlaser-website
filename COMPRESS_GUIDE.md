# 🎬 视频压缩指南

## 📊 当前视频信息

- **文件大小**: 67.59 MB
- **目标大小**: 5-10 MB
- **压缩比**: 约 85-90%

---

## 🔧 压缩方法

### 方法 1: 使用在线工具（最简单）

#### 推荐工具：

**1. FreeConvert**
- 网址：https://www.freeconvert.com/video-compressor
- 支持最大 1GB 文件
- 步骤：
  1. 上传 `video.mp4`
  2. 选择 "Target Size" 或设置比特率
  3. 下载压缩后的视频
  4. 替换原文件

**2. Compress2Go**
- 网址：https://www.compress2go.com/video
- 支持自定义参数
- 步骤：
  1. 上传文件
  2. 选择 "720p" 或 "480p"
  3. 下载压缩版本

**3. YouCompress**
- 网址：https://www.youcompress.com/
- 免费使用
- 自动优化参数

---

### 方法 2: 使用 HandBrake（推荐）

**下载安装**: https://handbrake.fr/

**压缩步骤**:

1. **打开 HandBrake**
2. **导入视频**: 拖拽 `video.mp4` 到 HandBrake
3. **选择预设**: 
   - 选择 "Fast 720p30" 预设
4. **调整参数**:
   - Video Tab:
     - Video Codec: H.264
     - Quality: RF 24-28（数字越大文件越小）
     - Framerate: Same as source
   - Audio Tab:
     - Codec: AAC
     - Bitrate: 128
5. **设置输出路径**: 选择保存位置
6. **开始压缩**: 点击 "Start Encode"

**推荐参数**:
```
Video:
- Codec: H.264
- RF: 26
- Preset: Slow
- Framerate: 30

Audio:
- Codec: AAC
- Bitrate: 128 kbps

Dimensions:
- Resolution: 1280x720 (720p)
```

---

### 方法 3: 使用 剪映/CapCut

如果你安装了剪映或 CapCut：

1. **导入视频**
2. **点击"导出"**
3. **设置参数**:
   - 分辨率：720p
   - 码率：中等或偏低
   - 格式：MP4
   - 编码：H.264
4. **导出**

---

## 📋 压缩参数建议

### 推荐配置（平衡质量和大小）

```
分辨率：1280x720 (720p)
视频编码：H.264
视频码率：1000-1500 kbps
音频编码：AAC
音频码率：128 kbps
帧率：30 fps
```

### 预期结果

- **原始**: 67.59 MB
- **压缩后**: 约 8-12 MB
- **压缩比**: 约 85%

---

## 🎯 压缩后处理

### 1. 备份原视频
```
video.mp4 → video-original.mp4 (备份)
video-compressed.mp4 → video.mp4 (替换)
```

### 2. 更新网站
压缩后的视频替换原文件即可，HTML 不需要修改。

### 3. 测试
- 本地测试播放
- 上传到 GitHub Pages 测试加载速度
- 检查字幕是否同步

---

## 💡 使用 Python 脚本（如果安装了 ffmpeg）

如果 ffmpeg 已正确安装，运行：

```bash
cd "C:\Users\komal\Desktop\laser-marking-website\(最终)kvlasermarking.com"
python compress_video.py
```

或双击运行：
```
compress.bat
```

---

## ✅ 完成检查清单

- [ ] 视频已压缩到 10MB 以下
- [ ] 视频画质可接受
- [ ] 音频清晰
- [ ] 字幕同步正常
- [ ] 备份原视频
- [ ] 替换原文件
- [ ] 本地测试播放
- [ ] 推送到 GitHub
- [ ] GitHub Pages 测试加载速度

---

## 🚀 推荐方案

**最简单**: 使用 FreeConvert 在线压缩

**最佳质量**: 使用 HandBrake 手动调整参数

**批量处理**: 安装 ffmpeg 使用脚本压缩

---

**选择一种方法开始压缩吧！** 🎬
