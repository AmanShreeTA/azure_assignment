# azure_assignment

Following are the steps I performed:
 - Created a storage account in Azure.
 - Then created a container inside the storage account. Within this container, I created three folders named folder1, folder2, and folder3 and added a total of 4 sample files within these folders.
 - Then write a flask app (flask_app.py) to fetch the names of the files present within the folders in the container.
 - Created a virtual network, a subnet, an azure vm of type D2s_v3 with ubuntu os and a public ip, and a network security group with inbound traffic allowed on port 22 and 5000.
   ![Screenshot (51)](https://github.com/AmanShreeTA/azure_assignment/assets/155889933/22fbdeaa-d686-4b60-8746-8e505fbb63c5)
 - SSH into the created vm using Putty tool
 - The vm has ubuntu os so python3 comes preinstalled in it , you can check it using the command "python3 --version". If python is not found in the system then you can install it using the command "sudo apt update" followed by "sudo apt install python3".
 - Now we need to install "pip" so that we can install "flask" and "azure.storage.blob" library using the pip package manager. The command to install pip is "sudo apt install python3-pip"
 - Then to install flask and azure.storage.blob run the commands: "pip install flask" and "pip install azure.storage.blob". this will install the required libraries that are need to run the flask app on the azure vm.
 - Now create a separate folder on the vm to store the code of the flask app: "mkdir flask-app"
 - Go into that folder using the change directory command: "cd flask-app/"
 - The flask app is present on my local system, so to transfer the code file to the azure vm, we can run the scp command on the local system's terminal. Open up the powershell window in your local system and type in this command:

   "scp -r /path/to/your/flask/app user@azure_vm_ip:/path/to/destination"
   
   Replace /path/to/your/flask/app with the path to your Flask app directory on your local system.
   Replace user with the username you use to SSH into your Azure VM.
   Replace azure_vm_ip with the public IP address or hostname of your Azure VM.
   Replace /path/to/destination with the path on your Azure VM where you want to upload the Flask app files.
   On running this command, the terminal will ask for the password that you have set on the vm. Enter the password and the code file will be copied to the vm.
 - Now on the vm, check whether the file has been received or not using the "ls -a" command to list all the contents of the current directory. The flask-app.py file will be present the respective directory in which you have assigned while doing the transfer using scp.
 - Now we can run the flask app on the azure vm. Go to the directory where the flask-app.py file is present. then enter the command: "python3 flask-app.py". This will run the flask app on the port specified in the code (by default it is port 5000).
   ![Screenshot (53)](https://github.com/AmanShreeTA/azure_assignment/assets/155889933/64b029d7-bea7-4b60-b91f-39d8145fdb04)
 - The terminal will show the localhost ip followed by the portnumber on which the flask app is running. To access the running flask app from the internet we need to use the public ip of the vm followed by the portnumber, for example : 40.71.6.155:5000
 - Open a browser on any system and type in the url: http://40.71.6.155:5000 (The IP address is subject to change based on the public IP of the created Azure VM)
 - You will be able to see the output page with the filenames present in the folders in the container on azure.
   ![Screenshot (50)](https://github.com/AmanShreeTA/azure_assignment/assets/155889933/ef3eb7be-80e2-42cf-8601-5651af2c96c7)
 - Here the billing information on the resources used in this assignment:
   ![Screenshot (54)](https://github.com/AmanShreeTA/azure_assignment/assets/155889933/156dbee0-3eb4-44dd-9e43-b8f3f097edcd)

