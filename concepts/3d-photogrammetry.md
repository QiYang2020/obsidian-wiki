---
title: 3D Photogrammetry
created: 2026-04-11
updated: 2026-04-11
type: concept
tags: [3D, Photogrammetry, Gaussian Splatting, PLY, SPZ, Oblique Photography, Unity]
sources:
  - /home/admin/wiki/_staging/4ed1b5af-356f-439b-a6fe-6347b2df3ebb-20230621-14-bd58e437bbf7.md
  - /home/admin/wiki/_staging/9e5c3461-a4aa-4494-be87-333fd4221f60-20240313-14-bb0db050f6cd.md
  - /home/admin/wiki/_staging/ply-spz-692d34cc-e798-8322-b916-4a196557a7b2-202-9e8eac025a35.md
---

# 3D Photogrammetry

3D 摄影测量与高斯溅射（Gaussian Splatting）相关的数据采集、格式转换与实时应用。

## 倾斜摄影（Oblique Photography）

倾斜摄影数据采集与输出：

- 使用多角度相机采集建筑物/场景的倾斜影像
- 常见输出格式：OSGB、OBJ、PLY
- Pix4D 等软件支持处理倾斜摄影数据
- 需查阅具体软件文档确认 OSGB 输出能力

## 转换 PLY 为 SPZ

将高斯溅射的 PLY 格式转换为 SPZ 格式（用于 Web/移动端渲染）：

**使用 gsbox 工具（Windows）：**

```powershell
gsbox p2z -i "D:\input.ply" -o "D:\output.spz" -ov 3
```

**常见问题：**
- `无法将"gsbox"项识别为 cmdlet` — 找不到可执行文件

**解决方法：**

方法 1：使用完整路径
```powershell
"C:\tools\gsbox\gsbox.exe" p2z -i "D:\input.ply" -o "D:\output.spz" -ov 3
```

方法 2：将 gsbox.exe 目录加入系统 PATH
- 找到 gsbox.exe 所在目录
- 系统属性 → 环境变量 → Path → 添加路径
- 重新打开终端即可直接使用 `gsbox` 命令

有空格的路径必须加引号。

## 照片墙应用实时更新

Unity 制作的照片墙应用，支持实时展示用户上传的作品：

**核心功能：**
- 检测用户上传成功后自动更新照片墙
- 支持检索上传者作品
- 支持按条件检索作品

**技术实现：**
- Unity 客户端实时轮询或 WebSocket 推送
- 后端 API 提供作品上传与查询接口
- 动态加载与卸载纹理资源

## 相关页面

- [[ai-image-generation]] — AI 图像生成与风格化
- [[webgl-development]] — WebGL 3D 渲染与展示
- [[ue5-development]] — UE5 中的 3D 资产导入
