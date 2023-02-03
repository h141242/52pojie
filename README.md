# 吾爱破解每日签到

青龙面板--环境变量--新建

Pojie52_COOKIE 填入吾爱破解COOKIES

# 注意:cookie中不要包含wzws_sid=xxxxx字段，该字段是实时更新的，脚本内自动获取

# 一般cookie只要htVC_2132_saltkey="xxxxxx";htVC_2132_auth="xxxxxxxxxxxx";两个字段就行了

# 第二步
将获取到的cookie填写进脚本的cookie = ""的引号里； 本地运行，青龙运行均可（需要requests和bs4依赖）
