import time

import paho.mqtt.client as mqtt
import ssl

# 单向证书效验，只用配置一个证书即可
cafile = "ca.crt"

# certfile = "C:/Users/UBAINS/Desktop/fsdownload/Myca/server.crt"
#
# keyfile = "C:/Users/UBAINS/Desktop/fsdownload/Myca/server.key"

user = "admin"
passwd = "123456"
server = "192.168.1.96"
port = 8883


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("BB")  # 订阅消息


def on_message(client, userdata, msg):
    print("主题:" + msg.topic + " 消息:" + str(msg.payload.decode('utf-8')))


def on_subscribe(client, userdata, mid, granted_qos):
    print("On Subscribed: qos = %d" % granted_qos)


def init_client():
    client = mqtt.Client(str(time.time()))
    client.tls_set(cafile, cert_reqs=ssl.CERT_NONE, tls_version=ssl.PROTOCOL_TLSv1_2)
    client.tls_insecure_set(True)
    client.username_pw_set(user, passwd)
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    client.on_connect = on_connect
    client.connect(server, port, 60)
    print("connect finish")

    client.loop_start()

    # 每2S 发送一次消息,发送500次
    for i in range(1, 500):
        time.sleep(2)
        client.publish("AA", "Time  is  " + str(time.time()), qos=0, retain=False)
        print("第%s次发送消息" % str(i))


init_client()
