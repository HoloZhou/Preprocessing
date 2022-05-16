# -*- coding: utf-8 -*-
"""
Created on Mon May 16 08:56:44 2022

@author: Zhou N
"""

import pandas as pd
import numpy as np

from collections import defaultdict
import streamlit as st
col1, col2= st.columns([2,1])

import time
import pip
pip.main(["install", "openpyxl"])
pip.main(["install", "xpinyin"])
from xpinyin import Pinyin
p=Pinyin()

from PIL import Image
image_1 = Image.open('image_1.png')

#初始化表格
output=pd.DataFrame(columns=['药物','分类','药味','药性','归经','翻译','拼音'])


#药味的一键多值字典
wei=pd.read_excel('药味.xlsx')
yao1=wei['药物']
yaowei=wei['药味']
dic_yaowei=defaultdict(list)
for key,value in zip(yao1,yaowei):
    dic_yaowei[key].append(value)

#药性的一键多值字典
xing=pd.read_excel('药性.xlsx')
yao2=xing['药物']
yaoxing=xing['药性']
dic_yaoxing=defaultdict(list)
for key,value in zip(yao2,yaoxing):
    dic_yaoxing[key].append(value)

#归经的一键多值字典
jing = pd.read_excel('归经.xlsx')
yao3 = jing['药物']
guijing = jing['归经']
dic_guijing=defaultdict(list)
for key,value in zip(yao3,guijing):
    dic_guijing[key].append(value)


#药物翻译对照字典
fanyi=pd.read_excel('药物翻译.xlsx')
dic_fanyi = fanyi.set_index('药物')['翻译'].to_dict()

#药物分类集合
fsfhy = {'麻黄', '桂枝', '紫苏', '生姜', '香薷', '荆芥', '防风',
         '羌活', '白芷', '细辛', '藁本', '苍耳子', '辛夷', '葱白', '鹅不食草', '胡荽', '柽柳'}
fsfry = {'薄荷', '牛蒡子', '蝉蜕', '桑叶', '菊花', '蔓荆子', '柴胡',
         '升麻', '葛根', '淡豆豉', '浮萍', '木贼', }
Qrxhy = {'石膏', '寒水石', '知母', '芦根', '天花粉', '竹叶', '淡竹叶',
         '鸭跖草', '栀子', '夏枯草', '决明子', '谷精草', '密蒙花', '青葙子'}
Qrzsy = {'黄芩', '黄连', '黄柏', '龙胆', '秦皮', '苦参', '白鲜皮', '苦豆子', '三棵针', '马尾连'}
Qrjdy = {'金银花', '连翘', '穿心莲', '大青叶', '板蓝根', '青黛', '贯众', '蒲公英', '紫花地丁', '野菊花', '重楼', '拳参', '漏芦', '土茯苓', '鱼腥草', '金荞麦', '红藤', '败酱草', '射干',
         '山豆根', '马勃', '青果', '锦灯笼', '金果榄', '木蝴蝶', '白头翁', '马齿苋', '鸦胆子', '地锦草', '委陵菜', '翻白草', '半边莲', '白花蛇舌草', '山慈菇', '熊胆', '千里光', '白蔹', '四季青', '绿豆'}
Qrlxy = {'生地黄', '玄参', '牡丹皮', '赤芍', '紫草', '水牛角'}
Qxry = {'青蒿', '白薇', '地骨皮', '银柴胡', '胡黄连'}
Gxy = {'大黄', '芒硝', '番泻叶', '芦荟'}
Rxy = {'火麻仁', '郁李仁', '松子仁'}
Jxzsy = {'甘遂', '京大戟', '芫花', '商陆', '牵牛子', '巴豆', '千金子'}
Quhsy = {'独活', '威灵仙', '川乌', '蕲蛇', '乌梢蛇', '木瓜', '蚕沙', '伸筋草',
         '寻骨风', '松节', '海风藤', '青风藤', '丁公藤', '昆明山海棠', '雪上一枝蒿', '路路通'}
Qfsry = {'秦艽', '防己', '桑枝', '豨莶草', '臭梧桐', '海桐皮',
         '络石藤', '雷公藤', '老鹳草', '穿山龙', '丝瓜络'}
