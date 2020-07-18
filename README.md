# Cloudflare Dynamic DNS

1. Clone the repo
2. Rename default_config.cfg to config.cfg
3. Complete the config file
4. Build the container

```
docker build -t cloudflare_dynamicdns_dynamic_dns:latest .
```

5. Run the container

```
docker-compose up -d --force-recreate
```

