#!/usr/bin/env python3
"""
《電馭寫作》專案建立腳本
自動複製模板並建立新的寫作專案
"""

import os
import shutil
import sys
from datetime import datetime
import argparse

def create_project(project_name, topic, target_audience="一般讀者", word_count="1000-3000字"):
    """
    建立新的寫作專案
    
    Args:
        project_name (str): 專案名稱
        topic (str): 文章主題
        target_audience (str): 目標讀者群體
        word_count (str): 預期字數範圍
    """
    
    # 確保專案名稱是有效的資料夾名稱
    safe_project_name = "".join(c for c in project_name if c.isalnum() or c in (' ', '-', '_')).rstrip()
    safe_project_name = safe_project_name.replace(' ', '-')
    
    # 設定路徑
    template_path = "templates/project-template"
    projects_dir = "projects"
    project_path = os.path.join(projects_dir, safe_project_name)
    
    # 檢查模板是否存在
    if not os.path.exists(template_path):
        print(f"錯誤：找不到模板資料夾 {template_path}")
        return False
    
    # 檢查專案是否已存在
    if os.path.exists(project_path):
        print(f"錯誤：專案 '{safe_project_name}' 已存在")
        return False
    
    # 確保 projects 資料夾存在
    os.makedirs(projects_dir, exist_ok=True)
    
    try:
        # 複製模板資料夾
        shutil.copytree(template_path, project_path)
        print(f"✓ 已複製模板檔案到 {project_path}")
        
        # 更新 README.md
        readme_path = os.path.join(project_path, "README.md")
        update_readme(readme_path, project_name, topic, target_audience, word_count)
        print(f"✓ 已更新專案 README")
        
        print(f"\n🎉 專案 '{project_name}' 建立成功！")
        print(f"📁 專案位置：{project_path}")
        print(f"📝 開始寫作：請開啟 {os.path.join(project_path, '01-選題.md')}")
        
        return True
        
    except Exception as e:
        print(f"錯誤：建立專案時發生問題 - {str(e)}")
        # 清理可能建立的不完整資料夾
        if os.path.exists(project_path):
            shutil.rmtree(project_path)
        return False

def update_readme(readme_path, project_name, topic, target_audience, word_count):
    """
    更新專案 README 檔案中的基本資訊
    
    Args:
        readme_path (str): README 檔案路徑
        project_name (str): 專案名稱
        topic (str): 文章主題
        target_audience (str): 目標讀者
        word_count (str): 預期字數
    """
    
    # 讀取模板內容
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 取得當前日期
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # 替換模板中的佔位符
    content = content.replace('[專案名稱]', project_name)
    content = content.replace('[文章主題]', topic)
    content = content.replace('[日期]', current_date)
    content = content.replace('[讀者群體]', target_audience)
    content = content.replace('[字數範圍]', word_count)
    
    # 寫回檔案
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    """主程式入口"""
    parser = argparse.ArgumentParser(
        description='《電馭寫作》專案建立工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用範例：
  python scripts/create-project.py "我的第一篇文章" "如何提升寫作效率"
  python scripts/create-project.py "產品評測" "最新筆電深度評測" --audience "科技愛好者" --words "2000-4000字"
        """
    )
    
    parser.add_argument('name', help='專案名稱')
    parser.add_argument('topic', help='文章主題')
    parser.add_argument('--audience', '-a', default='一般讀者', help='目標讀者群體 (預設: 一般讀者)')
    parser.add_argument('--words', '-w', default='1000-3000字', help='預期字數範圍 (預設: 1000-3000字)')
    
    # 如果沒有提供參數，顯示幫助訊息
    if len(sys.argv) == 1:
        parser.print_help()
        return
    
    args = parser.parse_args()
    
    print("《電馭寫作》專案建立工具")
    print("=" * 30)
    print(f"專案名稱：{args.name}")
    print(f"文章主題：{args.topic}")
    print(f"目標讀者：{args.audience}")
    print(f"預期字數：{args.words}")
    print("-" * 30)
    
    success = create_project(args.name, args.topic, args.audience, args.words)
    
    if success:
        print("\n下一步：")
        print("1. 開啟專案資料夾")
        print("2. 從 01-選題.md 開始七階段寫作流程")
        print("3. 參考 templates/ai-prompts.md 使用 AI 提詞助手")
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()