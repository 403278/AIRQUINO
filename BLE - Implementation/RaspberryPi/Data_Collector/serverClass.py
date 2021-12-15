
class Server:
     def _init_(self, macAddr, uuidC, uuidCC):
        self.c = uuidC
        self.cc = uuidCC
        self.esp = btle.Peripheral(macAddr, addrType=btle.ADDR_TYPE_PUBLIC)

     def disconnect(self):
         self.esp.disconnect()

     def getCharValue(self):
        self.espChar = self.esp.getCharacteristics()

     def getValue(self, sensor, zone):
        for char in characteristics:
        if(zone == self.c)
            if(self.espChar.uuid == self.cc ):
                T1_output = unpack('4B',self.espChar.read())
               # print("T1_ppm: ", T1_output[3]<<8 | T1_output[2])
               # print("T1_voc: ", T1_output[1]<<8 | T1_output[0])
                T1_ppm = T1_output[3]<<8 | T1_output[2]
                T1_voc = T1_output[1]<<8 | T1_output[0]
            elif(self.char.uuid == self.cc ):
                T2_output = unpack('4B',self.espChar.read())
               # print("T2_ppm: ", T2_output[3]<<8 | T2_output[2])
               # print("T2_voc: ", T2_output[1]<<8 | T2_output[0])
                T2_ppm = T2_output[3]<<8 | T2_output[2]
                T2_voc = T2_output[1]<<8 | T2_output[0]

