# 🔥 Firebase 设置指南

## 步骤 1: 创建 Firebase 项目

1. 访问 [Firebase Console](https://console.firebase.google.com/)
2. 点击 "Add project" 或 "创建项目"
3. 输入项目名称：`kingvan-technology`（或其他名称）
4. 启用/禁用 Google Analytics（可选）
5. 点击 "Create project"

---

## 步骤 2: 注册 Web 应用

1. 在 Firebase 控制台，点击网页图标 **</>** (Web)
2. 输入应用昵称：`KINGVAN Website`
3. 勾选 "Also set up Firebase Hosting"（可选）
4. 点击 "Register app"
5. **复制 Firebase 配置**（稍后会用到）

---

## 步骤 3: 启用 Authentication

1. 在左侧菜单，点击 **Build** → **Authentication**
2. 点击 "Get started"
3. 点击 "Email/Password"
4. 启用 "Email/Password" 登录方式
5. 点击 "Save"

### 可选：启用 Google 登录
1. 点击 "Google"
2. 启用并设置支持邮箱
3. 输入项目支持邮箱
4. 点击 "Save"

---

## 步骤 4: 创建 Firestore 数据库

1. 在左侧菜单，点击 **Build** → **Firestore Database**
2. 点击 "Create database"
3. 选择 **Start in test mode**（测试模式）
4. 选择位置（建议选 `asia-southeast1` 新加坡，速度较快）
5. 点击 "Enable"

### 设置安全规则
点击 "Rules" 标签，替换为以下规则：

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // 用户数据：只有用户可以读写自己的数据
    match /users/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
    
    // 文件数据：所有登录用户可以读取
    match /files/{fileId} {
      allow read: if request.auth != null;
      allow write: if false; // 只有管理员可以通过控制台写入
    }
    
    // 下载记录
    match /downloads/{downloadId} {
      allow read, write: if request.auth != null;
    }
  }
}
```

---

## 步骤 5: 设置 Storage（文件存储）

1. 在左侧菜单，点击 **Build** → **Storage**
2. 点击 "Get started"
3. 点击 "Next"（使用默认安全规则）
4. 选择位置（与 Firestore 相同）
5. 点击 "Done"

### 设置 Storage 安全规则
点击 "Rules" 标签，替换为：

```javascript
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    // 只有登录用户可以读取文件
    match /files/{allPaths=**} {
      allow read: if request.auth != null;
      allow write: if false; // 只有管理员可以上传
    }
  }
}
```

---

## 步骤 6: 获取配置并更新代码

### 从 Firebase 控制台复制配置

在 Project Settings → General → Your apps 下方，找到：

```javascript
const firebaseConfig = {
  apiKey: "AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXX",
  authDomain: "your-project.firebaseapp.com",
  projectId: "your-project-id",
  storageBucket: "your-project.appspot.com",
  messagingSenderId: "123456789012",
  appId: "1:123456789012:web:abcdef123456"
};
```

### 更新以下文件：

1. **signup.html** - 第 268-274 行
2. **signin.html** - 需要类似更新
3. **dashboard.html** - 第 213-219 行

将 `YOUR_API_KEY` 等占位符替换为实际配置值。

---

## 步骤 7: 上传文件到 Storage

### 方法 A：通过 Firebase 控制台

1. 前往 **Build** → **Storage**
2. 点击 "Add folder" 创建 `files` 文件夹
3. 上传文件（PDF、DOCX、XLSX 等）
4. 复制每个文件的下载链接
5. 更新 `dashboard.html` 中的 `filesData` 数组

### 方法 B：创建管理员上传页面

创建一个 `admin-upload.html` 页面用于上传文件（需要额外代码）。

---

## 步骤 8: 测试注册和下载

### 测试流程：

1. 打开 `signup.html`
2. 填写表单并注册
3. 成功后会自动跳转到 `dashboard.html`
4. 查看用户数据是否保存在 Firestore
5. 点击下载按钮测试文件下载

---

## 📊 Firestore 数据结构

### users 集合
```
/users
  /{userId}
    - firstName: string
    - lastName: string
    - email: string
    - company: string
    - phone: string
    - createdAt: timestamp
    - role: 'customer' | 'admin'
```

### files 集合（可选，用于动态文件列表）
```
/files
  /{fileId}
    - name: string
    - type: string
    - size: string
    - description: string
    - url: string
    - downloads: number
    - createdAt: timestamp
```

### downloads 集合（用于跟踪下载）
```
/downloads
  /{downloadId}
    - userId: string
    - fileId: string
    - downloadedAt: timestamp
```

---

## 🔒 安全建议

### 生产环境前的准备：

1. **更新 Firestore 安全规则** - 限制写入权限
2. **更新 Storage 安全规则** - 限制文件类型和大小
3. **启用 Firebase App Check** - 防止滥用
4. **设置使用量提醒** - 避免超额费用
5. **启用 Cloud Functions** - 用于发送欢迎邮件等

---

## 💰 费用说明

### 免费额度（Spark Plan）：

- **Authentication**: 每月 10,000 次邮箱登录
- **Firestore**: 1GB 存储，50,000 次读取/天
- **Storage**: 5GB 存储，1GB/天 下载
- **Hosting**: 10GB 存储，360MB/天 流量

### 付费计划（Blaze Plan）：

- 按使用量付费
- 非常便宜，小网站每月约 $5-25

---

## 🛠️ 常见问题

### Q: 如何查看注册用户？
A: 前往 Authentication → Users 查看所有注册用户

### Q: 如何删除测试用户？
A: Authentication → Users → 选择用户 → 删除

### Q: 如何备份数据？
A: Firestore → Data → 点击 "..." → Export

### Q: 忘记密码怎么办？
A: 需要实现密码重置功能（使用 `sendPasswordResetEmail`）

---

## 📞 需要帮助？

- [Firebase 官方文档](https://firebase.google.com/docs)
- [Firebase 社区论坛](https://stackoverflow.com/questions/tagged/firebase)
- [Firebase YouTube 教程](https://www.youtube.com/firebase)

---

**设置完成后，你的网站将拥有完整的用户注册、登录和文件下载功能！** 🎉
