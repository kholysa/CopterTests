from pyparrot.Bebop import Bebop

bebop = Bebop()
success = bebop.connect(2)
jumpSizes = float(input("Select your Jump size:\n\n2m Jumps (Type 2)"
                  "\n1m Jumps (Type 1)\n0.5m Jumps (Type 0.5)\n0.25m Jumps (Type 0.25)\n"))
bebop.safe_takeoff(10)
totalJump = 2
numberOfJumps = int(totalJump/jumpSizes)
for i in range(numberOfJumps):
    #fly forward
    bebop.move_relative(jumpSizes, 0, 0, 0)

for i in range(numberOfJumps):
    # fly right
    bebop.move_relative(0,jumpSizes,0,0)

for i in range(numberOfJumps):
    # fly backwards
    bebop.move_relative(-jumpSizes,0,0,0)

for i in range(numberOfJumps):
    # fly left
    bebop.move_relative(0,-jumpSizes,0,0)


print("Remaining battery: ",
      bebop.sensors.battery)

bebop.safe_land(10)
bebop.disconnect()