import pandas as pd
import os

# 入力ファイルのディレクトリ
input_dir = './csv/'
# 出力ファイルのディレクトリ
output_dir = './filtered_csv/'

# 入力ファイルのリスト
input_files = ['bcart_products.csv']  # ここにさらに読み込むファイル名を追加していく

for file_name in input_files:
    df = pd.read_csv(os.path.join(input_dir, file_name), encoding='shift_jis', 
                     usecols=['【基本】商品名','【セット】品番', '【基本】キャッチコピー','【基本】説明','【基本】生産地','【基本】画像','【セット】単価'])
    df = df[['【基本】商品名','【セット】品番', '【基本】生産地', '【セット】単価', '【基本】キャッチコピー','【基本】説明', '【基本】画像']]
    df.insert(2, 'メーカー名', '平和酒造')  # 適宜、メーカー名を変更する
    df.insert(4, '甘辛度', '中口')
    df.insert(5, '香り', 'やや強い')
    df.insert(6, 'スペック', '純米大吟醸')
    df.insert(7, 'ギフト', False)
    df.insert(8, 'クール', False)
    df.insert(7, '酒米', False)
    df.insert(8, '在庫', False)

    # ファイル名から拡張子を除去したものを新しい名前とする（例：'bcart_products_heiwa'）
    new_name = os.path.splitext(file_name)[0]
    
    # 新しい名前で出力する
    df.to_csv(os.path.join(output_dir, new_name + '.csv'), index=False)
    df.to_excel(os.path.join(output_dir, new_name + '.xlsx'), index=False)
