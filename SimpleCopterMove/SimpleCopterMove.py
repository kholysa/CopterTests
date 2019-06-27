from pyparrot.Bebop import Bebop
import numpy

if __name__ == "__main__":
    print(r"""
                Y
                ^
                |
                |
                |
                |
                |
    ------------x-------------------> X
                | (0,0) Initial Copter location
                |
                |
                |
                |
                """)
    previousPosition = (0, 0, 1, 0)
    bebop = Bebop(ip_address="10.202.0.1")
    success = bebop.connect(2)
    bebop.safe_takeoff(10)
    yesStrings = {'yes', 'y', 'ye'}
    while True:
        try:

            exit = input("\n\n\n\tExit the program and land the copter (y/n)?")
            if exit in yesStrings:
                break

            x = float(input("\n\n\n\tPlease input your desired coordinates:\n\tX: "))
            y = float(input("\n\tY: "))
            z = float(input("\n\tZ: "))
            rotation = float(input("\n\tCopter Rotation (Radians): "))
            delta = numpy.subtract((x, y, z, rotation), previousPosition)
            previousPosition = (x, y, z, rotation)

            print(delta)
            bebop.move_relative(0, 0, -delta[2], 0)
            bebop.move_relative(0, delta[0], 0, 0)
            bebop.move_relative(delta[1], 0, 0, 0)
            bebop.move_relative(0, 0, 0, delta[3])

        except:
            
            bebop.emergency_land()
            bebop.disconnect()
            print("\tError found. Closing application")
            import sys
            sys.exit(0)

    bebop.safe_land(10)
    bebop.disconnect()
