import re

users = {
    "Platon" : ["9913.jpg", "ru"],
    "alexis": ["7378.gif", "us"],
    "Александрович": ["47253.jpg", "ru"],
    "Dima-Stranik": ["27406.png", "by"],
    "Alterus": ["65306.jpg", "ua"],
    "Kreismalsarion": ["179526.png", "aq"],
    "Bes": ["5740.jpg", "ru"],
    "Космогоник": ["172583.png", "ua"],
    "Eclairius": ["75567.jpg", "ua"],
    "Rybinsk": ["45226.jpg", "ru"],
    "simonov-89": ["107737.jpg", "ru"],
    "Dart_Evil": ["33498.jpeg", "ru"],
    "ЯRopolk": ["174768.jpg", "ru"],
    "lavpaber" : ["52935.jpg", "ru"],
    "Henry Piast" : ["165247.png", "ru"],
    "Guboz" : ["107845.jpg", "ua"],
    "Zdrajca" : ["41938.png", "ru"],
    "Злo" : ["105744.png", "ru"],
    "Січовик" : ["80242.jpg", "ua"],
    "Labes" : ["92818.jpg", "ua"],
    "Москит" : ["82816.jpg", "ru"],
    "JLRomik" : ["88625.png", "ru"],
    "Vladian" : ["56621.jpg", "ru"],
    "лекс" : ["16141.png", "ru"],
    "Comandante Raven" : ["19720.png", "jp"],
    "Дoбро" : ["76.png", "ad"],
    "Raizel" : ["121536.png", "by"],
    "DARKEST": ["104539.png", "bb"],
    "Igrok23": ["32882.jpg", "ru"],
    "UBooT": ["data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201024%201024%22%20style%3D%22background%3A%23c4a662%22%3E%3Cg%3E%3Ctext%20text-anchor%3D%22middle%22%20dy%3D%22.35em%22%20x%3D%22512%22%20y%3D%22512%22%20fill%3D%22%23ffffff%22%20font-size%3D%22700%22%20font-family%3D%22-apple-system%2C%20BlinkMacSystemFont%2C%20Roboto%2C%20Helvetica%2C%20Arial%2C%20sans-serif%22%3EU%3C%2Ftext%3E%3C%2Fg%3E%3C%2Fsvg%3E", "ru"]
}
emojis = {
    r":\)" : ["smile", "png"],
    r":D" : ["grin", "png"],
    r":\(" : ["sad", "png"],
    r":mad:" : ["mad", "gif"],
    r":ex:" : ["ex", "gif"],
    r"o.O" : ["huh", "png"],
    r":001:" : ["devil", "gif"],
    r":Cherna-facepalm:" : ["facepalm", "gif"],
    r":madness:" : ["madness", "gif"],
    r":108196:" : ["ready", "gif"],
    r":winner2:" : ["winner", "gif"],
    r":good:" : ["good", "gif"],
    r";\)" : ["wink", "png"],
    r":103282:" : ["thumbsdown", "gif"],
    r":103338:" : ["ok", "gif"],
    r"\^\_\^" : ["happy", "png"],
    r":laughingxi3:" : ["rofl", "gif"],
    r":drink:" : ["sip", "gif"],
    r":boy-cleanglasses:" : ["cleanglasses", "gif"],
    r":smile37:" : ["think", "gif"],
    r":time:" : ["time", "gif"],
    r":Laie:" : ["laie", "gif"],
    r":smile117:" : ["letter", "gif"],
    r":Strong:" : ["strong", "png"],
    r":butcher:" : ["butcher", "gif"],
    r":Ambitious:" : ["ambitious", "png"],
    r":023:" : ["dunno", "gif"],
    r":prava:" : ["lawyer", "gif"]
}
times = {
    "22": ["10", "PM"],
    "23": ["11", "PM"],
    "12": ["12", "PM"],
    "10": ["10", "AM"],
    "11": ["11", "AM"],
    "00": ["12", "AM"],
    "13": ["1", "PM"],
    "14": ["2", "PM"],
    "15": ["3", "PM"],
    "16": ["4", "PM"],
    "17": ["5", "PM"],
    "18": ["6", "PM"],
    "19": ["7", "PM"],
    "20": ["8", "PM"],
    "21": ["9", "PM"],
    "01": ["1", "AM"],
    "02": ["2", "AM"],
    "03": ["3", "AM"],
    "04": ["4", "AM"],
    "05": ["5", "AM"],
    "06": ["6", "AM"],
    "07": ["7", "AM"],
    "08": ["8", "AM"],
    "09": ["9", "AM"]
}

