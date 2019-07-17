from pyparrot.Bebop import Bebop
import numpy


def getRealLocation(bebop,sleep=True):
    if sleep:
        bebop.smart_sleep(5)
    # Will read the text file and provide the most up to date localisation information
    location = open('C:\\Users\\blab\\Desktop\\test.txt')
    lastLine = location.readlines()[-1]
    lastLine = lastLine.replace('[', '')
    x = float(lastLine.split(']')[0])
    y = float(lastLine.split(']')[1])
    location.close()
    print(x,y)
    return (x,y)


def orientCopter(expectedLocation, bebop):
    realLocation = getRealLocation(bebop)
    error = numpy.subtract(realLocation, expectedLocation)
    print('errorX is: ',error[0])
    print('errorY is: ',error[1])
    bebop.move_relative(-error[1], -error[0], 0, 0)


bebop = Bebop(ip_address="10.202.0.1")
success = bebop.connect(2)
jumpSizes = float(input("Select your Jump size:\n\n2m Jumps (Type 2)"
                  "\n1m Jumps (Type 1)\n0.5m Jumps (Type 0.5)\n0.25m Jumps (Type 0.25)\n"))
bebop.safe_takeoff(10)
totalJump = 2
numberOfJumps = int(totalJump/jumpSizes)
startingPosition = getRealLocation(bebop, False)
expectedLocation = startingPosition
try:
    for i in range(numberOfJumps):
        #fly forward
        bebop.move_relative(jumpSizes, 0, 0, 0)
        #Orient the copter
        expectedLocation = numpy.add((0,jumpSizes),expectedLocation)
        orientCopter(expectedLocation,bebop)
    for i in range(numberOfJumps):
        # fly right
        bebop.move_relative(0,jumpSizes,0,0)
        #Orient the copter
        expectedLocation = numpy.add((jumpSizes,0),expectedLocation)
        orientCopter(expectedLocation,bebop)

    for i in range(numberOfJumps):
        # fly backwards
        bebop.move_relative(-jumpSizes,0,0,0)
        #Orient the copter
        expectedLocation = numpy.add((0,-jumpSizes),expectedLocation)
        orientCopter(expectedLocation,bebop)
    for i in range(numberOfJumps):
        # fly left
        bebop.move_relative(0,-jumpSizes,0,0)
        #Orient the copter
        expectedLocation = numpy.add((-jumpSizes,0),expectedLocation)
        orientCopter(expectedLocation,bebop)

    bebop.safe_land(10)
    bebop.disconnect()
except:
    bebop.safe_land(10)
    bebop.disconnect()

print("Remaining battery: ",
      bebop.sensors.battery)
