---
title: GZUCM_VRVideo UI 系统
created: 2026-04-14
updated: 2026-04-14
type: concept
tags: [Unity, VR, UI系统, 菜单管理, 背景音乐, 音频控制]
sources:
  - /home/admin/wiki/raw/assets/GZUCM_VRVideo/Assets/Scripts/MenuUI.cs
  - /home/admin/wiki/raw/assets/GZUCM_VRVideo/Assets/Scripts/BackgroundMusicController.cs
  - /home/admin/wiki/raw/assets/GZUCM_VRVideo/Assets/Scripts/CanvasController.cs
---

# GZUCM_VRVideo UI 系统

UI 系统是 GZUCM_VRVideo 项目的用户界面管理核心，负责菜单显示、音频控制、媒体播放控制等 UI 相关功能。

## 系统组成

### 1. MenuUI（菜单 UI 系统）
**文件**: `MenuUI.cs`

**核心功能**:
- 管理菜单显示/隐藏
- 处理场景切换提示
- 控制 UI 状态重置

**关键组件**:
```csharp
public GameObject Menu;        // 主菜单
public GameObject MainBuilding; // 主建筑（已注释）
public GameObject TipsPage;    // 提示页面
public static MenuUI instance; // 单例实例
```

**状态管理**:
- **单例模式**: 使用 DontDestroyOnLoad 实现跨场景保持
- **提示系统**: 显示场景切换确认对话框
- **UI 重置**: 重置菜单和提示页面状态

### 2. BackgroundMusicController（背景音乐控制器）
**文件**: `BackgroundMusicController.cs`

**核心功能**:
- 监听视频播放事件
- 控制背景音乐播放/暂停
- 实现音频状态同步

**事件处理**:
```csharp
void Start()
{
    // 监听视频开始和结束事件
    videoPlayer.started += OnVideoStarted;
    videoPlayer.loopPointReached += OnVideoStopped;
}

private void OnVideoStarted(VideoPlayer source)
{
    // 视频开始播放时，暂停背景音乐
    backgroundMusic.Pause();
}

private void OnVideoStopped(VideoPlayer source)
{
    // 视频停止播放时，恢复背景音乐
    backgroundMusic.Play();
}
```

### 3. CanvasController（Canvas 控制器）
**文件**: `CanvasController.cs`

**核心功能**:
- 管理媒体显示界面
- 控制背景音乐状态
- 处理媒体播放和关闭

**音频控制**:
```csharp
public void CloseMedia()
{
    // 恢复背景音乐
    if (backgroundMusicSource != null && !backgroundMusicSource.isPlaying)
    {
        backgroundMusicSource.Play();
    }
    
    // 停止视频播放
    videoPlayer.Stop();
    videoPlayer.targetTexture.Release();
}
```

## UI 状态管理

### 菜单状态机
```
关闭状态 → OpenMenu() → 显示菜单
     ↓
显示状态 → OpenTips() → 显示提示框，隐藏菜单
     ↓
提示状态 → ChangeScene() → 重置 UI
     ↓
关闭状态 → ResetUI() → 隐藏所有 UI
```

### 音频状态同步
```
视频播放 → OnVideoStarted() → 暂停背景音乐
     ↓
视频结束 → OnVideoStopped() → 恢复背景音乐
     ↓
手动关闭 → CloseMedia() → 恢复背景音乐
```

## 关键算法

### 1. 单例模式实现
```csharp
void Awake()
{
    if (instance == null)
    {
        instance = this;
        DontDestroyOnLoad(this.gameObject);
    }
    else
    {
        Destroy(this.gameObject);
    }
}
```

### 2. 动态 UI 引用获取
```csharp
void Start()
{
    // 动态获取 UI 组件引用
    Tips_text = TipsPage.transform.GetChild(0).Find("tips_text").GetComponent<Text>();
    Define_btn = TipsPage.transform.GetChild(0).Find("define_btn").GetComponent<Button>();
    Cancel_btn = TipsPage.transform.GetChild(0).Find("cancel_btn").GetComponent<Button>();
    
    // 绑定按钮事件
    Cancel_btn.onClick.AddListener(Cancle);
    Define_btn.onClick.AddListener(ChangeScene);
}
```

### 3. 音频状态管理
```csharp
public void CloseMedia()
{
    // 检查并恢复背景音乐
    if (backgroundMusicSource != null && !backgroundMusicSource.isPlaying)
    {
        backgroundMusicSource.Play();
    }
    
    // 清理视频资源
    videoPlayer.targetTexture.Release();
}
```

## 配置指南

### 1. 菜单系统配置
1. **MenuUI**: 场景中放置一个管理器
2. **Menu**: 拖入主菜单引用
3. **TipsPage**: 拖入提示页面引用
4. **UI 结构**: 确保 UI 层级结构正确

### 2. 背景音乐配置
1. **BackgroundMusicController**: 挂载在音频控制物体上
2. **backgroundMusic**: 拖入背景音乐 AudioSource
3. **videoPlayer**: 拖入 VideoPlayer 引用

### 3. Canvas 控制器配置
1. **CanvasController**: 挂载在 Canvas 控制物体上
2. **backgroundMusicSource**: 拖入背景音乐 AudioSource
3. **videoPlayer**: 拖入 VideoPlayer 引用

## UI 交互流程

### 场景切换流程
1. **打开菜单** → 显示传送选项
2. **选择目的地** → 显示确认对话框
3. **确认传送** → 执行场景切换
4. **重置 UI** → 隐藏所有菜单

### 媒体播放流程
1. **选择物体** → 显示媒体内容
2. **播放视频** → 暂停背景音乐
3. **关闭媒体** → 恢复背景音乐

## 高级功能

### 1. 多级菜单支持
- 支持嵌套菜单结构
- 支持返回上级菜单
- 支持菜单状态记忆

### 2. 音频管理
- 支持多音轨控制
- 支持音量调节
- 支持音频淡入淡出

### 3. UI 动画
- 支持菜单动画
- 支持提示框动画
- 支持按钮动画

## 调试方法

### 1. 菜单调试
- 检查 UI 引用是否正确
- 验证事件绑定
- 监控 UI 状态变化

### 2. 音频调试
- 检查音频引用
- 验证事件触发
- 监控音频状态

### 3. 常见问题
- **菜单不显示**: 检查 UI 引用和状态
- **音频不同步**: 检查事件绑定和状态管理
- **内存泄漏**: 确保移除事件监听

## 扩展可能性

### 1. UI 框架扩展
- 支持 UI 模板系统
- 支持动态 UI 生成
- 支持 UI 主题切换

### 2. 音频系统扩展
- 支持 3D 音频
- 支持音频可视化
- 支持语音交互

### 3. 交互增强
- 支持手势 UI 控制
- 支持语音 UI 控制
- 支持眼动 UI 控制

## 相关页面

- [[gzucm-vrvideo-unity-project]] — 主项目页面
- [[gzucm-vrvideo-media-system]] — 媒体展示系统
- [[gzucm-vrvideo-teleport-system]] — 传送系统
- [[gzucm-vrvideo-interaction-system]] — 交互系统