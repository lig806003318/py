#!/usr/bin/python3

import paramiko


def connect_server(ip, user, passwd, port):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, port=port, username=user, password=passwd)
    stdin, stdout, stderr = ssh.exec_command("pwd")
    result = stdout.readlines()
    print(result)
    ssh.close()


if __name__ == '__main__':
    connect_server(ip='147.139.29.156', user='root', passwd='oDgKhLEL4xDJv8f2', port='22')