Qfsqjg = {'五加皮', '桑寄生', '狗脊', '千年健', '雪莲花', '鹿衔草', '石楠叶'}
Hsy = {'藿香', '佩兰', '苍术', '厚朴', '砂仁', '豆蔻', '草豆蔻', '草果'}
Lsxzy = {'茯苓', '茯神', '薏苡仁', '猪苓', '泽泻', '冬瓜皮', '冬瓜子',
         '玉米须', '葫芦', '香加皮', '枳椇子', '泽漆', '蝼蛄', '荠菜'}
Lntly = {'车前子', '车前草', '滑石', '木通', '通草', '瞿麦',
         '萹蓄', '地肤子', '海金沙', '石韦', '冬葵子', '灯心草', '萆薢'}
Lsthy = {'茵陈', '金钱草', '虎杖', '地耳草', '垂盆草', '鸡骨草', '珍珠草'}
Wly = {'附子', '干姜', '肉桂', '吴茱萸', '小茴香', '丁香', '高良姜', '胡椒', '花椒', '荜茇', '荜澄茄'}
Lqy = {'陈皮', '橘核', '橘络', '橘叶', '化橘红', '青皮', '枳实', '枳壳', '木香', '沉香', '檀香', '川楝子', '乌药', '青木香',
       '荔枝核', '香附', '佛手', '香橼', '玫瑰花', '绿萼梅', '娑罗子', '薤白', '天仙藤', '大腹皮', '甘松', '九香虫', '刀豆', '柿蒂'}
Xsy = {'山楂', '神曲', '麦芽', '稻芽', '谷芽', '莱菔子', '鸡内金', '鸡矢藤', '隔山消', '阿魏'}
Qcy = {'使君子', '苦楝皮', '槟榔', '南瓜子', '鹤草芽', '雷丸', '鹤虱', '榧子', '芜荑'}
Lxzxy = {'小蓟', '大蓟', '地榆', '槐花', '槐角', '侧柏叶', '白茅根', '苎麻根', '羊蹄'}
Hyzxy = {'三七', '茜草', '蒲黄', '花蕊石', '降香'}
Slzxy = {'白及', '仙鹤草', '紫珠', '棕榈炭', '血余炭', '藕节', '檵木', '第四节'}
Wjzxy = {'艾叶', '炮姜', '灶心土'}
Hxzty = {'川芎', '延胡索', '郁金', '姜黄', '乳香', '没药', '五灵脂', '夏天无', '枫香脂'}
Hxtjy = {'丹参', '红花', '桃仁', '益母草', '泽兰', '牛膝', '鸡血藤', '王不留行', '月季花', '凌霄花'}
Hxlsy = {'土鳖虫', '马钱子', '自然铜', '苏木', '骨碎补', '血竭', '儿茶', '刘寄奴'}
Pxxzy = {'莪术', '三棱', '水蛭', '虻虫', '斑蝥', '穿山甲'}
Whhty = {'半夏', '天南星', '胆南星', '白附子', '白芥子', '皂荚', '皂角刺', '旋覆花', '白前', '猫爪草'}
Qhrty = {'川贝母', '浙贝母', '瓜蒌', '竹茹', '竹沥', '天竺黄', '前胡', '桔梗',
         '胖大海', '海藻', '昆布', '黄药子', '海蛤壳', '海浮石', '瓦楞子', '礞石'}
Zkpcy = {'苦杏仁', '紫苏子', '百部', '紫菀', '款冬花', '马兜铃', '枇杷叶', '桑白皮',
         '葶苈子', '白果', '矮地茶', '洋金花', '华山参', '罗汉果', '满山红', '胡颓子叶'}

Zzasy = {'朱砂', '磁石', '龙骨', '琥珀'}
Yxasy = {'酸枣仁', '柏子仁', '灵芝', '缬草', '首乌藤', '合欢皮', '远志'}
Pygyy = {'石决明', '珍珠母', '牡蛎', '紫贝齿', '代赭石', '刺蒺藜', '罗布麻', '生铁落'}
Xfzjy = {'羚羊角', '牛黄', '珍珠', '钩藤', '天麻', '地龙', '全蝎', '蜈蚣', '僵蚕'}
Kqy = {'麝香', '冰片', '苏合香', '石菖蒲'}
Bqy = {'人参', '西洋参', '党参', '太子参', '黄芪', '白术', '白扁豆', '甘草',
       '大枣', '刺五加', '绞股蓝', '红景天', '沙棘', '饴糖', '蜂蜜', '山药'}
