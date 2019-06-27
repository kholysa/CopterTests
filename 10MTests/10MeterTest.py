from pyparrot.Bebop import Bebop

bebop = Bebop()
success = bebop.connect(2)
bebop.safe_takeoff(10)
bebop.smart_sleep(5)
# flightDirection = int(input("Select your travel mode:\n\n1: Forward (Type 1)\n2: Backwards (Type 2)\n3: Left (Type 3)\n4: Right (Type 4)\n"))
# jumpSizes = float(input("Select your Jump size:\n\n10m Jumps (Type 10)\n5m Jumps (Type 5)\n2m Jumps (Type 2)"
#                   "\n1m Jumps (Type 1)\n0.5m Jumps (Type 0.5)\n0.2m Jumps (Type 0.2)\n0.1m Jumps (Type 0.1)\n"))
# bebop.safe_takeoff(10)
# numberOfJumps = int(10/jumpSizes)
# for i in range(numberOfJumps):
#     print("Moving step number", i)
#     #fly forward
#     if flightDirection == 1:
#         bebop.move_relative(jumpSizes, 0, 0, 0)
#     # fly Backward
#     elif flightDirection == 2:
#         bebop.move_relative(-jumpSizes,0,0,0)
#     # fly Left
#     elif flightDirection == 3:
#         bebop.move_relative(0,-jumpSizes,0,0)
#     # fly Right
#     elif flightDirection == 4:
#         bebop.move_relative(0,jumpSizes,0,0)
print("Remaining battery: ", bebop.sensors.battery)
bebop.safe_land(10)
bebop.disconnect()