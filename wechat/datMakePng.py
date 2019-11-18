import os
out_path=r"D:\\图片"
 
def imageDecode(f,fn):
    dat_read = open(f, "rb")
    out=out_path+"\\"+fn+".png"
    png_write = open(out, "wb")
    for now in dat_read:
	    for nowByte in now:
		    newByte = nowByte ^ 0x77
		    png_write.write(bytes([newByte]))
		dat_read.close()
		png_write.close()

def findFile(f):
    fsinfo = os.listdir(f)
    for fn in fsinfo:
	    temp_path = os.path.join(f, fn)
	    if not os.path.isdir(temp_path):
		    print('文件路径: {}' .format(temp_path))
		    print(fn)
		    imageDecode(temp_path,fn)
		else:
		    ...
																   
path = r'D:\\WeChat\\WeChat Files\\***\\FileStorage\\Image\\2019-11'
findFile(path)
