from bluepy import btle
from struct import *
from csv import writer
import csv
#import json
from datetime import datetime


MAC = "7C:9E:BD:45:12:9A"
T1_SERVICE_UUID = "00000010-0000-1000-8000-00805f9b34fb"
T1_CHARACTERISTIC_UUID = "00000001-0000-1000-8000-00805f9b34fb"
T2_SERVICE_UUID = "00000020-0000-1000-8000-00805f9b34fb"
T2_CHARACTERISTIC_UUID = "00000002-0000-1000-8000-00805f9b34fb"

#print("Connect to:" + MAC)
dev = btle.Peripheral(MAC)

#----------------------------------------------
characteristics = dev.getCharacteristics()

for char in characteristics:
    if(char.uuid == T1_CHARACTERISTIC_UUID ):
#        print("=== !Air Quality CHARACTERISTIC! ===")
        T1_output = unpack('4B',char.read())
        print("T1_ppm: ", T1_output[3]<<8 | T1_output[2])
        print("T1_voc: ", T1_output[1]<<8 | T1_output[0])
        T1_ppm = T1_output[3]<<8 | T1_output[2]
        T1_voc = T1_output[1]<<8 | T1_output[0]
    elif(char.uuid == T2_CHARACTERISTIC_UUID ):
        T2_output = unpack('4B',char.read())
        print("T2_ppm: ", T2_output[3]<<8 | T2_output[2])
        print("T2_voc: ", T2_output[1]<<8 | T2_output[0])
        T2_ppm = T2_output[3]<<8 | T2_output[2]
        T2_voc = T2_output[1]<<8 | T2_output[0]


current_time = datetime.now()
date = current_time.strftime("%m/%d/%Y")
time = current_time.strftime("%H:%M")

list_T1_data = [date,time,'Zone2','T1',T1_ppm,T1_voc]
list_T2_data = [date,time,'Zone2','T2',T2_ppm,T2_voc]

# T1 endnode sensors to be written
#T1_json = {"time": current_time,"Z1": "Zone1", "T1": {"ppm": T1_ppm,"voc": T1_voc}}

# T2 endnode sensors to be written
#T2_json = {"time": current_time,"Z1": "Zone1", "T2": {"ppm": T2_ppm,"voc": T2_voc}}

#T1_json_data = json.dumps(T1_json, default = str)
#T2_json_data = json.dumps(T2_json, default = str)

#T1_json_data = json.dumps(T1_json, separators=(" , ", " : "))
#T2_json_data = json.dumps(T2_json, separators=(" , ", " : "))

#T1_json_data = json.loads(T1_json_data)
#T2_json_data = json.loads(T2_json_data)


#with open('T1.csv', 'a', newline='', encoding='utf-8') as T1:
#    json.dump(T1_json_data,T1,ensure_ascii=False)

with open('Live.csv', 'a', newline='', encoding='utf-8') as T1:
    writer_object = writer(T1)
    writer_object.writerow(list_T1_data)

    # Close the file object
    T1.close()

#with open('T2.csv', 'a', newline='', encoding='utf-8') as T2:
#    json.dump(T2_json_data,T2,ensure_ascii=False)

with open('Live.csv', 'a', newline='', encoding='utf-8') as T2:
    writer_object = writer(T2)
    writer_object.writerow(list_T2_data)

    # Close the file object
    T2.close()
