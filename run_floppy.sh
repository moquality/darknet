#!/bin/sh
./darknet -i 2 detector train ../image_compare/deep_template_matching/data/floppy.data cfg/yolo-voc.cfg backup_2.5_centered/yolo-voc_36000.weights > out_2.txt 2>&1

