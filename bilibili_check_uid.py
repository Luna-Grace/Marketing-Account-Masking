import json
import sys

def is_positive_integer(s):
    return s.isdigit()

def validate_uids(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    accounts = data['accounts']
    invalid_uids = []
    
    for index, account in enumerate(accounts):
        uid = account['UID']
        if not is_positive_integer(uid):
            invalid_uids.append((index + 1, uid)) # 组别从1开始
    
    if invalid_uids:
        print("[ERROR] 发现以下无效的 UID:")
        for group, uid in invalid_uids:
            print(f"[ERROR] 第 {group} 组: 无效的 UID - {uid}")
        return 1
    else:
        print("[INFO] 所有 UID 格式都正确")
        return 0

def main():
    file_path = 'bilibili-normal.json'
    return validate_uids(file_path)

if __name__ == '__main__':
    sys.exit(main())
