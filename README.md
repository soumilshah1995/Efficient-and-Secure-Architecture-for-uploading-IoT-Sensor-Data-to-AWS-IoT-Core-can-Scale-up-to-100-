
# Efficient and Secure Architecture for uploading IoT Sensor Data to AWS IoT Core can Scale up to 100 + Sensor and Devices


![Class Diagram ](https://user-images.githubusercontent.com/39345855/67233717-c5b36300-f411-11e9-92ed-ea5d2653fcd6.png)


#### Results
![Screen Shot 2019-10-21 at 2 49 12 PM](https://user-images.githubusercontent.com/39345855/67233886-0f9c4900-f412-11e9-9700-a5df98423ae7.png)


## Getting Started

Hello! I’m Soumil Nitin Shah, a Software and Hardware Developer based in New York City. I have completed by Bachelor in Electronic Engineering and my Double master’s in Computer and Electrical Engineering. I Develop Python Based Cross Platform Desktop Application , Webpages , Software, REST API, Database and much more I have more than 2 Years of Experience in Python

In This Blog I will Introduce a Efficient Architecture to Upload IoT Sensor Data on AWS IoT Core. Well this Architecture uses Facade Design Pattern and Singleton Design Pattern and to Make it more efficient I have used Slots in Python.

The _ represent its a private and cannot be accessed from outside the class. slots makes sure that attributes cannot be added at run time and saves memory. Further I am working adding Queue Data Structure so all the Sensor Object can be Queued and one by one those values can be retrieved and uploaded on cloud. This is initial version I am still working on it to improve it :D

Above Figure shows MQTT messages are being Uploaded on AWS. and Further its Connected to IoT Analytics to provide real time Analysis. Later on Pipeline can be created which will store the data on S3 Bucket

What is Slots in Python?

In Python every class can have instance attributes. By default Python uses a dict to store an object’s instance attributes. This is really helpful as it allows setting arbitrary new attributes at runtime.

However, for small classes with known attributes it might be a bottleneck. The dict wastes a lot of RAM. Python can’t just allocate a static amount of memory at object creation to store all the attributes. Therefore it sucks a lot of RAM if you create a lot of objects (I am talking in thousands and millions). Still there is a way to circumvent this issue. It involves the usage of __slots__ to tell Python not to use a dict, and only allocate space for a fixed set of attributes.

What problems can the Facade design pattern solve? 

To make a complex subsystem easier to use, a simple interface should be provided for a set of interfaces in the subsystem.
The dependencies on a subsystem should be minimized.
What solution does the Facade design pattern describe?

implements a simple interface in terms of (by delegating to) the interfaces in the subsystem and
may perform additional functionality before/after forwarding a request.
