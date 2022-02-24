# TexturePackerResizeTool

## 執行縮圖並且縫圖
執行 ` python main.py ` 後輸入鈺縮放比例%(需大於0)  EX. 輸入為75則執行75%的比例縮放，將100*100的圖縮放為75*75

縮圖完成後會自動進行縫圖的動作


## 只執行縫圖
執行 ` python main.py ` 後直接 ` ENTER ` 即可對 ` dest `資料夾下的 jpg 以及 png 進行縫圖


## 將縫圖檔拆分
執行 ` python pngSplit.py  plist_name output_folder_name`  即可對同層資料夾下的縫圖檔拆分成png