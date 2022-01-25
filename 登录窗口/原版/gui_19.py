"""
时间：2021/03/11
版本号：2.6
重点：登录窗口3
"""
import tkinter as tk
import tkinter.messagebox
import pickle

root = tk.Tk()  # 实例化对象
root.title('Welcome to Python')     # 给窗口取名
root.geometry("400x300")


canvas = tk.Canvas(root, height=200, width=500)
image_file = tk.PhotoImage(file='welcome.gif')
image = canvas.create_image(35, 0, anchor='nw',
                            image=image_file)
canvas.pack(side='top')

tk.Label(root, text='User name:', font=('Arial', 14)).place(x=45, y=160)
tk.Label(root, text='Password:', font=('Arial', 14)).place(x=45, y=190)

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
            tk.messagebox.showinfo(title="Welcome", message='How are you?' + user_name)
        else:
            tk.messagebox.showerror(message="Error your password is wrong,try again!")
    else:
        is_sign_up = tk.messagebox.askyesno(title='Hi', message='You have not sign up yet,sign up today?')

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
            tk.messagebox.showerror(title="Error", message='Password and confirm password must be the same!')
        elif nn in exit_user_info:
            tk.messagebox.showerror(title="Error", message='The user has already signed up!')
        else:
            exit_user_info[nn] = np
            with open('usrs_info.pickle','wb') as user_file:
                pickle.dump(exit_user_info,user_file)
            tk.messagebox.showinfo(title='Welcome', message="You have successfully signed up!")
            root_sign_up.destroy()

    root_sign_up = tk.Toplevel(root)
    root_sign_up.geometry('350x200')
    root_sign_up.title('Sign up root')

    new_name = tk.StringVar()
    new_name.set('new.@croswuft.com')
    tk.Label(root_sign_up,text="User name:").place(x=10, y=10)
    entry_new_name = tk.Entry(root_sign_up,textvariable=new_name).place(x=120, y=10)

    new_psd = tk.StringVar()
    new_psd.set('')
    tk.Label(root_sign_up, text="Password:").place(x=10, y=60)
    entry_new_psd = tk.Entry(root_sign_up, textvariable=new_psd, show='*').place(x=120, y=60)

    new_psd_confirm = tk.StringVar()
    new_psd_confirm.set('')
    tk.Label(root_sign_up, text="Confirm Password:").place(x=10, y=110)
    entry_new_psd_confirm = tk.Entry(root_sign_up, textvariable=new_psd_confirm, show='*').place(x=120, y=110)

    btn_comfirm_sign_up = tk.Button(root_sign_up,text='Sign up',command=sign_up_admin)
    btn_comfirm_sign_up.place(x=170,y=160)

login = tk.Button(root, text='Login', command=user_login).place(x=170, y=210)
sign_up = tk.Button(root, text='Sign up', command=user_sign_up).place(x=240, y=210)

root.mainloop()     # 大型的while循环
