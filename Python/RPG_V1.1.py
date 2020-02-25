########################################
######## 综合练习：RPG回合游戏 #########
##### V1.1 版本作者：新网工 - 柚子 #####
####### 😀😀😀😀 非常感谢 😀😀😀😀 ######
########################################

########## V1.1 版本更新说明 ###########

# 增加了人数选择功能
# 法师：
#     变羊技能现在可以正常工作了
#
############### 技能说明 ###############

# 战士（HP:15）技能：
# - 顺劈：对敌方所有人造成2点伤害
# - 冲锋：对敌方目标造成3点伤害
# - 防护：防御接下来的一次伤害

# 法师（HP:8）技能：
# - 火球：对敌方目标造成4点伤害
# - 暴风雪：对敌方所有人造成3点伤害
# - 变羊：敌方目标本回合无法行动

# 牧师（HP:10）技能：
# - 治疗：对我方目标造成3点治愈效果
# - 痛：对敌方目标造成2点伤害
# - 痊愈：对我方目标造成5点治愈效果

# 裁判技能：
# - 统计本回合行动
# - 处理法师变羊
# - 处理战士防护
# - 处理单体技能
# - 处理群体技能
# - 处理死者
# - 宣布结果

########################################

import random
import time

print("【裁判通告】欢迎来到 Gai 的战场！")
time.sleep(1)
print("【裁判通告】战争将于3秒后开始！")
time.sleep(1)
print("【裁判通告】3")
time.sleep(1)
print("【裁判通告】2")
time.sleep(1)
print("【裁判通告】1")
time.sleep(1)

# 参数区域
skills = {"smooth": -2,
          "charge": -2,
          "defense": 0,
          "fire": -4,
          "blizzard": -3,
          "polymorph": 0,
          "treatment": 3,
          "pain": -2,
          "cured": 5
          }

a = int(input("输入队伍1人数为:"))
b = int(input("输入队伍2人数为:"))

# 战士类
class warrior():
    def __init__(self, name):
        self.name = name
        self.hp = 15
        self.hp_lim = 15
        self.is_def = False
        self.is_sheep = False
        self.move = None
        self.target_index = None
        self.death = False

    # 选择技能
    def decision(self):
        value = random.choice([1, 2, 3])
        if value == 1:
            self.smooth()
        elif value == 2:
            self.charge()
        else:
            self.defense()

    # 顺劈
    def smooth(self):
        self.move = "smooth"

    # 冲锋
    def charge(self):
        self.target_index = random.choice([0, 1, 2, 3, 4])
        self.move = "charge"

    # 防御
    def defense(self):
        self.move = "defense"
        self.target_index = True

    # 刷新自己状态
    def refresh(self):
        self.is_sheep = False
        self.move = None
        self.target_index = None


# 法师类
class mage():
    def __init__(self, name):
        self.name = name
        self.hp = 8
        self.hp_lim = 8
        self.is_def = None
        self.is_sheep = False
        self.move = None
        self.target_index = None
        self.death = False

    # 选择技能
    def decision(self):
        value = random.choice([1, 2, 3])
        if value == 1:
            self.fire()
        elif value == 2:
            self.blizzard()
        else:
            self.polymorph()

    # 火球
    def fire(self):
        self.move = "fire"
        self.target_index = random.choice([0, 1, 2, 3, 4])

    # 暴风雪
    def blizzard(self):
        self.move = "blizzard"

    # 变羊
    def polymorph(self):
        self.move = "polymorph"
        self.target_index = random.choice([0, 1, 2, 3, 4])

    # 刷新自己状态
    def refresh(self):
        self.is_sheep = False
        self.move = None
        self.target_index = None


# 牧师类
class priest():
    def __init__(self, name):
        self.name = name
        self.hp = 10
        self.hp_lim = 10
        self.is_def = None
        self.is_sheep = False
        self.move = None
        self.target_index = None
        self.death = False


    # 选择技能
    def decision(self):
        value = random.choice([1, 2, 3])
        if value == 1:
            self.treatment()
        elif value == 2:
            self.pain()
        else:
            self.cured()

    # 治疗
    def treatment(self):
        self.target_index = random.choice([0, 1, 2, 3, 4])
        self.move = "treatment"

    # 惩戒
    def pain(self):
        self.target_index = random.choice([0, 1, 2, 3, 4])
        self.move = "pain"

    def cured(self):
        self.target_index = random.choice([0, 1, 2, 3, 4])
        self.move = "cured"

    # 刷新自己状态
    def refresh(self):
        self.is_sheep = False
        self.move = None
        self.target_index = None


