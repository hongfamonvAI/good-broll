---
name: good-broll
description: "给视频口播、短视频脚本、分镜和旁白生成可用的 B-roll 素材提示词。输入视频文案后，提炼核心概念、视觉隐喻、素材方向和图像生成提示词。支持社媒拼贴插画风、温暖手绘插画风、卡通3D风、白板涂鸦讲解风、暖纸黑线产品草图风。关键词：B-roll、视频配图、短视频素材、口播配图、分镜提示词、文案视觉化。"
---

# Good B-roll Skill

为短视频口播脚本、旁白段落和分镜生成**可用的 B-roll 素材提示词**。

核心不是固定某个角色，而是把文案里的抽象概念变成可生成的画面：人物、道具、场景、动作、界面、隐喻和风格。

## 功能

1. **理解视频文案核心** → 提取关键概念和视觉隐喻
2. **选择视觉风格** → 社媒拼贴插画风/温暖手绘插画风/卡通3D风/白板涂鸦讲解风/暖纸黑线产品草图风
3. **设计场景** → 人物+元素+动作+背景
4. **生成提示词** → 输出可直接复制到图像生成模型的完整提示词

## 风格系统

本 skill 使用 5 种稳定风格。风格名描述画面语言，不绑定固定人物。

### 1. 社媒拼贴插画风（Editorial Collage）

适合短视频科普、AI工具讲解、效率对比、轻松教程。

- 剪纸拼贴、胶带、纸片层次
- 轻松、年轻、社媒感
- 可以有人物，也可以只用界面、道具、图标和隐喻元素
- 色彩清新，有明确视觉焦点

### 2. 温暖手绘插画风（Warm Hand-drawn Illustration）

适合温和教程、经验分享、教育型内容。

- 手绘线条、纸张质感
- 温暖、亲切、不严肃
- 适合人物、桌面、笔记、学习场景

### 3. 卡通3D风（Playful 3D Cartoon）

适合活泼、轻量、可爱、偏娱乐化的工具讲解。

- 圆润3D形体
- 明亮但柔和的色彩
- 适合角色、道具、按钮、流程模块

### 4. 白板涂鸦讲解风（Whiteboard Doodle）

适合讲逻辑、拆步骤、解释概念。

- 白板 / 笔记本背景
- 简笔人物、箭头、手写标注
- 随性、真实、像老师现场讲解

### 5. 暖纸黑线产品草图风（Warm Sketch Explainer）

适合产品概念、AI工作流、SaaS功能、抽象流程解释。

- 暖米色 / 燕麦纸张背景
- 粗黑马克笔线条，线条轻微抖动
- 白色块面、白色卡片、白色气泡承担重点信息
- 极简、克制、lo-fi SaaS explainer 感

## 使用方式

### 方式1：直接给视频文案
```
帮我给这段视频文案配图：\"今天教大家如何用AI编程工具搭建自己的工作流，不管你是工程师还是小白，都能轻松上手。\"
```

### 方式2：描述场景
```
帮我配一个插图：主题是新手学习使用AI工具，社媒拼贴插画风
```

## 默认风格：社媒拼贴插画风

**特点**：
- 扁平剪纸感（元素像剪下来的纸片）
- 轻松随性（不是严肃的企业风）
- 年轻活泼（适合短视频科普）
- 胶带拼接（纸片用胶带固定）

**画面元素**：
- 背景：米白或浅灰
- 色彩：蓝、紫、橙等清新配色
- 视觉主体：人物、界面、工具卡片、图标或视觉隐喻都可以
- 装饰：代码符号、闪电、星星、齿轮

## 🚨 重要：默认拼贴风中的人物

当使用**社媒拼贴插画风**时，人物必须是扁平剪纸风格，不能是写实/实拍风格：
- ✅ 正确：扁平剪纸风格的人物（简洁线条、轻微阴影、像纸片）
- ✅ 正确：卡通化的简洁五官（弯弯笑眼、简单表情）
- ❌ 错误：写实风格的人物
- ❌ 错误：实拍照片风格
- ❌ 错误：3D渲染的真人质感

