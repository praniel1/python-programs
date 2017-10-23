import urllib
import requests
url1='https://kp.christuniversity.in/KnowledgePro/images/StudentPhotos/'
url2='.jpg?2014-07-23%2010:46:41.0'
count = 1
file = 1
file_name='Images/file'
file_ex='.jpg'
while(count<105900):
    url3 = url1 + `count` + url2
    files = file_name + `count` + file_ex
    resource = urllib.urlopen(url3)
    r = requests.get(url3)
    if(r.status_code !=404):
        ut = open(files,"wb")
        print url3
        ut.write(resource.read())
    count+=1

ut.close()