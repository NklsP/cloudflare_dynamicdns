import requests
import configparser
import time

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
    
    # print(name)
    
    head = {'X-Auth-Email': email, 'X-Auth-Key': key}
    zone_id = requests.get("https://api.cloudflare.com/client/v4/zones?name=" + name, headers=head).json()['result'][0]['id']
    
    # print(zone_id)
    
    dns_records = requests.get("https://api.cloudflare.com/client/v4/zones/" + zone_id + "/dns_records", headers=head).json()['result']
    
    for record in dns_records:
        if record['type'] == 'A':
            data = {'type':record['type'],'name':record['name'],'content':ip,'ttl':record['ttl'],'proxied':record['proxied']}
            update_record = requests.put("https://api.cloudflare.com/client/v4/zones/" + zone_id + "/dns_records/"+ record["id"], headers=head, json=data).json()
           # print(update_record)
    
    print("Updated dns record")

    time.sleep(10)

