"""
小红正在玩一个《兽》的游戏。 在这个游戏中，有n个单位，每个单位的身份是“人”或者“兽”。每个人只知道自己的身份，不知道别人的身份。每个人的战斗力为
。 当两个单位相遇的时候，首先第一环节是确认身份(每个人可能会告诉对方自己身份，也可能隐藏)。

如果一个兽得知了对方是人，那么兽会直接攻击人，两方发生战斗; 如果一个人得知了对方是兽，那么他会权衡双方的战斗力:只有自己的战斗力大于对方时他才会发起攻击。 如果两个单位的阵营相同，则无事发生。

当两个单位攻击时，如果他们的战斗力相等，则最终同归于尽。如果某一方战斗力高，则战斗力高的将把对方杀死。

现在小红进行了m轮遭遇(每次选两个单位遭遇)，请你输出最终的存活情况。请注意，如果选择遭遇的两方存在某一方已经死亡，显然也不会发生战斗。

输入描述
第一行输入两个正整数n，m，代表单位数量、回合数。 接下来的n行，每行输入一个字符串
、一个正整数
，分别代表第 i 个单位的身份、战斗力。 接下来的m行，每行输入两个正整数u，v以及两个字符c1，c2，代表第u个单位和第v个单位遭遇。c1是'Y'字符代表u向v公布自己的身份，'N'代表隐藏身份;c2是'Y字符代表v向u公布自己的身份，'N'代表隐藏身份。




为"human"和"monster"中的一个，"human"代表人，"monster"代表兽。

输出描述
输出一个长度为n的字符串，仅由Y'和'N组成。Y代表第i个单位存活，'N'代表死亡。


4 3
human 2
monster 3
monster 10
monster 1
1 2 N Y
1 4 Y N
2 3 Y Y
"""
class Unit(object):
    def __init__(self,identity,power):
        self.identity = identity
        self.power = power
        self.alive=True

n,m=map(int,input().strip().split())
units=[]
for _ in range(n):
    identity,power=input().strip().split()
    units.append(Unit(identity,int(power)))

for _ in range(m):
    u,v,c1,c2=input().strip().split()
    u,v=int(u)-1,int(v)-1
    unit_u,unit_v=units[u],units[v]
    if not unit_u.alive or not unit_v.alive:
        continue
    if unit_u.identity=="human" and unit_v.identity=="monster":
        if c2=='Y':
            if unit_u.power>unit_v.power:
                unit_v.alive=False
                continue
        if c1=="Y" :
            if unit_u.power>unit_v.power:
                unit_v.alive=False
                continue
            if unit_u.power==unit_v.power:
                unit_u.alive=False
                unit_v.alive=False
                continue
            if unit_u.power<unit_v.power:
                unit_u.alive=False
                continue



    elif unit_u.identity=="monster" and unit_v.identity=="human":
        if c1=='Y':
            if unit_v.power>unit_u.power:
                unit_u.alive=False
                continue
        if c2=="Y":
            if unit_v.power>unit_u.power:
                unit_u.alive=False
                continue
            if unit_v.power==unit_u.power:
                unit_u.alive=False
                unit_v.alive=False
                continue
            if unit_v.power<unit_u.power:
                unit_v.alive=False
                continue



result="".join(['Y' if unit.alive else 'N' for unit in units])
print(result)