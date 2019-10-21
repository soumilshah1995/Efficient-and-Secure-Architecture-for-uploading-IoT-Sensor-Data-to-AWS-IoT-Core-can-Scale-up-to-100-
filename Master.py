

__Author__ = "Soumil Nitn Shah"
__Version__ = "0.0.1"
__Email__ = ["soushah@my.bridgeport.edu", "shahsoumil519@gmail.com"]

"""

Hello my Name is Soumil Nitin Shah this is what i want to say about coding "coding is art "
well i have use Facade and Singleton Design Pattern 
Entire  Architecture can be broken down into Severals Objects 

    >-----Sensor
    >-----Datetime
    >-----Metaclass
    >-----Argument
    >-----log
    >-----Facade
    
    Facade is Central Controller 
    
"""

try:

    from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
    import logging
    import time
    import argparse
    import json
    import datetime
    import random
    import os
    import sys

except Exception as e:
    print("Some modules are misisng {}".format(e))


class MetaClass(type):

    """ Singleton Design Pattern  """

    _instance = {}

    def __call__(cls, *args, **kwargs):

        """ if instance already exist dont create one  """

        if cls not in cls._instance:
            cls._instance[cls] = super(MetaClass, cls).__call__(*args, **kwargs)
            return cls._instance[cls]


class log(object):

    """ Create a Log File regarding Execution Time memory Address size etc """

    def __init__(self, func):
        """ Constructor  """
        self.func = func

    def __call__(self, *args, **kwargs):
        """ Wrapper Function """

        start = datetime.datetime.now()     # start time
        Tem = self.func(self, *args, **kwargs)    # call Function
        FunName = self.func.__name__        # get Function Name
        end = datetime.datetime.now()       # End time

        message = """                       # Form Message
            
            Function : {}
            Execution Time : {}
            Address : {}
            Memory: {} Bytes
            Date: {}
            Args: {}
            Kwargs {}
            
            """.format(FunName,
                       end-start,
                       self.func.__name__,
                       sys.getsizeof(self.func),
                       start, args, kwargs)

        cwd = os.getcwd()                       # get CWD
        folder = 'Logs'                         # Create Folder Logs
        newPath = os.path.join(cwd, folder)     # change Path

        try:
            """ try to create directory """
            os.mkdir(newPath)                   # create Folder
            logging.basicConfig(filename='{}/log.log'.format(newPath), level=logging.DEBUG)
            logging.debug(message)

        except Exception as e:

            """ Directory already exists """

            logging.basicConfig(filename='{}/log.log'.format(newPath), level=logging.DEBUG)
            logging.debug(message)

        return Tem


