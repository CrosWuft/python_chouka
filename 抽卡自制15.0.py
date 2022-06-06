#提示组
attention='''            《注意事项》
注意事项1：在v12.0以及以上版本需安装'requests'模块；

注意事项2：吴涛加密系统只能加密数字，base64加密系统能加密中文，英文字母和数字；

注意事项3：添加mods请到‘更多操作’使用‘pip’进行添加；

注意事项4：游戏由 CrosWuft 开发并代理，版权归 CrosWuft 所有，ResuRrction提供技术支持，禁止在未经作者的允许下私自篡改游戏内容，代码；

注意事项5：游戏作者联系方式-- croswuft202007@outlook.com ,欢迎向我提供本游戏的bug；

注意事项6：本游戏将会不定期更新，请留意最新版本，新版本更新网址： https://github.com/CrosWuft/python_chouka；

注意事项7：内置mods翻译请在联网时使用，'t'获取的时间只是本地时间；
'''

#模块组
import random
import time
import json
import webbrowser
import requests
import base64
import re

#参数组
date='2022.6.7s1'#更新日期
ver='v15.0'#版本
p=0#输入错误次数
cps=0#与mods有关
qwe=0#签到，兑换码，彩蛋
rmb=0#货币
rc=0#作弊次数
doc='jar'#储存文件的后缀名
used=0#输入次数
rozlist=[]#操作记录记录表
ast=False#math作弊系统的开关
loger=0#登录状态
mods = ['1.(内置)更多操作','2.(内置)翻译','3.(内置)计算器']#mods列表
sd1=['?(6星)','AWM龙狙（5星）','M416黄金龙骨（4星）','AKM暗黑杀手（4星）','AUG绿色巨人（3星）','Kar 98K无名（3星）','M16A4使命必达（3星）'
,'S686众生平等（2星）','P119无皮肤（1星）']#奖品列表
player=[]#玩家仓库
chenjiu=['是新游戏哎！']#玩家成就
#游戏ID生成
adv=str(random.randint(0,10000000000000))#本次游戏ID(数字部分)
ads='C-'#本次游戏ID(字母部分)
for i in range(4):
    list1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    l=random.choice(list1)
    ads=ads+l
pin=ads+' '+adv#本次游戏ID
fn = 'chouka '+ver+'.'+doc#文件名

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
    sell s   分项卖出
    ju       查看成就  
    log      注册
    reg      登录
    r        测试运气
    t        查看当前时间
    ***      敬请期待
    (更多小彩蛋等你去探索！！)
    '''
mhelp='''   morethings help list
    help          帮助
    break         退出
    pip3 install  加入其他mods
    ver           查看当前版本
    error code    查询错误代码的原因
    code          查看某一个参数的数值
    root          更改某个参数
    id            查看本次游戏ID
    del rozlist   清空操作记录
    code help     查看代码解析'''
things='''
    1.AWM龙狙（5星）       10,000元
    2.M416黄金龙骨（4星）   9,000元
    3.AKM暗黑杀手（4星）    7，999元
            (更多物品敬请期待)
    '''
allcd='''
    cw          开发者模式1（充钱）
    cw2         开发者模式2（添加物品）
    cw3         开发者模式3（添加成就）
    sb          扣取100元
    fuck        扣取100元
    20070623    此隐藏菜单
    [数字]       显示'数字'      
    root        进入开发者模式
    exit        显示'这个...才是'
    rock        装逼模式
    rock2       装逼模式2(试用)
    v           导出游戏信息
    croswuft    显示‘cr...万岁’
    hello,world 显示’he...ld!‘
    return      返回任意一个值
    check       对文件内容进行展开
    rozlist     输出操作记录
    get all ju  获得所有成就
    gw          进入官网(仅支持在电脑上使用)
    m           快速启动morethings
    m2          快速启动dictionary
    ju rst      查看成就获得规则
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
v12.6的更新内容
    允许在morethings中修改参数；
    在morethings中添加了‘help’查看帮助；
    对morethings进行了优化和更新；
    添加了一些彩蛋以及细节；
v12.7的更新内容
    添加了快速启动mods的按键；
    添加了另一种‘rock’(试用)；
    对游戏编码进行升级；
    更改了一些细节；
v12.8的更新内容
    修复了大量bug；
v12.9的更新内容
    添加了节日报告功能；
    添加了‘成就’功能；
    添加了’ju‘来查看成就；
    添加了一些其他功能；
v12.10的更新内容
    修复了一些内容；
    对'rock2'进行了升级；
    添加了'code help'功能；
v13.0的更新内容
    添加了'sell s'功能；
    添加了记录操作记录的功能；
    添加了备份功能--'roz'(实验功能)；
v14.0的更新内容
    修复了很多bug；
    添加了登录功能--'log'；
    更新了更多操作1.5；
    暂时移除了roz功能；
    在'sell s'中添加了简易选择；
    添加了获得?(6星)的方法；
    修复了无密码登录的bug；
v14.1的更新内容
    修复了一些显示bug；
    对'my all'进行了优化；
    添加了新功能--'cw3'；
    修复了一个登陆时的问题；
v14.2的更新内容
    修复了一个一直以来存在的bug；
    修复了一个显示bug；
    对'sells'进行了升级；
v14.3的更新内容
    对't','cw'进行了更新；
    利用'try'对一些功能进行了升级；
    对'return'进行了更新；
    在开启函数--'log'中添加了反作弊系统；
    添加了新功能--'gw'，但只能在电脑使用；
    修复了一些bug并添加了一些细节；
    更新了新功能--'check'；
    对'log'和'reg'进行了优化；
