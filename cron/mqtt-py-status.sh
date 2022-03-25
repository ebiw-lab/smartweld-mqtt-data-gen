#check if index.py is running if not star
if pgrep -f send_to_mqtt_multiple-devices.py >/dev/null 2>&1
then
echo 'mqtt send_to_mqtt_multiple-devices.py running'
else
echo 'mqtt send_to_mqtt_multiple-devices.py stopped, starting ....'
python3.7 -m virtualenv venv
source venv/bin/activate

cd send-data-to-mqtt-python
nohup python3 send_to_mqtt_multiple-devices.py > mqtt_data_gen.log &
fi