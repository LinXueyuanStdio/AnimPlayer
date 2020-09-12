# 公主连结的精灵播放器

## 说明

1. 基于 `https://redive.estertion.win` ，爬取了所有人物的动作和骨架。
2. 解析 cysp 生成可导入 Spine 编辑器的 skel 文件
3. 目录 `ue` 下是一个用于 Android 的 skel 示例，Android 项目为 https://github.com/LinXueyuanStdio/UEdbq
4. 本项目不再维护。本项目是 `https://redive.estertion.win` 未提供 skel 导出功能时，出于 skel 文件的需要而自己构建的。现在已经 `https://redive.estertion.win` 已经有了 skel 导出功能，使用它的即可。

## 爬虫

```python3
python3 run.py
```

## 页面部署

```python
python -m SimpleHttpServer 8989
```

访问 127.0.0.1:8989
