import paho.mqtt.client as mqtt
import json
import ast
import random
import time
import pandas as pd


from datetime import datetime as dt, timezone , timedelta

import configparser


def count():
    count.counter += 1
    return count.counter


def get_random_words(words_list):
    return words_list[random.randint(0, len(words_list)-1)]



def generate_data_array(hardware_id, dateinstance):

    # list to store JSON records
    # payload = {
    #               "type": "",
    #               "data": {
    #                 "mstatus": "",
    #                 "cur": "",
    #                 "volt": "",
    #                 "rpm": "",
    #                 "gasFR": "",
    #                 "hstemp": "",
    #                 "ambtemp": "",
    #                 "oid": "",
    #                 "dis": "",
    #                 "network": "",
    #                 "tm": ""
    #               }
    #             }

    payload = {
                  "d": [
                        {
                          "tag": "mstatus",
                          "value": ""                        
                        },
                        {
                          "tag": "tm",
                          "value":  ""                       
                        },
                        {
                          "tag": "current",
                          "value":   ""                       
                        },
                        {
                          "tag": "voltage",
                          "value": ""                         
                        },
                        {
                          "tag": "gasfr",
                          "value":  ""                        
                        },
                        {
                          "tag": "ambtemp",
                          "value": ""                        
                        },

                        {
                          "tag": "humidity",
                          "value": ""                       
                        },
                        {
                          "tag": "jointno",
                          "value": ""                         
                        },
                        {
                          "tag": "chuckspeed",
                          "value": ""                       
                        },
                        {
                          "tag":   "plc",
                          "value":   ""                     
                        },
                        {
                          "tag": "SYS_DATACARD_CAPACITY",
                          "value": ""                       
                        },
                        {
                          "tag": "SYS_DATACARD_FREE_SPACE",
                          "value":  ""                      
                        },
                        {
                          "tag": "DATALOG_ENABLE",
                          "value": ""                       
                        },
                        {
                          "tag": "DATALOG_ERROR",
                          "value":  ""                      
                        },
                        {
                          "tag": "oid",
                          "value":  ""                      
                        },
                        {
                          "tag": "dis",
                          "value": ""                       
                        },
                        {
                          "tag": "network",
                          "value": ""                       
                        }
                    ]
                }

    
    #Initialization
    mstatus                     =     ['1','0']
    current                     =     ''
    voltage                     =     ''
    gasfr                       =     ''
    ambtemp                     =     ''
    humidity                    =     ''
    jointno                     =     ''
    chuckspeed                  =     ''
    plc                         =     ['1','0']
    SYS_DATACARD_CAPACITY       =     '7948206080.00'
    SYS_DATACARD_FREE_SPACE     =     '7673053184.00'
    DATALOG_ENABLE              =     ['1','0']
    DATALOG_ERROR               =     '6'
    oid                         =     ''
    dis                         =     ''
    network                     =     ''





    #Assigning generated values to payload
    #payload['d'][0]['value'] = dateinstance.strftime('%Y-%m-%d %H:%M:%S')


    payload['d'][0]['value'] = get_random_words(mstatus) 

    if payload['d'][0]['value'] == 'stop':
        payload['d'][0]['value'] = get_random_words(mstatus)

    if payload['d'][0]['value'] == 'stop':
        payload['d'][0]['value'] = get_random_words(mstatus)

    if payload['d'][0]['value'] == 'stop':
        payload['d'][0]['value'] = get_random_words(mstatus)

    #Generating tm
    payload['d'][1]['value'] = dateinstance.strftime('%Y-%m-%d %H:%M:%S')

    #Generating current
    if payload['d'][0]['value'] == '1':
        current = random.randint(80, 90)   
    payload['d'][2]['value'] = str(current)

    #Generating voltage
    if payload['d'][0]['value'] == '1':
        voltage = random.randint(18, 24)   
    payload['d'][3]['value'] = str(voltage)

    #Generating gasfr
    if payload['d'][0]['value'] == '1':
        gasfr = random.randint(18, 22)   
    payload['d'][4]['value'] = str(gasfr)

    #Generating ambtemp
    if payload['d'][0]['value'] == '1':
        ambtemp = random.randint(27, 30)   
    payload['d'][5]['value'] = str(ambtemp)  

    #Generating humidity
    if payload['d'][0]['value'] == '1':
        humidity = random.randint(40, 90)   
    payload['d'][6]['value'] = str(humidity)

    #Generating jointno
    if payload['d'][0]['value'] == '1':
        jointno = random.randint(1, 100)   
    payload['d'][7]['value'] = str(jointno)

    #Generating chuckspeed
    if payload['d'][0]['value'] == '1':
        chuckspeed = random.randint(4, 10)   
    payload['d'][8]['value'] = str(chuckspeed)

    #Generating plc
    if payload['d'][0]['value'] == '1':
        payload['d'][9]['value'] = get_random_words(plc)

    #Generating SYS_DATACARD_CAPACITY
    if payload['d'][0]['value'] == '1':
        payload['d'][10]['value'] = str(SYS_DATACARD_CAPACITY)

    #Generating SYS_DATACARD_FREE_SPACE
    if payload['d'][0]['value'] == '1':
        payload['d'][11]['value'] = str(SYS_DATACARD_FREE_SPACE)

    #Generating DATALOG_ENABLE
    if payload['d'][0]['value'] == '1':
        payload['d'][12]['value'] = str(get_random_words(DATALOG_ENABLE))

    #Generating DATALOG_ERROR
    if payload['d'][0]['value'] == '1':
        DATALOG_ERROR = random.randint(1, 9)
    payload['d'][13]['value'] = str(DATALOG_ERROR)

    #Generating oid
    if payload['d'][0]['value'] == '1':
        payload['d'][14]['value'] = str(oid)

    #Generating dis
    if payload['d'][0]['value'] == '1':
        payload['d'][15]['value'] = str(dis)

    #Generating network
    if payload['d'][0]['value'] == '1':
        payload['d'][16]['value'] = str(network)

    return payload

        