class Argument(object):

    __slots__ = []

    def __init__(self):
        pass

    @staticmethod
    def customCallback(client, userdata, message):
        print("Received a new message: ")
        print(message.payload)
        print("from topic: ")
        print(message.topic)
        print("--------------\n\n")

    @staticmethod
    def configure(topic = "sdk/test/Python" ):

        """AWS configuration  """

        AllowedActions = ['both', 'publish', 'subscribe']
        # Read in command-line parameters
        parser = argparse.ArgumentParser()
        parser.add_argument("-e", "--endpoint", action="store", required=True, dest="host", help="Your AWS IoT custom endpoint")
        parser.add_argument("-r", "--rootCA", action="store", required=True, dest="rootCAPath", help="Root CA file path")
        parser.add_argument("-c", "--cert", action="store", dest="certificatePath", help="Certificate file path")
        parser.add_argument("-k", "--key", action="store", dest="privateKeyPath", help="Private key file path")
        parser.add_argument("-p", "--port", action="store", dest="port", type=int, help="Port number override")
        parser.add_argument("-w", "--websocket", action="store_true", dest="useWebsocket", default=False,
                            help="Use MQTT over WebSocket")
        parser.add_argument("-id", "--clientId", action="store", dest="clientId", default="basicPubSub",
                            help="Targeted client id")
        parser.add_argument("-t", "--topic", action="store", dest="topic", default="sdk/test/Python", help="Targeted topic")
        parser.add_argument("-m", "--mode", action="store", dest="mode", default="both",
                            help="Operation modes: %s"%str(AllowedActions))
        parser.add_argument("-M", "--message", action="store", dest="message", default="Hello World!",
                            help="Message to publish")

        args = parser.parse_args()
        host = args.host
        rootCAPath = args.rootCAPath
        certificatePath = args.certificatePath
        privateKeyPath = args.privateKeyPath
        port = args.port
        useWebsocket = args.useWebsocket
        clientId = args.clientId
        # topic = args.topic
        topic = topic

        if args.mode not in AllowedActions:
            parser.error("Unknown --mode option %s. Must be one of %s" % (args.mode, str(AllowedActions)))
            exit(2)

        if args.useWebsocket and args.certificatePath and args.privateKeyPath:
            parser.error("X.509 cert authentication and WebSocket are mutual exclusive. Please pick one.")
            exit(2)

        if not args.useWebsocket and (not args.certificatePath or not args.privateKeyPath):
            parser.error("Missing credentials for authentication.")
            exit(2)

        # Port defaults
        if args.useWebsocket and not args.port:  # When no port override for WebSocket, default to 443
            port = 443
        if not args.useWebsocket and not args.port:  # When no port override for non-WebSocket, default to 8883
            port = 8883

        # Configure logging
        logger = logging.getLogger("AWSIoTPythonSDK.core")
        logger.setLevel(logging.DEBUG)
        streamHandler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        streamHandler.setFormatter(formatter)
        logger.addHandler(streamHandler)

        # Init AWSIoTMQTTClient
        myAWSIoTMQTTClient = None
        if useWebsocket:
            myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId, useWebsocket=True)
            myAWSIoTMQTTClient.configureEndpoint(host, port)
            myAWSIoTMQTTClient.configureCredentials(rootCAPath)
        else:
            myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
            myAWSIoTMQTTClient.configureEndpoint(host, port)
            myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

        # AWSIoTMQTTClient connection configuration
        myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
        myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
        myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
        myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
        myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

        # Connect and subscribe to AWS IoT
        myAWSIoTMQTTClient.connect()
        if args.mode == 'both' or args.mode == 'subscribe':
            myAWSIoTMQTTClient.subscribe(topic, 1, Argument.customCallback)
        time.sleep(2)
        return args, myAWSIoTMQTTClient, topic


class Sensor(object):

    """Sensor Class for IoT """

    def __init__(self):
        self._datetime = DateTime()

    def get(self):
        Temperature = random.randint(1,89)
        Humidity = random.randint(1,77)
        return Temperature, Humidity

    def getPayload(self):

        Temperature, Humidity = self.get()
        message = {}
        Payload = {}

        Payload["Temperature"] = Temperature
        Payload["Humidity"] = Humidity
        Payload["Date"] = str(self._datetime.getDate())
        Payload["Time"] = str(self._datetime.getTime())
        message['message'] = Payload

        message['sequence'] = str(datetime.datetime.now())
        messageJson = json.dumps(message)

        return messageJson

class DateTime(object):

    """ Datetime Class """

    __slots__ = ["d"]

    def __init__(self):
        self.d = datetime.datetime.now()

    def getDate(self):
        return "{}-{}-{}".format(self.d.month, self.d.day, self.d.year)

    def getTime(self):
        return "{}:{}:{}".format(self.d.hour, self.d.minute, self.d.second)

    def getDateTime(self):
        return self.d


class Facade(metaclass=MetaClass):

    __slots__ = ["_argument", "_sensor", "_datetime", "_args", "_myAWSIoTMQTTClient", "_topic"]

    def __init__(self):

        """ Constructor """

        self._argument = Argument()
        self._sensor = Sensor()
        self._datetime = DateTime()
        self._args, self._myAWSIoTMQTTClient, self._topic = self._argument.configure()

    def upload(self):

        """ Upload Sensor Data """

        if self._args.mode == 'both' or self._args.mode == 'publish':
            payload = self._sensor.getPayload()
            self._myAWSIoTMQTTClient.publish(self._topic, payload, 1)
            time.sleep(4)


if __name__ == "__main__":
    obj = Facade()
    obj.upload()
