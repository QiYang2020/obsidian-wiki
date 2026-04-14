#!/usr/bin/env python3
"""
清理知识库用于公开展示
- 移除大型项目文件
- 保留完整文档结构
- 添加展示性README
"""

import os
import shutil
import glob

def clean_for_public():
    """清理知识库用于公开展示"""
    print("🧹 开始清理知识库...")
    
    # 1. 移除raw目录下的项目文件
    raw_dir = "raw"
    if os.path.exists(raw_dir):
        print(f"📁 清理 {raw_dir} 目录...")
        # 保留目录结构，但清空内容
        for item in os.listdir(raw_dir):
            item_path = os.path.join(raw_dir, item)
            try:
                if os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                    print(f"  ✅ 移除目录: {item}")
                else:
                    os.remove(item_path)
                    print(f"  ✅ 移除文件: {item}")
            except (OSError, PermissionError) as e:
                print(f"  ⚠️  无法移除 {item}: {e}")
    
    # 2. 移除大文件（>100KB的非文档文件）
    print("📄 清理大文件...")
    large_files_removed = 0
    for root, dirs, files in os.walk("."):
        # 跳过.git目录
        if '.git' in root:
            continue
            
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_size = os.path.getsize(file_path)
                # 移除大于100KB的非文档文件
                if file_size > 100*1024 and not file.endswith('.md'):
                    os.remove(file_path)
                    large_files_removed += 1
                    if large_files_removed <= 10:  # 只显示前10个
                        print(f"  ✅ 移除大文件: {file_path} ({file_size/1024:.1f}KB)")
            except (OSError, FileNotFoundError):
                continue
    
    print(f"  📊 共移除 {large_files_removed} 个大文件")
    
    # 3. 移除IDE和临时文件
    print("🗑️  清理IDE和临时文件...")
    ide_patterns = [
        '.vs/', '.vscode/', '.idea/', '*.csproj', '*.sln', '*.user',
        '*.pidb', '*.booproj', '*.svd', '*.pdb', '*.opendb', '*.VC.db',
        'Library/', 'Temp/', 'Obj/', 'Build/', 'Logs/', 'UserSettings/',
        'MemoryCaptures/', 'Binaries/', 'Intermediate/', 'Saved/',
        'DerivedDataCache/', '*.unitypackage', '*.tmp', '*.temp', '*.log',
        '*.cache', '.DS_Store', 'Thumbs.db', 'desktop.ini'
    ]
    
    ide_files_removed = 0
    for pattern in ide_patterns:
        for item in glob.glob(pattern, recursive=True):
            try:
                if os.path.isdir(item):
                    shutil.rmtree(item)
                else:
                    os.remove(item)
                ide_files_removed += 1
                if ide_files_removed <= 10:  # 只显示前10个
                    print(f"  ✅ 移除: {item}")
            except (OSError, FileNotFoundError):
                continue
    
    print(f"  📊 共移除 {ide_files_removed} 个IDE/临时文件")
    
    # 4. 更新.gitignore
    print("📝 更新 .gitignore...")
    update_gitignore()
    
    # 5. 创建公开版本的README
    print("📖 创建公开版本README...")
    create_public_readme()
    
    # 6. 统计清理结果
    print("📊 清理完成统计...")
    print_results()
    
    print("✅ 知识库已清理为公开版本！")

def update_gitignore():
    """更新.gitignore"""
    gitignore_content = """# 项目文件
*.uasset
*.umap
*.unity
*.prefab
*.asset
*.mat
*.shader
*.fbx
*.obj
*.png
*.jpg
*.tga
*.wav
*.mp3
*.mp4
*.mov
*.zip
*.rar
*.7z
*.exe
*.dll
*.so
*.dylib
*.unitypackage

# IDE文件
.vs/
.vscode/
.idea/
*.csproj
*.sln
*.user
*.pidb
*.booproj
*.svd
*.pdb
*.opendb
*.VC.db

# Unity文件
Library/
Temp/
Obj/
Build/
Logs/
UserSettings/
MemoryCaptures/

# UE5文件
Binaries/
Intermediate/
Saved/
DerivedDataCache/

# 大型资源文件
raw/assets/

# 临时文件
*.tmp
*.temp
*.log
*.cache

# 系统文件
.DS_Store
Thumbs.db
desktop.ini
"""
    
    with open(".gitignore", "w", encoding="utf-8") as f:
        f.write(gitignore_content)

def create_public_readme():
    """创建公开版本的README"""
    readme_content = """# 个人知识库

这是一个持续更新的个人技术知识库，包含多个技术领域的深度分析和项目经验。

## 📚 内容结构

### 核心概念
- **UE5 开发** - 全景相机渲染系统、画框管理、序列自动化
- **Unity 开发** - MR交互系统、VR视频播放、手势识别
- **XR/VR/AR** - 混合现实开发、交互设计、空间计算
- **AI/ML** - 图像生成、3D重建、深度学习

### 项目经验
1. **PanoRendering (UE5)** - 全景相机渲染系统
2. **MR Workshop (Unity)** - MR交互系统，手势识别、区域触发
3. **GZUCM_VRVideo (Unity)** - VR视频播放系统，媒体展示、传送

## 🎯 技术亮点

### 架构设计
- 模块化系统设计
- 数据驱动配置
- 事件解耦通信
- 跨平台支持

### 交互设计
- 手势识别与抓取
- 区域触发系统
- 媒体播放控制
- 传送与导航

## 📖 使用说明

1. **浏览文档** - 查看 `concepts/` 和 `entities/` 目录
2. **项目分析** - 每个项目都有详细的技术分析
3. **交叉引用** - 页面之间相互链接，形成完整知识网络

## 🔗 相关链接

- [Obsidian](https://obsidian.md/) - 推荐的文档浏览工具
- [Unity XR Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@2.0/manual/index.html)
- [Unreal Engine Documentation](https://docs.unrealengine.com/)

## 📝 更新日志

详见 `log.md` 文件。

## 📊 知识库统计

- **页面总数**: 187
- **概念页面**: 27
- **实体页面**: 7
- **对比页面**: 1
- **技术领域**: UE5、Unity、XR/VR/AR、AI/ML

## 🎨 特色功能

### 交叉引用系统
所有页面都通过 `[[wikilinks]]` 相互链接，形成完整的知识网络。

### 数据驱动
使用 JSON 配置文件管理项目数据，支持运行时加载。

### 跨平台支持
文档支持多种浏览工具，包括 Obsidian、Typora 等。

---

*最后更新: 2026-04-14*
"""
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

def print_results():
    """打印清理结果"""
    # 统计文件数量
    total_files = 0
    md_files = 0
    other_files = 0
    
    for root, dirs, files in os.walk("."):
        if '.git' in root:
            continue
        for file in files:
            total_files += 1
            if file.endswith('.md'):
                md_files += 1
            else:
                other_files += 1
    
    # 统计目录大小
    total_size = 0
    for root, dirs, files in os.walk("."):
        if '.git' in root:
            continue
        for file in files:
            try:
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)
            except (OSError, FileNotFoundError):
                continue
    
    print(f"  📊 清理结果:")
    print(f"    - 总文件数: {total_files}")
    print(f"    - Markdown文件: {md_files}")
    print(f"    - 其他文件: {other_files}")
    print(f"    - 总大小: {total_size/1024/1024:.1f} MB")

if __name__ == "__main__":
    clean_for_public()