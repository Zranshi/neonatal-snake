# string

string 库是一个 Python 标准库, 主要包含[字符常量](#字符常量)和 [Formatter](#formatter), 这里我们主要了解 Formatter.

## 字符常量

不过多解释啦, 都是某一类字符组成的字符串.

```py
import string

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

```

## Formatter
