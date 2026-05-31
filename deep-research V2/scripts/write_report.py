#!/usr/bin/env python3
"""
分段写入横纵分析报告。解决Claude Code处理长文本时的token限制问题。

用法：
  # 第一段：创建文件
  python3 write_report.py create /path/to/report.md "第一到第四部分的内容..."

  # 后续段：追加内容
  python3 write_report.py append /path/to/report.md "来源章节内容..."
  python3 write_report.py append /path/to/report.md "方法论和附录内容..."

  # 从文件追加（当内容太长无法作为参数传入时）
  python3 write_report.py append-file /path/to/report.md /tmp/segment.md

  # 验证文件状态
  python3 write_report.py verify /path/to/report.md
"""

import sys
import os

def create(path, content):
    """创建文件并写入第一段"""
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    size = os.path.getsize(path)
    chars = len(content)
    print(f"✓ 创建成功: {path}")
    print(f"  写入 {chars} 字符, 文件大小 {size} 字节")

def append(path, content):
    """追加内容到已有文件"""
    if not os.path.exists(path):
        print(f"✗ 文件不存在: {path}")
        print(f"  请先用 create 模式创建文件")
        sys.exit(1)
    with open(path, 'a', encoding='utf-8') as f:
        f.write(content)
    size = os.path.getsize(path)
    chars = len(content)
    print(f"✓ 追加成功: {path}")
    print(f"  本次追加 {chars} 字符, 文件总大小 {size} 字节")

def append_file(path, segment_path):
    """从文件追加内容"""
    if not os.path.exists(path):
        print(f"✗ 目标文件不存在: {path}")
        sys.exit(1)
    if not os.path.exists(segment_path):
        print(f"✗ 段文件不存在: {segment_path}")
        sys.exit(1)
    with open(segment_path, 'r', encoding='utf-8') as f:
        content = f.read()
    with open(path, 'a', encoding='utf-8') as f:
        f.write(content)
    size = os.path.getsize(path)
    chars = len(content)
    print(f"✓ 从文件追加成功: {segment_path} → {path}")
    print(f"  本次追加 {chars} 字符, 文件总大小 {size} 字节")

