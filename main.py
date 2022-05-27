# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
def is_ql() :
    a = 1
    b = 1
    a_1 = "1"
    b_1 = "1"
    a_1s = ["1"]
    b_1s = ["1"]
    f = lambda a, b: "==" if a is b else "is"
    print(f(a, b))
    print(f(a_1, b_1))
    print(f(a_1s, b_1s))

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        print("--ll--", n)
        yield n

def _not_divisible(n):
    print("==n==",n)
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        print("--N--",n)
        yield n
        print("it--",it)
        it =filter(_not_divisible(n), it)  # 构造新序列
        print("it--",it)

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # ll=[ i for i in range(20)]
    # print(list(filter(_not_divisible(5), ll)))
    for n in primes():
        if n < 20:
            print(n)
        else:
            break
    # # print_hi('PyCharm')
    # cmp_code = compile('print("single")', '', 'single')
    # exec(cmp_code)
    # eval_code = '1+2'
    # cmp_code2 = compile(eval_code, '', 'single')
    # eval(cmp_code2)
    #
    # eval_code = '1+2'
    # cmp_code2 = compile(eval_code, '', 'eval')
    # print(eval(cmp_code2))
    print(eval("1+2"))

    # exec_code = "for i in range(5):    print( i)"
    # cmp_code = compile(exec_code, '', 'exec')
    # exec(cmp_code)
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

