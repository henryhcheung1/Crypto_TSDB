# Crypto_TSDB

## Getting Started

### Local setup

```bash
docker-compose up -d
psql -h localhost -d postgres -U postgres
```



### Cleaning up
```bash
docker-compose down
```

### TODO:

1. Setup monitoring with Prometheus & Grafana dashboards
2. Investigate Promscale
3. Deploy into Kubernetes
4. Cronjob for fetching crypto data


### References:

https://docs.timescale.com/timescaledb/latest/tutorials/analyze-cryptocurrency-data/#set-up-the-schema