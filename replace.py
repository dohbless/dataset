import os
path = r'D:\keeplearning\dataset\water\water1'
filelist = os.listdir(path)
count=1001

for file in filelist:
    print(file)
for file in filelist:
    Olddir = os.path.join(path,file)
    if os.path.isdir(Olddir):
        continue
    filename = os.path.splitext(file)[0]
    filetype = os.path.splitext(file)[1]
    Newdir = os.path.join(path, 'img_'+str(count).zfill(4)+'_08'+filetype)
    os.rename(Olddir, Newdir)

    count += 1


