import copy
a=[1,2,3,4,5,6,7,8,9]
b=a
b[0]=10
#a数组发生变化
print(f'a数组为：{a}')
a=[1,2,3,4,5,6,7,8,9]
c=a.copy()
c[0]=10
#a数组未发生改变
print(f'使用copy后，a数组为：{a}')

def use_copy():
    d = [1,2,3,4,5,6,7,8,9]
    e = copy.copy(d)
    e[0] = 10
    #e和d的地址不一样了
    print(id(d))
    print(id(e))
    print(d)
    print(e)
if __name__=='__main__':
    use_copy()
    print()

#深copy
def use_deepcopy():
    a = [1,2]
    b = [3,4]
    c = [a,b]
    d = copy.deepcopy(c)
    print(id(c))
    print(id(d))
    a[0]=10
    print(f'c--{c}')
    print(f'd--{d}')
    print('-'*50)
    print(id(c[0]),id(c[1]))
    print(id(d[0]),id(d[1]))

if __name__ == '__main__':
    use_deepcopy()
    print()

class hero:
    def __init__(self,name,blood):
        self.name=name
        self.blood=blood
        self.equipment = ['鞋子','指环']

#应用举例
def use_copy_own_obj():
    old_hero = hero('蚂蚁',90)
    new_hero = copy.deepcopy(old_hero)
    new_hero.blood = 80
    new_hero.equipment.append('药水')
    print(old_hero.blood)
    print(old_hero.equipment)

if __name__ == '__main__':
    use_copy_own_obj()