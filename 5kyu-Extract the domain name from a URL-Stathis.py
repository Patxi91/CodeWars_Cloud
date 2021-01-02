def domain_name(url):
    first=url.find(':')
    url=url.replace('www.','')
    second=url.find('.')
    result = ''
    for i in url[first+1 : second]:
        result=result+ i
        result=result.replace('/','')
    return result
