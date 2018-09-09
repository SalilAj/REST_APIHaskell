# Work Stealing

REST API service with a Master worker communication to calculate the cyclomatic complexity of a python code

How to Run?

    Clone the repository
    run the master.py server using the below command
    (make sure all dependencies are installed)
    Command: $ python master.py
    Server will run locally on port 8001
    
    Then run the Worker service which will communicate with the Master
    Command: $ python worker.py
    
Description:
This project was developed using the Work stealing architecture where multiple workers will call a REST API get request to the Master server which would then assign the work to the workers.

The Master server queries all the commits of a repository and waits for the workers.
The Workers ping the Master server who sends then the SHA value of the commits along with the repository of the URL
The Workers are expected to calculate the Cyclomatic Complexity of the code during that commit
The Workers fist query the file tree of that commit and retrive the URL of the commit blobs.
On retrieveing the URL's of the blog the Workers download the files into a temporary folder.
Using the Radon python library the workers then calulate the average Cyclomatic Complexity of the files and returns the value back to the server.
Once the Work is completed the Workers are ready to accept (*Steal) more work from the Master server.
Once all the cyclomatic complexity of the commits are calculated we measure the time taken to complete the total work and compare the result with more workers working parallely, thus Scaling.

Current Issue:
Unable to retrieve value from CCHarvester class from Radon there by unable to proceed further.
REST API has been Implemented and workers can work parallely using the worker.py as a template.