# 裁判类
class judge():
    def __init__(self, skills):
        self.skills = skills
        self.create_team()

    # 以下部分完成队伍创建 #
    def _create_one(self, last_name):
        characters = ['warrior', 'mage', 'priest']
        value = random.choice([0, 1, 2])
        this_name = characters[value] + last_name
        if value == 0:
            this_char = warrior(this_name)
        elif value == 1:
            this_char = mage(this_name)
        else:
            this_char = priest(this_name)

        return this_char

    def create_team(self):
        # 创建队伍1
        global a
        global b
        o1 = ["_毁灭之锤","_吉尔尼斯","_巴罗夫","_灰鬓","_索瑞森"]
        o2 = ["_蛮锤","_乌瑞恩","_米奈希尔","_普罗德摩尔","_怒风"]
        a1 = []
        a2 = a - 1
        c = 0
        while c <= a2:
            n1 = o1[random.randrange(a2)]
            a1.append(self._create_one(n1))
            c = c + 1
        self.team1 = a1
        # self.t1c1 = self._create_one("_毁灭之锤")
        # self.t1c2 = self._create_one("_吉尔尼斯")
        # self.t1c3 = self._create_one("_巴罗夫")
        # self.t1c4 = self._create_one("_灰鬓")
        # self.t1c5 = self._create_one("_索瑞森")
        # self.team1 = [self.t1c1, self.t1c2, self.t1c3, self.t1c4, self.t1c5]

        # 创建队伍2
        b1 = []
        b2 = b - 1
        d = 0
        while d <= b2:
            n2 = o2[random.randrange(b2)]
            b1.append(self._create_one(n2))
            d = d + 1
        self.team2 = b1
        # self.t2c1 = self._create_one("_蛮锤")
        # self.t2c2 = self._create_one("_乌瑞恩")
        # self.t2c3 = self._create_one("_米奈希尔")
        # self.t2c4 = self._create_one("_普罗德摩尔")
        # self.t2c5 = self._create_one("_怒风")
        # self.team2 = [self.t2c1, self.t2c2, self.t2c3, self.t2c4, self.t2c5]

        print("【裁判通告】两队人马已经准备就绪！")
        time.sleep(1)
        print("首先登场的是队伍1，他们是：{}".format([one.name for one in self.team1]))
        time.sleep(1)
        print("紧接着登场的是队伍2，他们是：{}".format([one.name for one in self.team2]))
        time.sleep(1)
        print("*" * 90)
        print("\n")

        return self.team1, self.team2

    # 队伍创建结束 #
    # ------------ #

    # 以下部分完成队伍行动 #

    # 全队做出行动
    def _team_moving(self, team):
        for one in team:
            one.decision()

    # 处理变羊
    def _do_polymorph(self, to_whom):
        to_whom.is_sheep = True
        print("【变羊】{} 被变成了羊！".format(to_whom.name))
        time.sleep(1)

    # 处理防御
    def _do_defense(self, from_whom):
        from_whom.is_def = True
        print("【防御】{} 获得了防御效果！".format(from_whom.name))
        time.sleep(1)

    # 处理单体伤害技能
    def _hurt_single(self, hurt_value, to_whom):
        to_whom.hp += hurt_value
        print("{} 受到了 {} 点伤害！".format(to_whom.name, -hurt_value))
        time.sleep(1)

    # 处理单体恢复技能
    def _treat_single(self, hurt_value, to_whom):
        to_whom.hp += hurt_value
        print("{} 得到了 {} 点治疗！".format(to_whom.name, hurt_value))
        time.sleep(1)

    # HP超范围重置
    def _hp_check(self, to_team):
        for one in to_team:
            if one.hp > one.hp_lim:
                one.hp = one.hp_lim
            if one.hp < 0:
                one.hp = 0

    # 开战
    def _battle(self, from_team, to_team):

        # 单队行动触发
        self._team_moving(from_team)

        # 计算所有行动
        for one in from_team:

            ### TODO: 在下方合适的地方处理【变羊】这个技能,让已经被变羊的选手本回合无法行动 ###
            ### TODO: 行动前需判断人员死亡情况  ###

            if one.death is False and one.is_sheep is False:
                print("【攻击】{} 使用了 {} 技能".format(one.name, one.move))
                time.sleep(1)
                if one.target_index is not None:
                    if one.move == "polymorph":
                        _target = to_team[random.choice(range(len(to_team)))]
                        self._do_polymorph(_target)
                    elif one.move == "defense":
                        self._do_defense(one)
                    elif one.move in ["treatment", "cured"]:
                        _target = from_team[random.choice(range(len(from_team)))]
                        self._treat_single(self.skills[one.move], _target)
                        self._hp_check(from_team)
                    else:
                        _target = to_team[random.choice(range(len(to_team)))]
                        if _target.is_def != True:
                            self._hurt_single(self.skills[one.move], _target)
                            self._hp_check(to_team)
                        else:
                            print("【被防御】攻击被对方防御了！")
                            time.sleep(1)
                else:
                    for _target in to_team:
                        if _target.is_def != True:
                            aoe_hurt = self.skills[one.move]
                            _target.hp += aoe_hurt
                    self._hp_check(to_team)
                    print("{} 对敌方全体造成了 {} 点AOE伤害！".format(one.move, aoe_hurt))
                    time.sleep(1)
            elif one.death is True:
                print("{}已死亡".format(one.name))
            elif one.death is False and one.is_sheep is True:
                print("{}被变羊".format(one.name))
                one.move = None
                one.target_index = None


    # 队伍行动结束 #
    # ------------ #

    # 以下部分完成结果检测与信息输出 #

    # 队伍状态刷新
    def _team_refresh(self, from_team, to_team):
        for one in from_team:
            one.refresh()
        for one in to_team:
            one.is_def = False

    # 检查是否团灭，给予死亡个人进行标记
    def _cheak(self, from_team, to_team):

        END = False
        ALL_DEATH = len(to_team)

        for one in to_team:
            if one.hp <= 0:
                one.death = True
                print("{}已经死亡！".format(one.name))
                time.sleep(1)
                ALL_DEATH -= 1
        if ALL_DEATH == 0:
            END = True

        # 刷新进攻方状态
        self._team_refresh(from_team, to_team)

        return END

    # 刷新防御状态
    def _redefense(self,from_team,to_team):
        for one in from_team:
            one.is_def = False
        for oth_one in to_team:
            oth_one.is_def = False


    # 信息输出
    def print_hp(self):
        print("\n" + "*" * 40)
        print("结果：")
        time.sleep(1)
        print("*  " + "Team1 状态：")
        for one in self.team1:
            if one.hp is not 0:
                print("*  " + "{}的血量为{}".format(one.name, one.hp))
        print("\n" + "-" * 40 + "\n")
        time.sleep(1)
        print("*  " + "Team2 状态：")
        for one in self.team2:
            if one.hp is not 0:
                print("*  " + "{}的血量为{}".format(one.name, one.hp))
        print("*" * 40 + "\n")
        time.sleep(1)

    # 结果检测与信息输出过程完毕 #
    # -------------------------- #

    # 开始游玩
    def play(self):

        while True:
            print("\n" + "*" * 40)
            print("*  " + "Team1 开始进攻" + "  *")
            time.sleep(1)
            print("*" * 40)
            self._battle(self.team1, self.team2)
            self.print_hp()
            END = self._cheak(self.team1, self.team2)
            if END == True:
                print("\n" + "*" * 40)
                print("*  " + "恭喜 Team1 获胜！" + "  *")
                time.sleep(1)
                print("*" * 40)
                break

            print("\n" + "*" * 40)
            print("*  " + "Team2 开始进攻" + "  *")
            time.sleep(1)
            print("*" * 40)
            self._redefense(self.team1, self.team2)
            self._battle(self.team2, self.team1)
            self.print_hp()
            END = self._cheak(self.team2, self.team1)
            if END == True:
                print("\n" + "*" * 40)
                print("*  " + "恭喜 Team2 获胜！" + "  *")
                time.sleep(1)
                print("*" * 40)
                break
            time.sleep(2)


if __name__ == "__main__":
    my_judge = judge(skills)
    my_judge.play()
