# 📊 Google Analytics 设置指南

## 什么是 Google Analytics？

Google Analytics 是谷歌提供的免费网站分析工具，可以帮你追踪：
- ✅ 每日/每月访客数量
- ✅ 访客停留时间
- ✅ 访客来源国家/地区
- ✅ 访客使用的设备（手机/电脑）
- ✅ 访客浏览了哪些页面
- ✅ 访客如何找到你的网站（Google 搜索、直接访问等）
- ✅ 转化率（注册、下载等）

---

## 🚀 设置步骤（10 分钟完成）

### 步骤 1: 创建 Google Analytics 账户

1. 访问 [analytics.google.com](https://analytics.google.com/)
2. 点击 **"开始测量"** 或 **"Start measuring"**
3. 用你的 Google 账号登录（没有就注册一个）

### 步骤 2: 创建账户

1. **账户名称**: `KINGVAN Technology`
2. 点击 **"下一步"**

### 步骤 3: 创建媒体资源

1. **媒体资源名称**: `kingvanlaser.com`
2. **报告时区**: 选择你所在的时区（如 China Standard Time）
3. **货币**: CNY（人民币）或 USD（美元）
4. 点击 **"下一步"**

### 步骤 4: 业务信息

1. **行业类别**: 选择 "工业制造" 或 "其他"
2. **业务规模**: 选择你的公司规模
3. **使用目的**: 勾选所有适用选项
4. 点击 **"创建"**

### 步骤 5: 接受条款

- 阅读并接受服务条款
- 点击 **"我接受"**

---

## 📝 获取跟踪代码

### 步骤 6: 选择数据流

1. 点击 **"Web"**（网站）
2. 输入网站网址：`https://kingvanlaser.com`
3. **流名称**: `KINGVAN Website`
4. 点击 **"创建流"**

### 步骤 7: 复制跟踪 ID

你会看到：
- **测量 ID**: `G-XXXXXXXXXX`（10 位字母数字）
- 和一段 JavaScript 代码

**复制整个代码块**，类似这样：

```javascript
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-XXXXXXXXXX');
</script>
```

---

## 💻 安装到网站

### 方法 A: 手动安装（推荐）

将以下代码添加到 **每个 HTML 页面** 的 `<head>` 标签内：

**文件列表：**
- `index.html`
- `about.html`
- `signin.html`
- `signup.html`
- `dashboard.html`
- `blog.html`
- `news.html`
- `product-1.html` 到 `product-4.html`

**安装位置示例：**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- 🔥 Google Analytics 开始 🔥 -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-XXXXXXXXXX');
    </script>
    <!-- 🔥 Google Analytics 结束 🔥 -->
    
    <title>你的页面标题</title>
    ...
</head>
```

### 方法 B: 使用 Google Tag Manager（更灵活）

1. 访问 [tagmanager.google.com](https://tagmanager.google.com/)
2. 创建容器
3. 安装 GTM 代码
4. 在 GTM 中添加 Google Analytics 标签

---

## 📈 查看数据

### 实时数据（安装后立即生效）

1. 登录 Google Analytics
2. 左侧菜单：**报告** → **实时**
3. 可以看到：
   - 当前在线访客数
   - 访客正在浏览的页面
   - 访客来源国家/城市

### 常用报告

#### 1. 受众分析
**路径**: 报告 → 受众群体
- 访客数量
- 新用户 vs 回访用户
- 国家/地区
- 城市
- 语言
- 设备（手机/桌面/平板）

#### 2. 获取渠道
**路径**: 报告 → 获取
- 访客从哪里来
- Google 搜索（自然搜索）
- 直接访问
- 社交媒体
- 引荐网站

#### 3. 行为分析
**路径**: 报告 → 互动
- 页面浏览量
- 平均停留时间
- 跳出率（只看了一页就离开的比例）
- 最受欢迎的页面

#### 4. 转化跟踪
**路径**: 报告 → 转化
- 注册数量
- 文件下载数量
- 联系表单提交

---

## 🎯 设置目标转化（重要！）

### 追踪用户注册

1. 点击左侧 **"管理"**（齿轮图标）
2. 在 **"媒体资源"** 列，点击 **"目标"**
3. 点击 **"+ 新建目标"**
4. 选择 **"自定义"** → **"继续"**
5. 填写：
   - **目标名称**: `User Registration`
   - **目标类型**: 选择 **"目的地"**
   - **目标位置**: 包含 `/dashboard.html`
6. 点击 **"保存"**

### 追踪文件下载

1. 同样步骤创建新目标
2. 填写：
   - **目标名称**: `File Download`
   - **目标类型**: 选择 **"事件"**
   - **事件条件**: 
     - 参数 → 包含 → `download`
3. 点击 **"保存"**

---

## 📊 关键指标解释

| 指标 | 含义 | 健康标准 |
|------|------|----------|
| **会话数 (Sessions)** | 访客访问次数 | 越多越好 |
| **用户数 (Users)** | 独立访客数量 | 稳定增长 |
| **平均停留时间** | 访客平均停留时长 | > 2 分钟 |
| **跳出率 (Bounce Rate)** | 只看一页就离开的比例 | < 60% |
| **页面浏览量 (PV)** | 总共浏览的页面数 | 越多越好 |
| **转化率** | 完成目标（注册/下载）的比例 | > 2% |

---

## 🔔 设置邮件报告（可选）

1. 打开任意报告
2. 点击右上角 **"分享"** 图标
3. 选择 **"安排通过电子邮件发送"**
4. 设置：
   - 频率：每天/每周/每月
   - 收件人邮箱
   - 格式：PDF 或 Excel
5. 点击 **"发送"**

这样你就能定期收到网站数据报告！

---

## 📱 手机 App（随时查看数据）

1. 下载 **Google Analytics** App
   - iOS: [App Store](https://apps.apple.com/app/google-analytics)
   - Android: [Google Play](https://play.google.com/store/apps/details?id=com.google.android.apps.analytics)
2. 用你的 Google 账号登录
3. 随时随地查看网站数据

---

## 🎓 学习资源

- [Google Analytics 官方文档](https://support.google.com/analytics)
- [Google Analytics 学院](https://analytics.google.com/analytics/academy/) - 免费认证课程
- [YouTube 教程](https://www.youtube.com/googleanalytics)

---

## 💡 高级功能（可选）

### 1. 搜索控制台集成
连接 Google Search Console，查看：
- 哪些关键词带来流量
- 网站在 Google 搜索的排名
- 索引覆盖情况

### 2. 广告系列追踪
使用 UTM 参数追踪营销效果：
```
https://kingvanlaser.com/?utm_source=facebook&utm_medium=social&utm_campaign=spring_sale
```

### 3. 事件追踪
追踪特定用户行为：
- 点击下载按钮
- 点击邮件链接
- 视频播放
- 表单提交

---

## ⚠️ 注意事项

### GDPR 合规（欧洲访客）
如果你的网站有欧洲访客，需要：
- 显示 Cookie 同意横幅
- 允许用户拒绝跟踪

### 数据延迟
- 实时报告：即时
- 标准报告：24-48 小时延迟

### 数据保留
- 免费版本：数据保留 14 个月
- 付费版本（GA360）：可保留更久

---

## 📞 需要帮助？

完成设置后，你可以：
1. 在 Google Analytics 中查看 **"实时"** 报告
2. 访问你的网站，看是否能追踪到自己
3. 等待 24 小时后查看完整报告

**祝你数据分析顺利！** 📊
