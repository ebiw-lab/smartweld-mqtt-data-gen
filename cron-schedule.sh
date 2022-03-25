dt=$(date +%Y-%m-%d)
echo "$dt"
# generate cron-schedule
file_index=cron/mqtt-py-status.sh
# pwd
#chmod -R 777 cron/*.sh
crontab -l
echo "* * * * * $(pwd)/${file_index} >> $(pwd)/mqtt_data_gen_job_\`date +\%Y-\%m-\%d\`.log 2>&1" | crontab -
crontab -l
sudo service cron reload

