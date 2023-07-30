import time
import functools
from Jay_Tool.LogTool import myLogger


def clockTester(func, printRes=False, printArgs=False):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if printArgs is True:
            if args:
                arg_lst.append(', '.join(repr(arg) for arg in args))
            if kwargs:
                pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
                arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)

        if printRes is False:
            if myLogger.consoleLogger is None:
                print('[%0.8fs] %s(%s)' % (elapsed, name, arg_str))
            else:
                myLogger.myLogger_Logger().info('[%0.8fs] %s(%s)' % (elapsed, name, arg_str))
        else:
            if myLogger.consoleLogger is None:
                print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
            else:
                myLogger.myLogger_Logger().info('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))

        return result

    return clocked
