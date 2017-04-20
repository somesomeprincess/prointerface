1.以StartPreview为例
2.HeartBeat的IsConnect为发送心跳包

所有操作请求的url都是基于：{ip}:2000/osc/commands/execute ，其中{ip}为相机的ip地址
心跳包请求的url是：{ip}:2000//osc/state

所有操作请求建立在传输一个有效的Fingerprint参数才能请求成功
HttpRequest类简单对发送http请求进行了封装

具体例子详见StartPreview.py

流程：
取得fingerprint--发送心跳包确认连接--发送某操作的请求--验证返回的json

心跳包大概流程：
1.判断是否取得fingerprint：
N:发送取fingerprint的请求，把fingerprint存到某一位置中
无论取不取到fingerprint，以True/False返回
某操作请求的流程：
1.发送心跳包确认连接
2.调用HttpRequest的open方法，发送某操作请求，返回的json用data接收
ex：data=HR.open("camera._startPreview",parameters=param)
第一个入参是哪个操作；第二个入参是操作所需的参数，没有就不用传
3.unittest的验证方法去验证返回的data

用@parameterized.expand进行参数化，目的是改变个别传递的参数，复用同一段代码来进行测试