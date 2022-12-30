filenames= ["1.doc", "1.reportm","1.presentation"]

filenames = [filename.replace(".",'-')+".txt" for filename in filenames]
print(filenames)