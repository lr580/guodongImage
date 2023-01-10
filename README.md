果冻图片助手(`guodongImage`)是能够进行一些图片处理的 Python 组件库代码仓库。

请运行 `gdimage.py`，该代码文件作为主要入口。并传入 main 函数参数执行不同的指令。

## 功能说明

1. 查看帮助 `--help` 或 `-h`。后可以接一个参数，代表具体的功能说明。

   如：`python gdimage.py -h`，会输出帮助文档。

   如：`python gdimage.py -h keepOut` 会输出 `keepOut` 指令的帮助。

2. 查看版本信息 `--version` 或 `-v`。

3. `keepOut` 生成一张 `不要靠近xx，会变得不幸` 的定制图片

   参数:图片完整路径 输出路径

   如：`python gdimage.py --keepOut sample.jpg out.jpg`

   或参数:输入图片文件夹 输出文件夹。这将把输入图片文件夹里所有文件(含子目录)做一次处理，输出到目标文件夹里(名字同名,但目标文件夹没有子目录嵌套)(以下指令同理)
   如 `python gdimage.py --keepOut imgs result`

   示例效果：

   ![keepOutSample](readmeimg/keepOutSample.jpg)

   建议：输入的图片尽可能使方形的且大小大于180x180

4. `idk`

   生成一张定制表情包，内容为让xx告诉你吧，啊这，他说不知道。

   参数：图片路径 输出路径 名称

   如 `python gdimage.py --idk sample.jpg out.jpg lr580`

   参数：图片路径 输出路径 名称 性别代词(默认是他)

   如 `python gdimage.py --idk sample.jpg out.jpg 禾枫 她`

   参数：图片路径 输出路径 + 语句1 语句2 语句3 语句4

   如 `python gdimage.py --idk sample.jpg out.jpg + 你发现了一只lr580！ lr580 快告诉我吧！ [请选择:告诉Y/不告诉N]`

   建议图片大小不小于 500x500，输入文字里不能含空格和 `-`。

5. `histSpan` 只选取一张图片灰度范围在[low,high]的并将其拉伸到[0,255]。效果同 `matlab` 的 `imshow(,[])`。

   参数:源图片路径 输出文件路径 low high 是否为黑白图
   后三个参数可以省略，默认为min原图,max原图,False；如果min/max填N也默认

   如： `python gdimage.py --histSpan sample.jpg out.jpg`

6. `capooEat` 生成一张 `capoo` 定制图片 (制作中)

7. `resize` 或 `-s`，修改图片大小，具体请参见 `python gdimage.py -h resize`

   如：`python gdimage.py -s sample.jpg out.jpg 1024 256`

   如：`python gdimage.py -s sample.jpg out.jpg x1.5`

8. `convert` 或 `cvt` 或 `-c`，图片格式转换，具体请参见 `python gdimage.py -h convert`

   如： `python gdimage.py -c sample.webp sample.gif`

   如：`python gdimage.py -c test testres png` (文件夹内图片批量转换)



