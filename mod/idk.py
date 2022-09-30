import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors as mcolor
import sys
from PIL import Image
sys.path.append('../')
fileDealer = None
if not fileDealer:
    exec('import fileDealer')  # 以后建议AOP优化


def idk(src, des, name='我', *optional):
    fileDealer.batchRun(src, des, idkGen, name, optional)


def idkGen(src, des, name, *optional):
    try:  # 以后建议AOP优化
        img = Image.open(src)
    except Exception:
        print('[idk]%s格式错误' % src)
        return

    rows, cols = img.size
    mx, mrc = 500, max(rows, cols)
    if mrc > mx:
        rows = int(rows/mrc*mx)
        cols = int(cols/mrc*mx)
        img = img.resize((rows, cols), Image.ANTIALIAS)

    pwid, phei, dpi = 700, 800, 100  # dpi影响字体和矩形等大小
    plt.figure(figsize=(pwid//dpi, phei//dpi), dpi=dpi)
    plt.axis('off')
    plt.xlim([0, pwid])
    plt.ylim([0, phei])

    # 设置显示中文字体
    plt.rcParams['font.family'] = ['sans-serif']
    plt.rcParams['font.sans-serif'] = ['SimHei']

    if name == '+':
        text1, text2, text3, text4 = optional[0]
    else:
        text1 = '让%s告诉你吧' % name
        text2 = name
        text3 = '%s不知道哦。' % name
        text4 = '啊这，他说不知道'
        if len(optional) and len(optional[0]):
            text4 = '啊这，%s说不知道' % optional[0]
    plt.text(20, 750, text1, fontsize=20)

    plt.figimage(img, xo=20, yo=70, zorder=-1)  # 底层

    rect = mpatches.Rectangle(
        (10, 80), 650, 200, fill=True, color="silver", alpha=0.5, zorder=1)
    plt.gca().add_patch(rect)

    plt.text(80, 240, text2, fontsize=18, color='orange')

    rect2 = mpatches.Rectangle(
        (30, 220), 250, 2, fill=True, color="orange", zorder=1)
    plt.gca().add_patch(rect2)

    plt.text(70, 175, text3, fontsize=18, color='white')

    plt.text(20, 30, text4, fontsize=20)

    plt.savefig(des, bbox_inches='tight')
    print('[idk]%s保存成功' % des)  # 以后建议AOP优化
