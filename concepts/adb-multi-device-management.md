---
title: ADB 多设备管理
created: 2026-04-11
updated: 2026-04-11
type: concept
tags: [tool, android, xr]
sources:
  - raw/inbox/chatgpt_personal_backup_2026-04-10_md/ADB设备选择问题_6964c79b-7548-8330-b6c2-7414b6c729e9_20260112_180637.md
---

# ADB 多设备管理

当电脑同时连接多个 Android 设备或模拟器时，`adb` 命令会因无法确定目标设备而报错：`more than one device/emulator`。

## 问题根源

在 MR/XR 开发中特别常见，原因包括：
- Android Studio 留下的 offline 模拟器残留
- 同时连接 Quest、Pico、手机等多台设备
- Unity / Android Build Support 安装后自带模拟器组件

即使设备处于 offline 状态，它们仍会出现在 `adb devices` 列表中，导致 adb 失去目标。

## 核心解决方案：`adb -s`

使用 `-s` 参数指定设备序列号：

```powershell
adb devices                    # 先查看设备列表和序列号
adb -s PA7L10MGG6040110W install PicoPlayTest.apk       # 指定设备安装
adb -s PA7L10MGG6040110W install -r PicoPlayTest.apk    # 覆盖安装
```

## 清理离线模拟器

offline 的模拟器会干扰设备选择，可用以下方式清除：

```powershell
adb kill-server                # 杀掉 adb 服务
adb start-server               # 重启
adb devices                    # 确认列表
```

如果仍存在残留设备：
```powershell
adb disconnect                 # 强制断开所有网络连接的设备
adb devices
```

## 多设备工作流建议

当需要同时管理 Quest + Pico + 手机时，可以建立固定设备别名脚本（如 `adb pico install xxx.apk`），适合高频多设备切换场景。

## 相关概念

- [[cuda-toolkit-安装与路径管理]] — 同为开发环境路径与工具配置类问题