def on_publish(client, userdata, mid):
    print ("Message Published...")

      
def date_difference(dt1,dt2):
    if dt1 == dt2:
        return 1*60*24
    else:
        dif = dt2 - dt1
        return dif.days*60*60*24


if __name__ == "__main__":
    
    # Program Execution Time
   #exec_time = time.time()

    config = configparser.RawConfigParser()
    config.read('setup/config.cfg')
    mqtt_conf = config['mqtt_details']
    file = config['file']
    machine_list_filename = file['source_file_name']

    # Get List Of mid to subcribe
    machinesDF = pd.read_excel(machine_list_filename).astype(str)
    mid_list = machinesDF.to_numpy().flatten()

    #print(type(mid_list))
    #print(mid_list)

    #mid_list = ['869247043362190']
    
    startDate = dt.strptime(dt.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    endDate = dt.strptime("2022-12-31" + " 23:59:00", '%Y-%m-%d %H:%M:%S')

    size = date_difference(startDate, endDate)
    #size = 30

  
    # MQTT connection
    client = mqtt.Client()

    client.connect(mqtt_conf['host'], int(mqtt_conf['port']), int(mqtt_conf['keepalive']))

    
    for i in range(0,size):

        # Program Execution Time
        #exec_time = time.time()
        
        payload = {}
        
        date_instance = startDate + timedelta(seconds=i)

        for hardware_id in mid_list:
            payload = json.dumps(generate_data_array(hardware_id, date_instance))
            #print(payload)
            #print(type(str(payload).encode('utf-8')))
            data = str(payload).encode('utf-8')
            print(data)
            
            #client.publish("data/ecu1051/"+hardware_id, data)

        #print("---Execution time: %s seconds ---" % (time.time() - exec_time))
            
        time.sleep(0.99865)
        #time.sleep(3)

    
    print("Execution Started...")

    print("\nTask Completed.")
    #print("--- %s seconds ---" % (time.time() - exec_time))


