# coding=utf-8
import os
import time
import json
import codecs
import shutil

test_log_name = '\\test_log.txt'
log_format_dir = '..\\result\\%s\\log'
image_format_dir = '..\\result\\%s\\image'


def get_format_time():
    """
    返回当前系统时间以括号中（2014-08-29-15_21_55）展示
    """
    return time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))


def save_png_name(name):
    """
    name：自定义图片的名称
    """
    day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    image_dir = image_format_dir % day
    format_time = get_format_time()
    image_type = '.png'
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    file_name = image_dir + '\\' + format_time + '_' + name + image_type
    print file_name
    return file_name


def save_log(message):
    """
    保存日志
    :param message:日志内容
    """
    day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    fp = log_format_dir % day
    if not os.path.exists(fp):
        os.makedirs(fp)

    if not message.partition('setUp') and not message.partition('tearDown'):
        message = '[' + get_format_time() + '] ' + message
    with codecs.open(fp + test_log_name, 'ab', encoding='utf-8') as log_file:
        log_file.writelines(message)


def del_current_day_log():
    day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    fp = (log_format_dir + test_log_name) % day
    if os.path.exists(fp):
        os.remove(fp)


def del_current_day_image():
    day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    fp = image_format_dir % day
    if os.path.exists(fp):
        # os.removedirs(path)用于删除空文件夹
        # 删除所有非空文件夹，此处不能用os.removedirs(path)
        shutil.rmtree(fp)


def get_account():
    """
    获取账号密码
    :return json格式:
    """
    with open('..\\cases\\data\\account.json', 'r') as json_file:
        account = json.load(json_file)
        valid_account = account['valid_count']
        valid_phone_account = valid_account['account']
        valid_phone_password = valid_account['password']
        print(valid_phone_account + ' ' + valid_phone_password)

    return account


def save_password(password):
    """
    保存密码
    :param password:
    """
    with open('..\\cases\\data\\account.json', 'r') as json_file:
        account = json.load(json_file)
        print(account)

    with open('..\\cases\\data\\account.json', 'w+') as json_file:
        valid_account = account[u'valid_count']
        valid_account[u'password'] = password
        json_file.write(json.dumps(account, indent=4))



