# coding: UTF-8
import qrcode
from PIL import Image
codeFile = open("code.txt", "r")
i = 0
codeList = []
while True:
    code = codeFile.readline()
    if not code:
        break
    i += 1
    codeList.append(code)
merge_img = Image.new('RGB', (330, 330 * i), 0xffffff)
for j in range(codeList.__len__()):
    img = qrcode.make(codeList[j])
    img.save(codeList[j].replace('\n','')+'.png')
    merge_img.paste(img, (0, 330 * j))
codeFile.close()
merge_img.save('result.png')