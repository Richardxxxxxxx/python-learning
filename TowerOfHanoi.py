

def moveTower(sourceTower,tempTower,desTower,disks):
    if disks == 1 :
        print("move one from {0} to {1}".format(sourceTower,desTower))
    else:
        moveTower(sourceTower,desTower,tempTower,disks-1)
        moveTower(sourceTower,tempTower,desTower,1)
        moveTower(tempTower,sourceTower,desTower,disks-1)

def main():
    moveTower('A','B','C',4)

if __name__ == "__main__" :
    main()
