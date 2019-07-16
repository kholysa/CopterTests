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


def orientCopter(flightDirection, expectedLocation, bebop):
    realLocation = getRealLocation(bebop)
    error = numpy.subtract(realLocation, expectedLocation)
    #fly forward
    if flightDirection == 1:
        bebop.move_relative(-error[1], -error[0], 0, 0)
        # Orient Copter based on real position and expected position
    # fly Backward
    elif flightDirection == 2:
        bebop.move_relative(error[1], error[0], 0, 0)
        # Orient Copter based on real position and expected position
    # fly Left
    elif flightDirection == 3:
        bebop.move_relative(error[0], -error[1], 0, 0)
        # Orient Copter based on real position and expected position
    # fly Right
    elif flightDirection == 4:
        bebop.move_relative(-error[0], error[1], 0, 0)

bebop = Bebop()
success = bebop.connect(2)
flightDirection = int(input("Select your travel mode:\n\n1: Forward (Type 1)\n2: Backwards (Type 2)\n3: Left (Type 3)\n4: Right (Type 4)\n"))
jumpSizes = float(input("Select your Jump size:\n\n5m Jumps (Type 5)\n2.5m Jumps (Type 2.5)"
                  "\n1m Jumps (Type 1)\n0.5m Jumps (Type 0.5)\n0.25m Jumps (Type 0.25)\n0.1m Jumps (Type 0.1)\n"))
try:
    bebop.safe_takeoff(10)
    totalJump = 5
    numberOfJumps = int(totalJump/jumpSizes)
    firstPosition = getRealLocation(bebop,False)
    for i in range(numberOfJumps):
        print("Moving step number", i)
        expectedLocation = numpy.add((0,(1+i) * jumpSizes),firstPosition)
        #fly forward
        if flightDirection == 1:
            bebop.move_relative(jumpSizes, 0, 0, 0)
            # Orient Copter based on real position and expected position
            orientCopter(flightDirection,expectedLocation,bebop)
        # fly Backward
        elif flightDirection == 2:
            bebop.move_relative(-jumpSizes,0,0,0)
            # Orient Copter based on real position and expected position
            orientCopter(flightDirection, expectedLocation,bebop)
        # fly Left
        elif flightDirection == 3:
            bebop.move_relative(0,-jumpSizes,0,0)
            # Orient Copter based on real position and expected position
            orientCopter(flightDirection, expectedLocation,bebop)
        # fly Right
        elif flightDirection == 4:
            bebop.move_relative(0,jumpSizes,0,0)
            # Orient Copter based on real position and expected position
            orientCopter(flightDirection,expectedLocation,bebop)

    print("Remaining battery: ",
          bebop.sensors.battery)
    bebop.safe_land(10)
    bebop.disconnect()
except:
    bebop.safe_land(10)
    bebop.disconnect()
