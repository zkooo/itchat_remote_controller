"""
各个命令的处理函数
"""

import itchat
import os
# import ptyprocess  # 需开启shell功能去掉此行注释，后面还有
from time import sleep
from threading import Thread
from subprocess import check_output, STDOUT
from subprocess import CalledProcessError, TimeoutExpired
from logger import logger, encode_crlf


switch = False
shell = None
shell_path = os.getenv('SHELL')


def do_help(args):
    """获取帮助信息"""
    objs = globals()
    msg = '~~ 支持的命令有{\n'
    for name in objs:
        if name.startswith('do_'):
            cmd = '@' + name.strip('do_')
            doc = objs[name].__doc__
            msg += '    %s : %s\n' % (cmd, doc)
    msg += '}'
    itchat.send(msg, 'filehelper')


def do_exec(args):
    """执行系统命令"""
    if len(args) >= 2:
        # 至少有两个参数，第一个参数是这个处理函数的名字
        try:
            cmd = ' '.join(args[1:])
            result = check_output(cmd, stderr=STDOUT, timeout=5, shell=True).decode()
        except (CalledProcessError, TimeoutExpired)as e:
            result = e.output.decode()
            logger.warn(encode_crlf(result))
        except Exception as e:
            result = str(e)
            logger.error(result)

        msg = '<\n%s\n>' % result
        itchat.send(msg, 'filehelper')


def do_exit(args):
    """关闭程序，关闭后需手动开启"""
    itchat.send('关闭程序...', 'filehelper')
    sleep(2)
    itchat.logout()


    
''' # 若要开启shell功能，去掉这个多行注释
def do_shell(args):
    """打开/关闭交互式shell"""
    global switch, shell
    if shell_path:
        if not switch:
            # 开启shell
            try:
                shell = ptyprocess.PtyProcessUnicode.spawn([shell_path, '-i'])
                t = Thread(target=shell_output)
                t.setDaemon(True)
                t.start()
                switch = True
                itchat.send('<\nshell on\n>', 'filehelper')
                logger.info('shell on')
            except Exception as e:
                itchat.send('<\n开启失败\n>', 'filehelper')
                switch = False
                logger.error(encode_crlf(str(e) ) )
        else:
            # 关闭shell
            try:
                shell.terminate(True)
                switch = False
                itchat.send('<\nshell off\n>', 'filehelper')
                logger.info('shell off')
            except Exception as e:
                itchat.send('<\n关闭失败，请重新尝试\n>', 'filehelper')
                switch = True
                logger.error(encode_crlf(str(e) ) )
    else:
        itchat.send('<\n当前系统没有shell\n>', 'filehelper')


def do_s(args):
    """输入命令到交互式shell中"""
    if switch:
        cmd = ' '.join(args[1:]) + '\n'
        shell.write(cmd)
    else:
        itchat.send('<\nshell off\n>', 'filehelper')


def shell_output():
    """用于实时获取shell输出的线程"""
    try:
        while shell.isalive():
            line = shell.readline()  # 这一行有控制台转义序列，丢弃
            line = shell.readline()
            msg = '> %s' % line
            itchat.send(msg, 'filehelper')
            logger.debug(encode_crlf('shell %s' % line) )
    except Exception as e:
        logger.error(encode_crlf(str(e) ) )
'''
