#!/bin/sh
#./darknet detector train ../image_compare/deep_template_matching/data/floppy.data cfg/yolo-voc.cfg  > out.txt 2>&1
./darknet detector test ../image_compare/deep_template_matching/data/floppy.data cfg/yolo-voc.cfg backup_2.5_centered/yolo-voc_32000.weights data/floppy/211.bmp
