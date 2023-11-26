# SmartRoomData

Using Smart Room Data project, we can call APIs with image or video to detect presence of a person in a room. 


## Features 

    * Detect and Count Person
    * Recognize Empty Room
    * Real time Detection


## Setup SmartRoomData Locally

1. Please clone the repository

2. Create a virtual environment 

3. Install the libraries from requirement.txt

4. Please add the desired PyTorch model file and name it yolov5l.pt

5. Run ``` python -u app.py``` command

6. The application should run at http://127.0.0.1:5100


## Call Detect Person Api with Images

1. Make a post request at {Base URL}/detect_person using Postman

2. To upload the image, go Body -> form-data

3. In the Key column Add a key named 'file' (Select file in key)

4. In the Value column select the file and upload


## Tech Stack Used

    - Flask
    - PyTorch
    - Computer Vison
    - Machine Learning