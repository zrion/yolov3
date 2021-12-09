import os

def yolo_create_list(src_path, filepath):
    '''
        Generate .txt list file for yolo training data
    '''
    files = [src_path+"/"+x for x in os.listdir(src_path)]

    fopen = open(filepath, 'w')
    for file in files:
        if file.endswith('.jpg'):
            fopen.write(file+"\n")
    fopen.close()
    return

if __name__ == "__main__":
	listfilename = "../data/lb_train.txt"
	src_path = "/home/hai/workspace/yolov3/data/lb_train"
	yolo_create_list(src_path, listfilename)