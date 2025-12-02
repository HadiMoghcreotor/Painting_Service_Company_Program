DOOR_AREA = 2
total_Walllen = 0
total_Wallwid = 0
total_WallArea = 0
doorArea = 0
total_Winlen = 0
total_Winwid = 0
total_WinArea = 0
paintableArea = 0
Litresreq = 0
fiveL_tins = 0
remainder = 0
threeL_tins = 0
twoL_tins = 0
oneL_tins = 0
LABOUR_COST = 0
cost_fiveL_tins = 0
cost_threeL_tins = 0
cost_twoL_tins = 0
cost_oneL_tins = 0
Total_tins_cost = 0
Total_cost = 0
wallArea = 0
winArea = 0

#Wall's questions
numWalls = int(input("Enter number of walls you want to paint (1-20):..."))
while numWalls < 1 or numWalls > 20:
    print("Input should be betwwen 1 and 20")
    numWalls = int(input("Enter number of walls you want to paint (1-20):..."))
for i in range(numWalls):
    lenWall = float(input(f"Enter the length of wall number {i + 1}:..."))
    widWall = float(input(f"Enter the width of wall number {i + 1}:..."))
    wallArea = lenWall * widWall
    total_WallArea += wallArea
#Door's questions
Door_exist = input("Are there any doors in these walls? (y for yes, n for no):...")

while Door_exist != "y" and Door_exist != "n":
    print("That's an invalid input mate!")
    Door_exist = input("Are there any doors in these walls? (y for yes, n for no):...")

if Door_exist == "y":
    numDoor = int(input("How many are they?:..."))
    doorArea = numDoor * 2
else:
    doorArea = 0
    pass
#Window's questions
windowExist = input("Are there any windows in these walls?(y for yes, n for no)...")
while windowExist != "y" and windowExist != "n":
    print("That's an invalid input mate!")
    windowExist = input("Are there any windows in these walls?(y for yes, n for no)...")
if windowExist == "y":
    numWin = int(input("How many are they?..."))
    for i in range (numWin):
        lenWin = float(input(f"Enter length of window number {i + 1}:...."))
        widWin = float(input(f"Enter width of window number {i + 1}:...."))
        winArea =  lenWin * widWin
        total_WinArea += winArea
else:
    total_WinArea = 0
    pass
#Paintable Area calculation
paintableArea = total_WallArea - (doorArea + total_WinArea)

#paint tins section
Litresreq = paintableArea // 5
fiveL_tins = Litresreq // 5
remainder = Litresreq % 5
threeL_tins = remainder // 3
remainder = remainder % 3
twoL_tins = remainder // 2
remainder = remainder % 2
oneL_tins = remainder // 1
remainder = remainder % 1
#cost section
LABOUR_COST = 5*paintableArea
cost_fiveL_tins = fiveL_tins*50
cost_threeL_tins = threeL_tins*35
cost_twoL_tins = twoL_tins*25
cost_oneL_tins = oneL_tins*15
Total_tins_cost = cost_fiveL_tins + cost_threeL_tins + cost_twoL_tins + cost_oneL_tins
Total_cost = Total_tins_cost + LABOUR_COST
print(f"Your total bill is {Total_cost}£")