**人物描述时必须强调**：
- 「扁平剪纸风格的人物」
- 「简洁五官（剪纸风，不是写实）」
- 「像纸片剪出来的」

## 核心设计流程

### Step 1: 理解视频文案核心概念

**问题清单**：
- 视频在讲什么？（一句话概括）
- 涉及哪些人群？（工程师/小白/用户等）
- 核心动作是什么？（学习/使用/搭建等）
- 有哪些关键元素？（工具/功能/对比等）

**概念视觉化原则**：
- 抽象概念 → 具体视觉元素
- 例如：学习 → 看屏幕/做笔记/操作界面
- 例如：对比 → 左右两个场景（before/after）

### Step 2: 确定人物和场景

**人物类型**：
| 类型 | 视觉特征 | 适用场景 |
|---|---|---|
| **工程师** | 深色T恤、眼镜、代码界面 | 专业开发者 |
| **新手用户** | 轻松、好奇、面对图形化界面 | 入门教程、工具教学 |
| **通用角色** | 根据文案决定性别、年龄、服装和职业；不要强制固定角色 | 通用场景 |
| **视觉主体** | 可是人物、白色卡片、UI模块、道具或抽象物件 | 产品讲解、流程解释、抽象概念 |

**⚠️ 重要：角色不是硬约束**
- ✅ 正确：根据文案选择人物、物件、界面或抽象视觉主体
- ✅ 正确：根据风格选择人物、物件、界面或抽象视觉主体
- ✅ 正确：用风格语言描述画面，而不是绑定固定角色
- ❌ 错误：不管文案是什么都强制出现同一个固定人物
- ❌ 错误：把某个历史案例里的角色当成全局规则

**场景元素**：
- 桌面 + 笔记本电脑
- 屏幕：代码界面 / 图形化界面
- 前景：工具卡片/功能模块
- 装饰：相关符号、功能图标

### Step 3: 设计视觉元素

**常见对比场景**（适合before/after）：
| 左侧（Before/传统） | 右侧（After/新方式） |
|---|---|
| 工程师敲复杂代码 | 新手用户拖拽界面 |
| 手动重复操作 | 自动化流程 |
| 困惑表情 | 开心表情 |

**装饰元素**：
- 代码符号：`</>{}[]`
- 功能图标：⚡闪电、✨星星、🎯齿轮
- 工具卡片：蓝色（脚本）、紫色（指令）、橙色（API）

### Step 4: 生成图像提示词

**提示词模板（社媒拼贴插画风）**：
```
搜索"collage art style illustration"、"cut paper aesthetic"、"playful layered composition"、"[场景关键词]"，

【社媒拼贴插画风】

背景是纯色（米白或浅灰），

画面是拼贴风格，元素像剪纸剪下来的：

左侧 - [场景A描述]：
- 人物剪影（扁平，有细微阴影）
- [人物特征]
- [动作描述]
- [关键元素]

右侧 - [场景B描述]：
- [人物、物件、UI模块或风格化主体]
- [服装描述]
- [动作描述]
- [关键元素]

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
- 色彩清新（蓝、紫、橙，可按需加入红色焦点）

--ar 3:4
```

## 风格选项

除默认风格外，还支持：

| 风格 | 特点 | 适合 |
|---|---|---|
| **社媒拼贴插画风（Editorial Collage）** | 剪纸感、年轻、拼贴 | 短视频科普（默认）|
| **温暖手绘插画风（Warm Hand-drawn Illustration）** | 笔触感、温暖、亲切 | 想要精致但不严肃 |
| **卡通3D风（Playful 3D Cartoon）** | 圆润可爱、动画感 | 想要活泼 |
| **白板涂鸦讲解风（Whiteboard Doodle）** | 白板讲解、手绘标注 | 想要像老师讲课那样亲切 |
| **暖纸黑线产品草图风（Warm Sketch Explainer）** | 极简产品讲解草图、粗糙黑色马克笔线条、暖纸张底 | 知性、温暖、产品感 |

