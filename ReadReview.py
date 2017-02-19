import requests
import re
import csv

def readData(offset):
    apiurl = "https://api.bazaarvoice.com/data/batch.json?passkey=e8bg3vobqj42squnih3a60fui&apiversion=5.5&displaycode=6543-en_us&resource.q0=reviews&filter.q0=isratingsonly%3Aeq%3Afalse&filter.q0=productid%3Aeq%3Adev5800066&filter.q0=contentlocale%3Aeq%3Aen_US&sort.q0=rating%3Adesc&stats.q0=reviews&filteredstats.q0=reviews&include.q0=authors%2Cproducts%2Ccomments&filter_reviews.q0=contentlocale%3Aeq%3Aen_US&filter_reviewcomments.q0=contentlocale%3Aeq%3Aen_US&filter_comments.q0=contentlocale%3Aeq%3Aen_US&limit.q0=100&offset.q0="+str(offset)+"&limit_comments.q0=3&callback=bv_1111_63938"
    response = requests.get(apiurl)
    response_raw = response.content
    #print response_raw
    titles = re.findall(r'"Title":"[\w\s0-9_.\.\-,@#!*&()%:;\?\'{}\+\\<>\$\[\]\*\/=\^`~]+"',response_raw)[:100]
    #print titles
    names = re.findall(r'"UserNickname":"[\w\s0-9_.\.\-,@#!*&()%:;\?\'{}\+\\<>\$\[\]\*\/=\^`~]+"',response_raw)[:100]
    time = re.findall(r'"SubmissionTime":"[0-9-\w:]+',response_raw)[:100]
    reviews = re.findall(r'"ReviewText":"[\w\s0-9_.\.\-,@#!*&()%:;\?\'{}\+\\<>\$\[\]\*\/=\^~`]+"',response_raw)[:100]
    data_tmp=[]
    try:
        for i in range(0,100):
            tmp = []
            tmp.append("Galaxy-s7")
            #print titles[i]
            tmp.append(titles[i][len('"Title":"'):len(titles[i])-1])
            tmp.append(reviews[i][len('"ReviewText":"'):len(reviews[i])-1])
            tmp.append(time[i][len('"SubmissionTime":"'):len(time[i])-1])
            tmp.append(names[i][len('"UserNickname":"'):len(names[i])-1])
            data_tmp.append(tmp)
    except IndexError:
        pass
    return data_tmp

data = []
for i in range(0,5000,100):
    data += readData(i)
with open('Galaxy-s7.csv', 'wb') as csvfile:
        #fieldnames = ['Device','Title','ReviewText','SubmissionText','UserNickname']
        writer = csv.writer(csvfile)
        writer.writerow(['Device','Title','ReviewText','SubmissionText','UserNickname'])
        writer.writerows(data)
