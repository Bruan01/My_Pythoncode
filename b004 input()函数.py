import time

print('亲爱的同学：')
time.sleep(1)

print('我们愉快地通知您，您已获准在霍格沃茨魔法学校就读。')
time.sleep(2)

print('随信附上所需书籍及装备一览。')
time.sleep(1)

print('学期定于九月一日开始。')
time.sleep(1)

print('鉴于您对魔法世界的不熟悉，')
time.sleep(1)

print('我们将指派魔咒学老师——吴枫教授带您购买学习用品。')
time.sleep(2)

print('我们将于七月三十一日前静候您的猫头鹰带来的回信。')
time.sleep(2)

print('校长（女）米勒娃·麦格谨上')
time.sleep(1)

print('那么，您的选择是什么？ 1 接受，还是 2 放弃呢？')
time.sleep(2)

choice=input('请输入您选择的数字：')

if choice =='1':
    print('霍格沃茨欢迎您的到来。')

else:
    print('您可是被梅林选中的孩子，我们不接受这个选项。')
#================================================

name=input('请在以下四个选项【格兰芬多；斯莱特林；拉文克劳；赫奇帕奇】中，输入你想去的学院名字:')
print(name)
#input（）默认字符串
name = input('请在以下四个选项【格兰芬多；斯莱特林；拉文克劳；赫奇帕奇】中，输入你想去的学院名字: ')
print(name +'学院欢迎你，小萌新!')

#==================================================
choice = input('请输入您的选择：')
#变量赋值

if choice == 1:#错了这里 应该是 choice == '1'
#条件判断:条件1
    print('霍格沃茨欢迎您的到来。')
#条件1的结果

else:
#条件判断：其他条件
    print('您可是被梅林选中的孩子，我们不接受这个选项。')
#其他条件的结果

#==================================================

choice = input('请输入1或2:')
print(type(choice))#注意都是字符串的形式！！！！！！！

#===============================================

choice = int(input('请输入您的选择：'))
if choice==1:
    print('霍格沃茨欢迎您的到来.')
else :
    print('您可是被梅林选中的孩子，我们不接受这个选项.')
#============================================
money = int(input('你一个月工资多少钱？'))
#将输入的工资数（字符串），强制转换为整数

if money >= 10000:
#当工资数（整数）大于等于10000（整数）时
    print('土豪我们做朋友吧！')
#打印if条件下的结果
elif 5000<money<10000:
    print('我们都是搬砖族。。。')
else:
#当工资数（整数）小于10000（整数）时
    print('我负责赚钱养家，你负责貌美如花～')
#打印else条件下
#==============================================
