import requests
url="http://www.tianyancha.com/company/companyholder.html?id=22822&amp;ps=10&amp;_=1499396206098"
data= {
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer': 'http://www.tianyancha.com/company/22822',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4',
     'Cookie': 'aliyungf_tc=AQAAAGL98GWnpgMAftHidFh68eD0v58s; csrfToken=YYamfDWPutVjvO4muMM1HXQQ; TYCID=4fa5232062b311e7817ee7b56987f1b1; uccid=6c90560bb706ec067b8a5af95d7cf309; ssuid=3175448800; Qs_lvt_117460=1499390795; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzE4NDM5MDk4NyIsImlhdCI6MTQ5OTM5MDkyNCwiZXhwIjoxNTE0OTQyOTI0fQ.05DvNXNBwuSOy8pRI-i0Pfd3opmlKSsOMuGJKVmVBiOigqJVX-C4Itivw-iSFBsZcFndsPH7q8aPyv0HKdcCcg; tyc-user-info=eyJ0b2tlbiI6ImV5SmhiR2NpT2lKSVV6VXhNaUo5LmV5SnpkV0lpT2lJeE16RTRORE01TURrNE55SXNJbWxoZENJNk1UUTVPVE01TURreU5Dd2laWGh3SWpveE5URTBPVFF5T1RJMGZRLjA1RHZOWE5Cd3VTT3k4cFJJLWkwUGZkM29wbWxLU3NPTXVHSktWbVZCaU9pZ3FKVlgtQzRJdGl2dy1pU0ZCc1pjRm5kc1BIN3E4YVB5djBIS2RjQ2NnIiwic3RhdGUiOiIwIiwidm51bSI6IjAiLCJvbnVtIjoiMCIsIm1vYmlsZSI6IjEzMTg0MzkwOTg3In0=; _csrf=qlNUsSZL82j+T8hl0jqn0Q==; OA=AZ/KCjtxkR9Zdc4WngfZPZt74Uo2SlVlrWrBH7DKs7T49Rdk813r2im4bcFAQAyL; _csrf_bk=f5a03b8e609c2383d99ece3c6601a187; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1499390795; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1499394818; Qs_pv_117460=899594246339166100%2C1499053564686013700%2C1850326911606367000%2C2697579815315213000%2C3942526392433027600; _pk_id.6835.e431=85ccfb54429b591e.1499390795.1.1499394819.1499390795.; _pk_ses.6835.e431=*; mediav=%7B%22eid%22%3A%22398779%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22Yb8SKDdxC%3F9zBv*oGy%3ES%22%2C%22ctn%22%3A%22%22%7D; aliyungf_tc=AQAAAGL98GWnpgMAftHidFh68eD0v58s; csrfToken=YYamfDWPutVjvO4muMM1HXQQ; TYCID=4fa5232062b311e7817ee7b56987f1b1; uccid=6c90560bb706ec067b8a5af95d7cf309; ssuid=3175448800; Qs_lvt_117460=1499390795; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzE4NDM5MDk4NyIsImlhdCI6MTQ5OTM5MDkyNCwiZXhwIjoxNTE0OTQyOTI0fQ.05DvNXNBwuSOy8pRI-i0Pfd3opmlKSsOMuGJKVmVBiOigqJVX-C4Itivw-iSFBsZcFndsPH7q8aPyv0HKdcCcg; tyc-user-info=eyJ0b2tlbiI6ImV5SmhiR2NpT2lKSVV6VXhNaUo5LmV5SnpkV0lpT2lJeE16RTRORE01TURrNE55SXNJbWxoZENJNk1UUTVPVE01TURreU5Dd2laWGh3SWpveE5URTBPVFF5T1RJMGZRLjA1RHZOWE5Cd3VTT3k4cFJJLWkwUGZkM29wbWxLU3NPTXVHSktWbVZCaU9pZ3FKVlgtQzRJdGl2dy1pU0ZCc1pjRm5kc1BIN3E4YVB5djBIS2RjQ2NnIiwic3RhdGUiOiIwIiwidm51bSI6IjAiLCJvbnVtIjoiMCIsIm1vYmlsZSI6IjEzMTg0MzkwOTg3In0=; mediav=%7B%22eid%22%3A%22398779%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22Yb8SKDdxC%3F9zBv*oGy%3ES%22%2C%22ctn%22%3A%22%22%7D; _csrf=m4wNFjRPp5wGSlTmfJ3LDA==; OA=AZ/KCjtxkR9Zdc4WngfZPa6Bbndy2ZVSwn7URtw3QQo9LiwAoaDAdT1kWjHY37UP; _csrf_bk=ebb00e9d1adabec334ed2a09b94f4449; _pk_id.6835.e431=85ccfb54429b591e.1499390795.1.1499396206.1499390795.; _pk_ses.6835.e431=*; Qs_pv_117460=1499053564686013700%2C1850326911606367000%2C2697579815315213000%2C3942526392433027600%2C1285738707597412000; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1499390795; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1499396206',
    'Cache-Control': 'no-cache',
    

    
    'post':'Submit',
    }