messageHeaderLeft = '\t\t\t<section class="messageBox">\n\t\t\t\t<header class="messageHeader">\n\t\t\t\t\t<img class="userPhoto" height="44" src="../img/avatars/{}" alt="{}">\n\t\t\t\t\t<div class="messageInfo">\n\t\t\t\t\t\t<div class="messageAuthor"><b>\n\t\t\t\t\t\t\t<span class="flag flag-{}"></span>\n\t\t\t\t\t\t\t<span class="user">{}</span>\n\t\t\t\t\t\t</b></div>\n\t\t\t\t\t\t<div class="messageTime">'
messageHeaderRight = '</div>\n\t\t\t\t\t</div>\n\t\t\t\t</header>\n\t\t\t\t<article class="messageBody">'
messageEnd = '\n\t\t\t\t</article>\n\t\t\t</section>'
quoteHeaderLeft = '\n\t\t\t\t\t<blockquote>\n\t\t\t\t\t\t<div class="quoteHeader">'
quoteHeaderLeftClosed = '\n\t\t\t\t\t<blockquote class="closedQuote">\n\t\t\t\t\t\t<div class="quoteHeader">'
quoteHeaderRight = '</div>\n\t\t\t\t\t\t<div class="quoteBody">'
quoteEnd = '\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</blockquote>'
emojiBlank = '<span class = "emoji emoji-{}"></span>'

source = open('source_html.txt', 'r', encoding="utf-8")
text = source.read()
source.close()

text = re.sub(r'\n[ \t\r\n]*\r?\n', '\n', text)
text = re.sub(r'(\n|\r\n)+', '\n', text)
text = re.sub(r'(<p[\s\S]*?>)\r?\n\t+', '\\1', text)
text = re.sub(r'\r?\n\t*</p>', '</p>', text)

text = re.sub(r'\n<a id="comment\S{,12}"></a>\n', '\n', text)

pattern = r'\t*<article id="elComment[\s\S]+?Перейти в профиль[\s\S]+?">(<span[\s\S]+?>)*([\S ]+?)</[\s\S]+?>(\d\d\.\d\d\.\d\d\d\d, \d\d:\d\d:\d\d)</time>[\s\S]+?core.lightboxedImages"[\s\S]*?>'
text = re.sub(pattern, '\\2\n\nОтветил: \\3' + messageHeaderRight, text)

for user in users:
    pattern = user + "\n\nОтветил: "
    text = re.sub(pattern, messageHeaderLeft.format(users[user][0], user, users[user][1], user), text)

text = re.sub(r'\n\t*</div>\n\t*</div>\n\t*<div class="ipsItemControls">[\s\S]+?</article>', messageEnd, text)

for time in times:
    pattern = times[time][0] + r":(\d\d) " + times[time][1]
    text = re.sub(pattern, time + ":\\1", text)

text = re.sub(r'(\d+)/(\d+)/(\d\d\d\d)', '\\2.\\1.\\3', text)
text = re.sub(r'В (\d\.\d+\.\d+ в \d\d:\d\d)', 'В 0\\1', text)
text = re.sub(r'(В \d+\.)(\d\.\d+ в \d\d:\d\d)', '\\g<1>0\\g<2>', text)

