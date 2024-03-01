photosync
===

```
(crontab -l 2>/dev/null; echo "*/5 * * * * /usr/local/bin/python3 $PWD/sync.py >> $PWD/cron.log 2>&1") | crontab -
```
