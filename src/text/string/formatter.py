import datetime
import string

f = string.Formatter()
morning = "Good morning"

# 最基础用法
print(f.format("{greet}, {name}", name="Ranshi", greet=morning))

# 一般用法
print("{greet}, {name}".format(name="Ranshi", greet=morning))

# python3.6之后引入的 f-string用法
print(f"{morning}, {'Ranshi'}")

# 进阶用法

# 列表定位
print("{0}, {1}, {2}".format("a", "b", "c"))

print("{}, {}, {}".format("a", "b", "c"))

print("{0}, {0}, {1}".format("a", "b"))

print("{1}, {0}, {2}".format("a", "b", "c"))

# 字典定位

print("{greet}, {name}".format(greet="goodbye", name="Ranshi"))

# 解包

lst = ["a", "b", "c"]
print("{1}, {0}, {2}".format(*lst))

d = {"greet": "goodbye", "name": "Ranshi"}
print("{greet}, {name}".format(**d))

# 转换符

greet = "你好,\tRanshi"

print(f"{greet}")
print(f"{greet!s}")
print(f"{greet!r}")
print(f"{greet!a}")

# `=`

result = 15 * 32

print(f"{result=}!")
print(f"{  result=}!")
print(f"{result  =}!")

# align

x = 158

print(f"#{x:~<10}#")
print(f"#{x:~<+10}#")
print(f"#{x:~< 10}#")
print(f"#{-x:~<+10}#")
print(f"#{x:~^10}#")
print(f"#{x:~>10}#")


# base

num = 105
print(f"{num:b}")
print(f"{num:c}")
print(f"{num:d}")
print(f"{num:o}")
print(f"{num:x}")
print(f"{num:n}")

# else

num = 1316513216513216513
print(f"{num:,}")

d = datetime.datetime.now()
print(f"{d:%Y-%m-%d %H:%M:%S}")

per = 0.35
print(f"{per:%}")
