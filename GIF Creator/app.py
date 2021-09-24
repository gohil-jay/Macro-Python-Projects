from moviepy.editor import *

clip = (VideoFileClip("video_file.webm")
        .subclip((2.25),(6.25))
        .resize(0.3))

clip.write_gif("output_file.gif")
