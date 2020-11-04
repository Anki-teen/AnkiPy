import re

str = "183-125-44364"

print(re.match('小白', '程序员的小白学习笔记')) 
print(re.match('学习笔记', '小白程序员的学习笔记'))

print(re.fullmatch('学习笔记', '小白程序员的学习笔记'))

print(re.search('学习笔记', '小白程序员的学习笔记'))

print(re.sub("-","",str))
print(re.subn("-","",str))

print(re.split('a*', 'hello world'))

