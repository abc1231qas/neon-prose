#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
電馭寫作 - 文章整合腳本
將七階段寫作內容整合成最終文章

使用方法:
python scripts/compile-article.py <專案名稱>
"""

import os
import sys
import re
import logging
from datetime import datetime
from pathlib import Path

logging.basicConfig(
    filename='compile-article.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def extract_my_content(file_path):
    """
    從階段檔案中提取「我的內容」區塊
    
    Args:
        file_path (str): 階段檔案路徑
        
    Returns:
        str: 提取的內容，如果沒有找到則返回空字串
    """
    if not os.path.exists(file_path):
        return ""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 使用正則表達式提取「我的內容」區塊
        pattern = r'## 我的內容\s*\n(.*?)(?=\n## |$)'
        match = re.search(pattern, content, re.DOTALL)
        
        if match:
            my_content = match.group(1).strip()
            # 移除空的方括號提示文字
            my_content = re.sub(r'\[.*?\]', '', my_content).strip()
            return my_content
        
        return ""
    
    except Exception as e:
        print(f"讀取檔案 {file_path} 時發生錯誤: {e}")
        return ""

def extract_title_from_stage4(file_path):
    """
    從04-標題.md檔案中提取最終選定的標題
    
    Args:
        file_path (str): 標題階段檔案路徑
        
    Returns:
        str: 提取的標題，如果沒有找到則返回預設標題
    """
    content = extract_my_content(file_path)
    if not content:
        return "未命名文章"
    
    # 嘗試提取「主標題：」後面的內容
    title_match = re.search(r'\*\*主標題：\*\*\s*(.+)', content)
    if title_match:
        return title_match.group(1).strip()
    
    # 如果沒有找到主標題格式，嘗試提取第一行有意義的內容
    lines = content.split('\n')
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#') and not line.startswith('**') and len(line) > 5:
            return line
    
    return "未命名文章"

def get_project_info(project_path):
    """
    從專案README中提取基本資訊
    
    Args:
        project_path (str): 專案資料夾路徑
        
    Returns:
        dict: 包含專案資訊的字典
    """
    readme_path = os.path.join(project_path, 'README.md')
    info = {
        'name': os.path.basename(project_path),
        'topic': '',
        'target_audience': '',
        'create_date': ''
    }
    
    if os.path.exists(readme_path):
        try:
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 提取主題
            topic_match = re.search(r'\*\*主題：\*\*\s*(.+)', content)
            if topic_match:
                info['topic'] = topic_match.group(1).strip()
            
            # 提取目標讀者
            audience_match = re.search(r'\*\*目標讀者：\*\*\s*(.+)', content)
            if audience_match:
                info['target_audience'] = audience_match.group(1).strip()
            
            # 提取建立日期
            date_match = re.search(r'\*\*建立日期：\*\*\s*(.+)', content)
            if date_match:
                info['create_date'] = date_match.group(1).strip()
                
        except Exception as e:
            print(f"讀取專案資訊時發生錯誤: {e}")
    
    return info

def compile_article(project_name):
    """
    整合七階段內容成最終文章
    
    Args:
        project_name (str): 專案名稱
        
    Returns:
        bool: 成功返回True，失敗返回False
    """
    # 確認專案路徑
    project_path = os.path.join('projects', project_name)
    if not os.path.exists(project_path):
        print(f"錯誤: 找不到專案 '{project_name}'")
        print(f"請確認專案路徑: {project_path}")
        return False
    
    print(f"開始整合專案: {project_name}")
    
    # 七個階段的檔案名稱
    stages = [
        ('01-選題.md', '選題'),
        ('02-發想.md', '發想'),
        ('03-備料.md', '備料'),
        ('04-標題.md', '標題'),
        ('05-前言.md', '前言'),
        ('06-主體.md', '主體'),
        ('07-收尾.md', '收尾')
    ]
    
    # 提取各階段內容
    stage_contents = {}
    for filename, stage_name in stages:
        file_path = os.path.join(project_path, filename)
        content = extract_my_content(file_path)
        stage_contents[stage_name] = content
        
        if content:
            print(f"✓ 已提取 {stage_name} 階段內容")
        else:
            print(f"⚠ {stage_name} 階段內容為空")
    
    # 獲取專案資訊
    project_info = get_project_info(project_path)
    
    # 提取標題
    title = extract_title_from_stage4(os.path.join(project_path, '04-標題.md'))
    
    # 生成最終文章
    final_article = generate_final_article(title, stage_contents, project_info)
    
    # 儲存最終文章
    output_path = os.path.join(project_path, 'final-article.md')
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_article)

        print(f"✓ 文章整合完成!")
        print(f"✓ 最終文章已儲存至: {output_path}")
        logging.info("文章整合完成 - 專案: %s, 輸出檔案: %s", project_name, output_path)
        return True

    except Exception as e:
        print(f"錯誤: 儲存文章時發生問題: {e}")
        logging.error("文章整合失敗 - 專案: %s, 錯誤: %s", project_name, e)
        return False

def generate_final_article(title, stage_contents, project_info):
    """
    生成格式化的最終文章內容
    
    Args:
        title (str): 文章標題
        stage_contents (dict): 各階段內容
        project_info (dict): 專案資訊
        
    Returns:
        str: 格式化的最終文章
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    article = f"""# {title}

> **專案名稱:** {project_info['name']}  
> **主題:** {project_info['topic']}  
> **目標讀者:** {project_info['target_audience']}  
> **整合時間:** {current_time}

---

"""
    
    # 添加前言
    if stage_contents['前言']:
        article += stage_contents['前言'] + "\n\n"
    
    # 添加主體內容
    if stage_contents['主體']:
        article += stage_contents['主體'] + "\n\n"
    
    # 添加收尾
    if stage_contents['收尾']:
        article += stage_contents['收尾'] + "\n\n"
    
    # 添加創作過程附錄（可選）
    article += """---

## 創作過程記錄

"""
    
    # 添加各階段的創作記錄
    stage_names = ['選題', '發想', '備料', '標題', '前言', '主體', '收尾']
    for stage_name in stage_names:
        if stage_contents[stage_name]:
            article += f"""### {stage_name}階段

{stage_contents[stage_name]}

"""
    
    article += f"""---

*本文章由《電馭寫作》七階段寫作流程創作完成*  
*整合時間: {current_time}*
"""
    
    return article

def main():
    """主程式入口"""
    if len(sys.argv) != 2:
        print("使用方法: python scripts/compile-article.py <專案名稱>")
        print("\n範例:")
        print("  python scripts/compile-article.py my-article")
        print("\n可用的專案:")
        
        projects_dir = 'projects'
        if os.path.exists(projects_dir):
            projects = [d for d in os.listdir(projects_dir) 
                       if os.path.isdir(os.path.join(projects_dir, d)) and not d.startswith('.')]
            if projects:
                for project in projects:
                    print(f"  - {project}")
            else:
                print("  (目前沒有專案)")
        
        sys.exit(1)
    
    project_name = sys.argv[1]
    
    # 執行文章整合
    success = compile_article(project_name)

    if success:
        print("\n🎉 文章整合成功完成!")
        logging.info("整合流程完成 - 專案: %s", project_name)
        sys.exit(0)
    else:
        print("\n❌ 文章整合失敗")
        logging.error("整合流程失敗 - 專案: %s", project_name)
        sys.exit(1)

if __name__ == "__main__":
    main()