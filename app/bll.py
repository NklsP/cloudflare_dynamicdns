import configparser
import requests
import socket

<<<<<<< HEAD:app/bll.py
class ConfigData:
    def __init__(self, path, config):
        cp = configparser.RawConfigParser()
        configFilePath = path
        cp.read(configFilePath)

        self.name = cp.get(config, 'name')
        self.email= cp.get(config, 'email')
        self.key = cp.get(config, 'key')
        self.interval = int(cp.get(config, 'interval'))

class ip:
    def __init__(self, name):
        self.current_ip = requests.get('https://api.ipify.org?format=json').json()["ip"]
        self.dns_ip = socket.gethostbyname(name)    

def updateIP(email, key, name, ip):
=======
while True:
    # Get own ip
    ip = requests.get('https://api.ipify.org?format=json').json()["ip"]
    
    # print(ip)
    
    ## Get zone
    cp = configparser.RawConfigParser()
    configFilePath = './config.cfg'
    cp.read(configFilePath)
    
    name = cp.get('main-config', 'name') 
    email= cp.get('main-config', 'email') 
    key = cp.get('main-config', 'key') 
    update_time = cp.get('main-config', 'update_time')
    
    # print(name)
    
>>>>>>> 71a05f0f30e8485c816e7d13a4fd61ddb8e2d567:main.py
    head = {'X-Auth-Email': email, 'X-Auth-Key': key}
    zone_id = requests.get("https://api.cloudflare.com/client/v4/zones?name=" + name, headers=head).json()['result'][0]['id']
        
    dns_records = requests.get("https://api.cloudflare.com/client/v4/zones/" + zone_id + "/dns_records", headers=head).json()['result']
    
    for record in dns_records:
        if record['type'] == 'A' and record['name'] == name:
            data = {'type':record['type'],'name':record['name'],'content':ip,'ttl':record['ttl'],'proxied':record['proxied']}
            update_record = requests.put("https://api.cloudflare.com/client/v4/zones/" + zone_id + "/dns_records/"+ record["id"], headers=head, json=data).json()
<<<<<<< HEAD:app/bll.py
=======
           # print(update_record)
    
    print("Updated dns record")

    time.sleep(int(update_time))

>>>>>>> 71a05f0f30e8485c816e7d13a4fd61ddb8e2d567:main.py
