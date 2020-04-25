from urllib.request import urlopen
from pprint import pprint
import json
import os
baseUrl = "https://redive.estertion.win/spine/"


def get(url):
    return urlopen(baseUrl + url)


def download(filename, url):
    print("  " + url)
    if not os.path.exists(filename):
        try:
            data = get(url)
            with open(filename, "wb") as f:
                f.write(data.read())
        except:
            with open("error.log", "a") as f:
                f.write(url)
                f.write("\n")
            print("error when downloading " + url)


def getClass(i):
    if (int(i) < 10):
        return '0' + i
    else:
        return i


u = get("classMap.json")
classMap: dict = json.loads(u.read().decode("utf-8"))


for i in classMap:
    obj: dict = classMap[i]
    pprint(obj)
    Sid = int(i)
    Sname = obj["name"]
    Stype = int(obj["type"])
    ShasRarity6 = obj["hasRarity6"]
    if "hasSpecialBase" in obj.keys():
        ShasSpecialBase = obj["hasSpecialBase"]
    else:
        ShasSpecialBase = False

    def load(unit_id, class_id):
        baseUnitId = unit_id | 0
        baseUnitId -= baseUnitId % 100 - 1
        print("加载共用骨架 (1/6)")
        if ShasSpecialBase:
            baseId = str(baseUnitId)
            currentClass = str(baseUnitId)
        else:
            baseId = "000000"
            currentClass = str(class_id)
        filename = "common/" + baseId + "_CHARA_BASE.cysp"
        download(filename, filename)
        print("加载额外动画 (2/6)")
        additionAnimations = ["DEAR", "NO_WEAPON", "POSING", "RACE", "RUN_JUMP", "SMILE"]
        for i in additionAnimations:
            filename = "common/" + baseId + "_" + i + ".cysp"
            download(filename, filename)
        print("加载职介动画 (3/6)")
        filename = 'common/' + getClass(currentClass) + '_COMMON_BATTLE.cysp'
        download(filename, filename)
        print('加载角色技能动画 (4/6)')
        filename = 'unit/' + str(baseUnitId) + '_BATTLE.cysp'
        download(filename, filename)
        print('加载材质 (5/6)')
        filename = 'unit/' + str(unit_id) + '.atlas'
        download(filename, filename)
        print('加载材质图片 (6/6)')
        filename = 'unit/' + str(unit_id) + '.png'
        download(filename, filename)

    if Stype == 0 and not ShasSpecialBase:
        print(Sname + "未实装")
    else:
        print(Sname)
        print(Sname + "1★")
        load(Sid+10, Stype)
        print(Sname + "3★")
        load(Sid+30, Stype)
        if ShasRarity6:
            print(Sname + "6★")
            load(Sid+60, Stype)
