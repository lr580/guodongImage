from PIL import Image, ImageDraw, ImageFont


def roughLen(text):  # 中文字算1，其他算0.5
    def count_chinese_chars(text):
        count = 0
        for char in text:
            if '\u4e00' <= char <= '\u9fff':
                count += 1
        return count
    ch = count_chinese_chars(text)
    oth = len(text) - ch
    return ch + (oth+1)//2


def roughSplit(t):  # 中文字1个1组，其他最多2个一组分组
    res = []
    for c in t:
        if '\u4e00' <= c <= '\u9fff':
            res.append(c)
        else:
            if not len(res):
                res.append(c)
            elif len(res[-1]) == 1:
                if not '\u4e00' <= res[-1] <= '\u9fff':
                    res[-1] += c
                else:
                    res.append(c)
            else:
                res.append(c)
    return res


def preTeaFactory():
    return [((60, 115, 20, 0),),  # 0
            ((56, 115, 20, 1),),  # 1
            ((48, 115, 20, 2),),  # 2
            ((46, 115, 16, 3),),  # 3
            ((56, 114, 12, 2), (56, 128, 12, 2)),  # 4
            ((50, 114, 12, 3), (56, 128, 12, 2)),  # 5
            ((50, 114, 12, 3), (50, 128, 12, 3)),  # 6
            ((45, 114, 12, 4), (50, 128, 12, 3)),  # 7
            ((45, 114, 12, 4), (45, 128, 12, 4)),  # 8
            ((45, 116, 10, 5), (48, 130, 10, 4)),  # 9
            ((45, 116, 10, 5), (45, 130, 10, 5)),  # 10
            ((47, 110, 10, 4), (47, 124, 10, 4), (49, 138, 10, 3)),  # 11
            ((47, 110, 10, 4), (47, 124, 10, 4), (47, 138, 10, 4)),  # 12
            ((47, 111, 9, 5), (49, 124, 9, 4), (49, 137, 9, 4)),  # 13
            ((47, 111, 9, 5), (47, 124, 9, 5), (49, 137, 9, 4)),  # 14
            ((47, 111, 9, 5), (47, 124, 9, 5), (47, 137, 9, 5))]  # 15


def tea(des, text='', typ='0'):
    src = 'img/tea%s.jpg' % typ
    img = Image.open(src)
    n = roughLen(text)
    pre = preTeaFactory()
    if n >= len(pre):
        print('[tea] "%s"太长了，无法渲染' % text)
        return
    draw = ImageDraw.Draw(img)
    ts = roughSplit(text)
    for batch in pre[n]:
        font = ImageFont.truetype("msyhl.ttc", batch[2])
        cx, cy = batch[:2]
        nowts = ts[:batch[-1]]
        ts = ts[batch[-1]:]
        line = ''
        for i in nowts:
            line += i
        # tw, th = draw.textsize(text, font=font)
        # rx, ry = (cx-tw/2, cy-th/2)
        draw.text((cx, cy), line, font=font, fill=(0, 0, 0))
    img.save(des)
    print('[tea] %s 绘制成功' % des)