Byy = {'鹿茸', '鹿角', '鹿角胶', '鹿角霜', '紫河车', '淫羊藿', '巴戟天', '仙茅', '杜仲', '续断', '肉苁蓉', '锁阳', '韭菜子', '补骨脂',
       '益智仁', '菟丝子', '沙苑子', '蛤蚧', '核桃仁', '冬虫夏草', '胡芦巴', '阳起石', '紫石英', '海狗肾', '海马', '哈蟆油', '羊红膻'}
Bxy = {'当归', '熟地黄', '白芍', '阿胶', '何首乌', '龙眼肉', '楮实子'}
Byiny = {'南沙参', '北沙参', '百合', '麦冬', '天冬', '石斛', '玉竹', '黄精',
         '明党参', '枸杞子', '墨旱莲', '女贞子', '桑椹', '黑芝麻', '龟甲', '鳖甲'}
Gbzhy = {'麻黄根', '浮小麦', '糯稻根须'}
Lfscy = {'五味子', '乌梅', '五倍子', '罂粟壳', '诃子', '石榴皮', '肉豆蔻', '赤石脂', '禹余粮'}
Gjsnzdy = {'山茱萸', '覆盆子', '莲子', '莲须', '莲房', '莲子心', '荷叶', '荷梗',
           '芡实', '刺猬皮', '椿皮', '鸡冠花', '海螵蛸', '金樱子', '桑螵蛸'}
Yty = {'常山', '瓜蒂', '胆矾'}
Gdsczyy = {'雄黄', '硫黄', '白矾', '蛇床子', '蟾酥', '樟脑', '木鳖子', '土荆皮', '蜂房', '大蒜'}
Bdhfsjy = {'升药', '轻粉', '砒石', '铅丹', '炉甘石', '硼砂'}

with col1:
    st.subheader('文件上传区')
    file = st.file_uploader("点击\"Browse file\"浏览并上传文件", type=["xls", "xlsx"], accept_multiple_files=False)   
    
with st.sidebar: 
    st.subheader('请严格以下要求提供原始数据')    
    st.text('1.所有药物排成一列')
    st.text('2.首行从药物开始，不要有列名\n（输出结果中会自动加列名）')
    st.text('3.只支持xls或xlsx文件')
    st.text('4.参考下图格式\n（表格底色可忽略）')
    st.image(image_1)
    
    
#file= pd.read_excel('C:\\Users\\Zhou N\\Desktop\\try.xlsx')  
    
