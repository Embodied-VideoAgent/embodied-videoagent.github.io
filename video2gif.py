from moviepy.editor import VideoFileClip

# 输入视频路径
video_path = "hssd_clip.mp4"
output_path = "hssd_clip.gif"

# 读取视频
clip = VideoFileClip(video_path)
print(clip.size)
# 高质量 GIF 转换
clip = clip.resize(height=750)  # 设置高度，宽度自动适配
clip.write_gif(output_path, fps=15, program="ffmpeg", opt="palettegen", loop=True)

print(f"高清 GIF 已生成: {output_path}")