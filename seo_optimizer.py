#!/usr/bin/env python3
"""
SEO Optimizer for kvlasermarking.com
Optimizes product pages and other HTML files with precise keywords and structured data.
"""
import os
import re
import json

BASE_DIR = r"C:\Users\komal\Desktop\07_项目网站\laser-marking-website\(最终)kvlasermarking.com"
BASE_URL = "https://kvlasermarking.com"

# Product metadata
PRODUCTS = {
    "product-1.html": {
        "title": "Single Side Single Traction Laser Marking Machine | KINGVAN",
        "desc": "Economical automatic laser marking machine for thermal break strips. Single side marking with single traction system. Ideal for standard insulation strip coding applications.",
        "keywords": "single side laser marking, single traction laser coder, thermal strip marking machine, economical laser coder, insulation bar coding",
        "price": "2999.00",
        "category": "Thermal Strip Laser Marking"
    },
    "product-2.html": {
        "title": "Single Side Double Traction Laser Marking Machine | KINGVAN",
        "desc": "Stable automatic laser marking with dual traction system for longer thermal strips. Single side marking with enhanced feeding stability for consistent coding quality.",
        "keywords": "single side double traction, dual traction laser marking, long strip laser coder, stable feeding laser machine, thermal break strip coding",
        "price": "3999.00",
        "category": "Thermal Strip Laser Marking"
    },
    "product-3.html": {
        "title": "Double Side Single Traction Laser Marking Machine | KINGVAN",
        "desc": "Simultaneous double-side laser marking for thermal break strips. Single traction with dual marking heads. Maximum efficiency for production lines requiring both-side coding.",
        "keywords": "double side laser marking, dual side laser coder, simultaneous marking machine, thermal strip double coding, insulation bar dual marking",
        "price": "4999.00",
        "category": "Thermal Strip Laser Marking"
    },
    "product-4.html": {
        "title": "Double Side Double Traction Laser Marking Machine (Flagship) | KINGVAN",
        "desc": "Flagship automatic laser marking machine with double side marking and dual traction. Maximum production efficiency for high-volume thermal strip manufacturing.",
        "keywords": "double side double traction, flagship laser marking, high-speed laser coder, automatic thermal strip machine, premium laser marking system",
        "price": "6999.00",
        "category": "Thermal Strip Laser Marking"
    }
}

# Other pages metadata
OTHER_PAGES = {
    "about.html": {
        "title": "About KINGVAN | 激光打码机制造商与解决方案提供商",
        "desc": "Learn about KINGVAN Technology: a leading manufacturer of automatic laser marking machines for thermal break strips. Professional R&D team, global service network, and customized solutions.",
        "keywords": "KINGVAN Technology company, laser marking manufacturer, thermal strip coding company, about KINGVAN",
        "og_type": "website"
    },
    "blog.html": {
        "title": "Laser Marking Blog | KINGVAN - 隔热条打码技术指南",
        "desc": "Expert articles on thermal strip laser marking techniques, maintenance tips, industry trends, and application guides. Stay updated with KINGVAN knowledge base.",
        "keywords": "laser marking blog, thermal strip coding guide, laser technology news, insulation strip tips, KINGVAN articles",
        "og_type": "website"
    },
    "news.html": {
        "title": "Company News | KINGVAN - 激光打码机行业动态",
        "desc": "Latest news from KINGVAN Technology: product updates, industry exhibitions, customer success stories, and laser marking technology advancements.",
        "keywords": "KINGVAN news, laser marking industry news, thermal strip updates, company announcements",
        "og_type": "website"
    },
    "dashboard.html": {
        "title": "Dashboard | KINGVAN - 用户管理中心",
        "desc": "KINGVAN customer dashboard. Manage your orders, track shipments, and access technical documentation for your laser marking equipment.",
        "keywords": "KINGVAN dashboard, customer portal, order management, laser machine support",
        "og_type": "website"
    }
}

