"""
微信远程控制

by feather
"""

import itchat
import cmd
from logger import logger,encode_crlf


@itchat.msg_register('Text')
def cmd_parser(msg):
    text = msg['Text']
    to_name = msg['ToUserName']

    if to_name == 'filehelper' and text[0] == '@':
        # 命令的开头是@
        logger.info(encode_crlf(text))  # 先记录日志
        args = text.split(' ')
        func_name = 'do_' + args[0][1:]
        try:
            func = getattr(cmd, func_name)
        except:
            func = cmd.do_help

        try:
            func(args)
        except Exception as e:
            logger.error(encode_crlf(str(e) )  )


def main():
    itchat.auto_login(hotReload=True)
    itchat.run()
    itchat.dump_login_status()


if __name__ == '__main__':
    main()
