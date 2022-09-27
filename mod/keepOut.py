import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
sys.path.append('../')
fileDealer = None
if not fileDealer:
    exec('import fileDealer')  # 免得被格式化走了


def keepOut(src, des, limx=180, limy=180):
    fileDealer.batchRun(src, des, keepOutOpe, limx, limy)


# 主操作
def keepOutOpe(src, desc, limx, limy):
    suf = src[src.rfind('.'):]
    if suf not in ('.jpg', '.png'):
        print('[keepOut]暂不支持%s的格式' % src)
        return
    img = mpimg.imread('img/keepOut'+suf)  # 以主调函数路径为相对
    plt.figure(figsize=(10, 10), dpi=60)  # 600*600
    plt.axis('off')

    img1 = img.copy()
    img2 = mpimg.imread(src)
    ox, oy = 225, 10
    rows, cols = img2.shape[:2]
    rx, ry = min(rows, limx), min(cols, limy)
    for i in range(rx):
        for j in range(ry):
            x, y = int(i/rx*rows), int(j/ry*cols)
            img1[i+ox][j+oy] = img2[x][y]

    plt.imshow(img1)
    plt.savefig(desc, bbox_inches='tight')
    print('[keepOut]%s保存成功' % desc)
