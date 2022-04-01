def crawling(url, dic) :
    import urllib ; import pickle ; from bs4 import BeautifulSoup ; from data.textclean import cleaning
    data = urllib.request.urlopen(url)
    data = data.read()
    data = data.decode('euc-kr')
    data = BeautifulSoup(data, 'html.parser')
    data = data.select('.list_body a')
    hdls = []
    for x in data :
        if x.string :
            hdls.append(x.string.strip())
    hdls = [cleaning(row) for row in hdls]
    for line in hdls :
        for word in line.split() :
            if len(word) > 1 :
                dic[word] = dic.get(word,0) + 1
    return dic