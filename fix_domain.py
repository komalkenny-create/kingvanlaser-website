#!/usr/bin/env python3
"""
Fix Domain Name: kvlasermarking.com -> kingvanlaser.com
"""
import os
import re

BASE_DIR = r"C:\Users\komal\Desktop\07_项目网站\laser-marking-website\(最终)kvlasermarking.com"
OLD_DOMAIN = "kvlasermarking.com"
NEW_DOMAIN = "kingvanlaser.com"

def fix_file(filename):
    filepath = os.path.join(BASE_DIR, filename)
    if not os.path.exists(filepath):
        return

    # 尝试读取
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        enc = 'utf-8'
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='gbk', errors='replace') as f:
            content = f.read()
        enc = 'gbk'

    if OLD_DOMAIN in content:
        new_content = content.replace(OLD_DOMAIN, NEW_DOMAIN)
        with open(filepath, 'w', encoding=enc) as f:
            f.write(new_content)
        print(f"✅ Fixed: {filename}")
    else:
        print(f"⚪ Skipped (no match): {filename}")

if __name__ == "__main__":
    print(f"🔄 Replacing {OLD_DOMAIN} -> {NEW_DOMAIN}...")
    
    # 1. HTML Files
    html_files = [
        "index.html", "about.html", "blog.html", "news.html", "dashboard.html",
        "product-1.html", "product-2.html", "product-3.html", "product-4.html",
        "signin.html", "signup.html", "cart.html", "checkout.html" # 假设有的页面
    ]
    for f in html_files:
        fix_file(f)
        
    # 2. SEO Files
    fix_file("sitemap.xml")
    fix_file("robots.txt")
    
    print("\n✨ Done!")
