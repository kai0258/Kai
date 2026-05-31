# Source Quality Audit Methodology

## 事后审查方法（Batch Report Audit）

When auditing existing reports for source quality violations, check TWO areas:

### 1. 来源章节（五、信息来源）

Scan for banned source names. Run regex against the sources section for:
- [用户自定义的受控媒体名单，如：RT、塔斯社、朝中社等]
- [对应的域名列表]

### 2. 正文行内引用（据XXX报道/记载/研究）

This is where most violations hide. Scan all "据XXX" patterns and classify:

#### 真正违规（直接引用宣传机构当信源）

```
✗ 据[受控媒体A]记载...
✗ 据[受控媒体B]报道...
✗ 据[受控机构C]的研究论文...（机构名，缺论文标题/作者/期刊）
提示：将本地受控媒体和机构代入上述模式进行检测
```

#### 可接受（历史事实提及，不是把宣传机构当信源）

```
✓ 1978年5月11日，某报刊发表了一篇文章...（历史事件描述）
✓ 据Wikipedia - XXX词条记载，某年某月某日某媒体发表社论...（历史事件，来源是Wikipedia）
✓ 据Foreign Policy报道...（英文媒体）
✓ 据FRUS（美国外交档案）...（非受控来源的官方档案）
```

**判断标准**：如果宣传机构名出现在"据...记载"的主语位置 = 违规。如果出现在历史事件描述的宾语位置 = 可接受。

---

## 常见问题模式（按严重程度排序）

### 🔴 硬否决级别

1. **Wikipedia 当主信源**
   - 特征：正文大量出现"据Wikipedia记载""据Wikipedia - XXX词条"
   - 判断：>5处Wikipedia引用 = 严重依赖，需重写
   - Wikipedia可用于事实核查，但不能作为叙事的主要来源

2. **宣传机构当信源**
   - 特征："据[受控媒体A]""据[受控媒体B]"
   - 注意：某些学术或研究机构可能也受政权控制，需根据具体情况判断

### 🟡 需补全出处

3. **平台引用代替原始来源**
   - 特征："据华艺线上图书馆""据知网/CNKI""据爱思想网站"
   - 问题：这些是文献平台，不是学术来源。必须追溯到原始论文的：作者、期刊名、年份、DOI
   - 修正："据华艺线上图书馆收录的《XXX》" → "据XXX（作者名）在《期刊名》（年份）上的研究"

4. **模糊引用**
   - 特征："据历史学家""据多位学者""据研究""据媒体"
   - 问题：没有具体人名/期刊，无法验证
   - 修正：给出具名学者、期刊名、年份

5. **Wikipedia 作为辅助来源**
   - 特征：2-5处Wikipedia引用，其他来源正常
   - 修正：找到Wikipedia引用的原始来源（Wikipedia条目底部的参考文献），直接引用原始来源

### 🟢 可接受但应标注

6. **官方档案/官方网站**
   - "据英国议会官方网站"、"据美国国务院档案(FRUS)" = 可接受
   - 最好给具体页面URL

7. **具名学者但缺期刊**
   - "据[学者名]的研究" — 有学者名但缺期刊/年份
   - 修正：补全为"据[学者名]在《[期刊名]》（年份）中的研究"

---

## 审查脚本模板

```python
import os, re

def audit_citations(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "## 五、信息来源" in content:
        main = content.split("## 五、信息来源")[0]
    else:
        main = content
    
    lines = main.split('\n')
    issues = []
    
    banned = ['[用户自定义受控媒体名单]']  # 示例: ['RT', 'TASS', 'KCNA']
    platforms = ['华艺线上图书馆', '华艺', '知网', 'CNKI', '爱思想', '百度', '知乎']
    vague = ['据历史学家', '据多位学者', '据研究', '据媒体', '据记载']
    
    for i, line in enumerate(lines):
        for name in banned:
            if f'据' in line and name in line[:line.find(name)+10]:
                issues.append(('BANNED', i+1, name, line.strip()[:80]))
        for p in platforms:
            if p in line and '据' in line:
                issues.append(('PLATFORM', i+1, p, line.strip()[:80]))
        for v in vague:
            if v in line:
                issues.append(('VAGUE', i+1, v, line.strip()[:80]))
    
    return issues
```

---

## "历史提及" vs "信源引用" 判断规则

| 判断 | 模式 | 示例 |
|------|------|------|
| ✗ 违规 | 据[受控媒体] + 记载/研究/报道 | 据某受控媒体理论版记载 |
| ✗ 违规 | 据[模糊来源] + 记载/研究 | 据多位学者的研究 |
| ✓ 可接受 | [受控媒体] + 发表/刊登/出版（历史事实） | 某年某媒体发表了... |
| ✓ 可接受 | 据[非受控来源] + 记载 | 据Foreign Policy报道 |
| ✓ 可接受 | 据[具名学者] + 在[期刊] + 研究 | 据[学者名]在《[期刊名]》的研究 |
| ? 待确认 | 据[机构名] + 研究（缺论文标题） | 据某研究院的研究论文 |
| ✓ 可接受 | [排除声明中提到受控媒体] | 本报告排除了XX、YY、ZZ等... |
