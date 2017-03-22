import os
import subprocess

FOLDER = 'data/floppy_vm'

def cmd_for(file):
    cmd = "./darknet detector test ../image_compare/deep_template_matching/data/floppy.data cfg/yolo-voc.cfg backup_2.5_centered/yolo-voc_32000.weights " + FOLDER + "/" + file
    return cmd

for file in os.listdir(FOLDER):
    cmd = cmd_for(file)
    subprocess.check_output(cmd, shell=True)
    file_new = file.replace(".bmp", ".png")
    print "Performing for " + file
    subprocess.check_output("cp predictions.png " + FOLDER + "/out/" + file_new , shell=True)


# ffmpeg -i input.avi -vf scale=320:240 output.avi
# ffmpeg -r 10 -f image2 -s 360x640 -i %03.png -vcodec libx264 -crf 25  -pix_fmt yuv420p test.mp4