v15.0的更新内容(代码到达2000行!!)
      ☆(史诗级别的更新!)☆
    对'math'进行了重构更新；
    对'return'和'cr'进行了更新；
    添加了很多些彩蛋和优化了一些细节；
    添加了新功能--'get all ju'；
    添加了新功能--'del rozlist'；
    修复了一些bug；
    添加了退出登陆的功能；
    对'cs'进行了重构更新；
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
            if rc==0:
                if rmb==0:
                    if loger==0:
                        if player==[]:
                            if chenjiu==['是新游戏哎！']:
                                if ast==False:
                                    break
                                else:
                                    print("你已经修改了游戏参数'ast'，违反了《注意事项》第4条，将不能进入游戏！")
                                    print("解决办法：将参数修改成原来的样子或重新下载本游戏！")
                                    time.sleep(1000000)
                            else:
                                print("你已经修改了游戏参数'chenjiu'，违反了《注意事项》第4条，将不能进入游戏！")
                                print("解决办法：将参数修改成原来的样子或重新下载本游戏！")
                                time.sleep(1000000)
                        else:
                            print("你已经修改了游戏参数'player'，违反了《注意事项》第4条，将不能进入游戏！")
                            print("解决办法：将参数修改成原来的样子或重新下载本游戏！")
                            time.sleep(1000000)
                    else:
                        print("你已经修改了游戏参数'loger'，违反了《注意事项》第4条，将不能进入游戏！")
                        print("解决办法：将参数修改成原来的样子或重新下载本游戏！")
                        time.sleep(1000000)
                else:
                    print("你已经修改了游戏参数'rmb'，违反了《注意事项》第4条，将不能进入游戏！")
                    print("解决办法：将参数修改成原来的样子或重新下载本游戏！")
                    time.sleep(1000000)
            else:
                print("你已经修改了游戏参数'rc'，违反了《注意事项》第4条，将不能进入游戏！")
                print("解决办法：将参数修改成原来的样子或重新下载本游戏！")
                time.sleep(1000000)
#1.更多操作
def morethings():
    mver=1.6
    global rc,pin,used,cps,qwe,loger,doc,ver,fn,ast,rozlist
    print("欢迎使用 更多操作{0}".format(mver))
    while True:
        a=input('<C:/Users/Administrator> ')
        if a=='break' or a=='b':
            input('Process finished with exit code 0')
            break
        elif a.isspace() or a == '':
            pass
        elif a=='del rozlist':
            del rozlist
            rozlist=[]
            print("You successfully cleared rozlist list")
        elif a=='pip3 install':
            ab=input("Please select add mods path or url")
            if ab=='others.org' and cps==0:
                mods.append('4.(添加)其他')
                ad = 0
                cs = 0
                time.sleep(1)
                print("collecing others.org")
                time.sleep(4)
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
                time.sleep(2)
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
        elif a=='ver'  or  a=='version':
            print('the ’more operation‘ mods version for you is {0}'.format(mver))
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
        elif a=='check' or a=='code':
            code=input("Please enter the variables you want to see")
            if code == 'p':
                print(p)
            elif code == 'rmb':
                print(rmb)
            elif code == 'qwe':
                print(qwe)
            elif code == 'player':
                print(player)
            elif code == 'used':
                print(used)
            elif code == 'cps':
                print(cps)
            elif code == 'pin':
                print(pin)
            elif code == 'rc':
                print(rc)
            elif code == 'loger':
                print(loger)
            elif code == 'doc':
                print(doc)
            elif code =='ast':
                print(ast)
            else:
                print("The variable “{0}” cannot be found".format(code))
        elif a=='help':
            print(mhelp)
        elif a=='root':
            a = input("Please enter the parameters you want to change")
            if a == 'rc':
                cv = int(input("Please enter a variable"))
                rc = cv + rc
                print('You have successfully changed the parameters')
            elif a=='pin':
                print("Modifications to the string 'pin' are not legitimate")
            elif a=='used':
                cv = int(input("Please enter a variable"))
                used = cv + used
                print('You have successfully changed the parameters')
            elif a=='cps':
                cv = int(input("Please enter a variable"))
                cps = cv + cps
                print('You have successfully changed the parameters')
            elif a=='qwe':
                cv = int(input("Please enter a variable"))
                qwe = cv + qwe
                print('You have successfully changed the parameters')
            elif a=='loger':
                cv = int(input("Please enter a variable"))
                loger = cv + loger
                print('You have successfully changed the parameters')
            elif a=='doc':
                cv = input("Please enter a variable")
                doc=cv
                fn = 'chouka ' + ver + '.' + doc
                print('You have successfully changed the parameters')
            elif a=='ast':
                cv = input("Please enter a variable")
                if cv=='True':
                    ast=True
                    print('You have successfully changed the parameters')
                elif cv=='False':
                    ast=False
                    print('You have successfully changed the parameters')
                else:
                    print("Please enter the correct parameters")
            else:
                print('Parameter “{0}” cannot be found'.format(a))
        elif a=='game id' or a=='id':
            print('Your ID for this game is‘ {0} ‘'.format(pin))
        elif a=='code help':
            print('''Code Help
ver#版本
date#更新日期                  
p#输入错误次数
cps#与mods有关
qwe#签到，兑换码，彩蛋
rmb#货币
rc#作弊次数
used#输入次数
mods#mods列表
player#玩家仓库
loger#登录状态
ast#math作弊系统的开关
doc#储存文件的后缀名
rozlist#操作记录记录表
chenjiu#玩家成就              ''')
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
    time.sleep(4)
    input("错误,错误代码：401")

#函数执行组（有‘#’为关闭状态，无‘#’为开启）
#command=morethings()
#command=dictinonary()
#command=js()
#command=others()

command=log()

