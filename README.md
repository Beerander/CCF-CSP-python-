# CCF-CSP-python 能带进考场的东西

正则根据条件换字符串模板：

```python
def match(matched):
    var = matched.group('var')
    if var in var_dict:
        return var_dict[var]
    else:
        return ''
for string in string_list:
    string = re.sub('{{ (?P<var>\w*) }}', match, string)
    print(string)
```

