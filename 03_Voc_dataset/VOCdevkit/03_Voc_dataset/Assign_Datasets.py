import os

"""实现自动分配数据集给train，val等txt文件"""
img_path = "./VOCdevkit/VOC2007/JPEGImages"
txt_path = "./VOCdevkit/VOC2007/ImageSets/Segmentation"


def distrabution():
    n = 0
    for file in os.listdir(img_path):
        aa,bb = file.split('.')
        n = n+1
        if bb=='jpg':
            file_name = aa
            print(n)
            if n <= int(len(os.listdir(img_path)) * 0.7):
                with open(txt_path + '/' + 'train.txt','a') as f:
                    f.write(str(file_name) + '\n')
                with open(txt_path + '/' + 'trainval.txt','a') as f:
                    f.write(str(file_name) + '\n')
            elif int(len(os.listdir(img_path)) * 0.9) >= n > int(len(os.listdir(img_path)) * 0.7):
                with open(txt_path + '/' + 'val.txt', 'a') as f:
                    f.write(str(file_name) + '\n')
                with open(txt_path + '/' + 'trainval.txt','a') as f:
                    f.write(str(file_name) + '\n')
            elif int(len(os.listdir(img_path))) >= n > int(len(os.listdir(img_path)) * 0.9):
                with open(txt_path + '/' + 'test.txt', 'a') as f:
                    f.write(str(file_name) + '\n')
def main():
    """获取数据集分布"""
    distrabution()

if __name__ == '__main__':
    main()