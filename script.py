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
    "Січовик" : ["80242.jpg", "ua"]
}
emojis = {
    ":\)" : ["smile", "png"],
    ":D" : ["grin", "png"],
    ":\(" : ["sad", "png"],
    ":mad:" : ["mad", "gif"],
    ":ex:" : ["ex", "gif"],
    "o\.O" : ["huh", "png"],
    ":001:" : ["devil", "gif"],
    ":Cherna-facepalm:" : ["facepalm", "gif"],
    ":madness:" : ["madness", "gif"],
    ":108196:" : ["ready", "gif"],
    ":winner2:" : ["winner", "gif"],
    ":good:" : ["good", "gif"],
    ";\)" : ["wink", "png"],
    ":103282:" : ["thumbsdown", "gif"],
    ":103338:" : ["ok", "gif"],
    "\^\_\^" : ["happy", "png"],
    ":laughingxi3:" : ["rofl", "gif"],
    ":drink:" : ["sip", "gif"],
    ":boy-cleanglasses:" : ["cleanglasses", "gif"],
    ":smile37:" : ["think", "gif"],
    ":time:" : ["time", "gif"]
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
messageEnd = '\t\t\t\t</article>\n\t\t\t</section>\n'
quoteHeaderLeft = '\t\t\t\t\t<blockquote>\n\t\t\t\t\t\t<div class="quoteHeader">'
quoteHeaderLeftClosed = '\t\t\t\t\t<blockquote class="closedQuote">\n\t\t\t\t\t\t<div class="quoteHeader">'
quoteHeaderRight = '</div>\n\t\t\t\t\t\t<div class="quoteBody">'
emojiBlank = '<span class = "emoji emoji-{}"></span>'

source = open('source.txt', 'r', encoding="utf-8")
text = source.read()
source.close()

for user in users:
    pattern = user + "\n" + user + "\n\nОтветил: "
    text = re.sub(pattern, messageHeaderLeft.format(users[user][0], user, users[user][1], user), text)

text = re.sub('(\d\d\.\d\d\.\d\d\d\d, \d\d:\d\d:\d\d)', '\\1' + messageHeaderRight, text)
text = re.sub('(\t\t\t<section)', messageEnd + '\\1', text)
text = re.sub(messageEnd, '', text, 1)
text = text + '\n' + messageEnd

for time in times:
    pattern = times[time][0] + ":(\d\d) " + times[time][1]
    text = re.sub(pattern, time + ":\\1", text)

text = re.sub('\n \n', '\n&nbsp;\n', text)
text = re.sub('(\d+)/(\d+)/(\d\d\d\d)', '\\2.\\1.\\3', text)
text = re.sub('     \n    В (\d+\.\d+\.\d+ в \d\d:\d\d), ([\S ]+) сказал:', quoteHeaderLeft + '\\2, \\1' + quoteHeaderRight, text)
text = re.sub('\n      Цитата\n', '\n' + quoteHeaderLeft + 'Цитата' + quoteHeaderRight + '\n', text)
text = re.sub('\n  ([^\r\n]+) \(Скрыть\)\n', '\n' + quoteHeaderLeftClosed + '\\1' + quoteHeaderRight + '\n', text)
text = re.sub('(\n    )([\s\S]+?\n)(\n\S)', '\n\\2\t\t\t\t\t\t</div>\n\t\t\t\t\t</blockquote>\\3', text)
text = re.sub(', (\d\.\d+\.\d+ в \d\d:\d\d)', ', 0\\1', text)
text = re.sub('(, \d+\.)(\d\.\d+ в \d\d:\d\d)', '\\g<1>0\\g<2>', text)
text = re.sub('\n\s*\n', '\n', text)
text = re.sub('\n([^\t<])', '\n\t\t\t\t\t<p>\\1', text)
text = re.sub('<p>    ', '\t\t<p>', text)
text = re.sub('(<div class="quoteBody">[\s\S]+?)<p>([\s\S]+?</blockquote>)', '\\1\t\t<p>\\2', text)
text = re.sub('([^>])\n', '\\1</p>\n', text)
text = re.sub('@([^\s\.,;:?!<]+)', '<span class="ping">\\1</span>', text)
text = re.sub('https://reklama-no\.ru/smiles/lyulka\.gif', '<img src="../img/lyulka.gif" alt="lyulka.gif">', text)
text = re.sub('https://reklama-no\.ru/smiles/cossacks\.gif', '<img src="../img/cossacks.gif" alt="cossacks.gif">', text)
text = re.sub('(https?://[^\s<]+)', '<a href="\\1">\\1</a>', text)
for emoji in emojis:
    text = re.sub(emoji, '<img class="emoji" src="../img/emoji/' + emojis[emoji][0] + '.' + emojis[emoji][1] + '" alt=":' + emojis[emoji][0] + ':">', text)
text = re.sub('([^а-я])(ИМХО|имхо)([^а-я])', '\\1<abbr title="по моему скромному мнению">\\2</abbr>\\3', text)
text = re.sub('([^а-я])(ИРЛ|ирл)([^а-я])', '\\1<abbr title="в реальной жизни">\\2</abbr>\\3', text)

text = text[1:][:-1]

result = open('result.txt', 'w', encoding="utf-8")
result.write(text)
result.close()
