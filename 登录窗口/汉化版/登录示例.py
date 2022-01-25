#模块组
import tkinter as tk
import tkinter.messagebox
import pickle

#函数组
#要用到的函数
def a():
    wa = tk.Tk()
    wa.title("Internet Explorer")  # 主题文字
    wa.geometry("250x200")  # 窗口长宽

    la=tk.Label(wa,text='错误', # 标签的文字
            font=("Arial",23),# 字体和字体大小
            width=10,height=10)  # 标签长宽
    la.pack()# 固定窗口位置

    b = tk.Button(wa, text='重试',  # 标签的文字
                  width=4, height=1,  # 标签长宽
                  command=a)
    b.pack()  # 固定窗口位置
    la.place(x=35,y=-120)
    b.place(x=100,y=100)
def b():
    # 整个窗口
    win = tk.Tk()
    win.title("Internet Explorer")  # 主题文字
    win.geometry("850x530")  # 窗口长宽
    # 标签1
    l = tk.Label(win, text='无法连接至互联网',  # 标签的文字
                 font=("Arial", 30),  # 字体和字体大小
                 width=15, height=15)  # 标签长宽

    l.pack()  # 固定窗口位置
    # 标签2
    b = tk.Button(win, text='刷新',  # 标签的文字
                  width=4, height=1,  # 标签长宽
                  command=a)
    b.pack()  # 固定窗口位置

    # 各个窗口放置
    l.place(x=250, y=-200)
    b.place(x=390, y=200)

    win.mainloop()  # 循环


#运行组
root = tk.Tk()  # 实例化对象
root.title('Internet Explorer')     # 给窗口取名
root.geometry("400x300")


canvas = tk.Canvas(root, height=200, width=500)
image_file = tk.PhotoImage(file='welcome.gif')
image = canvas.create_image(35, 0, anchor='nw',
                            image=image_file)
canvas.pack(side='top')

tk.Label(root, text='用户名:', font=('Arial', 13)).place(x=70, y=160)
tk.Label(root, text='密码:', font=('Arial', 13)).place(x=70, y=190)

var_user_name = tk.StringVar()
var_user_name.set('new.@croswuft.com')

entry_user_name = tk.Entry(root, textvariable=var_user_name)
entry_user_name.place(x=160, y=160)

var_user_password = tk.StringVar()
entry_user_password = tk.Entry(root, textvariable=var_user_password, show='*')
entry_user_password.place(x=160, y=190)


def user_login():
    user_name = var_user_name.get()
    user_pssword = var_user_password.get()
    try:
        with open("usrs_info.pickle",'rb') as user_file:
            usrs_info = pickle.load(user_file)
    except FileNotFoundError:
        with open('usrs_info.pickle', 'wb') as user_file:
            usrs_info={'admin': 'admin'}
            pickle.dump(usrs_info, user_file)

    if user_name in usrs_info:
        if user_pssword == usrs_info[user_name]:
            tk.messagebox.showinfo(title="登陆成功", message='欢迎您，' + user_name)
        else:
            tk.messagebox.showerror(title="错误",message="密码错误，请重试!")
    else:
        is_sign_up = tk.messagebox.askyesno(title='错误', message='你还没有注册，是否现在注册？')

        if is_sign_up:
            user_sign_up()



def user_sign_up():
    def sign_up_admin():
        np = new_psd.get()
        npf = new_psd_confirm.get()
        nn = new_name.get()

        with open('usrs_info.pickle', 'rb') as user_file:
            exit_user_info = pickle.load(user_file)
        if np !=npf:
            tk.messagebox.showerror(title="错误", message='密码与确认密码不相同，请重试！')
        elif nn in exit_user_info:
            tk.messagebox.showerror(title="错误", message='该名称已被注册')
        else:
            exit_user_info[nn] = np
            with open('usrs_info.pickle','wb') as user_file:
                pickle.dump(exit_user_info,user_file)
            tk.messagebox.showinfo(title='注册成功', message="注册成功！")
            root_sign_up.destroy()

    root_sign_up = tk.Toplevel(root)
    root_sign_up.geometry('350x200')
    root_sign_up.title('Sign up root')

    new_name = tk.StringVar()
    new_name.set('new.@croswuft.com')
    tk.Label(root_sign_up,text="用户名:").place(x=10, y=10)
    entry_new_name = tk.Entry(root_sign_up,textvariable=new_name).place(x=120, y=10)

    new_psd = tk.StringVar()
    new_psd.set('')
    tk.Label(root_sign_up, text="密码:").place(x=10, y=60)
    entry_new_psd = tk.Entry(root_sign_up, textvariable=new_psd, show='*').place(x=120, y=60)

    new_psd_confirm = tk.StringVar()
    new_psd_confirm.set('')
    tk.Label(root_sign_up, text="确认密码:").place(x=10, y=110)
    entry_new_psd_confirm = tk.Entry(root_sign_up, textvariable=new_psd_confirm, show='*').place(x=120, y=110)

    btn_comfirm_sign_up = tk.Button(root_sign_up,text='注册',command=sign_up_admin)
    btn_comfirm_sign_up.place(x=170,y=160)

login = tk.Button(root, text='登录', command=user_login).place(x=170, y=230)
sign_up = tk.Button(root, text='注册', command=user_sign_up).place(x=240, y=230)

root.mainloop()     # 大型的while循环









