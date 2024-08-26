import json
import sys

def is_positive_integer(s):
    return s.isdigit()

def validate_uids_and_usernames(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    accounts = data['accounts']
    invalid_uids = []
    seen_uids = set()
    seen_usernames = set()
    duplicate_uids = set()
    duplicate_usernames = set()

    for index, account in enumerate(accounts):
        uid = account.get('UID')
        username = account.get('username', '')

        # 检查 UID 的有效性
        if not is_positive_integer(uid):
            invalid_uids.append((index + 1, uid)) # 组别从1开始
        else:
            if uid in seen_uids:
                duplicate_uids.add((index + 1, uid))
            seen_uids.add(uid)

        # 检查用户名的重复
        if username in seen_usernames:
            duplicate_usernames.add((index + 1, username))
        seen_usernames.add(username)

    has_errors = False

    if invalid_uids:
        print("[ERROR] 发现以下无效的 UID:")
        for group, uid in invalid_uids:
            print(f"[ERROR] 第 {group} 组: 无效的 UID - {uid}")
        has_errors = True
    
    if duplicate_uids:
        print("[WARN] 发现以下重复的 UID:")
        for group, uid in duplicate_uids:
            print(f"[WARN] 第 {group} 组: 重复的 UID - {uid}")
        has_errors = True

    if duplicate_usernames:
        print("[WARN] 发现以下重复的用户名:")
        for group, username in duplicate_usernames:
            print(f"[WARN] 第 {group} 组: 重复的用户名 - {username}")
        has_errors = True

    if not has_errors:
        print("[INFO] 所有 UID 和用户名格式正确且无重复")
        return 0

    return 2

def main():
    file_path = 'bilibili-normal.json'
    return validate_uids_and_usernames(file_path)

if __name__ == '__main__':
    sys.exit(main())
