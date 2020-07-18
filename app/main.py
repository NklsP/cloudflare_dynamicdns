import time
import bll

configData = bll.ConfigData('./config.cfg', 'main-config')

while True:
    ip = bll.ip(configData.name)

    if ip.current_ip != ip.dns_ip:
        bll.updateIP(configData.email, configData.key, configData.name, ip.current_ip)

    time.sleep(configData.interval)