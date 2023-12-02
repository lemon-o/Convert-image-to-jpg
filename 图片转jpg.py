import os
from PIL import Image
from psd_tools import PSDImage

def convert_images_to_jpg(input_folder, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # 遍历输入文件夹中的所有文件
    imgs = ['.jpg', '.webp', '.png', '.gif', '.bmp', '.psd', '.tga', '.tif']
    
    for filename in os.listdir(input_folder):
        # 检查文件的扩展名是否为图像扩展名之一
        if any(filename.endswith(img) for img in imgs):
            # 构建输入和输出文件的完整路径
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")

            # 如果是PSD文件，则使用psd-tools库处理
            if filename.endswith('.psd'):
                psd = PSDImage.open(input_path)
                image = psd.compose()              
                # 将 RGBA 转换为 RGB
                if image.mode == "RGBA":
                    image = image.convert("RGB")            
                image.save(output_path, "JPEG")

            else:
                # 其他图像文件使用Pillow库处理
                with Image.open(input_path) as image:
                    image.convert("RGB").save(output_path, "JPEG")
            print(f"转换完成：{filename} -> {os.path.basename(output_path)}")

# 获取脚本所在文件的目录路径
script_directory = os.path.dirname(os.path.abspath(__file__))
# 输入文件夹和输出文件夹的路径（使用脚本所在文件的目录路径）
input_folder = script_directory
output_folder = os.path.join(script_directory, "output_folder")
# 调用函数进行转换
convert_images_to_jpg(input_folder, output_folder)
