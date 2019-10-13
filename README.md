#Parking Lot

Feature 1 :

Park : Allocate a slot, record the registration number, slot and color of the car

 

Feature 2 :

Seek : Given a slot number, I should be able to get the details of the car

### Prerequisites:

    - Python 3.5 or above need to be installed

    Note: If permissions are not there to set the environmental variables use the absolute path of python to execute the script:

    Example: C:\python3.6\python sample.py

### Steps for performing Parking Lot Process

Step 1: Untar .tar file using following command and run cd parking_lot1.0
    
        tar -xzvf parking_lot-1.0.tar.gz
        
        cd parking_lot-1.0
       
Step 2: Execute the python file main_work_flow.py which is the Entry for Parking Lot workflow
    
        python main_work_flow.py
            
Step 3: The workflow will list 5 Options as shown below :
        **_Please choose one option from following:
        
        1.	create_parking_lot
        2.	park_vehicle (<----- IN)
        3.	seek_vehicle
        4.  exit_vehicle (-----> OUT)
        5.  terminate programme
   
        Option 1 : Create parking lot with given number
        Option 2 : Park a vehicle based on reg no and color, allocates slot to a vehicle
        Option 3 : Details of the car parked in the given slot
        Option 4 : Depart a vehicle based on slot / free up slots
        Option 5 : Terminate Programme

### Build the project locally
Step 1: Execute build.sh from project root - to generate build artifacts in the dist directory

 
    ./build.sh

Step 2: Find the tar.gz file in the dist directory under project root and export