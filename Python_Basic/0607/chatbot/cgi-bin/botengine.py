
# 1. botengine.py : 모듈을 생성(라이브러리) -> 마르코프 체인을 이용
import codecs
from bs4 import BeautifulSoup
from aiohanspell import spell_checker
from konlpy.tag import Twitter, Okt
import os, re, json, random

dict_file = "chatbot-data.json"
dic = {}
twitter = Twitter()

# 딕셔너리에 단어 등록
def register_dic(words):
    global dic
    if len(words) == 0 : return
    tmp=["@"]
    for i in words:
        word = i[0]
        if word == "" or word == "\r\n" or word == "\n":continue
        tmp.append(word)
        if len(tmp) < 3: continue
        if len(tmp) > 3: tmp = tmp[1:]
        set_word3(dic, tmp)
        if word == "." or word == "?":
            tmp = ["@"]
            continue
    # 딕셔너리가 변경될 때마다 저장
    json.dump(dic, open(dict_file,"w",encoding="utf-8"))

# 딕셔너리에 글 등록하기
def set_word3(dic,s3):
    w1, w2, w3 = s3
    if not w1 in dic: dic[w1] = {}
    if not w2 in dic[w1]: dic[w1][w2] = {}
    if not w3 in dic[w1][w2]: dic[w1][w2][w3] = 0
    dic[w1][w2][w3] += 1
        
# 문장 만들기 
def make_sentence(head):
    ret = []
    if not "@" in head: return ""
    if head != "@" : ret.append(head)
    top = dic[head]
    w1 = word_choice(top)
    w2 = word_choice(top[w1])
    ret.append(w1)
    ret.append(w2)
    while True:
        if w1 in dic and w2 in dic[w1]:
            w3 = word_choice(dic[w1][w2])
        else:
            w3 = ""
        ret.append(w3)
        if w3 == "." or w3 =="?" or w3 == "":break
        w1, w2 = w2, w3
    ret = "".join(ret)
    return ret

def word_choice(sel):
    keys = sel.keys()
    return random.choice(list(keys))

async def spell(text):
    re = await spell_checker.check(make_sentence(face))
    return re.checked

## 챗봇 응답 만들기 
def make_reply(text):
    # 단어 학습 시키기
    if not text[-1] in [".","?"]: text += "."
    words = twitter.pos(text)
    register_dic(words)
    ## 사전에 단어 있다면 그것을 기반으로 문장 만들기를 작업
    for word in words:
        face = word[0]
        if face in dic: return spell(make_sentence(face))
    return make_sentence("@")

# 딕셔너리가 있다면 읽어 들이기
if os.path.exists(dict_file):
    dic = json.load(open(dict_file,"r",encoding="utf-8"))