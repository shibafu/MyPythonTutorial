

words = ['cat', 'window', 'defence', 'ultimate']

for i in range(4):
    print(str(i) + '回目のループ')
    print('wordsは' + words[i] +'です')
    if 'cat' in words[i]:
        print('にゃーん')
    elif 'defence' in words[i]:
        print('はい顔面セーフ')

print('処理を終了しました')
