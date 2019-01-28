"""
管理日志
"""

import logging
from logging.handlers import TimedRotatingFileHandler

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = TimedRotatingFileHandler('log/log.txt', when='D', backupCount=20) # 按天分割日志
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setFormatter(formatter)
console.setLevel(logging.INFO)

logger = logging.getLogger('main')
logger.setLevel(logging.INFO)
logger.addHandler(handler)
logger.addHandler(console)


def encode_crlf(text):
    """编码回车换行符"""
    return text.replace('\n', r'\n').replace('\r', r'\r')


def decode_crlf(text):
    """解码回车换行符"""
    return text.replace(r'\r', '\r').replace(r'\n', '\n')
