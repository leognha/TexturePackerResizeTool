import os
from PIL import Image
from subprocess import check_output

# 原圖資料夾
project_dir = os.path.dirname(os.path.abspath(__file__))
inputDir = os.path.join(project_dir, 'src')
text_packer_check_path = r"C:\Program Files (x86)\CodeAndWeb\TexturePacker\bin\TexturePacker_check.exe"

# 輸出資料夾
outputDir = os.path.join(project_dir, 'dest')
if not os.path.isdir(outputDir):
    os.makedirs(outputDir)

def modify():
    # 切換資料夾
    os.chdir(inputDir)

    # 資料夾下所有的檔案
    for image_name in os.listdir(os.getcwd()):
        if image_name.split('.')[-1] == 'png' or image_name.split('.')[-1] == 'jpg':
            continue
        print(image_name)
        im = Image.open(os.path.join(inputDir, image_name))
        (w, h) = im.size
        im.thumbnail((w*rate/100, h*rate/100))
        im.save(os.path.join(outputDir, image_name))
    TexturePacker()

def TexturePacker():
     ## 縫圖
    name = input("縫圖檔名: ")
    os.chdir(outputDir)
   
    # 產生plist路徑75
    output_plist_path = os.path.join(outputDir, name+".plist")
    # 產生圖片路徑
    output_png_path = os.path.join(outputDir, name+".png")

    imgList = ""
    for frame in os.listdir(outputDir):
        test = frame.split('.')
        test = frame.split('.')[-1]
        if frame.split('.')[-1] == 'png' or frame.split('.')[-1] == 'jpg':
            imgList = imgList + frame  + ' '
    
    command = f'cmd /C "{text_packer_check_path}" {imgList}  --data {output_plist_path} --sheet {output_png_path} --size-constraints AnySize --max-width 2048 --max-height 2048 --no-trim --format cocos2d'
    check_output(command, shell=True)
    return
    
if __name__ == '__main__':
    while True:
        rate = input("縮放比例: ")
        try:
            if rate == "":
                TexturePacker()
                quit()
            rate = int(rate)
            if isinstance(rate, int ) and rate > 0:
                break
        except Exception as e:
            continue
    print(f"縮放比例為: {rate} %")
    modify()