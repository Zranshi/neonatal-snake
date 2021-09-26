# collections

collections 库实现了许多 Python 特定的容器.

大部分可以用标准内建容器 dict、list、set 和 tuple 替代, 但额外实现的功能可以方便我们使用.

### namedtuple

namedtuple 可以给元组中的每个位置添加一个名称, 这样就可以提高 Python 代码的可读性. 可以作用于任何普通元组, 因此不仅可以通过名称访问, 也可以通过索引访问.

在使用 namedtuple 时, 应该先定义一个 namedtuple 对象的结构. 然后就可以根据结构创建新的元组.

```py
Point = namedtuple("Point", ["x", "y"])

p = Point(11, y=22)

print(Point)
print(p)
print(p[0], p[1])
print(p.x, p.y)

# output:
# <class '__main__.Point'>
# Point(x=11, y=22)
# 11 22
# 11 22
```

由此可以见, namedtuple 实际上就是创建了一个名叫 Point 的类. 并实现了一些基础方法.

一般而言, 在读取 csv 或者 sqlite3 数据时, 可以方便地使用 namedtuple 接收.

例如我们有 `example.csv` 这样一个 csv 文件, 其中的列标签为 `Manufacturer,Rating,Speed`, 因此我们可以使用 namedtuple 来更好地接收.

```py
import csv

ManufacturerInfo = namedtuple("ManufacturerInfo", "Manufacturer, Rating, Speed")

for manu in map(
    ManufacturerInfo._make,
    csv.reader(open("src/data_type/collections/example.csv", "r")),
):
    print(manu.Manufacturer, manu.Rating, manu.Speed)

# output:
# Manufacturer Rating Speed
# Bosch 10 2500
# Siemens 10 3500
# Plessey 15 2500
```

### deque´

deque 是一个双向队列. 和 list 类似, 可以进行 pop 和 append 操作, 但不同的是, 它支持高效的头尾 pop 和 append 操作, 并且它是线程安全的.

```py
dq = deque([1, 2, 3])
print(dq)
dq.appendleft(5)
dq.appendleft(8)
dq.pop()
print(dq)

# output:
# deque([1, 2, 3])
# deque([8, 5, 1, 2])
```

deque 的内部实现是一个双向链表, 因此能够实现前后加减元素的时间复杂度为常数. 而索引访问就不是 deque 的强项了.
