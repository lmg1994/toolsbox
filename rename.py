# -*- coding:utf-8 -*-

import os


class ImageRename():
    def __init__(self):
        self.path = '/home/westwell/sgm/example/left'

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)


        for item in filelist:
            if item.endswith('.png'):
                src = os.path.join(os.path.abspath(self.path), item)
                middle = item[-6:-4]
                middle = middle.replace('t','0')
                dst = os.path.join(os.path.abspath(self.path), format(middle, '0>2s') + '.png')
                os.rename(src, dst)
                print 'converting %s to %s ...' % (src, dst)

        print 'total %d to rename ' % (total_num)


if __name__ == '__main__':
    newname = ImageRename()
    newname.rename()