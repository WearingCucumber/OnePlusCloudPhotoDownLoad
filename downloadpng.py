import requests
from PIL import Image
from io import BytesIO

# 定义一个函数来下载图像
def download_image(url, index):
    try:
        # 发送GET请求获取图像数据
        response = requests.get(url)
        if response.status_code == 200:
            # 读取图像数据
            image_data = response.content
            # 使用Pillow库打开图像数据
            image = Image.open(BytesIO(image_data))
            # 保存图像到本地
            image.save(f"image_{index}.jpg")
            print(f"图像 {index} 下载成功")
        else:
            print(f"无法下载图像 {index}，状态码: {response.status_code}")
    except Exception as e:
        print(f"下载图像 {index} 时发生错误: {e}")

# 读取文本文件中的URL
with open("photoUrls.txt", "r") as file:
    urls_str = file.read()

# 将字符串转换为Python列表
urls = eval(urls_str)

# 遍历URL列表并下载图像
for index, url in enumerate(urls):
    url = url.strip()  # 移除末尾的换行符
    download_image(url, index)
