from PIL import Image
import os

# 设置图片所在目录和输出GIF文件名
image_folder = "catch_can"  # 替换为存放PNG图片的文件夹路径
output_gif_path = "catch_can.gif"      # 生成的GIF文件名

# 获取文件夹中所有PNG文件，按名称排序
image_files = sorted(
    [f for f in os.listdir(image_folder) if f.endswith('.png')],
    key=lambda x: os.path.join(image_folder, x)
)

# 确保有图片文件
if not image_files:
    print("No PNG files found in the specified folder.")
else:
    # 打开图片并将其添加到列表中
    frames = [Image.open(os.path.join(image_folder, file)) for file in image_files]

    # 保存为GIF文件，设置帧速率和循环
    frames[0].save(
        output_gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=800,  # 每帧持续时间（毫秒）
        loop=0         # 循环次数（0表示无限循环）
    )
    print(f"GIF created successfully: {output_gif_path}")
