#! usr/env python3

import os
from PIL import Image

def genThumbnail(imgName):
    name=os.path.join("resource/img", imgName)
    im=Image.open(name)
    im.thumbnail((400,400))
    print(imgName,im.format,im.size,im.mode)
    im.save("resource/img/thumbnail/" + imgName,'JPEG')
    print('Done!')

def readImages(url):
    images = filter(lambda x: x.endswith((".jpg", ".png", ".jpeg")), os.listdir(url))
    return images

def buildImgSubPage(fileName):
    skeleton = """\
<!DOCTYPE html>
<html lang="zh-CN">

<head>
    <meta charset="UTF-8">
    <meta name="referrer" content="no-referrer">
    <link rel="stylesheet" type="text/css" href="../css/imageSubpage.css">
    <link rel="stylesheet" type="text/css" href="../css/watermark.css">
    <link rel="stylesheet" type="text/css" href="../css/skin.css"/>
    <script type="text/javascript" src="../js/skin.js"></script>

    <title>
        {0}
    </title>
    
    <style>
        #Header{{
            color:black;
            font-size:25px;
        }}
    </style>
</head>

<body class="Christmas">
    <header>
        <div>
            <span style="display: block; text-align:right">
                <button onclick="change('day')">日间模式</button>
                <button onclick="change('dark')">夜间模式</button>
                <button onclick="change('Christmas')">圣诞模式</button>
            </span>
        </div>
    </header>
    <main>
        <div class="watermark"></div> <!-- for full-screen watermark -->
        <h1 id="Header" style="text-align:center">{0}</h1>
        <canvas id="canvas" style="display: none;"></canvas>
        <img hidden id="source" src="../resource/img/{1}" alt="{0}"/>

        <div style="width: auto; margin: auto; text-align: center">
            <img id="result" class="image" src="" alt="{0}"/>
        </div>
    </main>
</body>

<script type="text/javascript" src="../js/CryptoStego-master/dist/cryptostego.min.js"></script>
<script>
    window.onload = function() {{
        encrypt();
    }}

    function imgToCanvas(src) {{
        let source = document.getElementById(src);
        let canvas = document.getElementById("canvas");
        canvas.width = source.width;
        canvas.height = source.height;

        canvas.getContext("2d").drawImage(source, 0, 0);
    }}

    function encrypt() {{
        imgToCanvas("source");
        let succ = writeMsgToCanvas("canvas", "WOW! 我太爱人机交互了", "password", 0);
        if (succ) {{
            let c = document.getElementById("canvas");
            let src = document.getElementById("source");
            let result = document.getElementById("result");
            console.log(src.width, src.height);
            result.width = src.width;
            result.height = src.height;
            result.src = c.toDataURL("image/png");
        }}
        //decode();
    }}

    function decode() {{
        let result = document.getElementById("result");
        let canvas = document.createElement("CANVAS");
        canvas.width = result.width;
        canvas.height = result.height;
        canvas.getContext("2d").drawImage(result, 0, 0);
        let msg = readMsgFromCanvas("canvas", "password", 0);
        console.log(msg);
    }}
</script>
</html>
"""
    imageName = fileName[0: fileName.rfind(".")]
    with open("subpage/" + imageName + ".html", "w+", encoding="utf-8") as f:
        f.write(skeleton.format(imageName, fileName))


def buildIndex():
    indexHead = """\
<!DOCTYPE html>
<html lang="zh-CN">

<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" href="css/index.css">
    <link rel="stylesheet" type="text/css" href="css/watermark.css"/>
    <link rel="stylesheet" type="text/css" href="css/skin.css"/>
    <script type="text/javascript" src="./js/skin.js"></script>

    <title>
        那抹秋意
    </title>
</head>

<body class="Christmas">
    <header>
        <div>
            <span style="display: block; text-align:right">
                <button onclick="change('day')">日间模式</button>
                <button onclick="change('dark')">夜间模式</button>
                <button onclick="change('Christmas')">圣诞模式</button>
            </span>
            <p></p>
            <span style="display: block; text-align:right">
                <a href="login.html"><button class="header_button">登陆</button></a>
                <a href="register.html"><button class="header_button">注册</button></a>
            </span>
        </div>
    </header>

    <main style="text-align:center;">
        <div class="watermark"></div> <!-- for full-screen watermark -->
        <h1>那抹秋意</h1>
        <div class="search_container">
            <form action="login.html" class="search_parent">
                <input type="text" placeholder="请输入图片名">
                <input type="button" value="搜索">
            </form>
        </div>
        <ul class="img-wrapper">
"""

    indexContent = \
        """            <li><a href="subpage/{0}.html"><img src="resource/img/thumbnail/{1}" alt="{0}"/></a></li>
"""

    indexTail = """\
        </ul>
    </main>
</body>

</html>
"""

    with open("index.html", "w+", encoding="utf-8") as f:
        f.write(indexHead)
        images = readImages("resource/img/")
        for fileName in images:
            imageName = fileName[0: fileName.rfind(".")]
            f.write(indexContent.format(imageName, fileName))
        f.write(indexTail)

def main():
    images = readImages("resource/img/")


    # build image high resolution pages.
    images = readImages("resource/img/")
    for image in images:
        # build thumbnail
        genThumbnail(image)
        # build image high resolution pages.
        buildImgSubPage(image)

    # build index.
    buildIndex()

if __name__ == "__main__":
    main()