详细风格模板见：`references/style_templates.md`

---

## 风格5：暖纸黑线产品草图风（Warm Sketch Explainer）

这类产品讲解视觉不是普通手绘插画，而是**编辑级产品讲解草图**（editorial explainer sketch）。

### 核心特征

| 维度 | 描述 |
|------|------|
| **本质** | Minimal hand-drawn explainer illustration, lo-fi SaaS explainer drawing style |
| **线条** | Rough black marker lines, uneven thickness, wobbly imperfect sketch lines |
| **配色** | Warm beige / oatmeal paper background with subtle grain, black ink lines, white blocks/cards/shapes as contrast accents |
| **构图** | Clear hierarchy, slight perspective, overlapping forms, generous negative space |
| **信息组织** | Hand-drawn UI window, arrows, sparse handwritten labels, product explanation feel |
| **氛围** | Intellectual but warm, restrained, editorial, approachable |

### 白色使用规则

暖纸黑线产品草图风里，白色不是零碎装饰，而是**核心构图层**。它通常承担主体、卡片、气泡、功能块、光区或说明块的角色。

- **背景层**：燕麦米色 / 奶油色，负责提供温暖底色
- **结构层**：黑色粗手绘线，负责轮廓、符号、文字和结构关系
- **焦点层**：白色主体 / 白色卡片 / 白色气泡 / 白色功能块，负责承载重点内容

使用原则：
- 白色优先用于主要信息承载物，而不是零散点点
- 白色块面要干净、简单、厚实，避免碎裂和过多纹理
- 白色通常出现在主体本身、卡片、面板、对话气泡、说明块、灯光区
- 黑色线条可以压在白色色块边缘或内部，让白色既轻又有结构
- 白色和燕麦底之间要形成清楚前后层次，不能糊成一片

不建议：
- 到处撒很多小白点
- 白色碎片过多，导致画面没有重心
- 白色面积平均铺满全画面，失去“焦点层”作用

### 构图与主次规则

暖纸黑线产品草图风虽然极简，但**不能把元素平均排开**。画面必须有主次、前后关系和视觉落点。

构图原则：
- 先决定谁是主角，主角必须最大或最有视觉重量
- 次要元素只能承担输入端、输出端、说明层，不能和主角同等大小
- 元素之间要有轻微透视关系，避免平铺 icon 排列
- 允许小范围重叠，用重叠制造前后层次
- 信息流要沿着一个明确方向成立，而不是四散解释

推荐做法：
- **主角**：通常是人物或核心动作，放在中间偏前
- **辅助输入端**：通常更小，放在前景左侧或下侧
- **辅助输出端**：通常更大但更靠后，放在右侧或后方承接信息
- **桥接/转换模块**：应该嵌在信息流中，而不是单独漂浮

禁止项：
- 三个视觉元素同等大小
- 手机、人物、电脑排排站，没有透视差
- 每个对象都完整孤立，没有重叠
- 靠大量文字箭头去解释本应由画面自己说明的关系

### 提示词模板

```
搜索"minimal hand drawn explainer illustration"、"editorial sketch"、
"rough black marker lines"、"lo-fi SaaS explainer drawing style"、
"warm beige paper background grain texture"，

【暖纸黑线产品草图风】

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

背景与质感：
- warm beige or oatmeal paper background
- subtle grain texture
- paper-like handcrafted feel

白色层：
- use white blocks, white cards, white bubbles, or simple white geometric shapes as focal accents
- white can appear in the main character, cards, UI panels, note blocks, or light areas
- keep white areas intentional and readable, not scattered decoration

信息组织：
- looks like a rough product explanation sketch
- if labels are needed: sparse handwritten Chinese keywords
- small hand-drawn arrows pointing to the core subject
- avoid dense annotations
- make the visual logic understandable without relying on labels

整体氛围：
- lo-fi SaaS explainer drawing style
- editorial, warm, restrained
- intellectual but approachable
- not cute poster, not marketing infographic

--ar 3:4
```

