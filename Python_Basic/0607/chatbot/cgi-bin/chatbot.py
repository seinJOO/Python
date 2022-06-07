# python -m http:server --cgi 8888

#!/usr/bin/env python3
import cgi, sys, asyncio
from botengine import make_reply


# 입력 양식의 글자 추출하기 --- (※1)
form = cgi.FieldStorage()

# 메인 처리 --- (※2)
def main():
    m = form.getvalue("m", default="")
    if   m == "" : show_form()
    elif m == "say" : api_say()

# 사용자의 입력에 응답하기 --- (※3)
def api_say():
    print("Content-Type: text/plain; charset=euc-kr\r\n")
    print("")
    txt = form.getvalue("txt", default="")
    if txt == "": return
    res = make_reply(txt)
    print(res)

# 입력 양식 출력하기 --- (※4)
def show_form():
    print("Content-Type: text/html; charset=euc-kr\r\n")
    print("""
    <html lang="ko">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=euc-kr">
    </head>
    <body>
    <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
    <style>
        h1   { background-color: #ffe0e0; }
        div  { padding:10px; }
        span { border-radius: 10px; background-color: #ffe0e0; padding:8px; }
        .bot { text-align: left; }
        .usr { text-align: right; }
    </style>
    <h1>대화하기</h1>
    <div id="chat"></div>
    <div class='usr'><input id="txt" size="40">
    <button onclick="say()">send</button></div>
    <script>
    var url = "./chatbot.py";
    function say() {
      var txt = $('#txt').val();
      $.get(url, {"m":"say","txt":txt},
        function(res) {
          var html = "<div class='usr'><span>" + esc(txt) +
            "</span>: Me</div><div class='bot'> Bot:<span>" + 
            esc(res) + "</span></div>";
          $('#chat').html($('#chat').html()+html);
          $('#txt').val('').focus();
        });
    }
    function esc(s) {
        return s.replace('&', '&amp;').replace('<','&lt;')
                .replace('>', '&gt;');
    }
    </script></body></html>
    """)

asyncio.run(main())