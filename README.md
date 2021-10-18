# Crypto_TSDB

## Getting Started

Crypto currency prices are fetched from [Alpha Vantage](https://github.com/RomelTorres/alpha_vantage)

### Local setup

```bash
docker-compose up -d
psql -h localhost -d postgres -U postgres

export API_KEY='aaabbbcccddd' # Request Alpha Vantage API Key here: https://www.alphavantage.co/support/#api-key
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
5. Setup Kafka 
