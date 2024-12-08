def limit_func_calls(call_limit):
    def decorator(func):
        call_count = 0
        def wrapper(*args):
            nonlocal call_count

            func_call = func(*args)

            if call_count >= call_limit:
                return f"Can't use decorator more than {call_limit} times"
            call_count += 1

            return func_call
        return wrapper
    return decorator

def quick_math(num1):
    return 5 + num1

decorator_ = (limit_func_calls(3)(quick_math))
print(decorator_(2))
print(decorator_(3))
print(decorator_(4))
print(decorator_(5))