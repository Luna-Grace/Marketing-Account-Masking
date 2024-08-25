import json
import yaml

# ================ NOTE ====================
# 处理步骤:
#   读JSON -> 提信息 -> 转YAML → 放TXT
# 限制:
#   - 本程序并未添加错误处理 (即 try...except...)
#   - 必须要求源json数据准确无误
# 需要注意的点:
#   - 使用 'w' 打开文件，为覆盖写入。即使原文比现在的长。
# ==========================================

def main():
    # 读取 JSON 文件
    with open('bilibili-normal.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        print("[INFO] 成功读取json数据")

    # 提取用户名和 UID 列表
    usernames = [account['username'] for account in data['accounts']]
    uids = [account['UID'] for account in data['accounts']]
    print("[INFO] 成功提取账户信息")

    # 转换为 YAML 格式并保存
    yaml_data = {
        'accounts': data['accounts']
    }
    print("[INFO] 成功将信息转换为 YAML 格式")
    with open('bilibili-normal.yaml', 'w', encoding='utf-8') as f:
        yaml.dump(yaml_data, f, allow_unicode=True)
        print("[INFO] 成功将信息写入 YAML 文件")

    # 将用户名保存到 TXT 文件
    with open('bilibili-normal-usernames.txt', 'w', encoding='utf-8') as f:
        f.write(','.join(usernames))
        print("[INFO] 成功将用户名信息写入 TXT 文件")

    # 将 UID 保存到 TXT 文件
    with open('bilibili-normal-uids.txt', 'w', encoding='utf-8') as f:
        f.write(','.join(uids))
        print("[INFO] 成功将UID信息写入 TXT 文件")

    # 生成 Markdown 表格
    markdown_table = '| 用户名 | UID |\n|-----|-----|\n'
    for username, uid in zip(usernames, uids):
        markdown_table += f'| {username} | {uid} |\n'

    # 保存 Markdown 表格到文件
    with open('bilibili-normal.md', 'w', encoding='utf-8') as f:
        f.write(markdown_table)
        print("[INFO] 成功将信息写入 Markdown 文件")

if __name__ == '__main__':
    main()
