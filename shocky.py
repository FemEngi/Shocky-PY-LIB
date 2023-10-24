# import shockybackend
import requests
import sys
import random
import os
import time
from paho.mqtt import client as mqtt_client
class Shocky:
    URL1="http://esp32.local"
    client_id = f'python-mqtt-{random.randint(0, 1000)}'
    username = 'data'
    password = 'HcYJiB5QeuJPpgC'
    stop_threads=False
    
    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)
    
    def connect_mqtt(self) -> mqtt_client:
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)
        def on_publish(client, userdata, mid):
            print("haiii12345")

        client = mqtt_client.Client(self.client_id)
        client.tls_set(ca_certs=self.resource_path('emqxsl-ca.crt'))
        
        client.username_pw_set(self.username, self.password)
        client.on_connect = on_connect
        client.on_publish = on_publish
        
        client.connect(self.broker, self.port)
        
        return client


    def initilize_shocky(self, key=-1):
        if key==-1:
            key = str(random.randint(0, 9999))
        if key=="":
            return "no"
        topic = key #+ "mqtt/python/mqtt/"
        client = self.connect_mqtt()
        # publish(client, key, bytearray([128,128,128]))
        return client, key
    
    
    def nbrq2(self,args):
        requests.get(self.URL1+args)
    
    def connect(self,key,espurl):
        client=self.init(key)
        URL=espurl
        return client, espurl
    def init_subscriber(self,client, key):
        self.subscribesys(client, key)
        

    def nbrq2(URL1,args):
        requests.get(URL1+args)
    def nbrq(args):
        requests.get(args)
    def init_publisher(key):
        print("done")
        # if not backendinit:
            # global client
            # client=shockybackend.init(key)
            # backendinit=True
        # shockybackend.subscribesys(client, key)
        # return client

    def send_shock_wan(self,client, key, power, duration):
        self.publishing(client, "mqtt/python/mqtt/"+str(key), str("/1/"+str(duration)+"/"+str(power)+"/"))
    def send_vibrate_wan(self,client, key, power, duration):
        self.publishing(client, "mqtt/python/mqtt/"+str(key), str("/1/"+str(duration)+"/"+str(power)+"/"))
    def send_shock(url, power, duration):
        Shocky.nbrq(url+str("/1/"+str(duration)+"/"+str(power)+"/"))
    def send_vibrate(url, power, duration):
        Shocky.nbrq(url+str("/2/"+str(duration)+"/"+str(power)+"/"))
    def estop(url):
        Shocky.nbrq(url+str("/1/"+str(10)+"/"+str(0)+"/"))
        Shocky.nbrq(url+str("/2/"+str(10)+"/"+str(0)+"/"))
    def estop_wan(self,client, key):
        self.publishing(client, "mqtt/python/mqtt/"+str(key), str("/1/"+str(10)+"/"+str(0)+"/"))
        self.publishing(client, "mqtt/python/mqtt/"+str(key), str("/2/"+str(10)+"/"+str(0)+"/"))
        

    def on_message(self,client, userdata, msg):
        print("gay")
        print(msg.payload.decode())
        requested=msg.payload.decode()
        self.nbrq2(requested)
    
    
    def start_loop(self,client):
        while True:
            client.loop()
            if self.stop_threads:
                time.sleep(1)
                self.stop_threads=False
                break
    def stop_loop(self, client):
        self.stop_threads=True
                