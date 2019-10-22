
# Efficient and Secure Architecture for uploading IoT Sensor Data to AWS IoT Core can Scale up to 100 + Sensor and Devices


![Class Diagram ](https://user-images.githubusercontent.com/39345855/67233717-c5b36300-f411-11e9-92ed-ea5d2653fcd6.png)


#### Results
![Screen Shot 2019-10-21 at 2 49 12 PM](https://user-images.githubusercontent.com/39345855/67233886-0f9c4900-f412-11e9-9700-a5df98423ae7.png)


## Getting Started

Hello! I’m Soumil Nitin Shah, a Software and Hardware Developer based in New York City. I have completed by Bachelor in Electronic Engineering and my Double master’s in Computer and Electrical Engineering. I Develop Python Based Cross Platform Desktop Application , Webpages , Software, REST API, Database and much more I have more than 2 Years of Experience in Python

In This Blog I will Introduce a Efficient Architecture to Upload IoT Sensor Data on AWS IoT Core. Well this Architecture uses Facade Design Pattern and Singleton Design Pattern and to Make it more efficient I have used Slots in Python.

## Guide to Use This 
* Go to AWS and click on IoT Core and get started download the package 
* Package has bunch of files and start.sh 
* Paste my Python file in Location of aws-iot-device-sdk-python>samples>basicpubsub> basicpubsub.py
* Run the Start.sh you should see posting Messages in AWS 
* Modify Code only place you need to modify is Sensor Class 

#### Make sure to change the certificate with whatever you have in shell script 
```
        >> python /Users/soumilshah/Desktop/AWSIoTCore/Master.py -e a15uvuidocrdo1-ats.iot.us-east-1.amazonaws.com -r root-CA.crt -c PyThing8oct.cert.pem -k PyThing8oct.private.key

```


## Authors

* **Soumil Nitin Shah** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks to Indian Pythonist 
