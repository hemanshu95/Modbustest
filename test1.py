import minimalmodbus as mmRtu
portName = 'com22'
baudrate = 153600
slaveId=1

mmc=mmRtu.Instrument(portName, 2)  # port name, slave address
mmc.serial.baudrate=baudrate
mmc.serial.timeout=timeoutSp
mmc.address = slaveId
try:
    print mmc.read_register(0)
except:
    print "err"
mmc.serial.close()
print mmc.serial