def optimize_product_page(filename, meta):
    filepath = os.path.join(BASE_DIR, filename)
    if not os.path.exists(filepath):
        print(f"⚠️  File not found: {filename}")
        return

    with open(filepath, 'r', encoding='gbk', errors='replace') as f:
        html = f.read()

    # 1. Replace <title>
    html = re.sub(r'<title>.*?</title>', f'<title>{meta["title"]}</title>', html, flags=re.IGNORECASE)

    # 2. Replace <meta name="description">
    html = re.sub(
        r'<meta name="description" content=".*?"',
        f'<meta name="description" content="{meta["desc"]}"',
        html, flags=re.IGNORECASE
    )

    # 3. Add <meta name="keywords"> if missing, or replace
    if '<meta name="keywords"' not in html:
        html = re.sub(
            r'<meta name="viewport"',
            f'<meta name="keywords" content="{meta["keywords"]}">\n    <meta name="viewport"',
            html, flags=re.IGNORECASE
        )
    else:
        html = re.sub(
            r'<meta name="keywords" content=".*?"',
            f'<meta name="keywords" content="{meta["keywords"]}"',
            html, flags=re.IGNORECASE
        )

    # 4. Fix robots
    if '<meta name="robots"' not in html:
        html = re.sub(
            r'<meta name="keywords"',
            f'<meta name="robots" content="index, follow, max-image-preview:large">\n    <meta name="keywords"',
            html, flags=re.IGNORECASE
        )
    else:
        html = re.sub(
            r'<meta name="robots" content=".*?"',
            '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"',
            html, flags=re.IGNORECASE
        )

    # 5. Add canonical if missing
    if '<link rel="canonical"' not in html:
        html = re.sub(
            r'<meta name="viewport"',
            f'<link rel="canonical" href="{BASE_URL}/{filename}">\n    <meta name="viewport"',
            html, flags=re.IGNORECASE
        )
    else:
        html = re.sub(
            r'<link rel="canonical" href=".*?"',
            f'<link rel="canonical" href="{BASE_URL}/{filename}"',
            html, flags=re.IGNORECASE
        )

    # 6. Inject JSON-LD before </head>
    json_ld = {
        "@context": "https://schema.org/",
        "@type": "Product",
        "name": meta["title"].split(" |")[0],
        "description": meta["desc"],
        "brand": {"@type": "Brand", "name": "KINGVAN"},
        "manufacturer": {"@type": "Organization", "name": "KINGVAN Technology Co., Ltd."},
        "offers": {
            "@type": "Offer",
            "url": f"{BASE_URL}/{filename}",
            "priceCurrency": "USD",
            "price": meta["price"],
            "availability": "https://schema.org/InStock",
            "itemCondition": "https://schema.org/NewCondition"
        },
        "category": meta["category"]
    }
    
    json_ld_str = json.dumps(json_ld, indent=2, ensure_ascii=False)
    script_tag = f'\n    <!-- JSON-LD Structured Data: Product -->\n    <script type="application/ld+json">\n{json_ld_str}\n    </script>\n'
    
    # Insert before </head>
    html = html.replace('</head>', script_tag + '</head>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ Optimized: {filename}")

def optimize_other_page(filename, meta):
    filepath = os.path.join(BASE_DIR, filename)
    if not os.path.exists(filepath):
        print(f"⚠️  File not found: {filename}")
        return

    with open(filepath, 'r', encoding='gbk', errors='replace') as f:
        html = f.read()

    # 1. Replace <title>
    html = re.sub(r'<title>.*?</title>', f'<title>{meta["title"]}</title>', html, flags=re.IGNORECASE)

    # 2. Replace <meta name="description">
    html = re.sub(
        r'<meta name="description" content=".*?"',
        f'<meta name="description" content="{meta["desc"]}"',
        html, flags=re.IGNORECASE
    )

    # 3. Add <meta name="keywords">
    if '<meta name="keywords"' not in html:
        html = re.sub(
            r'<meta name="viewport"',
            f'<meta name="keywords" content="{meta["keywords"]}">\n    <meta name="viewport"',
            html, flags=re.IGNORECASE
        )
    else:
        html = re.sub(
            r'<meta name="keywords" content=".*?"',
            f'<meta name="keywords" content="{meta["keywords"]}"',
            html, flags=re.IGNORECASE
        )

    # 4. Fix robots
    if '<meta name="robots"' not in html:
        html = re.sub(
            r'<meta name="keywords"',
            f'<meta name="robots" content="index, follow, max-image-preview:large">\n    <meta name="keywords"',
            html, flags=re.IGNORECASE
        )
    else:
        html = re.sub(
            r'<meta name="robots" content=".*?"',
            '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"',
            html, flags=re.IGNORECASE
        )

    # 5. Add canonical
    if '<link rel="canonical"' not in html:
        html = re.sub(
            r'<meta name="viewport"',
            f'<link rel="canonical" href="{BASE_URL}/{filename}">\n    <meta name="viewport"',
            html, flags=re.IGNORECASE
        )
    else:
        html = re.sub(
            r'<link rel="canonical" href=".*?"',
            f'<link rel="canonical" href="{BASE_URL}/{filename}"',
            html, flags=re.IGNORECASE
        )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ Optimized: {filename}")

def add_lazy_loading(filename):
    """Add loading='lazy' to images"""
    filepath = os.path.join(BASE_DIR, filename)
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r', encoding='gbk', errors='replace') as f:
        html = f.read()

    # Add loading="lazy" to images (except logo/hero)
    html = re.sub(
        r'<img(?!.*?loading=)(.*?)(?<!/)?>',
        lambda m: f'<img{m.group(1)} loading="lazy">' if not any(x in m.group(0).lower() for x in ['logo', 'hero', 'favicon', 'nav-logo']) else m.group(0),
        html
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    print("🚀 Starting SEO optimization for kvlasermarking.com...")
    print("\n📦 Optimizing Product Pages:")
    for filename, meta in PRODUCTS.items():
        optimize_product_page(filename, meta)
    
    print("\n📄 Optimizing Other Pages:")
    for filename, meta in OTHER_PAGES.items():
        optimize_other_page(filename, meta)
    
    print("\n🖼️  Adding lazy loading to images:")
    all_files = list(PRODUCTS.keys()) + list(OTHER_PAGES.keys()) + ["index.html"]
    for f in all_files:
        add_lazy_loading(f)
        print(f"✅ Lazy loading added: {f}")
    
    print("\n✨ All pages optimized successfully!")
