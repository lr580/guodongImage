import matplotlib.image as mpimg
import numpy as np
import sys
sys.path.append('../')
fileDealer = None
if not fileDealer:
    exec('import fileDealer')  # 免得被格式化走了


def histSpan(src, des, low=None, high=None, isGrey=False):
    fileDealer.batchRun(src, des, histSpanGen, low, high, isGrey)


def histSpanGen(src, des, low, high, isGrey):
    try:
        img = mpimg.imread(src)
    except Exception:
        print('[histSpan]%s格式错误' % src)
        return

    if not low or str(low).upper() == 'N':
        low = np.min(img)
    if not high or str(high).upper() == 'N':
        high = np.max(img)
    img2 = img.copy()
    img2 = ((img-low)/(high-low))*255
    img2 = img2.astype(np.uint8)
    if (type(isGrey) == type(True) and isGrey) or str(isGrey).upper() == 'TRUE':
        mpimg.imsave(des, img2, cmap="Greys_r")
    else:
        mpimg.imsave(des, img2)
    print('[histSpan]%s生成完毕' % des)