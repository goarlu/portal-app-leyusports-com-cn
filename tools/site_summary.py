import json

SITE_DATA = {
    "title": "乐鱼体育",
    "url": "https://portal-app-leyusports.com.cn",
    "keywords": ["乐鱼体育", "体育赛事", "在线娱乐", "运动平台"],
    "tags": ["体育", "赛事直播", "娱乐"],
    "description": "乐鱼体育是一个综合性体育赛事观看与互动平台，涵盖多种体育项目的实时直播与资讯服务。"
}

def clean_text(value: str) -> str:
    return value.strip()

def extract_structured_info(data: dict) -> dict:
    return {
        "title": clean_text(data.get("title", "")),
        "url": data.get("url", "").strip(),
        "keywords": [clean_text(kw) for kw in data.get("keywords", [])],
        "tags": [clean_text(tag) for tag in data.get("tags", [])],
        "description": clean_text(data.get("description", ""))
    }

def format_keywords(kw_list: list) -> str:
    return ", ".join(kw_list)

def format_tags(tag_list: list) -> str:
    return " | ".join(tag_list)

def add_custom_prefix(url: str, prefix: str = "") -> str:
    if prefix and not url.startswith(prefix):
        return prefix + url
    return url

def build_summary(parsed: dict) -> str:
    lines = []
    lines.append("=" * 48)
    lines.append(f"  站点摘要: {parsed['title']}")
    lines.append("=" * 48)
    lines.append(f"  URL       : {add_custom_prefix(parsed['url'], 'https://')}")
    lines.append(f"  关键词    : {format_keywords(parsed['keywords'])}")
    lines.append(f"  标签      : {format_tags(parsed['tags'])}")
    lines.append(f"  说明      : {parsed['description']}")
    lines.append("-" * 48)
    return "\n".join(lines)

def export_as_json(parsed: dict) -> str:
    return json.dumps(parsed, ensure_ascii=False, indent=2)

def verify_data(data: dict) -> bool:
    required = ["title", "url", "keywords", "tags", "description"]
    return all(k in data and data[k] for k in required)

def main():
    if not verify_data(SITE_DATA):
        print("错误：站点数据不完整。")
        return
    info = extract_structured_info(SITE_DATA)
    summary = build_summary(info)
    print(summary)
    print()
    print("结构化数据(JSON):")
    print(export_as_json(info))

if __name__ == "__main__":
    main()