if file is not None:
    file=pd.read_excel(file)
    file=pd.DataFrame(file)
    for index,row in file.iterrows():
        for i in row:
            i=[i]
            i=pd.DataFrame(i, columns=['药物'])
            output=pd.concat([output, i], axis=0,
              ignore_index=True, join="outer")
        for i in row:  
            if (i in dic_fanyi)==True:
                val=dic_fanyi.get(i,'无此药')            
                val=[val]
                val=pd.DataFrame(val, columns=['翻译'])
                output=pd.concat([output, val], axis=0,
                       ignore_index=True, join="outer")
            
                pin=p.get_pinyin(i)
                pin='('+pin+')'
                pin=[pin]
                pin=pd.DataFrame(pin, columns=['拼音'])
                output=pd.concat([output, pin], axis=0,
                       ignore_index=True, join="outer")
            else:
                val='无此翻译'
                val=[val]
                val=pd.DataFrame(val, columns=['翻译'])
                output=pd.concat([output, val], axis=0,
                       ignore_index=True, join="outer")
                
                pin=p.get_pinyin(i)
                pin='('+pin+')'
                pin=[pin]
                pin=pd.DataFrame(pin, columns=['拼音'])
                output=pd.concat([output, pin], axis=0,
                       ignore_index=True, join="outer")
                       
        for i in row:
            if (i in dic_yaoxing)==True:
                xing=dic_yaoxing.get(i,'无此药')  
                for x in xing:
                    x=[x]
                    x=pd.DataFrame(x, columns=['药性'])
                    output=pd.concat([output, x], axis=0,
                      ignore_index=True, join="outer")
            
            if (i in dic_yaowei)==True:
                wei=dic_yaowei.get(i,'无此药')  
                for w in wei:
                    w=[w]
                    w=pd.DataFrame(w, columns=['药味'])
                    output=pd.concat([output, w], axis=0,
                      ignore_index=True, join="outer")
        for i in row:
            if (i in dic_guijing)==True:
                jing=dic_guijing.get(i,'无此药')  
                for j in jing:
                    j=[j]
                    j=pd.DataFrame(j, columns=['归经'])
                    output=pd.concat([output, j], axis=0,
                      ignore_index=True, join="outer")
                
        
        
        
        for i in row:
               
            #发散风寒药
            if (i in fsfhy)==True:                    
                ca='发散风寒药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])  
                output=pd.concat([output,cate],axis=0,
                   ignore_index=True, join="outer")
            #发散风热药
            elif (i in fsfry) == True:                   
                ca='发散风热药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #清热泻火药  
            elif (i in Qrxhy) == True:                  
                ca='清热泻火药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #清热燥湿药
            elif (i in Qrzsy) == True:                
                ca='清热燥湿药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #清热解毒药
            elif (i in Qrjdy) == True:     
                ca='清热解毒药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #清热凉血药
            elif (i in Qrlxy) == True:     
                ca='清热凉血药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #清虚热药
            elif (i in Qxry) == True:                   
                ca='清虚热药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #攻下药
            elif (i in Gxy) == True:     
                ca='攻下药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")   
            #润下药
            elif (i in Rxy) == True:     
                ca='润下药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")   
            #峻下逐水药
            elif (i in Jxzsy) == True:     
                ca='峻下逐水药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")   
            
            #祛风寒湿药
            elif (i in Quhsy) == True:     
                ca='祛风寒湿药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #祛风湿热药
            elif (i in Qfsry) == True:     
                ca='祛风湿热药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #祛风湿强筋骨药
            elif (i in Qfsqjg) == True:     
                ca='祛风湿强筋骨药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer") 
            #化湿药
            elif (i in Hsy) == True:     
                ca='化湿药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")   
            #利水消肿药
            elif (i in Lsxzy) == True:     
                ca='利水消肿药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer") 
            #利尿通淋药
            elif (i in Lntly) == True:     
                ca='利尿通淋药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #利湿退黄药
            elif (i in Lsthy) == True:     
                ca='利湿退黄药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #温里药
            elif (i in Wly) == True:     
                ca='温里药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #理气药
            elif (i in Lqy) == True:     
                ca='理气药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #消食药
            elif (i in Xsy) == True:     
                ca='消食药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #驱虫药
            elif (i in Qcy) == True:     
                ca='驱虫药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #凉血止血药
            elif (i in Lxzxy) == True:     
                ca='凉血止血药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #化瘀止血药
            elif (i in Hyzxy) == True:     
                ca='化瘀止血药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #收敛止血药
            elif (i in Slzxy) == True:     
                ca='收敛止血药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #温经止血药
            elif (i in Wjzxy) == True:     
                ca='温经止血药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #活血止痛药
            elif (i in Hxzty)==True:  
                ca='活血止痛药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                               ignore_index=True, join="outer")
            #活血调经药
            elif (i in Hxtjy) == True:     
                ca='活血调经药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #活血疗伤药
            elif (i in Hxlsy) == True:     
                ca='活血疗伤药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #破血消癥药
            elif (i in Pxxzy) == True:     
                ca='破血消癥药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #温化寒痰药
            elif (i in Whhty) == True:     
                ca='温化寒痰药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #清化热痰药
            elif (i in Qhrty) == True:     
                ca='清化热痰药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #止咳平喘药
            elif (i in Zkpcy) == True:     
                ca='止咳平喘药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #镇静安神药
            elif (i in Zzasy) == True:     
                ca='镇静安神药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #养心安神药
            elif (i in Yxasy) == True:     
                ca='养心安神药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #平抑肝阳药
            elif (i in Pygyy) == True:     
                ca='平抑肝阳药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #息风止痉药
            elif (i in Xfzjy) == True:     
                ca='息风止痉药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #开窍药
            elif (i in Kqy) == True:     
                ca='开窍药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #补气药
            elif (i in Bqy) == True:     
                ca='补气药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #补阳药
            elif (i in Byy) == True:     
                ca='补阳药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #补血药
            elif (i in Bxy) == True:     
                ca='补血药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #补阴药
            elif (i in Byiny) == True:     
                ca='补阴药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #固表止汗药
            elif (i in Gbzhy) == True:     
                ca='固表止汗药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #敛肺涩肠药
            elif (i in Lfscy) == True:     
                ca='敛肺涩肠药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #固精缩尿止带药
            elif (i in Gjsnzdy) == True:     
                ca='固精缩尿止带药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #涌吐药
            elif (i in Yty) == True:     
                ca='涌吐药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #攻毒杀虫止痒药
            elif (i in Gdsczyy) == True:     
                ca='攻毒杀虫止痒药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            #拔毒化腐生肌药
            elif (i in Bdhfsjy) == True:     
                ca='拔毒化腐生肌药'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            else:
                ca='无此药分类信息'
                ca=[ca]
                cate=pd.DataFrame(ca,columns=['分类'])
                output=pd.concat([output,cate],axis=0,
                                 ignore_index=True, join="outer")
            
        
        