cookies = {
    'aliyungf_tc':'AQAAAGL98GWnpgMAftHidFh68eD0v58s',
    'csrfToken':'YYamfDWPutVjvO4muMM1HXQQ',
    'TYCID':'4fa5232062b311e7817ee7b56987f1b1',
    'uccid':'6c90560bb706ec067b8a5af95d7cf309',
    'ssuid':'3175448800',
    'Qs_lvt_117460':'1499390795',
    'auth_token':'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzE4NDM5MDk4NyIsImlhdCI6MTQ5OTM5MDkyNCwiZXhwIjoxNTE0OTQyOTI0fQ.05DvNXNBwuSOy8pRI-i0Pfd3opmlKSsOMuGJKVmVBiOigqJVX-C4Itivw-iSFBsZcFndsPH7q8aPyv0HKdcCcg',
    'tyc-user-info':'eyJ0b2tlbiI6ImV5SmhiR2NpT2lKSVV6VXhNaUo5LmV5SnpkV0lpT2lJeE16RTRORE01TURrNE55SXNJbWxoZENJNk1UUTVPVE01TURreU5Dd2laWGh3SWpveE5URTBPVFF5T1RJMGZRLjA1RHZOWE5Cd3VTT3k4cFJJLWkwUGZkM29wbWxLU3NPTXVHSktWbVZCaU9pZ3FKVlgtQzRJdGl2dy1pU0ZCc1pjRm5kc1BIN3E4YVB5djBIS2RjQ2NnIiwic3RhdGUiOiIwIiwidm51bSI6IjAiLCJvbnVtIjoiMCIsIm1vYmlsZSI6IjEzMTg0MzkwOTg3In0=',
    'mediav':'%7B%22eid%22%3A%22398779%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22Yb8SKDdxC%3F9zBv*oGy%3ES%22%2C%22ctn%22%3A%22%22%7D',
    '_csrf':'m4wNFjRPp5wGSlTmfJ3LDA==',
    'OA':'AZ/KCjtxkR9Zdc4WngfZPa6Bbndy2ZVSwn7URtw3QQo9LiwAoaDAdT1kWjHY37UP',
    '_csrf_bk':'ebb00e9d1adabec334ed2a09b94f4449',
    '_pk_id.6835.e431':'85ccfb54429b591e.1499390795.1.1499396206.1499390795.',
    '_pk_ses.6835.e431':'*',
    'Qs_pv_117460':'1499053564686013700%2C1850326911606367000%2C2697579815315213000%2C3942526392433027600%2C1285738707597412000',
    'Hm_lvt_e92c8d65d92d534b0fc290df538b4758':'1499390795',
    'Hm_lpvt_e92c8d65d92d534b0fc290df538b4758':'1499396206',
    }
print (requests.get(url, data=data, cookies=cookies).text)

