import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import argparse

iou = []
class_ = []
obj = []
no_obj = []
recall = []

def clean(_arr, _n):
    try:
        return float(_arr[_n].replace(",", ""))
    except:
        pass

def parse(file_):
    f = open(file_, "r")
    lines = f.readlines()
    for line in lines:
        splits = line.split()
        if len(splits) == 16:
            iou.append(clean(splits, 3))
            class_.append(clean(splits, 5))
            obj.append(clean(splits, 7))
            no_obj.append(clean(splits, 10))
            recall.append(clean(splits, 13))
    f.close()

    y1 = savgol_filter(np.asarray(iou), 5001, 3)
    y2 = savgol_filter(np.asarray(class_), 5001, 3)
    y3 = savgol_filter(np.asarray(obj), 5001, 3)
    y4 = savgol_filter(np.asarray(no_obj), 5001, 3)
    y5 = savgol_filter(np.asarray(recall), 5001, 3)
    x1 = np.arange(len(y1))
    x2 = np.arange(len(y2))
    x3 = np.arange(len(y3))
    x4 = np.arange(len(y4))
    x5 = np.arange(len(y5))
    

    plt.subplot(3, 1, 1)
    plt.plot(x1, y1, 'o-')
    plt.title('IOU')
    plt.ylabel('IOU')

    plt.subplot(3, 1, 2)
    plt.plot(x2, y2, '.-')
    plt.xlabel('Epochs')
    plt.ylabel('Class')

    plt.subplot(3, 1, 3)
    plt.plot(x5, y5, '.-')
    plt.xlabel('Epochs')
    plt.ylabel('Recall')


    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse darknet output.')
    parser.add_argument('file', help='an integer for the accumulator')
    
    args = parser.parse_args()
    parse(args.file)