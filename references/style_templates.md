# Good B-roll 风格提示词模板

本文档包含5种常用 B-roll 素材提示词模板，适用于常见图像生成模型。

## 风格列表

- 社媒拼贴插画风（Editorial Collage）
- 温暖手绘插画风（Warm Hand-drawn Illustration）
- 卡通3D风（Playful 3D Cartoon）
- 白板涂鸦讲解风（Whiteboard Doodle）
- 暖纸黑线产品草图风（Warm Sketch Explainer）

---

## 1. 社媒拼贴插画风（默认）

**特点**：剪纸感、年轻、拼贴、适合短视频科普

**完整提示词**：
```
搜索"collage art style illustration"、"cut paper aesthetic"、"playful layered composition"、"[场景关键词]"，

【社媒拼贴插画风】

背景是纯色（米白或浅灰），

画面是拼贴风格，元素像剪纸剪下来的：

左侧 - [场景A描述]：
- 人物剪影（扁平，有细微阴影）
- 简约造型（不画细节，只抓特征）
- [人物特征描述]
- [动作描述]
- [关键元素描述]

右侧 - [场景B描述]：
- 人物剪影
- [人物特征描述]
- [动作描述]
- [关键元素描述]

周围装饰元素（拼贴风）：
- 代码符号剪纸（</>{}[]）
- 小闪电⚡
- 星星✨
- 齿轮🎯

整体风格：
- 扁平、剪纸感
- 轻松、随性
- 像手工拼贴
- 年轻、活泼
- 色彩清新（蓝、紫、橙、[自定义颜色]）

--ar 3:4
```

---

## 2. 温暖手绘插画风

**特点**：笔触感、温暖、亲切、精致但不严肃

**完整提示词**：
```
搜索"warm hand drawn illustration"、"friendly sketchy art style"、"soft educational illustration"、"[场景关键词]"，

【温暖手绘插画风】

背景是米白色纸张质感（有细微纸纹），

画面是手绘风格的双人物场景：

左侧 - [场景A描述]：
- 手绘风格的男性角色，线条有笔触感
- [人物特征]
- 穿[服装描述]
- [动作描述]
- [关键元素]

右侧 - [场景B描述]：
- 手绘风格女性角色
- [人物特征]
- 穿[服装描述]
- [动作描述]
- [关键元素]

中间 - 悬浮的手绘标题框：
- "[核心概念标题]"
- 字体手写风格（像Marker笔）

整体风格：
- 有笔触、不完美的线条（像真实手绘）
- 温暖的色彩（米白、柔和蓝、粉、橙）
- 轻松、有人情味
- 像白板讲解

--ar 3:4
```

---

## 3. 卡通3D风

**特点**：圆润可爱、动画感、轻量活泼

**完整提示词**：
```
搜索"cute 3D cartoon style"、"playful 3D illustration"、"adorable 3D mascot"、"[场景关键词]"，

【卡通3D风】

背景是柔和的渐变色（浅蓝到浅粉），

画面是可爱卡通3D风格：

左侧 - [场景A描述]：
- 可爱的3D卡通人偶（圆润造型，像玩具）
- [人物特征]
- 穿[服装描述]
- 坐在圆角桌子前（光滑塑料质感）
- 笔记本是圆角3D模型（屏幕发光）
- [关键元素]

右侧 - [场景B描述]：
- 可爱3D卡通[人物描述]
- 穿[服装描述]
- [动作描述]
- [关键元素]

整体风格：
- 圆润、可爱、像动画片
- 色彩明亮但柔和
- 材质丰富（塑料、布料、发光）
- 有趣、活泼

--ar 3:4
```

---

## 4. 白板涂鸦讲解风

**特点**：白板讲解、最随意、像老师讲课

**完整提示词**：
```
搜索"whiteboard sketch illustration"、"doodle art style explainer"、"hand drawn notebook style"、"[场景关键词]"，

【涂鸦风，像白板讲解/手绘笔记】

背景像白板或笔记本纸（浅绿或米白，有网格线），

画面是涂鸦风格，像老师在白板上画出来：

左侧 - [场景A描述]：
- 简笔人物画（几笔画出轮廓）
- [人物特征]
- [服装描述]
- [动作描述]
- [关键元素]

右侧 - [场景B描述]：
- 简笔[人物描述]
- [人物特征]
- [服装描述]
- [动作描述]
- [关键元素]

中间有手写标注：
- "[核心概念说明]"
- 用荧光笔高亮（黄色半透明）

整体风格：
- 随性、真实
- 像白板讲解
- 线条不完美
- 亲切、易懂

--ar 3:4
```

---

## 5. 暖纸黑线产品草图风

**特点**：暖纸张、粗黑马克笔线条、极简、产品讲解草图

**完整提示词**：
```
搜索"minimal hand drawn explainer illustration"、"editorial sketch"、"rough black marker lines"、"lo-fi SaaS explainer drawing style"、"warm beige paper background grain texture"，

【暖纸黑线产品草图风】

背景是暖米色或燕麦色纸张，有轻微颗粒质感，

画面是极简产品讲解草图：

主体要求：
- [核心主体或场景]
- clear focal subject
- hierarchy with foreground and background
- slight perspective and overlap
- minimal composition
- generous negative space

线条要求：
- rough black marker lines
- uneven thickness
- wobbly imperfect sketch lines
- hand-drawn, not polished vector

白色信息层：
- white blocks, white cards, white bubbles, or simple white geometric shapes as focal accents
- white cards can represent UI panels, notes, speech bubbles, outputs, or light areas
- keep white areas intentional and readable

信息组织：
- looks like a rough product explanation sketch
- small hand-drawn arrows pointing to the core subject
- sparse handwritten labels only if needed
- avoid dense annotations

整体氛围：
- warm, restrained, editorial
- intelligent but approachable
- lo-fi SaaS explainer drawing style
- not realistic, not glossy, not polished vector

--ar 3:4
```

---

## 使用指南

### 如何选择风格？

| 你的需求 | 推荐风格 |
|---|---|
| 短视频科普、年轻观众 | **社媒拼贴插画风**（默认）|
| 想要精致但不严肃 | **温暖手绘插画风**|
| 想要活泼可爱 | **卡通3D风**|
| 想要像老师讲课那样亲切 | **白板涂鸦讲解风**|
| 产品概念、AI工作流、SaaS功能 | **暖纸黑线产品草图风**|

### 如何自定义？

1. **替换场景关键词**：把`[场景关键词]`换成你的具体场景
2. **替换人物描述**：把`[人物特征]`、`[服装描述]`具体化
   - **工程师：深色T恤、眼镜**
3. **替换关键元素**：把`[关键元素]`换成你的核心概念视觉化
4. **替换颜色**：在配色部分调整具体颜色

### 实战示例

见主文件 `SKILL.md` 中的"实战案例"部分。
