import string

f = string.Formatter()
morning = "Good morning"

# 最基础用法
print(f.format("{greet}, {name}", name="Ranshi", greet=morning))

# 一般用法
print("{greet}, {name}".format(name="Ranshi", greet=morning))

# python3.6之后引入的 f-string用法
print(f"{morning}, {'Ranshi'}")
