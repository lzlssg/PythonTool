# PythonTool
我的python工具集合，通过脚本对工作有一些帮助

**开发环境**：

**python**：使用Python 3

**代码工具**：[pycharm](https://www.jetbrains.com/pycharm/)

---
## excel

通过使用**openpyxl**对excel进行批量操作，目前操作不支持图片

---
## wechat

**datMakePng.py**：使用16进制编辑器看文件头与FFD8异或,FFD8是以jpg结尾文件的文件头
所以把dat文件头转换成这种形式就要把文件头异或，本人得到的结果是7777，所以每个字节进
行异或0x77进行解密，就可以得到dat文件的图片
