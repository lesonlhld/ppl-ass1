import os
from pathlib import Path
import filecmp

solutionsSample = [x for x in os.listdir('test/solutionsSample/') if x.endswith(".txt")]
FO = open('check.txt', 'w')

count =0
for filename in solutionsSample:
    if os.path.isfile('test/solutions/'+filename):
        file1="test/solutionsSample/"+filename
        file2="test/solutions/"+filename
        comp = filecmp.cmp(file1, file2)
        if comp==True:
            count+=1
        FO.write("%s: %s\n" % (filename[:-4], comp))
    else:
        FO.write("%s: File khong ton tai\n" %filename[:-4])
print("Pass: %d/%d" %(count, len(solutionsSample)))