### 关键区分

**这是**：
- 极简产品讲解草图，不是装饰型插画
- 黑色马克笔感线条，粗细不均，带轻微抖动
- 暖米色纸张背景，带轻微颗粒
- 白色主体、白色卡片、白色气泡或白色功能块承担重点信息
- 元素有主次差异，有轻微透视和重叠
- 中心主体明确，像产品概念说明图
- 稀疏手写标注和箭头，而不是密集信息图

**这不是**：
- 干净光滑的矢量插画
- 过度可爱或儿童简笔画
- 拼贴海报风
- 高饱和营销信息图
- 写实、3D、照片质感
- 三个元素同等大小、平铺排开

### 使用偏好

- 如果用户说“暖纸黑线产品草图风”，默认理解为 `warm sketch explainer` / `editorial explainer sketch`，不是普通 `hand-drawn line art`
- 优先生成单主体、单界面、低信息密度的构图
- 中文标注只作为辅助信息，数量要少
- 默认不要橙色小点或额外斑点装饰，除非用户明确要求
- 暖纸黑线产品草图风里要主动考虑白色色块/白色卡片/白色气泡的使用，避免画面只有黑线和燕麦底
- 如果场景里有手机、人物、电脑三类元素，默认不要做成等大三件套，必须拉开主次、远近和重叠关系

### 固定参考模板：暖纸黑线产品草图风

这个模板可以作为后续复用底稿。应用到其他场景时，优先替换动作、场景、屏幕内容和中文标注，其他风格约束尽量保持不变。

```text
minimal hand-drawn explainer illustration, rough black marker lines, uneven line thickness, wobbly imperfect sketch lines

Color palette:
- background: warm oatmeal (#F5F0E8) or soft cream
- lines: black ink (#1A1A1A)
- highlights: pure white only
- supporting cards/panels/shapes: pure white when needed

Use white cards, white bubbles, white panels, or simple white geometric forms as the main information layer; keep them intentional, readable, and clearly separated from the warm paper background

[Replace here with the specific scene/action]
[Decide which element is the focal subject, which is the input source, and which is the destination]

If the scene includes cards, UI panels, notes, speech bubbles, or simple geometric supporting shapes, prefer pure white fills with black ink outlines for those elements as well

Use clear size hierarchy, slight perspective, and small overlaps between elements so the scene does not feel flat or evenly distributed

Minimal composition, generous negative space, looks like a rough product explanation sketch

Sparse handwritten Chinese annotations with small arrows:
[Replace here with the specific Chinese labels]

Warm, restrained, editorial, intelligent but slightly playful, lo-fi SaaS explainer drawing style, not polished vector, not realistic, not glossy, no orange dots, no extra decorative speckles, no busy background, no poster-like layout

--ar 3:4
```

### 固定参考模板：写代码场景示例

这是可作为暖纸黑线产品草图风下的默认示例参考。

```text
minimal hand-drawn explainer illustration, rough black marker lines, uneven line thickness, wobbly imperfect sketch lines

Color palette:
- background: warm oatmeal (#F5F0E8) or soft cream
- lines: black ink (#1A1A1A)
- highlights: pure white only
- supporting tool panels: pure white

A software builder is the clear focal subject in the center foreground, sitting at a desk writing code on a laptop. The laptop is slightly larger than the supporting elements and sits a bit behind the person, screen showing a simple hand-drawn code editor with a few lines of code, small terminal window, and a couple of minimal pure white tool panels beside it, showing the idea of constantly building tools for oneself in the coding agent era

Clear hierarchy, slight perspective, gentle overlap, generous negative space, looks like a rough product explanation sketch

Sparse handwritten Chinese annotations with small arrows:
“coding agent时代”
“时刻给自己造工具”

Warm, restrained, editorial, intelligent but slightly playful, lo-fi SaaS explainer drawing style, not polished vector, not realistic, not glossy, no orange dots, no extra decorative speckles, no busy background, no poster-like layout
```

