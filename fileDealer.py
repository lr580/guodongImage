import os


# 若输入文件，返回文件本身
# 若输入目录，返回目录下所有文件(含嵌套子目录的)
def getPath(src):
    if not os.path.isdir(src):
        return [src]
    else:
        res = []
        for root, dirs, files in os.walk(src):
            for file in files:
                res.append(os.path.join(root, file))
        return res


def batchRun(src, des, f, *extParam):
    srcs = getPath(src)
    if len(srcs) == 1:
        f(*([src, des] + list(extParam)))
    else:
        if not os.path.exists(des):
            os.mkdir(des)
        for i in srcs:
            fileName = os.path.split(i)[1]
            newDes = os.path.join(des, fileName)
            f(*([i, newDes] + list(extParam)))


def gcd(a, b):
    return gcd(b, a % b) if b > 0 else a



