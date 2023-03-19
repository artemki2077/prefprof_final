import requests


r = requests.get('https://dt.miet.ru/ppo_it_final', headers={"X-Auth-Token": "629q2skt"})
print(r.text)