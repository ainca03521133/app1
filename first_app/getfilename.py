import glob

myfile= glob.glob(r"first_app\\*.py")
for item in myfile :
    item.strip(r"first_app\\")
    print(item)