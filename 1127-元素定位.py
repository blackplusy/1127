#coding=utf-8
#1.导入selenium库
from selenium import webdriver
#2.设置启动所需浏览器
br=webdriver.Chrome()
#3.打开目标网页
br.get("https://www.baidu.com")
#通过id进行定位
# br.find_element_by_id("kw").send_keys("55开")
#通过name定位
# br.find_element_by_name("wd").send_keys("美国大选")
#通过class定位
# br.find_element_by_class_name("s_ipt").send_keys("塔朗普")
#通过tag标签进行定位
# br.find_element_by_tag_name("input").send_keys("拜登")
#通过link定位
# br.find_element_by_link_text("hao123").click()
#通过partial_link
# br.find_element_by_partial_link_text("闻").click()
#通过xpath定位
# br.find_element_by_xpath("//*[@id='kw']").send_keys("巧碧螺")
#通过css定位
br.find_element_by_css_selector("#kw").send_keys("张大仙")
