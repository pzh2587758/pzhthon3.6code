import requests

class requests_xx():
     def 获取():
          r = requests.get(r'https://www.baidu.com')#获取某个网页
     def http_其他请求类型():
          r = requests.post("http://httpbin.org/post")
          r = requests.put("http://httpbin.org/put")
          r = requests.delete("http://httpbin.org/delete")
          r = requests.head("http://httpbin.org/get")
          r = requests.options("http://httpbin.org/get")

     def 传递参数():
          payload = {'key1': 'value1', 'key2': ['value2', 'value3']}#还可以将一个列表作为值传入
          r = requests.get("http://httpbin.org/get", params=payload)
          
          print(r.url)#通过打印输出该 URL，你能看到 URL 已被正确编码

          
