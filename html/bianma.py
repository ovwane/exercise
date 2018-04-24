# a = {"data":{"id":{"createTime":"2017-08-02 11:52:55","delStatus":2},"createTime":"2017-08-02 11:52:55","delStatus":2,"updateTime":"2018-03-21 11:27:43","phone":"18202886913","pin":"1000000723213884","token":"e479cdbc5bd144fbbf2ab533ab6b9411","idcard":"53038118876567057x","name":"一二三四五六七八","email":"","nickName":"聚聚","sexType":1,"pic":"/nidone/0d5ed831bd27443799c86f35d9613fd0.jpg","firstLogin":2,"selfRegist":1,"gatewayKey":"d7f79452ba3b495487c9c8493ad8fd4e","estateId":"13","unitNo":"6666","buildingNo":"A","buildingId":38,"ownerType":1,"client":True,"estateFcirclePic":"/nidone/47b0f42be5bc43958600ef7771b53509.png","birthday":"1991-04-14 01:00:00","status":1,"height":"120","weight":"10.4"},"success":True}
# n = "<response[66]>"
#
#
# def c(f, b):
#     if isinstance(b, dict):
#         for i in b:
#             m = (f+"[\"%s\"]" %i)
#             print(m)
#             c(m, b[i])
#
# c(n,a)
#
# class Fuck(object):
#     def __init__(self, func):
#         self.func = func
#     def __call__(self, *args, **kwargs):
#         import time
#         start_time = time.time()
#         res = self.func(*args, **kwargs)
#         end_time = time.time()
#         print('the function "%s" run time is %s' % (self.func.__name__,
#                                                     (end_time - start_time)))
#         return res

a = eval("{'data': {'id': 51, 'createTime': '2017-12-01 16:31:07', 'delStatus': 2, 'updateTime': '2018-02-08 13:51:32', 'phone': '18202886913', 'pin': '1000001203055707', 'token': 'cc86bf60939545918ea0399a0c8e1d9e', 'name': 'nn', 'nickName': 'N8l79', 'sexType': 2, 'pic': '/nidone/2b1aab0706ec4929a4c72ed24a7998d4.jpg', 'firstLogin': 2, 'selfRegist': 1, 'gatewayKey': '9c9fb140960f40d98efa0b6d519f0b8c', 'estateId': '13', 'unitNo': '6666', 'buildingNo': 'A', 'buildingId': 40, 'ownerType': 2, 'client': False, 'estateFcirclePic': '/nidone/47b0f42be5bc43958600ef7771b53509.png', 'birthday': '2018-02-08 00:00:00', 'status': 1}, 'success': True}")

def write_json(data):
    try:
        for n in data:
            print('"%s"' % n)
            if isinstance(data[n], dict):
                write_json(data[n])
    except:
        pass


if __name__ == "__main__":
    write_json(a)