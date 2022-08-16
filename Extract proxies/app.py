import requests
from bs4 import BeautifulSoup

url = "https://free-proxy-list.net/"  # proxy providing website
req = requests.get(url) #send request to website
print(f"RESPONSE FROM WEBSITE {req}") #send rsponse from website

soup = BeautifulSoup(req.text, "html.parser") #parse the response
table = soup.find("table") #table from website
all_rows = table.find_all("tr") #get all the rows from table

#get the proxies
def getproxy(n):                   
    tr = table.find_all('tr')[n]  #get the nth row of table
    ip = tr.find_all("td")[0].get_text() #get the text of first column
    port = tr.find_all("td")[1].get_text() #get the text of second column
    return f"{ip}:{port}" #return ip and port combinely 


txt = ""
for i in range(101):
    # print("finding")
    if i == 0:
        continue
    if i == 1:
        txt = txt + f"{getproxy(i)}"
    else:
        txt = txt + f"\n{getproxy(i)}"


with open("proxy.txt", "w+") as f:
    f.write(txt)
print("text file is written")
    # print("following code is written")

with open("proxy.txt", "r") as t:
    text = t.read()
    # print(f"\n\n\n\n###############\n{text}\n##################\n\n\n\n")
    ans = text.split("\n")

print(f"WE HAVE ADDED {len(ans)} PROXIES TO PROXIES.TXT")
