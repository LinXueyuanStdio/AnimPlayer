# 公主连结的精灵播放器

## 说明

1. 基于 `https://redive.estertion.win` ，爬取了所有人物的动作和骨架。
2. 解析 cysp 生成可导入 Spine 编辑器的 skel 文件
3. 使用 vue 美化原有页面，重新部署

## 爬虫

```python3
python3 run.py
```

## 页面部署

``` bash
npm install
npm run dev
npm run build
```