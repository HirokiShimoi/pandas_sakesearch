import pandas as pd

# CSVファイルを読み込む
df = pd.read_excel('./filtered_excel/bcart_products_heiwa.xlsx')

df.replace(['\t', '\n', '\r'], ['', '',''], regex=True, inplace=True)

# 同一商品名の行をまとめる
grouped = df.groupby('【基本】商品名')

# 新たなJSONデータを作成
new_data = []
for name, group in grouped:
    spicy = []
    if pd.notnull(group['甘辛度1'].iloc[0]):
        spicy.append(group['甘辛度1'].iloc[0])
    if pd.notnull(group['甘辛度2'].iloc[0]):
        spicy.append(group['甘辛度2'].iloc[0])

    smell = []
    if pd.notnull(group['香り1'].iloc[0]):
        smell.append(group['香り1'].iloc[0])
    if pd.notnull(group['香り2'].iloc[0]):
        smell.append(group['香り2'].iloc[0])

    item = {
        'productName': name,
        'maker': group['メーカー名'].iloc[0],
        'region': group['【基本】生産地'].iloc[0],
        'spicy': spicy,  # Update here
        'smell': smell,  # Update here
        'spec': group['スペック'].iloc[0],
        'rice': group['酒米'].iloc[0],
        'gift': group['ギフト'].iloc[0],
        'cool': group['クール'].iloc[0],
        'imageUrl': group['【基本】画像'].iloc[0],
        'description': group['【基本】キャッチコピー'].iloc[0],
        'content': group['【基本】説明'].iloc[0],
        'variations': [
            {
                'products_id' : row['【セット】品番'],
                'products': row['【セット】セット名'],
                'price': row['【セット】単価'],
                'stock': row['在庫'],
            }
            for _, row in group.iterrows()
        ]
    }
    new_data.append(item)

# JSONファイルとして保存
pd.DataFrame(new_data).to_json('converted.json_heiwa', orient='records',force_ascii=False)
