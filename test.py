# -- coding: utf-8 --
"""
@time : 2022/8/7 22:18
@author : fuqiang
@file : test.py
@project : Pytorch-UNet
"""
# import os
# path = 'D:/User/wgy/workplace/data/notMNIST_large.tar'
# root = os.path.splitext(path)[0]
# print(root)

import os
a = ['sssssss']
print(a[0])
exit()
a = os.listdir('./data/imgs/')


def get_output_filenames(args):
    def _generate_name(fn):
        return f'./result/{os.path.splitext(fn)[0]}_OUT.png'

    return list(map(_generate_name, args))


print(get_output_filenames(a))