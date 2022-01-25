#提示组
attention='''            《注意事项》
注意事项1：在v12.0以及以上版本需安装'requests'模块；

注意事项2：吴涛加密系统只能加密数字，base64加密系统能加密中文，英文字母和数字；

注意事项3：添加mods请到‘更多操作’使用‘pip’进行添加；

注意事项4：游戏由 CrosWuft 开发并代理，版权归 CrosWuft 所有，ResuRrction提供技术支持，禁止在未经作者的允许下私自篡改游戏内容，代码；

注意事项5：游戏作者联系方式-- croswuft202007@outlook.com ,欢迎向我提供本游戏的bug；

注意事项6：本游戏将会不定期更新，请留意最新版本；
'''

#模块组
import random
import time
import json
import requests
import base64
import re

#参数组
date='2022.1.24s1'#更新日期
ver='v12.5'#版本
p=0#输入错误次数
cps=0#与mods有关
qwe=0#签到，兑换码，彩蛋
rmb=0#货币
rc=0#作弊次数
used=0#输入次数
pin=random.randint(0,10000000000000)#本次游戏ID
mods = ['1.(内置)更多操作','2.(内置)翻译','3.(内置)计算器']#mods列表
sd1=['?(6星)','AWM龙狙（5星）','M416黄金龙骨（4星）','AKM暗黑杀手（4星）','AUG绿色巨人（3星）','Kar 98K无名（3星）','M16A4使命必达（3星）'
,'S686众生平等（2星）','P119无皮肤（1星）']#奖品列表
player=[]#玩家仓库
#说明组
help='''
    help     显示帮助（本列表）
    ath      显示所有奖品
    quit     退出
    nun      小数化余额
    ver      查看游戏版本
    rmb      显示我的余额
    freecj   进入免费抽奖
    cj       进入高级抽奖
    my       查看我的物品
    my all   查看各个物品数量
    sell     卖出我的物品
    cj 10    10连抽（付费）
    cj any   随心抽（付费）
    math     通过计算来赚钱
    qd       签到
    cz       充值
    cs       猜数游戏
    store    商店
    pr code  兑换码
    rz       查看更新日志
    base1    进入base64加密
    base2    进入base64解密 
    mia      进入吴涛加密模式
    mib      进入吴涛解密模式
    mods     添加及调用mods
    sell all 全部卖出    
    r        测试运气
    t        查看当前时间
    ***      敬请期待
    (更多小彩蛋等你去探索！！)
    '''
things='''
    1.AWM龙狙（5星）       10,000元
    2.M416黄金龙骨（4星）   9,000元
    3.AKM暗黑杀手（4星）    7，999元
            (更多物品敬请期待)
    '''
allcd='''
    cw          开发者模式1（免费充钱）
    cw2         开发者模式2（添加物品）
    sb          扣取100元
    fuck        扣取100元
    20070623    此隐藏菜单
    [数字]       显示'数字'      
    root        进入开发者模式
    exit        显示'这个...才是'
    rock        装逼模式
    v           导出游戏信息
    croswuft    显示‘cr...万岁’
    hello,world 显示’he...ld!‘
    '''
rz='''
v5.1的更新内容
    对‘cj any’中输入负数刷钱进行了修复；
    添加了新选项——‘rz’以查看更新日志；
    添加了‘quit’来退出；
v6.0的更新内容
    添加了新选项——‘my all’；
    添加新枪械-P119无皮肤（1星）；
    添加了乱按提示；
    添加了小数化--'nun'；
v7.0的更新内容
    调整了抽奖几率；
    对抽奖会退出的bug进行了修复；
    添加了root模式；
    添加了新物品--'?(6星)'；
v8.0的更新内容
    对‘rz’和‘20070623’进行了优化；
    对‘store’中易退出的bug进行了修复；
    添加了新功能--‘rock’；
    添加了一些小彩蛋；
v9.0的更新内容
    加入了‘解密以及加密’模式；
    加入了’全部卖出‘功能；
    优化部分内容
v10.0的更新内容
    加入了‘mods’功能；
    添加内置mods--更多操作1.0；
v10.1的更新内容
    修复了一些bug；
    对内置mods‘更多操作‘进行了升级；
v10.2的更新内容
    修复了一些bug；
    添加了一些小彩蛋；
    对错误提示进行了优化；
    对内置mods‘更多操作‘进行了升级；
    添加新功能--’pr code‘；
v11.0的更新内容
    添加了一些彩蛋；
v11.1的更新内容
    添加新功能-‘r’测试运气；
v11.2的更新内容
    在‘更多操作’中添加了一些内容；
    添加了mods的导入方法；
    添加了一些小功能以及功能注解；
    添加了导出游戏信息的功能--‘v’；
v12.0的更新内容
    添加并完善了mods--‘dictionary’的功能；
    优化了添加新mods的过程；
v12.1的更新内容
    添加了新加密方式--‘base64加密’；
v12.2的更新内容
    添加了一些提示；
    添加了了-’rc‘来统计作弊次数；
    优化了一些内容；
v12.3的更新内容
    优化了UI显示界面；
    加入《用户协议》和《注意事项》；
    添加新mods--’计算器‘；
v12.4的更新内容(代码到达1000行!!)
    添加了--‘t’查看当前时间；
    优化了一些操作；
v12.5的更新内容
    优化了一些内容；
    添加了一些彩蛋；
............................
上次更新：{0}
您的版本为：{1}
    '''.format(date,ver)

