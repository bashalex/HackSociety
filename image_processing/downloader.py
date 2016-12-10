import requests

for i in range(200):
    response = requests.get("http://rockthehackathons.com:5000/api/fax?app=something").content
    with open('images/image{}.png'.format(i), 'bw') as f:
        f.write(response)
        print("image {} downloaded".format(i))
