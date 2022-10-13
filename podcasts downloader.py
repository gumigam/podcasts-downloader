#imports required libraries
import feedparser
import requests
import os
 
#get user inputs
pod_link = input("rss feed link : ")
max_loop = input("The maximum number of podcasts to download : ")
 
#parsing the rss file
print("parsing the rss file...")
feed = feedparser.parse(pod_link)
 
#validating the feed
if feed['feed'] == {}:
    raise RuntimeError("Something bad happened")
 
#initialize the counter
loop = 0
 
#preparing the log file
if not os.path.exists("pod_list.lst"):
    f = open("pod_list.lst", 'w')
    f.close()
pod_list = open("pod_list.lst", 'r+')
pod_list.write("new session" + '\n')
content = pod_list.read()
current_pods = []
 
#starts working
for entry in feed.entries:
    link = entry.links[0]
    link1 = link["href"]
    pod_title = entry.title
    if not loop == int(max_loop):
        if link1 in content:
            print("skipping podcast number" + str(loop+1))
            loop += 1
            continue
        else:
            print("downloading podcast number " + str(loop+1))
            podcast = requests.get(link1)
            open(pod_title + ".mp3", 'wb').write(podcast.content)
            current_pods += link1+'\n'
    else:
        break

    loop += 1

with open("pod_list.lst", 'a') as f:
    for line in current_pods:
        f.write(f"{line}")