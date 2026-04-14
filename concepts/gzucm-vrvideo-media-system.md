---
title: GZUCM_VRVideo 媒体展示系统
created: 2026-04-14
updated: 2026-04-14
type: concept
tags: [Unity, VR, 媒体播放, 图片加载, 视频播放, JSON配置]
sources:
  - /home/admin/wiki/raw/assets/GZUCM_VRVideo/Assets/Scripts/CanvasController.cs
  - /home/admin/wiki/raw/assets/GZUCM_VRVideo/Assets/Scripts/DataManager.cs
  - /home/admin/wiki/raw/assets/GZUCM_VRVideo/Assets/Scripts/InteractableData.cs
  - /home/admin/wiki/raw/assets/GZUCM_VRVideo/Assets/Scripts/InteractableDataContainer.cs
---

# GZUCM_VRVideo 媒体展示系统

媒体展示系统是 GZUCM_VRVideo 项目的核心功能，通过数据驱动的方式实现 VR 环境中的图片和视频展示。

## 系统组成

### 1. 数据层

#### InteractableData（交互数据组件）
**文件**: `InteractableData.cs`

**核心功能**:
- 挂载在可交互物体上
- 定义媒体类型（图片/视频）
- 存储媒体 URL 列表

**字段**:
```csharp
public string UniqueID => uniqueID;        // 唯一标识
public MediaType MediaType => mediaType;   // 媒体类型
public List<string> MediaUrls => mediaUrls; // 媒体 URL 列表
```

#### InteractableDataContainer（数据容器）
**文件**: `InteractableDataContainer.cs`

**核心功能**:
- JSON 数据容器类
- 存储多个 InteractableInfo 对象

**数据结构**:
```csharp
[Serializable]
public class InteractableInfo
{
    public string UniqueID;
    public string MediaType; // 使用 string 支持 JSON 反序列化
    public List<string> MediaUrls;
}
```

#### DataManager（数据管理器）
**文件**: `DataManager.cs`

**核心功能**:
- 从 JSON 文件加载交互数据
- 管理数据字典
- 提供数据查询接口

**工作流程**:
1. 启动时加载 `Resources/Test.json`
2. 解析 JSON 数据到 `InteractableDataContainer`
3. 构建以 UniqueID 为键的字典
4. 提供 `GetInteractableInfo()` 查询方法

### 2. 显示层

#### CanvasController（Canvas 控制器）
**文件**: `CanvasController.cs`

**核心功能**:
- 管理媒体显示界面
- 处理交互事件
- 控制媒体播放

**交互事件**:
- `OnSelectEnter()`: 选择物体时触发媒体显示
- `OnHoverEntered()`: 悬停时改变材质
- `OnHoverExited()`: 离开时恢复材质
- `OnSelectExited()`: 选择结束时的处理

## 数据流

```
JSON 配置 → DataManager → 数据字典
     ↓
用户交互 → InteractableData.UniqueID → DataManager.GetInteractableInfo()
     ↓
CanvasController.ShowMedia() → 媒体类型判断
     ↓
图片/视频加载 → 显示到 RawImage/VideoPlayer
```

## 媒体加载机制

### 图片加载
```csharp
public IEnumerator LoadImage(string imageUrl)
{
    // 跨平台路径处理
    if (Application.platform == RuntimePlatform.Android)
        fullPath = Path.Combine("jar:file://" + Application.dataPath + "!/assets/", imageUrl);
    else
        fullPath = Path.Combine("file://" + Application.streamingAssetsPath, imageUrl);
    
    // 异步加载图片
    using (UnityWebRequest uwr = UnityWebRequestTexture.GetTexture(fullPath))
    {
        yield return uwr.SendWebRequest();
        // 处理纹理，调整 RawImage 大小
    }
}
```

