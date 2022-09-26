果冻图片助手(`guodongImage`)是能够进行一些图片处理的 Python 组件库代码仓库。

请运行 `gdimage.py`，该代码文件作为主要入口。并传入 main 函数参数执行不同的指令。

## 功能说明

1. 查看帮助 `--help` 或 `-h`。后可以接一个参数，代表具体的功能说明。

   如：`python gdimage.py -h`，会输出帮助文档。

2. 查看版本信息 `--version` 或 `-v`。

3. `keepOut` 生成一张 `不要靠近xx，会变得不幸` 的定制图片

   参数:图片完整路径(目前仅支持jpg) 输出路径

   如：`python gdimage.py --keepOut sample.jpg out.jpg`

   示例效果：

   ![keepOutSample](readmeimg/keepOutSample.jpg)

4. `capooEat` 生成一张 `capoo` 定制图片 (制作中)



