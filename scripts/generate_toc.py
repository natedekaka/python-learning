#!/usr/bin/env python3
import os
import re
import json
from datetime import datetime
from pathlib import Path

def extract_title(html_content):
    title_match = re.search(r'<title>(.*?)</title>', html_content, re.IGNORECASE)
    if title_match:
        return title_match.group(1).strip()
    
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', html_content, re.IGNORECASE | re.DOTALL)
    if h1_match:
        text = re.sub(r'<[^>]+>', '', h1_match.group(1))
        return text.strip()
    
    return "Untitled"

def extract_headings(html_content):
    headings = []
    pattern = r'<h([123])([^>]*)>(.*?)</h\1>'
    
    for match in re.finditer(pattern, html_content, re.IGNORECASE | re.DOTALL):
        level = int(match.group(1))
        attrs = match.group(2)
        text = re.sub(r'<[^>]+>', '', match.group(3)).strip()
        
        id_match = re.search(r'id=["\']([^"\']+)["\']', attrs)
        heading_id = id_match.group(1) if id_match else None
        
        headings.append({
            'level': level,
            'text': text,
            'id': heading_id
        })
    
    return headings

def count_words(html_content):
    clean = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', html_content, flags=re.IGNORECASE | re.DOTALL)
    clean = re.sub(r'<[^>]+>', ' ', clean)
    return len(clean.split())

def estimate_reading_time(word_count, wpm=200):
    return max(1, round(word_count / wpm))

def scan_modules(modules_dir):
    modules = []
    
    if not os.path.exists(modules_dir):
        return modules
    
    for filepath in sorted(Path(modules_dir).glob('*.html')):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        modules.append({
            'file': f"modules/{filepath.name}",
            'title': extract_title(content),
            'headings': extract_headings(content),
            'word_count': count_words(content),
            'reading_time_min': estimate_reading_time(count_words(content))
        })
    
    return modules

def generate_json(modules, output_file):
    data = {
        'generated_at': datetime.now().isoformat(),
        'modules': modules
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def generate_markdown(modules, output_file):
    lines = [
        "# Python Learning - Table of Contents",
        "",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Modules",
        ""
    ]
    
    total_words = 0
    total_time = 0
    
    for mod in modules:
        lines.append(f"### [{mod['title']}]({mod['file']})")
        lines.append(f"- **Words:** {mod['word_count']:,}")
        lines.append(f"- **Reading time:** {mod['reading_time_min']} min")
        lines.append("")
        
        if mod['headings']:
            lines.append("**Contents:**")
            for h in mod['headings']:
                indent = "  " * (h['level'] - 1)
                link = f"#{h['id']}" if h['id'] else ""
                lines.append(f"{indent}- [{h['text']}]({mod['file']}{link})")
            lines.append("")
        
        total_words += mod['word_count']
        total_time += mod['reading_time_min']
    
    lines.append("---")
    lines.append(f"**Total:** {len(modules)} modules, {total_words:,} words, ~{total_time} min reading")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

def main():
    base_dir = Path(__file__).parent.parent
    modules_dir = base_dir / 'modules'
    
    modules = scan_modules(modules_dir)
    
    if not modules:
        return
    
    generate_json(modules, base_dir / 'toc.json')
    generate_markdown(modules, base_dir / 'toc.md')

if __name__ == '__main__':
    main()
