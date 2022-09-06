def remove_url_anchor(url):
    return url[: url.find('#') if url.find('#')>0 else len(url)]
