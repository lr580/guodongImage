# 将参数列表转化为命令列表，元素为 [命令名, 参数...]


def paraSplit(argv):
    argv.append('--end')  # 尾处理
    res = []
    tmp = []
    for i in argv[1:]:
        if i[0] == '-':
            if len(tmp):
                res.append(tmp)
            paraName = i.replace('-', '')
            tmp = [paraName]
        else:
            tmp.append(i)
    return res


paraMap = {}
helpList = {}


def loadFuncList():
    with open('funcList.txt', 'r', encoding='utf8') as f:
        raw = f.readlines()
    raw.append('#DEF author lr580')  # 尾处理
    helpText = ''
    prFuncName = ''
    for i in raw:
        if len(i) >= 4 and i[:4] == '#DEF':
            if len(helpText):  # 首处理
                helpList[prFuncName] = helpText
            names = i.split()
            funcName = names[1]
            prFuncName = funcName
            helpText = ''
            aliasCnt = 0
            for j in names[2:]:
                paraMap[j] = funcName
                if aliasCnt >= 1:
                    helpText += ' 或 '
                if len(j) == 1:
                    helpText += '-%s' % j
                else:
                    helpText += '--%s' % j
                aliasCnt += 1
            helpText += ': '
        else:
            helpText += i


def printHelp(funcName):
    if len(funcName):
        if not funcName in paraMap.keys():
            print('指令不存在')
        else:
            print(helpList[paraMap[funcName]])
    else:
        for i in helpList:
            print(helpList[i], end='')


def printVersion():
    print('当前版本: 0.0.6')
