pgrep -f send_to_mqtt_multiple-devices.py
pkill -f send_to_mqtt_multiple-devices.py

cd send-data-to-mqtt-python
nohup python3 send_to_mqtt_multiple-devices.py > ../mqtt_gen_data.log &
cd ..

pgrep -f send_to_mqtt_multiple-devices.py

sh ./cron-schedule.sh
