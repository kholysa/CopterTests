from pyparrot.Bebop import Bebop

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

    try:
        x = float(input("\n\n\nPlease input your desired coordinates:\nX: "))
        y = float(input("\nY: "))
        z = float(input("\nZ: "))
        rotation = float(input("\nCopter Rotation (Radians): "))
    except:
        print("Error found. Closing application")
        import sys
        sys.exit(0)

    waitAfterArriving = input('Wait after arriving? (Y/N): ').lower()
    bebop = Bebop(ip_address="10.202.0.1")
    try:
        success = bebop.connect(2)
        print("connecting")

        bebop.safe_takeoff(10)
        bebop.move_relative(y,x,-z+1,rotation)
        if waitAfterArriving in {'yes','y', 'ye', ''}:
            while True:
                keyPress = input("\n\n\n\nPress Enter to land")
                break
        bebop.safe_land(10)
        bebop.disconnect()
    except:
        bebop.emergency_land()
        bebop.disconnect()