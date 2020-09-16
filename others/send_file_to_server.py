import pexpect
import time

local_file_dir = input('本地文件路径:')
remote_user_name = input('服务器用户名:')
remote_user_passwd = input('服务器登陆密码:')
remote_host_addr = input('服务器IP:')
remote_file_dir = input('服务器文件路径:')

cmd = 'scp ' + local_file_dir + ' ' + remote_user_name + '@' + remote_host_addr + ':' + remote_file_dir

while True:
    try:
        p = pexpect.spawn(cmd)
        p.expect('pasword:')
        p.sendline(remote_user_passwd)
        time.sleep(10)
    except Exception as e:
        print(e)
        break
