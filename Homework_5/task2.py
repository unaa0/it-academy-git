import time

def func_timer_outer(secs_or_mins):
    def func_timer(func):
        def wrapper(*args, **kwargs):
            print(f"starting timer and calling {func.__name__}")

            start_timer = time.time()
            start_func = func(*args, **kwargs)

            finish_timer = time.time()

            result_time = finish_timer - start_timer
            if not secs_or_mins:
                result_time = result_time / 60
                result_time = round(result_time, 2)
                print(f"ending timer with {result_time} minutes elapsed")
            else:
                result_time = round(result_time, 2)
                print(f"ending timer with {result_time} seconds elapsed")

            return start_func
        return wrapper
    return func_timer

def rand_func(num):

    for i in range(num):
        i = num * 2
        time.sleep(3)

    return f"rand_func was completed \n"

print(func_timer_outer(secs_or_mins=True)(rand_func)(2))
print(func_timer_outer(secs_or_mins=False)(rand_func)(20))
# print(func_timer_outer(secs_or_mins=False)(rand_func)(30))