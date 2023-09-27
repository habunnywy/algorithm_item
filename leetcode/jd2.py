"""
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