def verify(path):
    """验证文件状态和内容质量"""
    if not os.path.exists(path):
        print(f"✗ 文件不存在: {path}")
        sys.exit(1)
    size = os.path.getsize(path)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    chars = len(content)
    lines = content.count('\n') + 1

    # 检查章节完整性（原有）
    sections = {
        '一句话定义': '## 一、' in content,
        '纵向分析': '## 二、' in content,
        '横向分析': '## 三、' in content,
        '横纵交汇': '## 四、' in content,
        '信息来源': '## 五、' in content,
        '方法论说明': '## 六、' in content,
    }

    # --- 新增检查 (Patch 13) ---

    errors = {
        'missing': [],
        'empty': [],
        'placeholder': [],
        'truncated': [],
    }

    # REQUIRED_SECTIONS: 检查新增必要章节是否存在
    required_sections = ['Core Findings', 'Scope and Boundaries', 'Research Date']
    for sec in required_sections:
        if sec not in content:
            errors['missing'].append(sec)

    # EMPTY_SECTION: 检测标题存在但内容为空的章节
    import re
    # 匹配 markdown 标题行，检查其后到下一个标题之间是否有实质内容
    heading_pattern = re.compile(r'^(#{1,4})\s+(.+)$', re.MULTILINE)
    headings = list(heading_pattern.finditer(content))
    for i, match in enumerate(headings):
        heading_text = match.group(2).strip()
        start = match.end()
        if i + 1 < len(headings):
            end = headings[i + 1].start()
        else:
            end = len(content)
        section_body = content[start:end].strip()
        # 去掉纯空白/换行后检查是否为空
        body_no_whitespace = section_body.replace('\n', '').replace('\r', '').replace(' ', '')
        if len(body_no_whitespace) < 10:  # 少于10个非空白字符视为空
            errors['empty'].append(heading_text)

    # PLACEHOLDER_CONTENT: 检测占位符
    placeholders = ['...', 'TODO', 'TBD', '待补', '待完善', '[待补]', '[TODO]']
    placeholder_pattern = re.compile(r'^(.*(?:' + '|'.join(re.escape(p) for p in placeholders) + r').*)$', re.MULTILINE)
    placeholder_matches = placeholder_pattern.findall(content)
    for m in placeholder_matches:
        # 找到占位符所在的章节
        pos = content.find(m)
        section_name = '(unknown section)'
        for h_match in headings:
            if h_match.start() < pos:
                section_name = h_match.group(2).strip()
        errors['placeholder'].append(f"{section_name}: \"{m.strip()[:60]}\"")

    # TRUNCATED_CONTENT: 检测截断
    # 1. 异常结尾（最后50字符不是正常结束标点或空白）
    tail = content[-50:].strip() if len(content) > 50 else content.strip()
    if tail and not re.search(r'[.!。！\)\]」』#*>\-]$', tail):
        # 允许以 markdown 标记结尾
        if not tail.endswith('```') and not tail.endswith('---'):
            errors['truncated'].append('File ends abruptly (no proper termination)')

    # 2. 未闭合代码块
    code_block_count = content.count('```')
    if code_block_count % 2 != 0:
        errors['truncated'].append(f'Unclosed code block ({code_block_count} occurrences of ```)')

    # 3. 未闭合列表（文件最后是一个列表项但没有后续内容）
    last_lines = content.strip().split('\n')[-3:]
    for line in last_lines:
        stripped = line.strip()
        if stripped.startswith('- ') or stripped.startswith('* ') or re.match(r'^\d+\.\s', stripped):
            # 列表项内容很短可能被截断
            if len(stripped) < 20:
                errors['truncated'].append(f'Possibly truncated list item: "{stripped[:60]}"')

    # --- 输出结果 ---
    print(f"文件状态: {path}")
    print(f"  大小: {size} 字节 | 字符: {chars} | 行数: {lines}")
    print(f"  章节完整性:")
    for name, exists in sections.items():
        mark = "✓" if exists else "✗"
        print(f"    {mark} {name}")

    all_complete = all(sections.values())
    has_errors = any(errors.values())

    if all_complete and not has_errors:
        print(f"  → 所有章节完整，内容检查通过")
    else:
        if not all_complete:
            missing_sections = [k for k, v in sections.items() if not v]
            print(f"  → 缺失章节: {', '.join(missing_sections)}")

    if has_errors:
        print()
        print("VERIFY FAILED")
        print()
        if errors['missing']:
            print("Missing:")
            for m in errors['missing']:
                print(f"  - {m}")
        if errors['placeholder']:
            print("Placeholder:")
            for p in errors['placeholder']:
                print(f"  - {p}")
        if errors['empty']:
            print("Empty:")
            for e in errors['empty']:
                print(f"  - {e}")
        if errors['truncated']:
            print("Truncated:")
            for t in errors['truncated']:
                print(f"  - {t}")
        sys.exit(1)
    else:
        print("  → VERIFY PASSED")

def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    
    mode = sys.argv[1]
    path = sys.argv[2]
    
    if mode == 'create':
        if len(sys.argv) < 4:
            print("用法: write_report.py create <path> <content>")
            sys.exit(1)
        create(path, sys.argv[3])
    elif mode == 'append':
        if len(sys.argv) < 4:
            print("用法: write_report.py append <path> <content>")
            sys.exit(1)
        append(path, sys.argv[3])
    elif mode == 'append-file':
        if len(sys.argv) < 4:
            print("用法: write_report.py append-file <path> <segment_path>")
            sys.exit(1)
        append_file(path, sys.argv[3])
    elif mode == 'verify':
        verify(path)
    else:
        print(f"未知模式: {mode}")
        print("支持的模式: create, append, append-file, verify")
        sys.exit(1)

if __name__ == '__main__':
    main()
