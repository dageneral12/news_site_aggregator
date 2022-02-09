from bs4 import BeautifulSoup
import requests
import json
import datetime


CURRENT_DATETIME = datetime.datetime.now()


#news_api_key = '4f641ee2e5894fa981870a8f6c0cf758'

#guardian api key
g_api_key = "8e20101f-8f30-48e2-be9a-8f4d7a843d1d"

#endpoints per each country
URL_GERMANY = "https://content.guardianapis.com/search?q=germany"
URL_US = "https://content.guardianapis.com/search?q=america"
URL_UK = "https://content.guardianapis.com/search?q=britain"
URL_RUSSIA = "https://content.guardianapis.com/search?q=russia"

headers = {
        "api-key": g_api_key,
        "format": "json"
        }


#get initial article from Guardian API:
def get_guardian_content(url, g_api_key, headers):

    response = requests.get(url, headers=headers)

    json_context = json.loads(response.text)        # print(response.text)
    
    return json_context

def get_articles():
    temp_dict = get_guardian_content['response']['results']
    temp_list = []
    keys = ['webUrl', 'webPublicationDate']

    for i in temp_dict:
        for key in keys:
            j = i.get(key)
            temp_list.append(j)
            
    return temp_list


# how to decide, which news to overwrite?
# check what the latest date in db is and the title (create a dictionary out of title:date_db and title:date_new and compare)

# we need to add 'apiUrl' as well to check for publication date (add that logic : if publication date > today, don't store the results)


# pull only titles and time stamps to compare with what we have in db


# convert data into dictionary
def get_articles():
    temp_list = get_articles()
    dict_to_check = {temp_list[i]: temp_list[i + 1]
                for i in range(0, len(temp_list), 2)}
    url2 = temp_list[0]
    response2 = requests.get(url=url2, headers=headers)
    soup = BeautifulSoup(response2.text, 'html.parser')
    list_of_ps = (soup.find_all('p'))

    list_w_text = []
    # print/append raw text clean without the tags
    for j in list_of_ps:
        list_w_text.append(j.get_text())


# print(type(json_context['response']['results'][0]))


# print(response2.text)




# print(soup.find_all(
#    class_='article-body-commercial-selector article-body-viewer-selector  dcr-ucgxn1"'))


# print(soup.find_all(id='mainconent'))

# get all the text within the tags 'p'


# print(list_w_text)
# print(CURRENT_DATETIME)

print(dict_to_check)




#---- Request to summarizer api

#SUMMARIZER_API_KEY = ''

def request_summary(db_txt):
    r = requests.post(
        "https://api.deepai.org/api/summarization",
        data={
            'text': db_txt,
        },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
)
    return r.json()