#运行组
print("..........Cros Wuft Games...........")
print(help)
print("您本次游戏的ID为{0}".format(pin))
while True:
    a=input("请输入命令>>>")
    rozlist.append(a)
    used=used+1
    if a=='help' or a=='list':
        print(help)
    elif a=='rozlist':
        print(rozlist)
    elif a=='rmb':
        print('你的余额为{0}'.format(rmb))
    elif a=='exit':
        print("这个不是退出哦，‘quit’才是")
    elif a=='rz':
        print(rz)
    elif a=='***' or a=='*' or a=='**':
        print("敬请期待")
    elif a=='hello,world!' or a=='hello,world':
        print("hello,world!")
    elif a=='m' or a=='m1':
        command = morethings()
    elif a=='m2':
        command = dictinonary()
    elif a=='ju':
        print("你所拥有的成就为{}".format(chenjiu))
    elif a=='gw':
        webbrowser.open('https://github.com/CrosWuft/python_chouka')
        print("正在进入官网....")
        print("Tips:手机用户使用时会报错！请不要使用手机进行该行为！")
        time.sleep(2)
        print("启动成功！")
    elif a=='return' or a=='return ':
        ax=random.randint(1,10)
        if ax==1:
            print(f"p(输入错误次数)={p}")
        elif ax==2:
            print(f"cps(与mods有关)={cps}")
        elif ax==3:
            print(f"qwe(签到，兑换码，彩蛋)={qwe}")
        elif ax==4:
            print(f"rc(作弊次数)={rc}")
        elif ax==5:
            print(f"doc(储存文件的后缀名)={doc}")
        elif ax==6:
            print(f"used(输入次数)={used}")
        elif ax==7:
            print(f"loger(登录状态)={loger}")
        elif ax==8:
            print(f"fn(文件名)={fn}")
        elif ax==9:
            print(f"ast(math作弊系统的开关)={ast}")
        elif ax==10:
            print("None Return!")
    elif a=='get all ju':
        rc=rc+1
        if "最佳运气王！" not in chenjiu:
            time.sleep(1)
            print("恭喜你获得成就--‘最佳运气王！’")
            chenjiu.append("最佳运气王！")
        if "?这运气！" not in chenjiu:
            time.sleep(1)
            print("恭喜你获得成就--‘?这运气！‘")
            chenjiu.append("?这运气！")
        if "充值成功！" not in chenjiu:
            time.sleep(1)
            print("达成成就--‘充值成功！’")
            chenjiu.append("充值成功!")
        if "新的世界！" not in chenjiu:
            time.sleep(1)
            print("恭喜你获得成就--‘新的世界！’")
            chenjiu.append("新的世界！")
        if '是新游戏哎！' not in chenjiu:
            print("恭喜你获得成就--‘是新游戏哎！’")
            chenjiu.append("是新游戏哎！")
    elif a=='ju rst':
        print('''成就规则：
第1个成就一一最佳运气王:需要在R测试运气中，运气值为1万
第2个成就一一？这运气！：需要在R测试运气中,运气值为1
第3个成就一一充值成功：需要在充值界面中反复充值，直到充值成功
第4个成就一一新的世界：需要打开隐藏菜单（注意：本成要最先完成，若先完成其他成就，将无法再获得此成就）''' )
    elif a=='croswuft' or a=='cw' or a=='cros' or a=='cr':
        if qwe != 0:
            print('croswuft万岁!')
        else:
            kf = random.randint(1, 20)
            if a=='croswuft':
                if kf<16:
                    rmb = rmb + 0.5
                print('croswuft万岁!')
            else:
                if a=='cros':
                    if kf<4:
                        rmb=rmb+0.5
                if a=='cr' or a=='cw':
                    if kf==1:
                        rmb = rmb + 0.5
                print('croswuft万岁!')
    elif a.isdigit():
        if a == '20070623':
            print("恭喜你发现了隐藏菜单")
            print(allcd)
            if '新的世界！' not in chenjiu:
                time.sleep(1)
                print("恭喜你获得成就--‘新的世界！’")
                chenjiu.append("新的世界！")
            else:
                pass
        elif a=='114514':
            print("你好恶臭呀！")
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
        try:
            b=int(a)
        except ValueError:
            print("请您输入数字！")
        else:
            rmb=rmb+b
            print('添加成功，已经为您添加{0}元到余额,可输入’rmb‘查看'.format(b))
    elif a=='cw2':
        rc=rc+1
        print('恭喜你发现了开发者模式2')
        a = input('请输入你要添加的人物(一个)')
        player.append(a)
        print('添加成功，已经为您添加{0},可输入”my“查看'.format(a))
    elif a=='cw3':
        rc=rc+1
        print('恭喜你发现了开发者模式')
        a=input("请输入你想要添加的成就")
        chenjiu.append(a)
        print('添加成功，已经为您成就-- {0},可输入”ju“查看'.format(a))
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
                    player.append('S686众生平等（2星）')
                    print('恭喜你，你抽中了”S686众生平等（2星）“')
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
                        player.append('S686众生平等（2星）')
                        print('恭喜你，你抽中了”S686众生平等（2星）“')
                    if 50 < a < 201:  # 150
                        player.append('P119无皮肤（1星）')
                        print('恭喜你，你抽中了”P119无皮肤（1星）“')
                print('物品已经放置到你的仓库，可输入’my‘前去查看')
        else:
            print("已取消抽奖")
    elif a=='math':
        mathver = '2022.6.5'  # 最近一次的更新时间
        x = 0  # 答题次数
        n = 0  # 答对的题
        m = 0  # 答错的题
        re = 0  # 是否退钱
        rk = 0  # 款数
        rmb = 0
        print("....................计算挑战.....................")
        print('''难度规则：
1.简单:5~30以内的数加法运算(题目奖励√，正确率奖励x)
2.普通:两位数以内加减运算(题目奖励√，正确率奖励√)
3.困难:两位数到三位数的加减乘运算(题目奖励√，正确率奖励√)
                    ''')
        dif = input("请输入你想要挑战的难度编号，难度越高，奖励越丰富")
        if dif == '1':  # 简单模式
            print("................简单模式.................")
            print("简单模式规则:每作答5道题就奖励1元(作答不够5道题不送钱；若作答题目大于或等于20道还会额外送钱),但如果最后的正确率评级小于C则没有奖励")
            ab = input('请输入你想要答的题数')
            try:
                ac = int(ab)
            except ValueError:
                print("请输入数字！")
            else:
                rmb = rmb + (ac / 5)
                if ac < 5:
                    print("你所答的题目数量不够5，无法获得奖励,但是你仍然可以答题")
                    rmb = rmb - (ac / 5)
                    re = re - 1
                if 4 < ac < 20:
                    print('已经赠送您{0}元，可输入“rmb”查看余额'.format(ac / 5))
                if 50 > ac > 20 or ac == 20:
                    print('已经赠送您{0}元，可输入“rmb”查看余额'.format(ac / 5))
                    print("还有，本次作答将额外赠送你20元!")
                    rk = rk + 20
                    rmb = rmb + 20
                if ac > 50 or ac == 50:
                    print('已经赠送您{0}元，可输入“rmb”查看余额'.format(ac / 5))
                    print("另外，本次作答将额外赠送你100元!")
                    rmb = rmb + 100
                    rk = rk + 100
                while (x < ac):
                    x = x + 1
                    a = random.randint(5, 30)
                    b = random.randint(5, 30)
                    print("请问 {0}+{1} 等于多少".format(a, b))
                    if ast == True:
                        print(f"答案是' {a + b} '")
                    c = input("请输入等于几：")
                    try:
                        d = int(c)
                    except ValueError:
                        print("请输入数字！")
                        print("现在你做的题目数为 {0} ,还要做的题目数为 {1}".format(x, ac - x))
                        print("....................................................................")
                        time.sleep(1)
                        m = m + 1
                    else:
                        e = a + b
                        if e == d:
                            print("真棒，你答对了，继续答题吧")
                            n = n + 1
                        else:
                            print("糟糕，你答错了，正确答案是 {0}".format(e))
                            m = m + 1
                        print("现在你做的题目数为 {0} ,还要做的题目数为 {1}".format(x, ac - x))
                        print("....................................................................")
                        time.sleep(1.3)
                print(f"你做对的题数为:  {n}")
                print(f"你做错的题数为:  {m}")
                if ac >= n >= 0.8 * ac:
                    print("你的评分为：     A")
                if 0.8 * ac > n >= 0.6 * ac:
                    print("你的评分为：     B")
                if 0.6 * ac > n >= 0.4 * ac:
                    print("你的评分为：     C")
                if 0.4 * ac > n >= 0.2 * ac:
                    print("你的评分为：     D")
                    re = re + 1
                if 0.2 * ac > n >= 0:
                    print("你的评分为：     E")
                    re = re + 1
                if re > 0:
                    print("由于你的成绩太差了，你将没有奖励")
                    rmb = rmb - rk - (ac / 5)
                print(f'你现在拥有的rmb:{rmb}')
        elif dif == '2':  # 普通模式
            print("................普通模式.................")
            print("普通模式规则:每作答5道题就奖励1元(若作答题目大于或等于20道还会额外送钱),但如果最后的正确率评级小于D则没有奖励,若准确率为A，还会额外奖励15元")
            ab = input('请输入你想要答的题数')
            try:
                ac = int(ab)
            except ValueError:
                print("请输入数字！")
            else:
                rmb = rmb + (ac / 5)
                if ac < 20:
                    print('已经赠送您{0}元，可输入“rmb”查看余额'.format(ac / 5))
                if 40 > ac > 20 or ac == 20:
                    print('已经赠送您{0}元，可输入“rmb”查看余额'.format(ac / 5))
                    print("还有，本次作答将额外赠送你30元!")
                    rk = rk + 30
                    rmb = rmb + 30
                if ac > 40 or ac == 40:
                    print('已经赠送您{0}元，可输入“rmb”查看余额'.format(ac / 5))
                    print("另外，本次作答将额外赠送你100元!")
                    rmb = rmb + 100
                    rk = rk + 100
                while (x < ac):
                    x = x + 1
                    a = random.randint(10, 100)
                    b = random.randint(10, 100)
                    way = random.randint(1, 2)
                    if way == 1:
                        print("请问 {0}+{1} 等于多少".format(a, b))
                        if ast == True:
                            print(f"答案是' {a + b} '")
                        c = input("请输入等于几：")
                        try:
                            d = int(c)
                        except ValueError:
                            print("请输入数字！")
                            print("现在你做的题目数为 {0} ,还要做的题目数为 {1}".format(x, ac - x))
                            print("....................................................................")
                            time.sleep(1)
                            m = m + 1
                        else:
                            e = a + b
                            if e == d:
                                print("真棒，你答对了，继续答题吧")
                                n = n + 1
                            else:
                                print("糟糕，你答错了，正确答案是 {0}".format(e))
                                m = m + 1
                            print("现在你做的题目数为 {0} ,还要做的题目数为 {1}".format(x, ac - x))
                            print("....................................................................")
                            time.sleep(1.3)
                    if way == 2:
                        print("请问 {0}-{1} 等于多少".format(a, b))
                        if ast == True:
                            print(f"答案是' {a - b} '")
                        c = input("请输入等于几：")
                        try:
                            d = int(c)
                        except ValueError:
                            print("请输入数字！")
                            print("现在你做的题目数为 {0} ,还要做的题目数为 {1}".format(x, ac - x))
                            print("....................................................................")
                            time.sleep(1)
                            m = m + 1
                        else:
                            e = a - b
                            if e == d:
                                print("真棒，你答对了，继续答题吧")
                                n = n + 1
                            else:
                                print("糟糕，你答错了，正确答案是 {0}".format(e))
                                m = m + 1
                            print("现在你做的题目数为 {0} ,还要做的题目数为 {1}".format(x, ac - x))
                            print("....................................................................")
                            time.sleep(1.3)
                print(f"你做对的题数为:  {n}")
                print(f"你做错的题数为:  {m}")
                if ac >= n >= 0.8 * ac:
                    print("你的评分为：     A")
                    if ac > 15:
                        print("由于你的成绩太好了，就奖励你15元吧")
                        rmb = rmb + 15
                if 0.8 * ac > n >= 0.6 * ac:
                    print("你的评分为：     B")
                if 0.6 * ac > n >= 0.4 * ac:
                    print("你的评分为：     C")
                if 0.4 * ac > n >= 0.2 * ac:
                    print("你的评分为：     D")
                if 0.2 * ac > n >= 0:
                    print("你的评分为：     E")
                    re = re + 1
                if re > 0:
                    print("由于你的成绩太差了，你将没有奖励")
                    rmb = rmb - rk - (ac / 5)
                print(f'你现在拥有的rmb:{rmb}')
        elif dif == '3':  # 困难模式
            print("................困难模式.................")
            print("困难模式规则:每作答两道题就奖励一元(若作答题目大于10道还会额外送钱),但是如果最后的正确率为D或E就没有奖励,若正确率是A,还会额外奖励")
            ab = input('请输入你想要答的题数')
            try:
                ac = int(ab)
            except ValueError:
                print("请输入数字！")
            else:
                rmb = rmb + (ac / 2)
                if ac < 11:
                    print('已经赠送您{0}元，可输入“rmb”查看余额'.format(ac / 5))
                if 10 < ac < 25:
                    print('已经赠送您{0}元，可输入“rmb”查看余额'.format(ac / 5))
                    print("还有，本次作答将额外赠送你50元!")
                    rk = rk + 50
                    rmb = rmb + 50
                if 50 > ac > 24:
                    print('已经赠送您{0}元，可输入“rmb”查看余额'.format(ac / 5))
                    print("还有，本次作答将额外赠送你100元!")
                    rk = rk + 100
                    rmb = rmb + 100
                if ac > 50 or ac == 50:
                    print('已经赠送您{0}元，可输入“rmb”查看余额'.format(ac / 5))
                    print("另外，本次作答将额外赠送你500元!")
                    rmb = rmb + 500
                    rk = rk + 500
                while (x < ac):
                    x = x + 1
                    a = random.randint(20, 1000)
                    b = random.randint(20, 1000)
                    way = random.randint(1, 3)
                    if way == 1:
                        print("请问 {0}+{1} 等于多少".format(a, b))
                        if ast == True:
                            print(f"答案是' {a + b} '")
                        c = input("请输入等于几：")
                        try:
                            d = int(c)
                        except ValueError:
                            print("请输入数字！")
                            print("现在你做的题目数为 {0} ,还要做的题目数为 {1}".format(x, ac - x))
                            print("....................................................................")
                            time.sleep(1)
                            m = m + 1
                        else:
                            e = a + b
                            if e == d:
                                print("真棒，你答对了，继续答题吧")
                                n = n + 1
                            else:
                                print("糟糕，你答错了，正确答案是 {0}".format(e))
                                m = m + 1
                            print("现在你做的题目数为 {0} ,还要做的题目数为 {1}".format(x, ac - x))
                            print("....................................................................")
                            time.sleep(1.3)
                    if way == 2:
                        print("请问 {0}-{1} 等于多少".format(a, b))
                        if ast == True:
                            print(f"答案是' {a - b} '")
                        c = input("请输入等于几：")
                        try:
                            d = int(c)
                        except ValueError:
                            print("请输入数字！")
                            print("现在你做的题目数为 {0} ,还要做的题目数为 {1}".format(x, ac - x))
                            print("....................................................................")
                            time.sleep(1)
                            m = m + 1
                        else:
                            e = a - b
                            if e == d:
                                print("真棒，你答对了，继续答题吧")
                                n = n + 1
                            else:
                                print("糟糕，你答错了，正确答案是 {0}".format(e))
                                m = m + 1
                            print("现在你做的题目数为 {0} ,还要做的题目数为 {1}".format(x, ac - x))
                            print("....................................................................")
                            time.sleep(1.3)
                    if way == 3:
                        print("请问 {0}x{1} 等于多少".format(a, b))
                        if ast == True:
                            print(f"答案是' {a * b} '")
                        c = input("请输入等于几：")
                        try:
                            d = int(c)
                        except ValueError:
                            print("请输入数字！")
                            print("现在你做的题目数为 {0} ,还要做的题目数为 {1}".format(x, ac - x))
                            print("....................................................................")
                            time.sleep(1)
                            m = m + 1
                        else:
                            e = a * b
                            if e == d:
                                print("真棒，你答对了，继续答题吧")
                                n = n + 1
                            else:
                                print("糟糕，你答错了，正确答案是 {0}".format(e))
                                m = m + 1
                            print("现在你做的题目数为 {0} ,还要做的题目数为 {1}".format(x, ac - x))
                            print("....................................................................")
                            time.sleep(1.3)
                print(f"你做对的题数为:  {n}")
                print(f"你做错的题数为:  {m}")
                if ac >= n >= 0.8 * ac:
                    print("你的评分为：     A")
                    if ac > 10:
                        print("由于你的成绩太好了，就奖励你50元吧")
                        rmb = rmb + 50
                if 0.8 * ac > n >= 0.6 * ac:
                    print("你的评分为：     B")
                    if ac > 15:
                        print("由于你的成绩太好了，就奖励你30元吧")
                        rmb = rmb + 30
                if 0.6 * ac > n >= 0.4 * ac:
                    print("你的评分为：     C")
                if 0.4 * ac > n >= 0.2 * ac:
                    print("你的评分为：     D")
                    re = re + 1
                if 0.2 * ac > n >= 0:
                    print("你的评分为：     E")
                    re = re + 1
                if re > 0:
                    print("由于你的成绩太差了，你将没有奖励")
                    rmb = rmb - rk - (ac / 2)
                print(f'你现在拥有的rmb:{rmb}')
        else:
            print("请输入正确的选项！")
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
                if '充值成功！' not in chenjiu:
                    time.sleep(1)
                    print("达成成就--‘充值成功！’")
                    chenjiu.append("充值成功!")
            else:
                print("充值失败，请联系管理员或者作者并把错误代码提供")
                print("错误代码：404  滞留金额：{0}".format(za))
        else:
            print("充值失败，请联系管理员或者作者并把错误代码提供")
            print("错误代码：404  滞留金额：{0}".format(za))
    elif a=='cs':
        csver = '2022.6.7' # 最近一次的更新时间
        print("..............猜数游戏..............")
        print('''难度规则：
1.简单:简单的数字
2.普通:困难多变的数字组合
3.困难:简单的数字字母组合
4.地狱：困难多变的数字字母组合            ''')
        choicedif = input("请选择你的难度")
        if choicedif == '1':
            print("..............简单模式..............")
            print("规则：机会：5次,奖励：第1或第2次猜中分别奖励10元和5元")
            dc1 = random.randint(1, 25)
            dc2 = random.randint(15, 35)
            secret = random.randint(dc1, dc2)
            if ast == True:
                print(f"这个数字是' {secret} '")
            temp = input(f"猜一下我心里想的是哪个数字(范围：{dc1}-{dc2})，你只有五次机会,猜中有惊喜")
            try:
                guess = int(temp)
            except:
                print("输入错误！")
            else:
                az = 0
                while az < 5:
                    az = az + 1
                    if az == 5:
                        if guess != secret:
                            print(f"哎，这都猜不对，正确答案是{secret}")
                        else:
                            print('终于在最后一次猜对了呀！')
                    if az != 5:
                        if guess > secret:
                            temp = input("哎呀,猜大了!请重新输入吧")
                            try:
                                guess = int(temp)
                            except:
                                print("输入错误！")
                            else:
                                pass
                        if guess == secret:
                            if az == 1:
                                print("卧槽,居然第一次就猜中了！")
                                print("送你10元吧")
                                rmb = rmb + 10
                            elif az == 2:
                                print("卧槽,居然第二次就猜中了！")
                                print("送你5元吧")
                                rmb = rmb + 5
                            else:
                                print(f"居然用了{az}次才猜中...")
                            break
                        if guess < secret:
                            temp = input("哎呀,猜小了!请重新输入吧")
                            try:
                                guess = int(temp)
                            except:
                                print("输入错误！")
                            else:
                                pass
        elif choicedif == '2':
            print("..............普通模式..............")
            print("规则：机会：8次,奖励：第1~3次猜中奖励30元，第4~5次猜中奖励10元，第6~8次猜中奖励5元")
            dc1 = random.randint(1, 80)
            dc2 = random.randint(50, 100)
            secret = random.randint(dc1, dc2)
            if ast == True:
                print(f"这个数字是' {secret} '")
            temp = input(f"猜一下我心里想的是哪个数字(范围：{dc1}-{dc2})，你只有八次机会,猜中有惊喜")
            try:
                guess = int(temp)
            except:
                print("输入错误！")
            else:
                az = 0
                while az < 8:
                    az = az + 1
                    if az == 8:
                        if guess != secret:
                            print(f"哎，这都猜不对，正确答案是{secret}")
                        else:
                            print('终于在最后一次猜对了呀！')
                    if az != 8:
                        if guess > secret:
                            temp = input("哎呀,猜大了!请重新输入吧")
                            try:
                                guess = int(temp)
                            except:
                                print("输入错误！")
                            else:
                                pass
                        if guess == secret:
                            if 0 < az < 4:
                                print(f"卧槽,居然那么快，只用{az}次就猜中了！")
                                print("送你30元吧")
                                rmb = rmb + 30
                            elif az == 4 or az == 5:
                                print(f"居然才第{az}次就猜中了！")
                                print("送你10元吧")
                                rmb = rmb + 10
                            elif az == 6 or az == 7 or az == 8:
                                print(f"你用了{az}次才猜中...")
                                print("送你5元吧")
                                rmb = rmb + 5
                            break
                        if guess < secret:
                            temp = input("哎呀,猜小了!请重新输入吧")
                            try:
                                guess = int(temp)
                            except:
                                print("输入错误！")
                            else:
                                pass
        elif choicedif == '3':
            print("..............困难模式..............")
            print("规则：1~3次猜中奖励1000元，4~6次猜中奖励300元，7~10次猜中奖励100元")
            list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
            l1 = random.choice(list1)
            l2 = random.choice(list1)
            dc1 = random.randint(1, 30)
            dc2 = random.randint(20, 50)
            secret = random.randint(dc1, dc2)
            if ast == True:
                print(f'字母是’ {l1 + l2} ‘ 或 ‘{l2 + l1} ’')
            temp = input("猜一下我心里想的是那两个字母(均为大写字母)，你只有10次机会,猜中有惊喜")
            c = 0
            az = 0
            while az < 9:
                az = az + 1
                if l1 in temp or l2 in temp:
                    if l1 in temp and l2 in temp:
                        print(f"真棒，你只用了{az}次机会，接下来还有{10 - az}次机会猜数字")
                        c = c + 1
                        break
                    if l1 in temp:
                        print(f"你猜中了一个字母‘{l1}’")
                    if l2 in temp:
                        print(f"你猜中了一个字母‘{l2}’")
                if l1 not in temp or l2 not in temp:
                    temp = input(f"你猜错了，还有{10 - az}次机会")
            if c != 0:
                if ast == True:
                    print(f"这个数字是' {secret} '")
                timp = input(f"猜一下我心里想的是哪个数字(范围：{dc1}-{dc2})，你还有{10 - az}次机会,猜中有惊喜")
                try:
                    guess = int(timp)
                except:
                    print("输入错误！")
                else:
                    while az < 10:
                        az = az + 1
                        if az == 10:
                            if guess != secret:
                                print(f"哎，这都猜不对，正确答案是{secret}")
                            else:
                                print('终于在最后一次猜对了呀！')
                        if az != 10:
                            if guess > secret:
                                temp = input("哎呀,猜大了!请重新输入吧")
                                try:
                                    guess = int(temp)
                                except:
                                    print("输入错误！")
                                else:
                                    pass
                            if guess == secret:
                                if az < 4:
                                    print(f"卧槽,居然那么快({az}次)就猜中了！")
                                    print("送你1000元吧")
                                    rmb = rmb + 1000
                                if 3 < az < 7:
                                    print(f"居然猜{az}次就猜中了！")
                                    print("送你300元吧")
                                    rmb = rmb + 300
                                if 6 < az < 11:
                                    print(f"居然用了{az}次才猜中...")
                                    print("还是奖励你100元吧!")
                                    rmb = rmb + 100
                                break
                            if guess < secret:
                                temp = input("哎呀,猜小了!请重新输入吧")
                                try:
                                    guess = int(temp)
                                except:
                                    print("输入错误！")
                                else:
                                    pass
        elif choicedif == '4':
            print("..............地狱模式..............")
            print("规则：1~5次猜中奖励2000元，6~10次猜中奖励800元，11~15次猜中奖励500元")
            list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
            word = ''
            l1 = random.choice(list1)
            l2 = random.choice(list1)
            l3 = random.choice(list1)
            l4 = random.choice(list1)
            word = l1 + l2 + l3 + l4
            dc1 = random.randint(1, 80)
            dc2 = random.randint(50, 120)
            secret = random.randint(dc1, dc2)
            if ast == True:
                print(f'字母是’ {word} ‘')
            temp = input("猜一下我心里想的是那四个字母(均为大写字母)，你只有15次机会,猜中有惊喜")
            c = 0
            az = 0
            while az < 14:
                az = az + 1
                if word != temp:
                    temp = input(f"你猜错了，还有{15 - az}次机会")
                elif word == temp:
                    print(f"真棒，你只用了{az}次机会，接下来还有{15 - az}次机会猜数字")
                    c = c + 1
                    break
            if c != 0:
                if ast == True:
                    print(f"这个数字是' {secret} '")
                timp = input(f"猜一下我心里想的是哪个数字(范围：{dc1}-{dc2})，你还有{15 - az}次机会,猜中有惊喜")
                try:
                    guess = int(timp)
                except:
                    print("输入错误！")
                else:
                    while az < 15:
                        az = az + 1
                        if az == 15:
                            if guess != secret:
                                print(f"哎，这都猜不对，正确答案是{secret}")
                            else:
                                print('终于在最后一次猜对了呀！')
                        if az != 15:
                            if guess > secret:
                                temp = input("哎呀,猜大了!请重新输入吧")
                                try:
                                    guess = int(temp)
                                except:
                                    print("输入错误！")
                                else:
                                    pass
                            if guess == secret:
                                if az < 6:
                                    print(f"卧槽,居然那么快({az}次)就猜中了！")
                                    print("送你2000元吧")
                                    rmb = rmb + 2000
                                if 5 < az < 11:
                                    print(f"居然猜{az}次就猜中了！")
                                    print("送你800元吧")
                                    rmb = rmb + 800
                                if 10 < az < 16:
                                    print(f"居然用了{az}次才猜中...")
                                    print("还是奖励你500元吧!")
                                    rmb = rmb + 500
                                break
                            if guess < secret:
                                temp = input("哎呀,猜小了!请重新输入吧")
                                try:
                                    guess = int(temp)
                                except:
                                    print("输入错误！")
                                else:
                                    pass
        else:
            print("请输入正确的选项！")
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
                                player.append('S686众生平等（2星）')
                                print('恭喜你，你抽中了”S686众生平等（2星）“')
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
        za=player.count('S686众生平等（2星）')
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
        alp = ah + zf + ax + cx + sq + cb + xd + co + cv
        adq = int(len(player))
        c=adq-alp
        print("你有 {0} 个未知物品".format(c))
        print("你一共拥有 {0} 件物品".format(adq))
    elif a=='nun':
        rmb=rmb+0.00
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
            player.append('?(6星)')
            if '最佳运气王！' not in chenjiu:
                time.sleep(1)
                print("恭喜你获得成就--‘最佳运气王！’")
                chenjiu.append("最佳运气王！")
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
            print("我不知道该说你的运气如何，说好吧，又那么少；说不好吧，又那么特别，你自己看吧")
            print('你的运气点数为{0}'.format(r))
            player.append('?(6星)')
            if '?这运气！' not in chenjiu:
                time.sleep(1)
                print("恭喜你获得成就--‘?这运气！‘")
                chenjiu.append("?这运气！")
        else:
            print("出错")
    elif a=='v':
        if rc==0:
            print("你的游戏信息为")
            print('ver={0}'.format(ver))
            print("date={0}".format(date))
            print("loger={0}".format(loger))
            print('p={0}'.format(p))
            print('cps={0}'.format(cps))
            print('qwe={0}'.format(qwe))
            print('rmb={0}'.format(rmb))
            print('used={0}'.format(used))
            print('pin={0}'.format(pin))
            print('rc={0},Flase'.format(rc))
            print('mods={0}'.format(mods))
            print('player={0}'.format(player))
            print("chenjiu={0}".format(chenjiu))
        else:
            print("你的游戏信息为")
            print('ver={0}'.format(ver))
            print("date={0}".format(date))
            print("loger={0}".format(loger))
            print('p={0}'.format(p))
            print('cps={0}'.format(cps))
            print('qwe={0}'.format(qwe))
            print('rmb={0}'.format(rmb))
            print('used={0}'.format(used))
            print('pin={0}'.format(pin))
            print('rc={0},True'.format(rc))
            print('mods={0}'.format(mods))
            print('player={0}'.format(player))
            print("chenjiu={0}".format(chenjiu))
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
        t = time.localtime()
        print("当前时间为 {}年{}月{}日{}点{}分{}秒".format(t[0], t[1], t[2], t[3], t[4], t[5]))
        if t[1] == 1 and t[2] == 1:
            print("元旦快乐")
        elif t[1] == 3 and t[2] == 12:
            print("今天是植树节，你植树了吗？")
        elif t[1] == 4 and t[2] == 5:
            print("“清明时节雨纷纷...”")
        elif t[1] == 5 and t[2] == 1:
            print("今天是劳动节喔！")
        elif t[1] ==5 and t[2] ==20:
            print("今天是‘520’喔！")
        elif t[1] == 6 and t[2] == 1:
            print("今天是儿童节喔！")
        elif t[1] == 6 and t[2] == 23:
            print("今天是作者生日喔！")
        elif t[0] == 2022 and t[1] == 6 and t[2] == 26:
            print("今天是生地中考喔")
        elif t[1] == 10 and t[2] == 1:
            print("国庆节快乐！")
        elif t[1] == 12 and t[2] == 24:
            print("今天是平安夜，你吃苹果了吗？")
        elif t[1] == 12 and t[2] == 25:
            print("圣诞快乐！")
    elif a=='rock2':
        print("安装中...")
        time.sleep(1)
        print("已完成0%")
        time.sleep(1)
        for i in range(1, 100):
            print("已完成{}%".format(i))
            time.sleep(0.01)
        time.sleep(4)
        print("已完成100%!")
        time.sleep(1)
        print("加载成功！")
        time.sleep(1.5)
        print("解压中....")
        time.sleep(2)
        ad=0
        while ad<30:
            cs = random.randint(1, 8)
            t2 = random.randint(0, 100)
            t = t2 * 0.003
            time.sleep(t)
            ad=ad+1
            if cs == 0:
                print('HKCU\Software\Policies\Microsoft\Internet Explorer\Restrictions')
            elif cs == 1:
                print("Microsoft\Internet Explorer\Control Panel\Connwiz Admin Lock")
            elif cs == 2:
                print("Software\Microsoft\Internet Explorer\Main\Default_Search_URL")
            elif cs == 3:
                print("HKEY_USERS.DEFAULT\Software\Microsoft\Internet Explorer")
            elif cs == 4:
                print('HKCU\Software\Microsoft\Windows\CurrentVersion\Internet')
            elif cs == 5:
                print("HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion")
            elif cs == 6:
                print("Microsoft\Windows\CurrentVersion\Internet Settings\Zones")
            elif cs == 7:
                print('Windows\CurrentVersion\Internet Settings\Zones')
            elif cs == 8:
                print("SoftWare/Microsoft/Internet Exploer/Main")
        time.sleep(1.5)
        input("解压成功！")
    elif a=='sell something' or a=='sell s' or a=='sells':
        a=0
        if player==[]:
            print('检测到你的背包没有物品，不能卖出')
        else:
            af = player.count('P119无皮肤（1星）')
            ah = int(af)
            za = player.count('S686众生平等（2星）')
            zf = int(za)
            az = player.count("M16A4使命必达（3星）")
            ax = int(az)
            sd = player.count("Kar 98K无名（3星）")
            cx = int(sd)
            sw = player.count("AUG绿色巨人（3星）")
            sq = int(sw)
            cv = player.count("AKM暗黑杀手（4星）")
            cb = int(cv)
            xv = player.count('M416黄金龙骨（4星）')
            xd = int(xv)
            cj = player.count('AWM龙狙（5星）')
            co = int(cj)
            ch = player.count('?(6星)')
            cv = int(ch)
            print("你有 {0} 个P119无皮肤（1星）".format(ah))
            print("你有 {0} 个S686众生平等（2星）".format(zf))
            print("你有 {0} 个M16A4使命必达（3星）".format(ax))
            print("你有 {0} 个Kar 98K无名（3星）".format(cx))
            print("你有 {0} 个AUG绿色巨人（3星）".format(sq))
            print("你有 {0} 个AKM暗黑杀手（4星）".format(cb))
            print("你有 {0} 个M416黄金龙骨（4星）".format(xd))
            print("你有 {0} 个AWM龙狙（5星）".format(co))
            print("你有 {0} 个?(6星)".format(cv))
            alp = ah + zf + ax + cx + sq + cb + xd + co + cv
            adq = int(len(player))
            c = adq - alp
            print("你有 {0} 个未知物品".format(c))
            print("你一共拥有 {0} 件物品".format(adq))
            print('''卖出价格
1.P119无皮肤（1星）    5rmb
2.S686众生平等（2星）  8rmb
3.M16A4使命必达（3星） 10rmb
4.Kar 98K无名（3星）  10rmb
5.AUG绿色巨人（3星）   10rmb
6.AKM暗黑杀手（4星）   15rmb
7.M416黄金龙骨（4星）  18rmb
8.AWM龙狙（5星）      30rmb
9.?(6星)            1000rmb
                          ''')
            th = input("请输入你要卖出的物品名称或序号")
            if th == 'P119无皮肤（1星）' or th=='1':
                while True:
                    if 'P119无皮肤（1星）' in player:
                        player.remove('P119无皮肤（1星）')
                        rmb = rmb + 5
                        a = a + 5
                    else:
                        print("已全部卖出共计{1}个物品,换得{0}rmb".format(a,ah))
                        break
            elif th == 'S686众生平等（2星）' or th=='2':
                while True:
                    if 'S686众生平等（2星）' in player:
                        player.remove('S686众生平等（2星）')
                        rmb = rmb + 8
                        a = a + 8
                    else:
                        print("已全部卖出共计{1}个物品,换得{0}rmb".format(a,zf))
                        break
            elif th == 'M16A4使命必达（3星）' or th=='3':
                while True:
                    if 'M16A4使命必达（3星）' in player:
                        player.remove('M16A4使命必达（3星）')
                        rmb = rmb + 10
                        a = a + 10
                    else:
                        print("已全部卖出共计{1}个物品,换得{0}rmb".format(a,ax))
                        break
            elif th == 'Kar 98K无名（3星）' or th=='4':
                while True:
                    if 'Kar 98K无名（3星）' in player:
                        player.remove('Kar 98K无名（3星）')
                        rmb = rmb + 10
                        a = a + 10
                    else:
                        print("已全部卖出共计{1}个物品,换得{0}rmb".format(a,cx))
                        break
            elif th == 'AUG绿色巨人（3星）' or th=='5':
                while True:
                    if 'AUG绿色巨人（3星）' in player:
                        player.remove('AUG绿色巨人（3星）')
                        rmb = rmb + 10
                        a = a + 10
                    else:
                        print("已全部卖出共计{1}个物品,换得{0}rmb".format(a,sq))
                        break
            elif th == 'AKM暗黑杀手（4星）' or th=='6':
                while True:
                    if 'AKM暗黑杀手（4星）' in player:
                        player.remove('AKM暗黑杀手（4星）')
                        rmb = rmb + 15
                        a = a + 15
                    else:
                        print("已全部卖出共计{1}个物品,换得{0}rmb".format(a,cb))
                        break
            elif th == 'M416黄金龙骨（4星）' or th=='7':
                while True:
                    if 'M416黄金龙骨（4星）' in player:
                        player.remove('M416黄金龙骨（4星）')
                        rmb = rmb + 18
                        a = a + 18
                    else:
                        print("已全部卖出共计{1}个物品,换得{0}rmb".format(a,xd))
                        break
            elif th == 'AWM龙狙（5星）' or th=='8':
                while True:
                    if 'AWM龙狙（5星）' in player:
                        player.remove('AWM龙狙（5星）')
                        rmb = rmb + 30
                        a = a + 30
                    else:
                        print("已全部卖出共计{1}个物品,换得{0}rmb".format(a,co))
                        break
            elif th == '?(6星)' or th=='9':
                while True:
                    if '?(6星)' in player:
                        player.remove('?(6星)')
                        rmb = rmb + 1000
                        a = a + 1000
                    else:
                        print("已全部卖出共计{1}个物品,换得{0}rmb".format(a,cv))
                        break
            elif th in player:
                print("物品{0}过于昂贵，不能被卖出".format(th))
            else:
                print("找不到物品{0}，可能是你输入错误了".format(th))
    elif a=='log':
        print("注册页面")
        with open(fn, 'a') as cr:
            pass
        with open(fn, 'r') as cr:
            lines = cr.readlines()
        mm = ''
        zh = ''
        lin=0
        for line in lines:
            if lin == 1:
                zh += line.rstrip()
                zh += ","
                lin = lin - 1
            else:
                mm += line.rstrip()
                mm += ','
                lin = lin + 1
        czh = input("请输入账号")
        if czh in zh:
            print("该账户已被创建!请重新输入")
        else:
            cmm = input("请输入密码")
            if cmm=='':
                print("密码不能为空！")
            else:
                zcmm=input("请再次输入密码")
                if zcmm==cmm:
                    with open(fn, 'a') as cr:
                        cr.write(czh)
                        cr.write("\n")
                        cr.write(cmm)
                        cr.write("\n")
                    print("注册成功！")
                else:
                    print("两次输入的密码不一样！")
    elif a=='reg':
        if loger > 0:
            try:
                # noinspection PyUnboundLocalVariable
                print(f"当前登录账户--' {szh} '")
            except NameError:
                print("程序产生冲突！")
            else:
                pass
            choice=input("请不要进行多次登录！如果要退出登录请输入1")
            if choice=='1':
                time.sleep(1)
                print("已退出登录！")
                loger=loger-1
            else:
                pass
        else:
            print("登录界面")
            with open(fn, 'a') as cr:
                pass
            with open(fn, 'r+') as cr:
                lines = cr.readlines()
            mm = ''
            zh = ''
            lin = 1
            for line in lines:
                if lin == 1:
                    zh += line.rstrip()
                    zh += ","
                    lin = lin - 1
                else:
                    mm += line.rstrip()
                    mm += ','
                    lin = lin + 1
            szh = input("请输入你的账号")
            smm = input("请输入你的密码")
            if szh in zh:
                if smm in mm:
                    if smm != '':
                        print(f"登陆成功！欢迎您，尊贵的{szh}")
                        loger = loger + 1
                    else:
                        print("密码不能为空！")
                else:
                    print("密码错误,请重新输入")
            else:
                print("账号错误,请重新输入")
    elif a=='check':
        with open(fn, 'a') as cr:
            pass
        with open(fn, 'r+') as cr:
            lines = cr.readlines()
        ast=''
        for line in lines:
            ast+=line.rstrip()
            ast+=('\n')
        print("文件储存内容如下\n")
        print(ast)
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
            print("好吧，你太闲了，我输了，送你5块钱，不要再来烦我...")
            print("               ")
            p=p-p
#version=15.0,line in 2140 CrosWuft,2022,6,7,s1 TM
#v15.0特殊Tips:这次版本我做了很久，也是积累和创作时间最久的一次，从几周前就开始思考构造了，但为了版本完整性，我没有选择正常的‘每周发布’，由于有些东西对于我来说非常难，特别是'cs'和'math'的重构，我花了很多时间和精力，到写这段话为止，已经是凌晨一点多了，我很疲惫，但也很高兴，因为我写完了那么长的东西，不出意外的话，这次应该是中考前的最后一次更新了，也是我的生日作，如果你能看到这句话，那就请祝我生日快乐吧，我的生日是六月23日！












