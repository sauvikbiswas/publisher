import re
import os

tagRe = re.compile('\s*\[(\w+)\]\s*')
tagLinkRe = re.compile('(\s*):(\w+)(\s*)')

cmdfilename = 'sync.cmd'
if os.path.isfile(cmdfilename):
    with open(cmdfilename, 'r') as fp:
        data = fp.read()

        splitloc = []
        tags = []
        for item in tagRe.finditer(data):
            print(item.group(1),item.start(),item.end())
            tags += [item.group(1)]
            splitloc += [item.start(),item.end()]
        splitloc += [len(data)]

        for i in range(len(tags)):
            filedata = '#!/bin/bash\n'+data[splitloc[i*2+1]:splitloc[i*2+2]]
            filedata = tagLinkRe.sub(lambda mo: mo.group(1)+'./_'+mo.group(2)+'.cmd'+mo.group(3),filedata)
            filename = '_'+tags[i]+'.cmd'
            with open(filename, 'w') as fpout:
                fpout.write(filedata)
            if os.path.isfile(filename):
                os.chmod(filename,0o755)
