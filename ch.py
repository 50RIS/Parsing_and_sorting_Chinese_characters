#!/usr/bin/python3.5
# coding: utf-8

# 大家好！
# by Boris Zubov (鲍里斯) contact@technodrive.ru

# UPD: To get the Chinese characters sorted, -- not only parsed -- run two scripts in pipe:
# ./ch.py | sort_Chinese_characters.sh

# The characters are kept in the unicode string below for a now:

# Let's parse the string of Chinese characters and get the single ones, separated with '/n'

import tensorflow as tf

def preprocess_func(x):
	ret= "\n".join(x.decode('utf-8'))
	return ret

str = tf.py_func(
	preprocess_func,
	[tf.constant(u"一七万丈三上下不东两个中为久么乐九也习书买了二五些交京亮人什今从他以们件休会伦位体作你便俄信假做健儿元八公六共关兴再冒写冰准几出刀分别到刻前办加务动助勺包北医十千午半华单卡印厕去叉友发只叫可台右号吃名后吗吧听告员呢周和咖哥哪唱商啡啤喂喜喝四回因国在地坐块外多大天太夫头女奶她好妈妹妻始姐姓子字学孩它安定宜客室家对小少岁工左差市师帮常年床应店度康开弟张往很得德心忙快怎思息您想意感慢懂戏我房所手打找抱拍拿攵收放敦整文料斯新方旁旅日早时明星昨是晚最月有朋服期末本机李条来杯松果树校样桌椅次欢歉歌步每毛气水汁汉汽没注泳洗浪海港游湾漂漫点炼烧热照爱爸片牙牛狗猪猫王玩现班球瓜瓶生用电男留疼病白百的盘相看睡知矮码碗秒租空站等筷箱篮米糕糖系累约纽给罗羊美老肉肚胖脑舒舞船英苹茶药菜蔬蕉蛋行衣袋西要见觉订认识诉话该语说请读谁谢贵走起超足跑路跳踢蹈身车轻辆边过迎运近还这进道那都酒里金钟钱铁错锻门问间院随难零需非面韩音飯饭饮馆香马骑高魚鲜鸟鸡")],
	tf.string)

with tf.Session() as sess:
	value = sess.run(str)
	print(value.decode('utf-8'))


