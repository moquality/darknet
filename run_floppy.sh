#!/bin/sh
./darknet detector train ../image_compare/deep_template_matching/data/floppy.data cfg/yolo-voc.cfg  > out.txt 2>&1

