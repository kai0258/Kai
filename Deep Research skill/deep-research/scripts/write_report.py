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
    """验证文件状态"""
    if not os.path.exists(path):
        print(f"✗ 文件不存在: {path}")
        sys.exit(1)
    size = os.path.getsize(path)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    chars = len(content)
    lines = content.count('\n') + 1
    
    # 检查章节完整性
    sections = {
        '一句话定义': '## 一、' in content,
        '纵向分析': '## 二、' in content,
        '横向分析': '## 三、' in content,
        '横纵交汇': '## 四、' in content,
        '信息来源': '## 五、' in content,
        '方法论说明': '## 六、' in content,
    }
    
    print(f"文件状态: {path}")
    print(f"  大小: {size} 字节 | 字符: {chars} | 行数: {lines}")
    print(f"  章节完整性:")
    for name, exists in sections.items():
        mark = "✓" if exists else "✗"
        print(f"    {mark} {name}")
    
    all_complete = all(sections.values())
    if all_complete:
        print(f"  → 所有章节完整")
    else:
        missing = [k for k, v in sections.items() if not v]
        print(f"  → 缺失章节: {', '.join(missing)}")

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
