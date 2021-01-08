#!/usr/bin/python3
# -*- coding:utf-8 -*-
import os
import time

backup_base_dir = 'D:\\test\\'
backup_user = 'repl'
backup_passwd = 'qwe123'
postgresql_port = '5432'
postgresql_bin_path = os.path.join('D:\\pgdata\\', 'bin')
backup_data = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
backup_master_ip = '139.180.209.229'
backup_dir = os.path.join(backup_base_dir, backup_data)


def backup():
    if not backup_dir:
        os.mkdir(backup_dir)
    print('打印备份命令， 开始备份.........')
    time.sleep(1)
    os.system('mkdir {}'.format(backup_dir))
    #os.chdir(postgresql_bin_path)
    print('命令bin路径:   ' + str(os.getcwd()))
    print('备份路径：  ', backup_dir)
    os.system(
        ".\\pg_basebackup.exe  -h {} -U {} -D {} -l replback -v".format(backup_master_ip, backup_user, backup_dir))
    print('备份完成.')


if __name__ == '__main__':
    backup()
    # os.listdir(backup_dir)