## 实战案例

### 案例1：AI工具使用教学

**视频文案**：
"今天教大家如何用AI编程工具搭建自己的工作流，不管你是工程师还是小白，都能轻松上手。"

**视觉分析**：
- 核心概念：工作流搭建 = 连接功能模块
- 人群：工程师（代码）+ 小白（图形化界面）
- 对比：复杂代码 vs 拖拽操作

**提示词**：
```
搜索"collage art style illustration"、"cut paper aesthetic"、"playful layered composition"、"workflow automation"，

【社媒拼贴插画风】

背景是纯色（米白或浅灰），

画面是拼贴风格，元素像剪纸剪下来的：

左侧 - 工程师部分：
- 男性人物剪影（扁平，有细微阴影）
- 戴圆眼镜（黑色镜框）
- 深色T恤
- 坐在桌前，正在敲代码（手放在键盘上）
- 笔记本屏幕显示代码图案（彩色波浪线</>{}）
- 表情专注认真

右侧 - 小白部分：
- 新手用户角色，使用醒目的色彩焦点增强识别度
- 浅色卫衣（粉色或米白）
- 坐在桌前，正在拖拽功能卡片
- 面前是图形化界面（大按钮+箭头，不是代码）
- 功能卡片用虚线箭头连接（像手绘）
- 表情轻松愉快

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
- 色彩清新（蓝、紫、橙，可加入红色焦点）

--ar 3:4
```

### 案例2：Before/After对比

**视频文案**：
"以前手动复制粘贴要花1小时，现在用自动化脚本10秒搞定。"

**视觉分析**：
- 核心概念：效率提升（时间对比）
- 场景：手动操作 vs 自动化
- 情绪：疲惫 vs 轻松

**提示词**：
```
搜索"collage art style illustration"、"cut paper aesthetic"、"before after comparison"，

【社媒拼贴插画风】

背景是纯色（米白或浅灰），

画面是拼贴风格，元素像剪纸剪下来的：

左侧 - Before（手动）：
- 新手用户角色
- 浅色T恤
- 坐在桌前，疲惫地手动复制粘贴
- 屏幕上有很多文档窗口（乱糟糟）
- 旁边有计时器显示"1小时"
- 表情疲惫（额头冒汗）

右侧 - After（自动化）：
- 同一个新手用户角色，延续清晰的色彩焦点
- 浅色T恤
- 轻松地坐着，看着脚本自动运行
- 屏幕显示齿轮图标+进度条（自动化运行）
- 旁边有计时器显示"10秒"
- 表情轻松愉快（微笑）

周围装饰元素（拼贴风）：
- 闪电符号⚡（代表速度）
- 对比箭头→（从左到右）
- 星星✨

整体风格：
- 扁平、剪纸感
- 轻松、随性
- 像手工拼贴
- 年轻、活泼
- 色彩清新（蓝、紫、橙，可加入红色焦点）

--ar 3:4
```

## 工作流程

1. **用户输入视频文案**
2. **AI分析核心概念**（人群、动作、对比等）
3. **确认视觉风格**（默认拼贴风，可选其他）
4. **设计场景、主体和素材方向**（人物、物件、UI、抽象隐喻都可以）
5. **生成完整提示词**（可直接复制到图像生成模型）

## 文件结构

```
good-broll/
├── SKILL.md                      # 本文件
├── README.md                     # 开源说明与展示图
├── assets/
│   └── showcase/                 # 5种风格示例图与总览长图
├── scripts/
│   └── generate_showcase.py      # 本地生成展示图
└── references/
    └── style_templates.md        # 风格提示词模板
```
