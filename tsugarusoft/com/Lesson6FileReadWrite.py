file = open("read.txt", 'a', encoding="utf-8")

writingData = "aaaaaaaaaaaaaa"
writingData += '\n' + "ssssssssss"
writingData += '\n' + "XXXXXXXXXXX"

file.write(writingData) #ファイル書き込み
file.flush() #この処理でファイル入出力を確定させるため
file.close() #この処理でファイルを閉じる。基本的に同一ファイルを開きなおさない限り意識しなくてよいが、念のためやって置く

file = open("read.txt", 'r', encoding="utf-8")

fileData: str = file.read() #ファイル書き込み
file.readline()
file.close()

print(fileData)