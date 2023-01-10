from mod.importFileDealer import fileDealer
from PIL import Image


def convert(src, des, *param):
    fileDealer.batchRun(src, des, convertGen, *param)


def convertGen(src, des, form=None):
    if not form:
        form = des[des.rfind('.')+1:]
    else:
        des = des[:des.rfind('.')]+'.'+form
    try:
        img = Image.open(src)
    except Exception:
        print('[convert]%s格式错误' % src)
        return
    img.save(des, form, save_all=True, background=0)
