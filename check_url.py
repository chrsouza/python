import requests 

def url_ok(url):
    r = requests.head(url)
    return r.status_code == 200

def url_statuscode(url):
    r = requests.head(url)
    return r.status_code

url = "https://www.google.com.br" 
#print(url_ok("https://www.uol.com.br"))

print("URL: ", url)
print("Status code: ", url_statuscode(url))
