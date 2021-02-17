import itchat
# 导入itchat库
itchat.auto_login(hotReload=True)
# 登录 开启热登录
friendList = itchat.get_friends(update=True)[1:]
# 获取好友信息 信息是列表 其元素是作者定义的数据结构
# 作者定义的数据结构类似字典 就叫类字典 能用键对值
# 键有 UserName NickName 等等 其中itchat.send()用到UserName
# itchat.send(message,ToUserName=类字典[UserName])
