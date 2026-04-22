#!/usr/bin/env python3
"""
Final SEO Verification Script for kvlasermarking.com
Checks if all new keywords are correctly present in HTML files.
"""
import os
import re

BASE_DIR = r"C:\Users\komal\Desktop\07_项目网站\laser-marking-website\(最终)kvlasermarking.com"

# Keywords to verify per file
CHECKS = {
    "index.html": [
        "CE certified",
        "IPG source",
        "Southeast Asia",
        "aluminum window manufacturers",
        "PA66 strip laser marking",
        "fiber laser marking machine"
    ],
    "product-1.html": [
        "PA66 strip laser marking",
        "fiber laser marking machine",
        "permanent non-contact marking",
        "thermal strip manufacturers"
    ],
    "product-2.html": [
        "thermal break strip production line coding",
        "20W 30W laser coder",
        "high speed laser coding system",
        "batch manufacturing"
    ],
    "product-3.html": [
        "insulation bar batch production marking",
        "0.01mm precision laser marking",
        "window frame traceability marking",
        "quality traceability"
    ],
    "product-4.html": [
        "high speed laser coding system",
        "IPG source laser marker",
        "ISO standard laser coding machine",
        "large-scale production"
    ]
}

def verify_file(filename, keywords):
    filepath = os.path.join(BASE_DIR, filename)
    if not os.path.exists(filepath):
        return False, "File not found"
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='gbk', errors='replace') as f:
            content = f.read()
    
    missing = []
    for kw in keywords:
        if kw.lower() not in content.lower():
            missing.append(kw)
    
    if missing:
        return False, f"Missing: {', '.join(missing)}"
    return True, "All keywords present"

if __name__ == "__main__":
    print("🔍 开始最终 SEO 验证...")
    print("="*60)
    
    all_passed = True
    for filename, keywords in CHECKS.items():
        success, message = verify_file(filename, keywords)
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} | {filename}: {message}")
        if not success:
            all_passed = False
    
    print("="*60)
    if all_passed:
        print("🎉 所有文件验证通过！文件已准备好上传。")
    else:
        print("⚠️  部分文件验证失败，请检查。")
