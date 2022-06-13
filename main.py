import os

system = "macos"  # 根据个人情况改成macos、linux或者windows（使用小写）

def clear():    # 清屏函数
    if system == "macos" or system == "linux":
        os.system("clear")
    elif system == "windows":
        os.system("cls")
    else:
        print("清屏失败！请检查文件第3行的系统变量！")

class player:
    def __init__(self, name, balance=1500):
        self.name = name
        self.balance = balance

    def getBalance(self):
        return self.balance

    def getName(self):
        return self.name

    def setBalance(self, balance):
        self.balance = balance

    def addBalance(self, amount):
        self.balance += amount

    def subtractBalance(self, amount):
        self.balance -= amount

def transfer(player1, player2, amount):
    if player1.getBalance() >= amount:
        player1.subtractBalance(amount)
        player2.addBalance(amount)
        print(f"转账成功！已从{player1.getName()}转账{amount}元给{player2.getName()}！")
        return True
    else:
        print("钱不够捏！转账失败！")
        return False
print("欢迎使用大富翁资金控制系统")
player_num = 0
while player_num < 2:
    player_num = int(input("请输入玩家数量："))
playerList = []
for i in range(player_num):
    print("请输入玩家" + str(i+1) + "号的名字：")
    name = input()
    playerList.append(player(name))
clear()
gaming = True
while gaming:
    print("当前余额状态：")
    for i in range(player_num):
        print(f"P{i+1} - {playerList[i].getName()}：{playerList[i].getBalance()}元")
    print("操作列表：1.转账 2.扣除钱 3.添加钱 4.退出")
    choice = 100
    while choice > 4 or choice < 1:
        choice = int(input("请输入对应数字进行操作："))
    if choice == 1:
        payPlayer = int(input("请输入转账玩家ID："))-1
        receivePlayer = int(input("请输入接收玩家ID："))-1
        amount = int(input("请输入转账金额："))
        clear()
        transfer(playerList[payPlayer], playerList[receivePlayer], amount)
    elif choice == 2:
        playerID = int(input("请输入玩家ID："))-1
        amount = int(input("请输入扣除金额："))
        clear()
        if playerList[playerID].getBalance() >= amount:
            playerList[playerID].subtractBalance(amount)
            print(f"扣除成功！已从{playerList[playerID].getName()}扣除{amount}元！剩余{playerList[playerID].getBalance()}元")
        else:
            print("钱不够捏！扣除失败！")
    elif choice == 3:
        valid = False
        while not valid:
            playerID = int(input("请输入玩家ID："))-1
            if playerID < player_num:
                valid = True
            else:
                print("玩家ID不存在！")
        amount = int(input("请输入获得金额："))
        clear()
        playerList[playerID].addBalance(amount)
        print(f"添加成功！已向{playerList[playerID].getName()}添加{amount}元！当前余额{playerList[playerID].getBalance()}元")
    elif choice == 4:
        clear()
        gaming = False
        print("游戏结束！感谢使用此系统！")
        print("当前余额状态：")
        for i in range(player_num):
            print(f"P{i+1} - {playerList[i].getName()}：{playerList[i].getBalance()}元")
        input("按回车键退出...")