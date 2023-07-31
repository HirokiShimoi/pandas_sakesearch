import pandas as pd
import os

input_dir = './csv/'

output_dir = './filtered_excel'

# 入力ファイルのリスト
input_files = ['bcart_products.csv']  #ここの名称を変更

def calc_spec(name):
    if '純米大吟醸' in name:
        return '純米大吟醸'
    elif '純米吟醸' in name:
        return '純米吟醸'
    elif '純米' in name:
        return '純米'
    else:
        return ''


for file_name in input_files:
    df = pd.read_csv(os.path.join(input_dir, file_name), encoding='shift_jis', 
                     usecols=['【基本】商品名','【セット】品番', '【基本】キャッチコピー','【基本】説明','【基本】生産地','【基本】画像','【セット】単価','【セット】セット名'])
    
    df = df[['【基本】商品名','【セット】セット名','【セット】品番', '【基本】生産地', '【セット】単価', '【基本】キャッチコピー','【基本】説明', '【基本】画像']]
    df.insert(3, 'メーカー名', '平和酒造')  # 適宜、メーカー名を変更する
    df.insert(5, '甘辛度1', '中口')
    df.insert(6, '甘辛度2', '')
    df.insert(7, '香り1', 'やや強い')
    df.insert(8, '香り2', '普通')
    df['スペック'] = df['【基本】商品名'].apply(calc_spec) 
    df.insert(11, 'クール', False)
    df.insert(12, 'にごり', False)
    df.insert(13, '酒米', '山田錦')
    df.insert(14, '在庫', True)



    new_name = os.path.splitext(file_name)[0]
    

    df.to_excel(os.path.join(output_dir, new_name + '_heiwa' +'.xlsx'), index=False)    # 名称変更
    #df.to_csv(os.path.join(output_dir, new_name + '.csv'), index=False)