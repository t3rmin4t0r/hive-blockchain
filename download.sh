DT=$(date --date yesterday "+%Y-%m-%d")
# remove rate limit if you're not fussy about bandwidth
wget --limit-rate=2M -c http://dumps.webbtc.com/bitcoin/bitcoin_${DT}.sql.gz 
