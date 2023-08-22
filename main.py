import requests
import re
url = "https://yoyochinese.com/chinese-learning-tools/Mandarin-Chinese-pronunciation-lesson/pinyin-chart-table"

page = requests.get(url)
occur = [m.start() for m in re.finditer('data-text0', page.text)]
words =[]

for index in occur:
    word = ""
    iter = index + 12
    while page.text[iter] != "\"" and page.text[iter] != "&":
        if page.text[iter] == "ü":
            word += "u"
        else:
            word += page.text[iter]
        iter = iter + 1
    words.append(word)

goodWords = sorted(set(words))
goodWords.remove("")

print(goodWords)

for i in goodWords:
    count = 1
    for n in {1, 2, 3, 4}:
        mp3Link = "https://cdn.yoyochinese.com/audio/pychart/" + i + str(n) + ".mp3"
        filename = "D:/Vanderbilt/Fall 2022/CHIN 1101/pinyin-scrape/audioFiles/" + i + str(n) + ".mp3"
        doc = requests.get(mp3Link)
        if doc.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(doc.content)
    print(count)

print("Done!")