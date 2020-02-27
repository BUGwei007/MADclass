"""
Author: yaming
Email: wei_ym@yeah.net
Wechat: ahrztj_wei


date: 2019/12/18 18:30
desc: classify the data
"""


import os
import re
import shutil


def classify(fpath, tpath):
    for root, dirs, files in os.walk(fpath):
        for file in files:
            # AllFilesList.append(os.path.join(root, file))
            if re.search(r'Melville', file):        ## 匹配自定义需求
                # OriFilesList.append(os.path.join(root, file))
                shutil.copy(os.path.join(root, file), tpath)    ## 将匹配的文件复制过去
    return True


if __name__ == '__main__':

    frompath = r'./data/all_data'
    topath = r'./data/Melville'     ## 分类的目标文件夹

    print(classify(frompath, topath))