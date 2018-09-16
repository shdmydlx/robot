import os
from time import strftime,gmtime
from common.tool import getRootDir
# 01. 拿到图片存储目录
root_dir = getRootDir()
screenshotsPath = os.path.join(root_dir,'screenshots')
# 02. 拿到当前月份目录
def get_y_m():
    return strftime("%Y_%m",gmtime())

png_y_m_dir =os.path.join(screenshotsPath, get_y_m())
# 03. 判断是否存在当前月份目录，不存在就创建一个
if os.path.exists(png_y_m_dir):
    pass
else:
    os.mkdir(png_y_m_dir)


#04. 判断当前月份目录下的当前日期目录，不存在也创建一个



#05 写一个函数 返回当前日期目录  return /${rootDir}/scrrenshot/Y_m/Y_m_d






"""
01. 拿到所有的report文件
reports = ['Test_LoginTest_2018-09-02_15-11-05',''Test_LoginTest_2018-09-02_10-11-05',','Test_LoginTest_2018-09-00_15-11-05']

02-01
reports[0]

02-02
对比每个文件的创建日期，--> 排序问题，拿到最新创建的文件名 返回文件名



"""





