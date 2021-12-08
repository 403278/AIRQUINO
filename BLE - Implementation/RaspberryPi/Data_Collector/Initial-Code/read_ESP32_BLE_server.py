from bluepy import btle
from ast import literal_eval

MAC = "08:3A:F2:6E:6A:FA"
SERVICE_UUID = "000000ff-0000-1000-8000-00805f9b34fb"
CHARACTERISTIC_UUID = "0000ff01-0000-1000-8000-00805f9b34fb"

print("Connect to:" + MAC)
dev = btle.Peripheral(MAC)

#print("\n--- dev ----------------------------")
#print(type(dev))
#print(dev)

#print("\n--- dev.services -------------------")
#for svc in dev.services:
#    print(str(svc))
    
#print("\n------------------------------------")
#print("Get Serice By UUID: " + SERVICE_UUID)
#service_uuid = btle.UUID(SERVICE_UUID)
#service = dev.getServiceByUUID(service_uuid)

#print(service)
#print("\n--- service.getCharacteristics() ---")
#print(type(service.getCharacteristics()))
#print(service.getCharacteristics())

#----------------------------------------------
characteristics = dev.getCharacteristics()
#print("\n--- dev.getCharacteristics() -------")
#print(type(characteristics))
#print(characteristics)

for char in characteristics:
#    print("----------")
#    print(type(char))
#    print(char)
#    print(char.uuid)
    if(char.uuid == CHARACTERISTIC_UUID ):
        print("=== !Air Quality CHARACTERISTIC! ===")
#        print(char)
#        print(dir(char))
#        print(char.getDescriptors)
#        print(char.propNames)
#        print(char.properties)
#        print(type(char.read()))
        hex = char.read()
#        print(char.read())
    
dec = literal_eval(hex)
print(dec)
#print("=== dev ============================")
#print(dir(dev))
#print("=== service ========================")
#print(dir(service))
