writingData = "aaaaaaaaaaaaaa\n"
writingData += "ssssssssss\n"
writingData += "XXXXXXXXXXX\n"

with open("read.txt", 'a', encoding="utf-8") as file:
    file.write(writingData)

with open("read.txt", 'r', encoding="utf-8") as file:
    dataList = file.readlines() #readLinesはリストで取得できる便利機能だが、改行文字も一緒に読み込むので注意が必要


for data in dataList:
    print(data[:-1])
