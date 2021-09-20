# Import Libraries
import requests # gets the information from the site
from bs4 import BeautifulSoup # html parser
import time
from random import randrange


# Create headers & params in order to bypass blocking
headers = {
    'authority': 'www.skroutz.gr',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome"; v="83"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cookie': '_helmet_couch=eyJzZXNzaW9uX2lkIjoiNjgzNzhmMmNmNjI5OTcxNjI5NzU2ZWNmMTM5MzE5MmIiLCJidWNrZXRfaWQiOiJmNTk1ZGRhYy00ZmVhLTQ5NmYtODNkNS00OWQzODgzMWFhYTAiLCJsYXN0X3NlZW4iOjE1OTEyNjgwNTUsInZvbCI6MSwiX2NzcmZfdG9rZW4iOiI1a3Yxb3FKTmhXTCs1YUxzdjYzRFk3TlNXeGs5TlhXYmZhM0UzSmtEL0NBPSJ9--22dfbfe582c0f3a7485e20d9d3932b32fbfb721b',
    'if-none-match': 'W/"e6fb8187391e99a90270c2351f9d17cd"',
}
params = (
    ('o', '\u039C\u03C0\u03BF\u03C5\u03C1\u03BD\u03BF\u03CD\u03B6\u03B9 Guy Laroche Linda Red'),
)



#=====================================================================
# Funtions
#=====================================================================

def perBookPage(url):
    time.sleep(randrange(5))
    result = requests.get(url, headers=headers, params=params)
    soup = BeautifulSoup(result.text,'lxml')

    cnt = soup.findAll('div',{'id':"centerCol"})

    title       = cnt[0].findAll('span',{'id':"productTitle"})[0].text 
    subtitle    = cnt[0].findAll('span',{'id':"productSubtitle"})[0].text 
    review_avg  = cnt[0].findAll('span',{'class':"a-icon-alt"})[0].text

    print("Title: " + title.replace("\n", ""))
    print("Subtitle: " + subtitle.replace("\n", ""))
    print("Review Average: " + review_avg.replace("\n", ""))
    print("-----------------------------------")

#=====================================================================
# Start
#=====================================================================


# connect to the site
url = "https://www.amazon.com/s?bbn=4&rh=n%3A2578998011%2Cp_n_feature_five_browse-bin%3A6118623011&dc&qid=1609620292&rnid=2578998011&ref=lp_4_nr_p_n_feature_five_browse-bin_0"
result = requests.get(url, headers=headers, params=params)

# check if connection was made properly
print("Request status: " + str(result.status_code) + " (200=good)")
print(url)

# parse site
soup = BeautifulSoup(result.text,'lxml')

# find left job postings
div = soup.findAll('div',{'class':"s-main-slot s-result-list s-search-results sg-row"})


print(len(div))

booklist = []

for x in div:
    tmp = x.findAll('a', {'class':"a-link-normal a-text-normal"})
    
    for i in tmp:
        booklink = i.get('href')
        if(booklink.endswith("kindle_edition") == False):
            booklist.append("http://amazon.com" + booklink)

print(len(booklist))

for url in booklist:
    perBookPage(url)

