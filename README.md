# Max Profit Script


Assum you have the yesterday stock price list, where:

* The numbers in the list are stock price of every minute 
* Started at 10:00 when the stock market open
* The values are the price in Australia Dollor
* You can only sell the stock after purshase.

The python script in the repo will take the provided stock price list as variable and output:

* List the best buy/sell plan, time & trade prices which would produce the max profit.


## Developement and test environment

Windows 10  
Python 3.9.2  
Docker version 20.10.8, build 3967b7d  
Visual Studio Code  
  
Ubuntu 20.04.2 LTS  
Python 3.8.10  
Docker version 20.10.7, build 20.10.7-0ubuntu1~20.04  
Visual Studio Code  
  

## Run the script in IDE

Python script can be executed in IDE, e.g. VSCode and prompts user to input the stock price as list, separate by space.

The script will compare the stock prices in the list and generate purchase and sell plan with the best profit. 


```
C:\> python maxprofit.py
Enter stock price as list, separated by space: 
 11 15 16 13 20 13 11 15 9 12 13 15 
Buy at price A$11.0 @ 10:01 and sell it at price A$20.0 @ 10:05 for the max profit A$9.0
```

## Run the script with Docker Container

You can also build a docker image with the Dockerfile in the repo. And run the docker to execute the script without install the Python binaries on your local machine.

### Build docker image 

1. Clone the repo to computer where you have Docker engine installed
2. Create docker image with the Dockerfile and tag it as necessary
3. Confirm the docker image created locally with no errors

```
C:\>docker build . -t maxprofit-alpine
[+] Building 9.0s (8/8) FINISHED
 => [internal] load build definition from Dockerfile                                                                         0.1s 
 => => transferring dockerfile: 146B                                                                                         0.0s 
 ...
 => => writing image sha256:f199b456bcd0bd30d899e325f495adcf38ff9c97323f80204c1911288a084b2f                                 0.0s 
 => => naming to docker.io/library/maxprofit-alpine                                                                          0.0s 

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them

C:\> docker image list 
REPOSITORY         TAG       IMAGE ID       CREATED         SIZE
maxprofit-alpine   latest    f199b456bcd0   2 minutes ago   45.1MB
```

### Run docker to execute the script

Run docker with newly created image and enter stock price as list to outpu th best buy/sell plan.

```
C:\> docker run -it maxprofit-alpine
Enter stock price as list, separated by space: 
 11 15 16 13 20 13 11 15 9 12 13 15
Buy at price A$11.0 @ 10:01 and sell it at price A$20.0 @ 10:05 for the max profit A$9.0
```
