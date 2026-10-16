# 🚀 Google Analytics 快速设置 - 5 分钟完成

## 第一步：获取 Google Analytics 账户（3 分钟）

1. **访问**: [analytics.google.com](https://analytics.google.com/)
2. **登录**: 用你的 Google 账号（没有就注册一个）
3. **创建账户**:
   - 账户名：`KINGVAN Technology`
   - 网站名：`kingvanlaser.com`
   - 时区：选择你的时区
   - 货币：CNY 或 USD

4. **创建 Web 流**:
   - 网址：`https://kingvanlaser.com`
   - 流名称：`KINGVAN Website`

5. **复制测量 ID**: 格式类似 `G-XXXXXXXXXX`

---

## 第二步：替换代码中的 ID（2 分钟）

打开以下文件，**全部替换** `G-XXXXXXXXXX` 为你的实际测量 ID：

### 需要修改的文件：
- ✅ `index.html`（已添加 GA 代码）
- `about.html`
- `signin.html`
- `signup.html`
- `dashboard.html`
- `blog.html`
- `news.html`
- `product-1.html`
- `product-2.html`
- `product-3.html`
- `product-4.html`

### 替换示例：
```html
<!-- 替换前 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>

<!-- 替换后 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-ABC123DEF4"></script>
```

**提示**: 用文本编辑器（如 VS Code、Notepad++）的"查找替换"功能，可以一次性替换所有文件！

---

## 第三步：验证安装（1 分钟）

1. 打开 Google Analytics
2. 点击左侧 **"报告"** → **"实时"**
3. 访问你的网站（打开 index.html）
4. 应该能看到 **1 个活跃访客**（就是你自己！）

---

## 📊 查看数据

### 实时数据（立刻可见）
- 当前在线人数
- 正在浏览的页面
- 访客来源

### 标准报告（24 小时后）
- **受众群体**: 访客数量、国家、城市、设备
- **获取渠道**: 访客从哪里来（Google、直接访问等）
- **互动**: 页面浏览量、停留时间、跳出率
- **转化**: 注册数、下载数

---

## 📱 手机查看

下载 **Google Analytics** App：
- iOS: App Store 搜索 "Google Analytics"
- Android: Google Play 搜索 "Google Analytics"

---

## ✅ 完成！

现在你可以：
1. 实时查看网站访客
2. 了解访客来源和地区
3. 追踪用户行为（注册、下载）
4. 优化网站内容

**详细指南请查看**: `GOOGLE_ANALYTICS_SETUP.md`

---

## 🎯 下一步建议

### 1 周后
- 查看哪些页面最受欢迎
- 分析访客主要来自哪些国家
- 了解访客使用手机还是电脑

### 1 月后
- 设置转化目标（注册、下载）
- 追踪营销渠道效果
- 优化跳出率高的页面

### 长期
- 定期查看数据报告
- 根据数据优化网站内容
- 设置邮件定期报告

**祝你数据分析顺利！** 📊