text = re.sub(r'\n\t*<blockquote class="ipsQuote"[\s\S]+?(В (\d+\.\d+\.\d+ в \d\d:\d\d)[\s\S]+?do=hovercard"[\s\S]*?>([\S ]+?)</a>|Цитата)[\s\S]+?"Развернуть"[\s\S]*?>', quoteHeaderLeft + '\\3, \\2' + quoteHeaderRight, text)
text = re.sub(r'<div class="quoteHeader">, </div>', '<div class="quoteHeader">Цитата</div>', text)
text = re.sub(r'</div>[ \t]+<a class="ipsTruncate_more"[\s\S]+?</a>', '</div>', text)
text = re.sub(r'\n\t*</div>\s*\n\t*</blockquote>', quoteEnd, text)

text = re.sub(r'<br>\n\t*', '<br>', text)
text = re.sub(r'<a contenteditable="false"[\s\S]+?>@([\S ]+?)</a>', '<span class="ping">\\1</span>', text)

text = re.sub(r'\n\t*(<p[\s\S]*?>)', '\n\t\t\t\t\t\\1', text)
text = re.sub(r'\n\t*<div class="ipsSpoiler"[\s\S]+?data-ipsspoiler-option="([\s\S]+?)"[\s\S]+?<div class="ipsSpoiler_contents"[\s\S]+?>(\n[\s\S]+?)\n\t*</div>\n\t*</div>', quoteHeaderLeftClosed + '\\1' + quoteHeaderRight + '\\2' + quoteEnd, text)

text = re.sub(r' rel=""', '', text)
text = re.sub(r' data-[a-z-]+="[\s\S]*?"', '', text)
text = re.sub(r' class="ipsImage ipsImage_thumbnailed" height="\d+" style="height:auto;"', '', text)
text = re.sub(r' class="ips[\S ]+?"', '', text)
text = re.sub(r'(href="https://www.strategium.ru/forum/topic/\d+)\S+?/', '\\1--/', text)
text = re.sub(r'&amp;((comment|mid)=\d+")', '&\\1', text)

text = re.sub(r'<a href="https://reklama-no\.ru/smiles/lyulka\.gif[\s\S]+?</a>', '<img src="../img/lyulka.gif" alt="lyulka.gif">', text)
text = re.sub(r'<a href="https://reklama-no\.ru/smiles/cossacks\.gif[\s\S]+?</a>', '<img src="../img/cossacks.gif" alt="cossacks.gif">', text)

#for emoji in emojis:
#    pattern = r'<img[\S ]+?alt="' + emoji + r'[\s\S]*?>'
#    text = re.sub(pattern, '<img class="emoji" src="../img/emoji/' + emojis[emoji][0] + '.' + emojis[emoji][1] + '" alt=":' + emojis[emoji][0] + ':">', text)

text = re.sub(r'<iframe[^>]+?comment=(\d+)[^>]+?></iframe>', '\t\t\t\t\t<a class="linkBox" href="https://www.strategium.ru/forum/index.php?app=core&module=system&controller=content&do=find&content_class=forums_Topic&content_commentid=\\1">\n\t\t\t\t\t\t<div class="linkText">\n\t\t\t\t\t\t\t<p class="linkTopic"></p>\n\t\t\t\t\t\t\t<p class="linkTime"></p>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t<span class="linkArrow"></span>\n\t\t\t\t\t</a>', text)

result = open('result_html.txt', 'w', encoding="utf-8")
result.write(text)
result.close()

result = open('result_html.txt', 'r', encoding="utf-8")
base = result.readlines()
result.close()

indentFlag = False
for i in range(len(base)):
    if "quoteBody" in base[i]:
        indentFlag = True
        #print("Flag set at line:")
        #print(line)
        continue
    if indentFlag and "/blockquote" in base[i]:
        indentFlag = False
        #print("Flag cleared at line:")
        #print(line)
    #if indentFlag:
        #print(line)
    if indentFlag and "\t<" in base[i] and not "</div>" in base[i]:
        base[i] = '\t\t' + base[i]
        #print(line)

del base[0]
del base[-1]

result = open('result_html.txt', 'w', encoding="utf-8")
result.writelines(base)
result.close()