#函数组
#0.登陆时
def log():
    print("..........Cros Wuft Games...........")
    while True:
        print("在使用本产品之前请务必同意《用户协议》和阅读《注意事项》，否则将无法进入游戏")
        a = input("输入回车键表示同意；输入‘1’查看《注意事项》；输入2查看《用户协议》")
        if a == '1':
            print("加载中.....")
            time.sleep(0.3)
            print(attention)
            input('输入回车键表示同意')
            print("  ")
        elif a == '2':
            print("加载中.....")
            time.sleep(5)
            input("在加载《用户协议》时出现了一点错误,请重试,错误代码：402")
            print("  ")
        else:
            break
#1.更多操作
def morethings():
    global cps
    print("欢迎使用 更多操作1.3")
    ver=1.3
    while True:
        a=input('<C:/Users/Administrator> ')
        if a=='break':
            input('Process finished with exit code 0')
            break
        elif a.isspace() or a == '':
            pass
        elif a=='pip3 install':
            ab=input("Please select add mods path or url")
            if ab=='others.org' and cps==0:
                mods.append('4.(添加)其他')
                ad = 0
                cs = 0
                time.sleep(1)
                print("collecing others.org")
                time.sleep(3)
                while ad < 11:
                    time.sleep(0.2)
                    ad = ad + 1
                    if cs == 0:
                        time.sleep(0.1)
                        print('HKCU\Software\Policies\Microsoft\Internet Explorer\Restrictions')
                        cs = cs + 1
                    if cs == 1:
                        time.sleep(0.1)
                        print("Microsoft\Internet Explorer\Control Panel\Connwiz Admin Lock")
                        cs = cs + 1
                    if cs == 2:
                        time.sleep(0.1)
                        print("Software\Microsoft\Internet Explorer\Main\Default_Search_URL")
                        cs = cs + 1
                    if cs == 3:
                        time.sleep(0.1)
                        print("HKEY_USERS.DEFAULT\Software\Microsoft\Internet Explorer")
                        cs = cs - 3
                time.sleep(1)
                input('Added successfully!')
                cps=+1
            elif ab=='others.org' and cps!=0:
                time.sleep(1)
                print("collecing others.org")
                time.sleep(3)
                print("Mods cannot be added repeatedly!")
            else:
                print("The file cannot be found,please try again")
        elif a== 'pip2 install'  or  a== 'pip install'  or  a== 'pip':
            print("please use the 'pip3 install' to add mods or jar")
        elif a=='ver':
            print('the ’more operation‘ mods version for you is {0}'.format(ver))
        elif a=='error code'  or  a=='wrong code':
            ab=input("Please enter your encountered error code when using this product")
            if ab=='404':
                print('That may be your network problem, please try a few times')
            elif ab=='401':
                print('Probably there is no content in the mods')
            elif ab=='402':
                print('That may be your network problem, please try a few times')
            else:
                print('Please contact the CrosWuft Corporation with "croswuft202007@outlook.com" for the help')
        elif a=='check' or a=='root' or a=='code':
            code=input("Please enter the variables you want to see")
            if code=='p':
                print(p)
            elif code=='rmb':
                print(rmb)
            elif code=='qwe':
                print(qwe)
            elif code=='player':
                print(player)
            elif code=='used':
                print(used)
            elif code=='cps':
                print(cps)
            elif code=='pin':
                print(pin)
            elif code=='rc':
                print(rc)
            else:
                print("The variable “{0}” cannot be found".format(code))
        else:
            print("'{0}'  is not internal or external command,not to run the program or a batch file".format(a))
#2.翻译
def dictinonary():
    print('欢迎使用CR翻译工具，本mods支持外文转中文和中文转外文，可输入‘quit’退出')
    while True:
        word = input('请输入你想要翻译的词或句：')
        if word == 'quit':
            print('已退出')
            break
        else:
            list_trans = translate(word)
            get_reuslt(list_trans)
