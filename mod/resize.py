from mod.importFileDealer import fileDealer
from PIL import Image


def resize(src, des, *param):
    fileDealer.batchRun(src, des, resizeGen, *param)


def resizeGen(src, des, w, h=0, resample='nearest'):
    try:
        img = Image.open(src)
    except Exception:
        print('[resize]%s格式错误' % src)
        return
    rows, cols = img.size
    if w[0] == 'x':
        k = float(w[1:])
        rows, cols = int(k*rows), int(k*cols)
    else:
        w, h = int(w), int(h)
        if w == 0:
            w = rows*h//cols
        if h == 0:
            h = w*cols//rows
        rows, cols = w, h
    resampleType = eval('Image.Resampling.'+resample.upper())
    img = img.resize((rows, cols), resample=resampleType)
    img.save(des)
    print('[resize]保存 %s (%dx%d)' % (des, rows, cols))
