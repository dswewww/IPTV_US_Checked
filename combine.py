

from os import listdir
from os.path import isfile, join
filenames = [f for f in listdir("./") if isfile(join("./", f)) and f.endswith("m3u")]
print(filenames)
with open('m3u/final.m3u', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                if line.startswith("#") or line.startswith("http") or line.startswith("rtmp") :
                    outfile.write(line)
                else:
                    print(line)