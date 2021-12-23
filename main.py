import requests
import threading

url = "https://GG-Feedback.garuda3141.repl.co"

location = {'lat':9.795678,'lon':14.841446,'mood':'good'}

def do_req():
    for j in range(100):
        data = location
        requests.post(url, allow_redirects=False, data={
                'location': data
            })
        print(location, j)
threads = []
for i in range(20):
    t = threading.Thread(target=do_req)
    t.daemon = True
    threads.append(t)
for i in range(20):
    threads[i].start()
for i in range(20):
    threads[i].join()