### 视频播放
```csharp
void PlayVideo(string videoUrl)
{
    // 暂停背景音乐
    backgroundMusicSource.Pause();
    
    // 设置视频路径
    videoPlayer.url = fullPath;
    videoPlayer.prepareCompleted += OnVideoPrepared;
    videoPlayer.Play();
}
```

## 关键算法

### 1. 图片尺寸调整
```csharp
private void AdjustRawImageSize(Texture texture)
{
    // 计算宽高比
    float imageAspectRatio = (float)texture.width / texture.height;
    
    // 根据父容器尺寸计算目标尺寸
    float targetHeight = parentRectTransform.rect.height;
    float targetWidth = targetHeight * imageAspectRatio;
    
    // 如果超出宽度限制，重新计算
    if (targetWidth > parentRectTransform.rect.width)
    {
        targetWidth = parentRectTransform.rect.width;
        targetHeight = targetWidth / imageAspectRatio;
    }
    
    // 设置 RawImage 尺寸
    rawImageRectTransform.sizeDelta = new Vector2(targetWidth, targetHeight);
}
```

### 2. 视频尺寸处理
```csharp
private void OnVideoPrepared(VideoPlayer source)
{
    // 获取设备支持的最大纹理尺寸
    int maxTextureSize = SystemInfo.maxTextureSize;
    
    // 计算视频宽高比
    float videoAspectRatio = (float)source.width / source.height;
    
    // 限制尺寸不超过设备最大纹理尺寸
    if (videoWidth > maxTextureSize || videoHeight > maxTextureSize)
    {
        // 根据宽高比调整尺寸
    }
    
    // 创建 RenderTexture
    RenderTexture renderTexture = new RenderTexture(videoWidth, videoHeight, 24);
}
```

## 配置指南

### 1. JSON 数据配置
**文件位置**: `Assets/Resources/Test.json`

**数据格式**:
```json
{
  "interactables": [
    {
      "UniqueID": "image001",
      "MediaType": "Image",
      "MediaUrls": ["images/image1.jpg", "images/long_image.jpg"]
    },
    {
      "UniqueID": "video001",
      "MediaType": "Video",
      "MediaUrls": ["videos/video1.mp4"]
    }
  ]
}
```

### 2. 场景设置
1. **DataManager**: 场景中放置一个管理器
2. **CanvasController**: 挂载在 Canvas 控制物体上
3. **InteractableData**: 挂载在每个可交互物体上

### 3. 资源放置
- **图片**: 放在 `StreamingAssets/images/` 目录
- **视频**: 放在 `StreamingAssets/videos/` 目录
- **JSON**: 放在 `Assets/Resources/Test.json`

## 跨平台支持

### Android (Pico)
```csharp
if (Application.platform == RuntimePlatform.Android)
{
    fullPath = Path.Combine("jar:file://" + Application.dataPath + "!/assets/", imageUrl);
}
```

### 编辑器/其他平台
```csharp
else
{
    fullPath = Path.Combine("file://" + Application.streamingAssetsPath, imageUrl);
}
```

## 调试方法

### 1. 数据加载调试
- 查看控制台 JSON 加载日志
- 检查数据字典是否正确构建

### 2. 媒体加载调试
- 监控 UnityWebRequest 错误
- 检查文件路径是否正确

### 3. 常见问题
- **图片不显示**: 检查路径和文件格式
- **视频不播放**: 检查视频编码格式
- **内存泄漏**: 确保释放 RenderTexture

## 扩展可能性

### 1. 新媒体类型
- 支持 360° 视频
- 支持 3D 模型展示
- 支持音频播放

### 2. 交互增强
- 支持缩放和旋转
- 支持多点触控
- 支持手势控制

### 3. 性能优化
- 实现资源缓存
- 支持流式加载
- 优化内存管理

## 相关页面

- [[gzucm-vrvideo-unity-project]] — 主项目页面
- [[gzucm-vrvideo-teleport-system]] — 传送系统
- [[gzucm-vrvideo-interaction-system]] — 交互系统
- [[gzucm-vrvideo-ui-system]] — UI 系统