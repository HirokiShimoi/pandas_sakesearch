import json

# JSON ファイルを読み込む
with open('converted.json', 'r') as f:
    data = json.load(f)

# 整形して出力する
print(json.dumps(data, indent=4, ensure_ascii=False))
