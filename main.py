class player:
    def __init__(self, name, balance=1500):
        self.name = name

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

print("欢迎使用大富翁资金控制系统")
print("请输入玩家数量：")
player_num = int(input())
playerList = []
for i in range(player_num):
    print("请输入玩家" + str(i+1) + "号的名字：")
    name = input()
    playerList.append(player(name))
print("请输入玩家名称：")
player_name = input()
gaming = True
while gaming:
    print("请输入数字来进行操作：")