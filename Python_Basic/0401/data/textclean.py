def cleaning(text) :
    import re
    text_re = re.sub("[-=+,#/\?:^$.·@*\"※~&%ㆍ℃!』\\‘∼’|\(\)\[\]\<\>`\'‥…》]", ' ', text)
    text_re = ' '.join(text_re.split())
    return text_re



    
