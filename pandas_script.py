import pandas as pd

df = pd.read_csv('C:/Users/kagiy/OneDrive/デスクトップ/Shimoi/pandas/csv/bcart_products.csv', encoding='shift_jis', usecols=['【基本】商品名', '【基本】キャッチコピー','【基本】生産地','【基本】画像','【セット】単価'])
df = df[['【基本】商品名', '【基本】生産地', '【セット】単価', '【基本】キャッチコピー', '【基本】画像']]
df.insert(1, 'メーカー名', '平和酒造')
df.insert(3, '甘辛度', '中口')
df.insert(4, '香り', 'やや強い')
df.insert(5, 'スペック', '純米大吟醸')
df.insert(6, 'ギフト', False)
df.insert(7, 'クール', False)
df.insert(10, '説明詳細', None)
df.to_csv('C:/Users/kagiy/OneDrive/デスクトップ/Shimoi/pandas/filename.csv', index=False)
