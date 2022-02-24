import plistlib
import os
import sys
from PIL import Image


def export_image(img, pathname, item):
    # 去透明後的子圖矩形
    x, y, w, h = tuple(map(int, item['frame']))
    # 子圖原始大小
    size = tuple(map(int, item['sourceSize']))
    # 子圖在原始圖片中的偏移
    ox, oy, _, _ = tuple(map(int, item['sourceColorRect']))

    # 獲取子圖左上角，右下角
    if item['rotated']:
        box = (x, y, x + h, y + w)
    else:
        box = (x, y, x + w, y + h)

    # 使用原始大小創建全透明圖
    image = Image.new('RGBA', size, (0, 0, 0, 0))
    # 從圖集中裁剪出子圖
    sprite = img.crop(box)

    # rotated紋理旋轉90度
    if item['rotated']:
        sprite = sprite.transpose(Image.ROTATE_90)

    # 粘貼子圖，設置偏移
    image.paste(sprite, (ox, oy))

    # 保存到文件
    print('保存文件：%s' % pathname)
    image.save(pathname, 'png')

# 獲取 frame 參數
def get_frame(frame):
    result = {}
    if frame['frame']:
        result['frame'] = frame['frame'].replace('}', '').replace('{', '').split(',')
        result['sourceSize'] = frame['sourceSize'].replace('}', '').replace('{', '').split(',')
        result['sourceColorRect'] = frame['sourceColorRect'].replace('}', '').replace('{', '').split(',')
        result['rotated'] = frame['rotated']
    return result

# 生成圖片
def gen_image(file_name, export_path):
    # 檢查文件是否存在
    plist = file_name + '.plist'
    if not os.path.exists(plist):
        print('plist文件【%s】不存在！請檢查' % plist)
        return

    png = file_name + '.png'
    if not os.path.exists(png):
        print('png文件【%s】不存在！請檢查' % plist)
        return

    # 檢查輸出目錄
    if not os.path.exists(export_path):
        try:
            os.mkdir(export_path)
        except Exception as e:
            print(e)
            return

    # 使用plistlib庫加載 plist 文件
    lp = plistlib.load(open(plist, 'rb'))
    # 加載 png 圖片文件
    img = Image.open(file_name + '.png')

    # 讀取所有小圖數據
    frames = lp['frames']
    for key in frames:
        item = get_frame(frames[key])
        export_image(img, os.path.join(export_path, key), item)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        exportPath = sys.argv[2]
        gen_image(filename, exportPath)
