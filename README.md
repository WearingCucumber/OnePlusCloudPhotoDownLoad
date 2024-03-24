# OnePlusCloudPhotoDownLoad
用于一加云服务照片下载(真的很无语照片居然不给批量下载的功能)

## 食用教程：

### 1.进入照片列表页面

![image-20240325010302748](C:\Users\lzp\Desktop\新建文件夹 (2)\OnePlusCloudPhotoDownLoad\mdImages\image-20240325010302748.png)

### 2.通过f12抓到这个请求

![image-20240325010406609](C:\Users\lzp\Desktop\新建文件夹 (2)\OnePlusCloudPhotoDownLoad\mdImages\image-20240325010406609.png)

右键复制为cURL(bash) 这是edge的用法

### 3.进入 [爬虫工具库-spidertools.cn](https://spidertools.cn/#/curl2Request) copy进去 

![image-20240325010636472](C:\Users\lzp\Desktop\新建文件夹 (2)\OnePlusCloudPhotoDownLoad\mdImages\image-20240325010636472.png)

取cookie 那一段的内容 copy到saveUrl代码中 

![image-20240325010817153](C:\Users\lzp\Desktop\新建文件夹 (2)\OnePlusCloudPhotoDownLoad\mdImages\image-20240325010817153.png)

### 4.脚本运行

```powershell
	#安装依赖
	pip install requests
	pip install jsonpath-python
	pip install Image
	pip install ByteIO
	#先运行saveUrl.py
	python saveUrl.py
	#运行完成后 当前目录会有一个photoUrls.txt 再去运行 downloadpng.py
	python downloadpng.py
	#图片会下载到当前目录中
```
