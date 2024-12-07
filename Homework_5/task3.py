def checking_types(func):
    def wrapper(*args):
        calling = func(*args)

        types_to_check = [str, list, tuple]
        for arg in args:
            for func_check in types_to_check:
                if isinstance(arg, func_check):
                    print(f"{arg} => Mentioned type")
                    break
            else:
                print(f"{arg} => Unknown type")

        return calling
    return wrapper

def types_check(*args):
    return "\n"

print(checking_types(types_check)("args", {1:0}, (1, 2), 5, [2, 5]))