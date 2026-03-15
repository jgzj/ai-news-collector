#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""归档今日新闻到历史档案"""
import json, os
from datetime import datetime
from pathlib import Path

def archive_news():
    base_dir = Path(__file__).parent.parent
    latest_path = base_dir / 'data' / 'latest.json'
    archive_dir = base_dir / 'data' / 'archive'
    archive_dir.mkdir(exist_ok=True)
    if not latest_path.exists():
        print("❌ 未找到最新新闻文件")
        return
    with open(latest_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    today = datetime.now().strftime('%Y-%m-%d')
    archive_path = archive_dir / f'{today}.json'
    archive_data = {'archived_at': datetime.now().isoformat(), 'date': today, 'count': data.get('count', 0), 'articles': data.get('articles', [])}
    with open(archive_path, 'w', encoding='utf-8') as f:
        json.dump(archive_data, f, ensure_ascii=False, indent=2)
    print(f"✅ 已归档 {archive_data['count']} 条新闻到 {archive_path.name}")

if __name__ == '__main__':
    archive_news()
