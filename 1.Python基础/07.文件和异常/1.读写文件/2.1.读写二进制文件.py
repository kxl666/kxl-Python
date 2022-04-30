# 下面的代码实现了复制图片文件的功能


def main():
    try:
        with open('guido.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # <class 'bytes'>
        with open('吉多.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开.', e)
    except IOError as e:
        print('读写文件时出现错误.', e)
    print('程序执行结束.')


if __name__ == '__main__':
    main()
