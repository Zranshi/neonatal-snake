# string

string 库是一个 Python 标准库, 主要包含[字符常量](#字符常量)和 [Formatter](#formatter), 这里我们主要了解 Formatter.

## 字符常量

不过多解释啦, 都是某一类字符组成的字符串.

```py
# 小写字母组成的字符串
print(f"All lowercase letters characters: {list(string.ascii_lowercase)}")

# 大写字母组成的字符串
print(f"All uppercase letters characters: {list(string.ascii_uppercase)}")

# 英文字母组成的字符串 ascii_letters = ascii_lowercase + ascii_uppercase
print(f"All letters characters: {list(string.ascii_letters)}")

# 十进制数字
print(f"All digits number characters: {list(string.digits)}")

# 十六进制数字
print(f"All hexdigits number characters: {list(string.hexdigits)}")

# 八进制数字
print(f"All octdigits number characters: {list(string.octdigits)}")

# 标点符号
print(f"All punctuation characters: {list(string.punctuation)}")

# 空白符号
print(f"All whitespace characters: {list(string.whitespace)}")

# 所有可打印的字符 printable = digits + ascii_letters + punctuation + whitespace
print(list(string.printable))

# All lowercase letters characters: abcdefghijklmnopqrstuvwxyz
# All uppercase letters characters: ABCDEFGHIJKLMNOPQRSTUVWXYZ
# All letters characters: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# All digits number characters: 0123456789
# All hexdigits number characters: 0123456789abcdefABCDEF
# All octdigits number characters: 01234567
# All punctuation characters: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# All whitespace characters: [' ', '\t', '\n', '\r', '\x0b', '\x0c']
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ', '\t', '\n', '\r', '\x0b', '\x0c']
```

[ 因为空白字符的打印在命令行不便查看, 使用列表将其变为字符形式 ]

## Formatter

### 基础使用

Formatter 是 string.py 包中定义的一个类, 其中定义了一个用于格式化字符串的方法: format(这是我们主要适用的 API), 这是一个简单的例子:

```py
f = string.Formatter()
morning = "Good morning"

print(f.format("{greet}, {name}", name="Ranshi", greet=morning))

# output:
# Good morning, Ranshi
```

根据输出结果可以看出, 两个字符串被拼接起来了. 但是这种形式看起来并不是非常优雅, 因为我们还需要定义一个 string.Formatter 的对象, 然后才调用 format 方法. 其实, Python 针对 str 对象就实现了 format 方法, 我们可以直接调用一个 str 对象的 format 方法.

```py
morning = "Good morning"

print("{greet}, {name}".format(name="Ranshi", greet=morning))

# output:
# Good morning, Ranshi
```

而在 python3.6 之后, 引入了 f-string 写法, 进一步地简化了格式化字符串的使用.

```py
morning = "Good morning"

print(f"{morning}, {'Ranshi'}")

# output:
# Good morning, Ranshi
```

相比起来是不是非常简单, 那我们以后就都用这种形式来书写格式化字符串.

### 进阶