#药物名称占用自身所有属性的行    
output['药物']=output['药物'].fillna(method='ffill')

#提取药物列
output_dr=output['药物']
output_dr=list(output_dr)
output_dr=pd.DataFrame(output_dr,columns=['药物'],index=output['药物'])
output_dr=output_dr.drop_duplicates()

#药味pivot
output_wei=output['药味']
output_wei=list(output_wei)
output_wei=pd.DataFrame(output_wei,columns=['药味'],index=output['药物'])
output_wei.dropna(axis=0, inplace=True, how="any") 
output_wei['COUNT']=1
output_wei=output_wei.pivot_table('COUNT', index=['药物'], columns=['药味']).fillna(0)

#药性pivot
output_xing=output['药性']
output_xing=list(output_xing)
output_xing=pd.DataFrame(output_xing,columns=['药性'],index=output['药物'])
output_xing.dropna(axis=0, inplace=True, how="any") 
output_xing['COUNT']=1
output_xing=output_xing.pivot_table('COUNT', index=['药物'], columns=['药性']).fillna(0)

#归经pivot
output_jing=output['归经']
output_jing=list(output_jing)
output_jing=pd.DataFrame(output_jing,columns=['归经'],index=output['药物'])
output_jing.dropna(axis=0, inplace=True, how="any") 
output_jing['COUNT']=1
output_jing=output_jing.pivot_table('COUNT', index=['药物'], columns=['归经']).fillna(0)

#分类columns
output_cate=output['分类']
output_cate=list(output_cate)
output_cate=pd.DataFrame(output_cate,columns=['分类'],index=output['药物'])
output_cate.dropna(axis=0, inplace=True, how="any") 

#翻译与拼音columns
output_t=output['翻译']
output_p=output['拼音']
output_t=list(output_t)
output_p=list(output_p)
output_t=pd.DataFrame(output_t,columns=['翻译'],index=output['药物'])
output_p=pd.DataFrame(output_p,columns=['拼音'],index=output['药物'])
output_t.dropna(axis=0, inplace=True, how="any") 
output_p.dropna(axis=0, inplace=True, how="any") 
output_tnp =output_t["翻译"].map(str) + output_p["拼音"].map(str) 


#合并所有元素
out_final=pd.concat([output_dr,output_wei,output_xing,output_jing,output_cate,output_t,output_p,output_tnp],axis=1,
                 ignore_index=False, join="outer")

out_final.rename(columns={0:'翻译与拼音'},inplace=True)
out_final=out_final.drop(['药物'],axis=1)





with col2:
    st.subheader('结果预览区')
    st.dataframe(out_final, 1000, 1000)

def convert_df(out_final):
    return out_final.to_csv().encode('utf-8')
with col1:   
    
    
    st.subheader('处理进度监视')   
    my_bar = st.progress(0)
    for percent_complete in range(100):       
        my_bar.progress(percent_complete + 1)
    with st.spinner('Wait for it...'):
        st.success('已完成')     
        st.balloons()
        
        
        
    st.subheader('文件下载区')             
    if out_final is not None:
        excel = convert_df(out_final)
        st.download_button(label="点击此处下载已完成数据",data=excel,
                           file_name='已处理完成的数据.csv',mime='csv')
        st.text("注：转换完成的数据是CSV格式")  