def translate(word):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    key = {
        'type': "AUTO",
        'i': word,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    response = requests.post(url, data=key)
    if response.status_code == 200:
        return response.text
    else:
        print("错误")
        return None
def get_reuslt(repsonse):
    result = json.loads(repsonse)
    print ("输入的词为：%s" % result['translateResult'][0][0]['src'])
    print ("翻译结果为：%s" % result['translateResult'][0][0]['tgt'])
#3.计算器
def js1():
    s = input("请输入你要计算的算式")
    s = s.replace(' ', '')
    while '(' in s and ')' in s:
        ret1 = re.search('\([^()]+\)', s).group()  # 用search一个个的找括号里面的公式
        while 1:
            if '*' in ret1 or '/' in ret1:
                e, f = s.split(ret1)  # 用括号里面的内容将公式切割
                # ret1 = ret1.lstrip('(').rstrip(')')    #去掉括号的左右俩边"()"
                ret2 = re.search('\d+(\.\d+)?[*/]-?\d+(\.\d+)?', ret1).group()  # 用search一个个的找括号里面的公式的乘除法
                c, d = ret1.split(ret2)  # 把括号里面的内容用乘除法切割
                if '*' in ret2:
                    a, b = ret2.split('*')  # 用符号切割得到两边的数字
                    ret2 = float(a) * float(b)  # 将字符串转化成浮点数进行运算
                    ret1 = c + str(ret2) + d  # 把运算结果再转回字符串拼接到括号里面
                    s = e + ret1 + f  # 把括号拼接到公式里
                elif '/' in ret2:
                    a, b = ret2.split('/')
                    ret2 = float(a) / float(b)
                    ret1 = c + str(ret2) + d
                    s = e + ret1 + f
            else:
                break
        if '+' in ret1 or '-' in ret1:
            e, f = s.split(ret1)  # 用括号里面的内容将公式切割
            ret1 = ret1.lstrip('(').rstrip(')')  # 去掉括号的左右俩边"()"
            if '--' in s:
                s = s.replace('--', '+')
            if '-+' in s:
                s = s.replace('-+', '-')
            if '+-' in s:
                s = s.replace('+-', '-')
            if '++' in s:
                s = s.replace('++', '+')
            lst = re.findall('[+-]?\d+(?:\.\d+)?', ret1)  # 用findall找到所有的加减法,放到列表里
            res = sum([float(i) for i in lst])
            s = e + str(res) + f
    while '*' in s or '/' in s:  # 计算括号外面的乘除法
        ret = re.search('\d+(\.\d+)?[*/]-?\d+(\.\d+)?', s).group()
        a, b = s.split(ret)
        if '*' in ret:
            c, d = ret.split('*')
            ret = float(c) * float(d)
            s = a + str(ret) + b
        elif '/' in ret:
            a, b = ret.split('/')
            ret = float(c) * float(d)
            s = a + str(ret) + b
    if '--' in s:
        s = s.replace('--', '+')
    if '-+' in s:
        s = s.replace('-+', '-')
    if '+-' in s:
        s = s.replace('+-', '-')
    if '++' in s:
        s = s.replace('++', '+')
    lst = re.findall('[+-]?\d+(?:\.\d+)?', s)  # 用findall找到所有的加减法,放到列表里
    res = sum([float(i) for i in lst])
    print('你的答案为 {0} '.format(res))
def js():
    while True:
        ab = input('即将开始计算，输入’1‘退出')
        if ab == '1':
            print('已退出')
            break
        else:
            command = js1()
#4.其他
def others():
    print("加载中.....")
    time.sleep(3)
    input("错误,错误代码：401")

#函数执行组（‘#’为关闭状态，无‘#’为开启）
#command=morethings()
#command=dictinonary()
#command=js()
#command=others()

command=log()

#运行组
print("..........Cros Wuft Games...........")
print(help)
while True:
    a=input("请输入命令>>>")
    used=used+1
    if a=='help':
        print(help)
    elif a=='rmb':
        print('你的余额为{0}'.format(rmb))
    elif a=='exit':
        print("这个不是退出哦，‘quit’才是")
    elif a=='rz':
        print(rz)
    elif a=='***':
        print("敬请期待")
    elif a=='hello,world!' or a=='hello,world':
        print("hello,world!")
    elif a == 'croswuft':
        if qwe != 0:
            print('croswuft万岁!')
        else:
            rmb = rmb + 0.5
            print('croswuft万岁!')
    elif a.isdigit():
        if a == '20070623':
            print("恭喜你发现了隐藏菜单")
            print(allcd)
        else:
            print(a)
    elif a=='freecj':
        print('欢迎进入免费抽奖,分为三个奖励： 一等奖（1000）  二等奖（50元）  三等奖（8元）')
        input("按下转行键来进行抽奖，你只有三次机会")
        l = 0
        while (l < 3):
            l = l + 1
            print(".......到底有没有中奖呢?........")
            time.sleep(1.8)
            a = random.randint(1, 20)
            if a == 20:
                print("恭喜中大奖--1000")
                rmb = rmb + 1000
            if a == 19:
                print("恭喜中二等奖--50元")
                rmb = rmb + 50
            if 16 < a < 19:
                print("恭喜中三等奖--8元")
                rmb = rmb + 8
            if a < 17:
                print("很遗憾，您没有中奖")
                input("按下转行键来再次进行抽奖")
            if a > 16:
                print("MD，你运气居然那么好，不敢跟你玩了，我怕还吃亏")
                break
    elif a=='cw':
        rc=rc+1
        print('恭喜你发现了开发者模式')
        a=input('请输入你要添加的余额数')
        b=int(a)
        rmb=rmb+b
        print('添加成功，已经为您添加{0}元到余额,可输入’rmb‘查看'.format(b))
    elif a=='cw2':
        rc=rc+1
        print('恭喜你发现了开发者模式2')
        a = input('请输入你要添加的人物(一个)')
        player.append(a)
        print('添加成功，已经为您添加{0},可输入”my“查看'.format(a))
    elif a=='my':
        print('你拥有的物品')
        print(player)
    elif a=='cj':#
        b=input('每次抽奖都将花费10元，是否继续？（输入1继续）')
        if b=='1':
            if rmb<10:
                print("你的余额不足，请到免费抽奖获取")
            else:
                rmb=rmb-10
                print("抽奖奖品有")
                print(sd1)
                print(".......到底会抽中什么奖品呢?........")
                time.sleep(1.8)
                a = random.randint(1, 200)
                if a==1:#1
                    player.append('AWM龙狙（5星）')
                    print('恭喜你，你抽中了”AWM龙狙（5星）“')
                    print('物品已经放置到你的仓库，可输入’my‘前去查看')
                if 1<a<5:#3
                    player.append('M416黄金龙骨（4星）')
                    print('恭喜你，你抽中了”M416黄金龙骨（4星）“')
                    print('物品已经放置到你的仓库，可输入’my‘前去查看')
                if 4<a<8:#3
                    player.append('AKM暗黑杀手（4星）')
                    print('恭喜你，你抽中了”AKM暗黑杀手（4星）“')
                    print('物品已经放置到你的仓库，可输入’my‘前去查看')
                if 7<a<15:#7
                    player.append('AUG绿色巨人（3星）')
                    print('恭喜你，你抽中了”AUG绿色巨人（3星）“')
                    print('物品已经放置到你的仓库，可输入’my‘前去查看')
                if 14<a<25:#10
                    player.append('Kar 98K无名（3星）')
                    print('恭喜你，你抽中了”Kar 98K无名（3星）“')
                    print('物品已经放置到你的仓库，可输入’my‘前去查看')
                if 24<a<35:#10
                    player.append('M16A4使命必达（3星）')
                    print('恭喜你，你抽中了”M16A4使命必达（3星）“')
                    print('物品已经放置到你的仓库，可输入’my‘前去查看')
                if 34<a<51:#16
                    player.append('S686众生平等（2星)')
                    print('恭喜你，你抽中了”S686众生平等（2星)“')
                    print('物品已经放置到你的仓库，可输入’my‘前去查看')
                if 50<a<201:#150
                    player.append('P119无皮肤（1星）')
                    print('恭喜你，你抽中了”P119无皮肤（1星）“')
                    print('物品已经放置到你的仓库，可输入’my‘前去查看')
        else:
            print("已取消抽奖")
    elif a=='sell':
        if player==[]:
            print('检测到你的背包没有物品，不能卖出')
        if player!=[]:
            print('你现在拥有的物品')
            print(player)
            print('注意：无论卖出什么，余额都只增加5')
            a=input('请选择你要卖出的物品序号,一次只能卖出一个（从左到右依次为0，1，2，3.....）')
            if not a.isdigit():
                print("请输入数字")
            else:
                b = int(a)
                c=player.pop(b)
                print('你已经卖出{0}'.format(c))
                rmb=rmb+5
                print("余额已经增加5，可以输入”rmb“查看")
    elif a=='cj 10':
        az=0
        b=input('本次抽奖都将花费100元，是否继续？（输入1继续）')
        if b=='1':
            if rmb<100:
                print("你的余额不足，请到免费抽奖获取")
            else:
                rmb=rmb-100
                while (az<10):
                    time.sleep(1.3)
                    az = az + 1
                    a = random.randint(1, 200)
                    if a == 1:  # 1
                        player.append('AWM龙狙（5星）')
                        print('恭喜你，你抽中了”AWM龙狙（5星）“')
                    if 1 < a < 5:  # 3
                        player.append('M416黄金龙骨（4星）')
                        print('恭喜你，你抽中了”M416黄金龙骨（4星）“')
                    if 4 < a < 8:  # 3
                        player.append('AKM暗黑杀手（4星）')
                        print('恭喜你，你抽中了”AKM暗黑杀手（4星）“')
                    if 7 < a < 15:  # 7
                        player.append('AUG绿色巨人（3星）')
                        print('恭喜你，你抽中了”AUG绿色巨人（3星）“')
                    if 14 < a < 25:  # 10
                        player.append('Kar 98K无名（3星）')
                        print('恭喜你，你抽中了”Kar 98K无名（3星）“')
                    if 24 < a < 35:  # 10
                        player.append('M16A4使命必达（3星）')
                        print('恭喜你，你抽中了”M16A4使命必达（3星）“')
                    if 34 < a < 51:  # 16
                        player.append('S686众生平等（2星)')
                        print('恭喜你，你抽中了”S686众生平等（2星)“')
                    if 50 < a < 201:  # 150
                        player.append('P119无皮肤（1星）')
                        print('恭喜你，你抽中了”P119无皮肤（1星）“')
                print('物品已经放置到你的仓库，可输入’my‘前去查看')
        else:
            print("已取消抽奖")
    elif a=='math':
        x=0
        n=0
        m=0
        print(".................计算答题..................")
        ab=input('请输入你想要答的题数,答五题得一元(不足五题不送钱),无论对错都获得:而且如果你答题超过14题且准确率高的话还会额外再送钱')
        ac=int(ab)
        if ac>4:
            rmb=rmb+(ac/5)
            print('已经赠送您{0}元，可输入“rmb”查看余额'.format(ac/5))
        else:
            print("你所答的题目数量不够5，无法获得rmb,但是你仍然可以答题")
        while (x < ac):
            x = x + 1
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            print("请问 {0}+{1} 等于多少".format(a,b))
            c = input("请输入等于几：")
            d = int(c)
            e = a + b
            if e == d:
                print("真棒，你答对了，继续答题吧")
                n = n + 1
            else:
                print("糟糕，你答错了，正确答案是 {0}".format(e))
                m = m + 1
            print("现在你做的题目数为 {0} ,还要做的题目数为 {1}".format(x, ac - x))
            print("....................................................................")
            time.sleep(1)
        print("你做对的题数为")
        print(n)
        print("你做错的题数为")
        print(m)
        if 20 >= n >= 0.8 * ac:
            print("你的评分为：     A")
            if ac>14:
                print("看你那么厉害，就奖励你30元吧")
                rmb = rmb + 30
        if 0.8 * ac > n >= 0.6 * ac:
            print("你的评分为：     B")
            if ac > 14:
                print("看你那么厉害，就奖励你10元吧")
                rmb = rmb + 10
        if 0.6 * ac> n >= 0.4 * ac:
            print("你的评分为：     C")
            if ac > 14:
                print("看你那么厉害，就奖励你5元吧")
                rmb = rmb + 5
        if 0.4 * ac > n >= 0.2 * ac:
            print("你的评分为：     D")
        if 0.2 * ac > n >= 0:
            print("你的评分为：     E")
    elif a=='qd':
        if qwe!=0:
            print("你今日已经签过到了，明天再来吧")
        if qwe==0:
            qwe=qwe+1
            rmb=rmb+10
            print('签到成功，余额+10，可以输入指令“rmb”查看余额')
    elif a=='sb':
        print("小子，不要乱骂人，叔叔为了教训你先没收你几块钱吧")
        print("rmb—100")
        rmb = rmb - 100
    elif a=='fuck':
        print("小子，不要乱骂人，叔叔为了教训你先没收你几块钱吧")
        print("rmb—100")
        rmb = rmb - 100
    elif a=="cz":
        zs=input('你的余额为{0},请问你要充多少？'.format(rmb))
        za=int(zs)
        if 0<za<100:
            a=random.randint(1,10)
            if a==1:
                print("恭喜你，充值成功")
                print("已到账{0}元，可输入“rmb”查看".format(za))
                rmb=rmb+za
            else:
                print("充值失败，请联系管理员或者作者并把错误代码提供")
                print("错误代码：404  滞留金额：{0}".format(za))
        else:
            print("充值失败，请联系管理员或者作者并把错误代码提供")
            print("错误代码：404  滞留金额：{0}".format(za))
    elif a=='cs':
        secret = random.randint(1, 20)
        print(".........猜数游戏.........")
        temp = input("不妨猜一下我心里想的是哪个数字，你只有五次机会,第一次就猜中有惊喜")
        guess = int(temp)
        az = 0
        while az < 5:
            az = az + 1
            if guess != secret:
                temp = input("哎呀，猜错了，请重新输入吧")
                guess = int(temp)
                if guess == secret:
                    print("卧槽，这你都知道")
                    break
                else:
                    if guess > secret:
                        print(" 哥，大了大了")
                    else:
                        if guess < secret:
                            print("哥，小了小了")
            else:
                print("wow，你居然一下子就猜中了，奖励你50吧")
                rmb = rmb + 50
                break
    elif a=='store':
        print('欢迎进入商店，请问你要买什么？')
        print(things)
        a=input("请输入你要买的物品的编号")
        if not a.isdigit():
            print("请输入数字！")
        else:
            b = int(a)
            if b == 1:
                c = input("你确认要使用10，000元购买AWM龙狙（5星）吗？按下1确认")
                if c == '1':
                    if rmb < 10000:
                        print("您的余额不足，无法购买")
                    else:
                        rmb = rmb - 10000
                        player.append('AWM龙狙（5星）')
                        print('恭喜你，你获得了”AWM龙狙（5星）",物品已经放置到你的仓库，可输入’my‘前去查看')
                else:
                    print("已取消购买")
            if b == 2:
                c = input("你确认要使用9000元购买M416黄金龙骨（4星）吗？按下1确认")
                if c == '1':
                    if rmb < 9000:
                        print("您的余额不足，无法购买")
                    else:
                        rmb = rmb - 9000
                        player.append('M416黄金龙骨（4星）')
                        print('恭喜你，你获得了”M416黄金龙骨（4星）",物品已经放置到你的仓库，可输入’my‘前去查看')
                else:
                    print("已取消购买")
            if b == 3:
                c = input("你确认要使用7999元购买AKM暗黑杀手（4星）吗？按下1确认")
                if c == '1':
                    if rmb < 7999:
                        print("您的余额不足，无法购买")
                    else:
                        rmb = rmb - 7999
                        player.append('AKM暗黑杀手（4星）')
                        print('恭喜你，你获得了”AKM暗黑杀手（4星）",物品已经放置到你的仓库，可输入’my‘前去查看')
                else:
                    print("已取消购买")
            if b > 3 or b < 1:
                print("查无此货,请输入正确编号")
    elif a=='ver':
        print("游戏版本为{0}".format(ver))
        print("游戏由 CrosWuft 开发并代理，版权归 CrosWuft 所有，ResuRrction提供技术支持")
        print("ver.date={0}".format(date))
    elif a=='cj any':
        ac=input("请问你要抽几次奖，抽一次奖将花费10元")
        ab=int(ac)
        if ab<1:
            print("数字{0}出现错误,请重新尝试".format(ac))
        else:
            moy=10*ab
            b=input("您确定花费 {0} 元抽 {1} 次奖吗？，按下1确定".format(moy,ab))
            if not b.isdigit():
                print("请输入数字！")
            else:
                c=int(b)
                if c==1:
                    if rmb<moy:
                        print("你的余额不足，请到免费抽奖获取")
                    else:
                        az=0
                        rmb=rmb-moy
                        while (az < ab):
                            time.sleep(0.2)
                            az = az + 1
                            a = random.randint(1, 200)
                            if a == 1:  # 1
                                player.append('AWM龙狙（5星）')
                                print('恭喜你，你抽中了”AWM龙狙（5星）“')
                            if 1 < a < 5:  # 3
                                player.append('M416黄金龙骨（4星）')
                                print('恭喜你，你抽中了”M416黄金龙骨（4星）“')
                            if 4 < a < 8:  # 3
                                player.append('AKM暗黑杀手（4星）')
                                print('恭喜你，你抽中了”AKM暗黑杀手（4星）“')
                            if 7 < a < 15:  # 7
                                player.append('AUG绿色巨人（3星）')
                                print('恭喜你，你抽中了”AUG绿色巨人（3星）“')
                            if 14 < a < 25:  # 10
                                player.append('Kar 98K无名（3星）')
                                print('恭喜你，你抽中了”Kar 98K无名（3星）“')
                            if 24 < a < 35:  # 10
                                player.append('M16A4使命必达（3星）')
                                print('恭喜你，你抽中了”M16A4使命必达（3星）“')
                            if 34 < a < 51:  # 16
                                player.append('S686众生平等（2星)')
                                print('恭喜你，你抽中了”S686众生平等（2星)“')
                            if 50 < a < 201:  # 150
                                player.append('P119无皮肤（1星）')
                                print('恭喜你，你抽中了”P119无皮肤（1星）“')
                        print('物品已经放置到你的仓库，可输入’my‘前去查看')
    elif a=='ath':
        print("我们的奖品有")
        print(sd1)
    elif a=='quit':
        print('已退出')
        break
    elif a=='my all':#
        af=player.count('P119无皮肤（1星）')
        ah=int(af)
        za=player.count('S686众生平等（2星)')
        zf=int(za)
        az=player.count("M16A4使命必达（3星）")
        ax=int(az)
        sd=player.count("Kar 98K无名（3星）")
        cx=int(sd)
        sw=player.count("AUG绿色巨人（3星）")
        sq=int(sw)
        cv=player.count("AKM暗黑杀手（4星）")
        cb=int(cv)
        xv=player.count('M416黄金龙骨（4星）')
        xd=int(xv)
        cj=player.count('AWM龙狙（5星）')
        co=int(cj)
        ch=player.count('?(6星)')
        cv=int(ch)
        print("你有 {0} 个P119无皮肤（1星）".format(ah))
        print("你有 {0} 个S686众生平等（2星）".format(zf))
        print("你有 {0} 个M16A4使命必达（3星）".format(ax))
        print("你有 {0} 个Kar 98K无名（3星）".format(cx))
        print("你有 {0} 个AUG绿色巨人（3星）".format(sq))
        print("你有 {0} 个AKM暗黑杀手（4星）".format(cb))
        print("你有 {0} 个M416黄金龙骨（4星）".format(xd))
        print("你有 {0} 个AWM龙狙（5星）".format(co))
        print("你有 {0} 个?(6星)".format(cv))
        alp=ah+zf+ax+cx+sq+cb+xd+co+cv
        print("你一共拥有 {0} 件物品".format(alp))
    elif a=='nun':
        rmb=rmb+0.0
        print("小数化成功")
    elif a=='root':
        rc=rc+1
        rmb=rmb+10000000000
        player.append("?(6星)")
        player.append('AWM龙狙（5星）')
        player.append('M416黄金龙骨（4星）')
        player.append('AKM暗黑杀手（4星）')
        print("已启用开发者模式")
    elif a=='rock':
        ad=0
        cs=0
        atime=input("请输入函数T的值")
        if not atime.isdigit():
            print("请输入数字！")
        else:
            btime=int(atime)
            ctime=2*btime
            while ad<ctime:
                time.sleep(0.2)
                ad=ad+1
                if cs==0:
                    time.sleep(0.1)
                    print('HKCU\Software\Policies\Microsoft\Internet Explorer\Restrictions')
                    cs=cs+1
                if cs==1:
                    time.sleep(0.1)
                    print("Microsoft\Internet Explorer\Control Panel\Connwiz Admin Lock")
                    cs=cs+1
                if cs==2:
                    time.sleep(0.1)
                    print("Software\Microsoft\Internet Explorer\Main\Default_Search_URL")
                    cs=cs+1
                if cs==3:
                    time.sleep(0.1)
                    print("HKEY_USERS.DEFAULT\Software\Microsoft\Internet Explorer")
                    cs=cs-3
            print("完成")
    elif a=='mia':
        print("吴涛加密系统1.0》加密文件")
        wen1 = random.randint(1, 100000000)
        a = input("请输入明文,系统将会将其转化为密文")
        if not a.isdigit():  # 报错
            print("请输入数字!!!")
        else:
            b = int(a)
            miwen2 = input("请输入密钥,(输入0为随机)")
            if not miwen2.isdigit():
                print("错误!!!")  # 报错
            else:
                miwen1 = int(miwen2)
                if miwen1 == 0:
                    print("你的密钥为{0}".format(wen1))
                else:
                    wen1 = wen1 - wen1 + miwen1
                    print("你的密钥为{0}".format(wen1))
                scret = ((b * wen1) / 2) * wen1 * 600
                print('加密成功！ 你的密文为{:.0f}'.format(scret))
    elif a=='mib':
        print("吴涛加密系统1.0》解密文件")
        a = input("请输入密文,系统将会将其转化为明文")
        if not a.isdigit():  # 报错
            print("请输入数字!!!")
        else:
            miyao2 = input("请输入密钥")
            if not miyao2.isdigit():  # 报错
                print("错误!!!")
            else:
                b = int(a)
                miyao = int(miyao2)
                miwen = (b / 600) / miyao * 2 / miyao
                print("明文为{:.0f}".format(miwen))
    elif a=='sell all':
        a=len(player)
        b=input('你一共有{0}个物品,你确定要全部清除吗？(按下’1‘确定)'.format(a))
        if b=='1':
            del player
            player=[]
            print("已清除")
        else:
            print("已取消")
    elif a=='mods' or a=='mod':
        print("可使用mods")
        print(mods)
        ab=input("请选择你要使用的mods")
        if not ab.isdigit():  # 报错
            print("请输入正确的选项!!!")
        else:
            b=int(ab)
            if b==1:
                print('已成功启动')
                command=morethings()
            elif b==2:
                print('已成功启动')
                command = dictinonary()
            elif b==3:
                print('已成功启动')
                command = js()
            elif b==4 and cps==1:
                print('已成功启动')
                command = others()
            else:
                print("无该mods,请输入正确的选项")
    elif a=='pr code':
        code=input("请输入兑换码")
        if not code.isdigit():
            print("请输入数字")
        elif code=='20070623':
            if qwe==0:
                rmb=rmb+50
                print("兑换成功，已添加50元至你的钱包，可使用‘rmb’查询")
                qwe=qwe+1
            else:
                print("该兑换码已被使用，不能再次使用")
        else:
            print('请输入正确的兑换码')
    elif a=='r':
        r=random.randint(1,10000)
        if r==10000:#1
            print("wow,你今天的运气超好！快去抽彩票吧，你一定会中奖的，欧皇！")
            print('你的运气点数为{0}'.format(r))
        elif 9996<r<10000:#3
            print('wow,你今天的运气超好！十分适合去抽彩票！')
            print('你的运气点数为{0}'.format(r))
        elif 9990<r<9997:#6
            print("你今天的运气超好呢！")
            print('你的运气点数为{0}'.format(r))
        elif 9980<r<9991:#10
            print("你今天的运气很好哦！")
            print('你的运气点数为{0}'.format(r))
        elif 9950<r<9981:#30
            print("你今天的运气比较好呢！")
            print('你的运气点数为{0}'.format(r))
        elif 9899<r<9951:#50
            print("你今天的运气还偏好吧")
            print('你的运气点数为{0}'.format(r))
        elif 9799<r<9900:#99
            print("你今天的运气还算算不错吧")
            print('你的运气点数为{0}'.format(r))
        elif 8000<r<9800:#1798
            print("你今天的运气还算正常吧")
            print('你的运气点数为{0}'.format(r))
        elif 3999<r<8001:#4000
            print("你的运气不算差了")
            print('你的运气点数为{0}'.format(r))
        elif 1499<r<4000:#2499
            print("你的运气不是太好哦")
            print('你的运气点数为{0}'.format(r))
        elif 998<r<1500:#500
            print("你的运气比较坏哦")
            print('你的运气点数为{0}'.format(r))
        elif 507<r<999:#490
            print("你的运气很糟糕啊！")
            print('你的运气点数为{0}'.format(r))
        elif 400<r<508:#106
            print("你的运气简直差到爆炸啊！")
            print('你的运气点数为{0}'.format(r))
        elif 100<r<401:#299
            print("你的运气....,惨不忍睹啊！")
            print('你的运气点数为{0}'.format(r))
        elif 50<r<101:#49
            print("你的运气...,这是要完啊！")
            print('你的运气点数为{0}'.format(r))
        elif 15<r<51:#34
            print("我都不想说了，你自己看吧.....")
            print('你的运气点数为{0}'.format(r))
        elif 5<r<16:#9
            print("这几天出门记得看黄历...")
            print('你的运气点数为{0}'.format(r))
        elif 3<r<6:#2
            print("你的运气已经无可救药了....")
            print('你的运气点数为{0}'.format(r))
        elif r==3 or r==2:#2
            print("最近别做任何赌运气的事情，你会后悔的，最好去拜佛，注意身体健康，保重吧.....")
            print('你的运气点数为{0}'.format(r))
        elif r==1:#1
            print("w我不知道该说你的运气如何，说好吧，又那么少；说不好吧，又那么特别，你自己看吧")
            print('你的运气点数为{0}'.format(r))
        else:
            print("出错")
    elif a=='v':
        if rc==0:
            print("你的游戏信息为")
            print('ver={0}'.format(ver))
            print("date={0}".format(date))
            print('p={0}'.format(p))
            print('cps={0}'.format(cps))
            print('qwe={0}'.format(qwe))
            print('rmb={0}'.format(rmb))
            print('used={0}'.format(used))
            print('pin={0}'.format(pin))
            print('rc={0},Flase'.format(rc))
            print('mods={0}'.format(mods))
            print('player={0}'.format(player))
        else:
            print("你的游戏信息为")
            print('ver={0}'.format(ver))
            print("date={0}".format(date))
            print('p={0}'.format(p))
            print('cps={0}'.format(cps))
            print('qwe={0}'.format(qwe))
            print('rmb={0}'.format(rmb))
            print('used={0}'.format(used))
            print('pin={0}'.format(pin))
            print('rc={0},True'.format(rc))
            print('mods={0}'.format(mods))
            print('player={0}'.format(player))
    elif a=='base1':
        s=input('请输入你要加密的内容')
        bs = base64.b64encode(s.encode("utf8"))
        print('密文：(注：密文取‘’中间部分)')
        print(bs)
    elif a=='base2':
        bs=input("请输入你要解密的内容")
        decode = base64.b64decode(bs)
        r=(decode.decode("utf8"))
        print('原文是: {0}'.format(r))
    elif a=='t':
        time_tuple = time.localtime(time.time())
        print("当前时间为 {}年{}月{}日{}点{}分{}秒".format(time_tuple[0], time_tuple[1], time_tuple[2], time_tuple[3], time_tuple[4],
                                             time_tuple[5]))
    else:
        if p<26: #25
            print('请输入正确的指令，可输入”help“寻求帮助')
            p=p+1
        elif 25<p<31: #5
            print("求你了，别再乱按了")
            p=p+1
        elif 30<p<51: #20
            print("说别按就别乱按了嘛，你再乱按？")
            p=p+1
        elif 50<p<81: #30
            print("这是最后的次警告，你再乱按试试？")
            p=p+1
        else:
            rmb=rmb+5
            print("好吧，你太闲了，我输了...")
            print("               ")
            p=p-p