#
# GET  HTTP/1.1
# Host: www.tianyancha.com
# Accept: */*
# X-Requested-With: XMLHttpRequest
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36
# Referer: http://www.tianyancha.com/company/22822
# Accept-Encoding: gzip, deflate, sdch
# Accept-Language: en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4
# Cookie: aliyungf_tc=AQAAAGL98GWnpgMAftHidFh68eD0v58s; csrfToken=YYamfDWPutVjvO4muMM1HXQQ; TYCID=4fa5232062b311e7817ee7b56987f1b1; uccid=6c90560bb706ec067b8a5af95d7cf309; ssuid=3175448800; Qs_lvt_117460=1499390795; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzE4NDM5MDk4NyIsImlhdCI6MTQ5OTM5MDkyNCwiZXhwIjoxNTE0OTQyOTI0fQ.05DvNXNBwuSOy8pRI-i0Pfd3opmlKSsOMuGJKVmVBiOigqJVX-C4Itivw-iSFBsZcFndsPH7q8aPyv0HKdcCcg; tyc-user-info=eyJ0b2tlbiI6ImV5SmhiR2NpT2lKSVV6VXhNaUo5LmV5SnpkV0lpT2lJeE16RTRORE01TURrNE55SXNJbWxoZENJNk1UUTVPVE01TURreU5Dd2laWGh3SWpveE5URTBPVFF5T1RJMGZRLjA1RHZOWE5Cd3VTT3k4cFJJLWkwUGZkM29wbWxLU3NPTXVHSktWbVZCaU9pZ3FKVlgtQzRJdGl2dy1pU0ZCc1pjRm5kc1BIN3E4YVB5djBIS2RjQ2NnIiwic3RhdGUiOiIwIiwidm51bSI6IjAiLCJvbnVtIjoiMCIsIm1vYmlsZSI6IjEzMTg0MzkwOTg3In0=; _csrf=qlNUsSZL82j+T8hl0jqn0Q==; OA=AZ/KCjtxkR9Zdc4WngfZPZt74Uo2SlVlrWrBH7DKs7T49Rdk813r2im4bcFAQAyL; _csrf_bk=f5a03b8e609c2383d99ece3c6601a187; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1499390795; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1499394818; Qs_pv_117460=899594246339166100%2C1499053564686013700%2C1850326911606367000%2C2697579815315213000%2C3942526392433027600; _pk_id.6835.e431=85ccfb54429b591e.1499390795.1.1499394819.1499390795.; _pk_ses.6835.e431=*; mediav=%7B%22eid%22%3A%22398779%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22Yb8SKDdxC%3F9zBv*oGy%3ES%22%2C%22ctn%22%3A%22%22%7D; aliyungf_tc=AQAAAGL98GWnpgMAftHidFh68eD0v58s; csrfToken=YYamfDWPutVjvO4muMM1HXQQ; TYCID=4fa5232062b311e7817ee7b56987f1b1; uccid=6c90560bb706ec067b8a5af95d7cf309; ssuid=3175448800; Qs_lvt_117460=1499390795; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzE4NDM5MDk4NyIsImlhdCI6MTQ5OTM5MDkyNCwiZXhwIjoxNTE0OTQyOTI0fQ.05DvNXNBwuSOy8pRI-i0Pfd3opmlKSsOMuGJKVmVBiOigqJVX-C4Itivw-iSFBsZcFndsPH7q8aPyv0HKdcCcg; tyc-user-info=eyJ0b2tlbiI6ImV5SmhiR2NpT2lKSVV6VXhNaUo5LmV5SnpkV0lpT2lJeE16RTRORE01TURrNE55SXNJbWxoZENJNk1UUTVPVE01TURreU5Dd2laWGh3SWpveE5URTBPVFF5T1RJMGZRLjA1RHZOWE5Cd3VTT3k4cFJJLWkwUGZkM29wbWxLU3NPTXVHSktWbVZCaU9pZ3FKVlgtQzRJdGl2dy1pU0ZCc1pjRm5kc1BIN3E4YVB5djBIS2RjQ2NnIiwic3RhdGUiOiIwIiwidm51bSI6IjAiLCJvbnVtIjoiMCIsIm1vYmlsZSI6IjEzMTg0MzkwOTg3In0=; mediav=%7B%22eid%22%3A%22398779%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22Yb8SKDdxC%3F9zBv*oGy%3ES%22%2C%22ctn%22%3A%22%22%7D; _csrf=m4wNFjRPp5wGSlTmfJ3LDA==; OA=AZ/KCjtxkR9Zdc4WngfZPa6Bbndy2ZVSwn7URtw3QQo9LiwAoaDAdT1kWjHY37UP; _csrf_bk=ebb00e9d1adabec334ed2a09b94f4449; _pk_id.6835.e431=85ccfb54429b591e.1499390795.1.1499396206.1499390795.; _pk_ses.6835.e431=*; Qs_pv_117460=1499053564686013700%2C1850326911606367000%2C2697579815315213000%2C3942526392433027600%2C1285738707597412000; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1499390795; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1499396206
# Cache-Control: no-cache
# Postman-Token: 52cac135-9b6a-9723-c39a-2018e43d2fbf
