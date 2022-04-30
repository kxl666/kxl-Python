# 用 zipfile 模块压缩文件
import os
import zipfile

os.chdir(r'C:\Users\kxl666\Desktop\Python\1.Python基础\08.文件和异常\_temp')
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
