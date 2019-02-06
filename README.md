#### SI 507 Python Programming Project 1 Assignment
This is a README.md for file SI507_project_1.py. This is a homework assignment for SI 507/ Professor Jackie Cohen at the University of Michigan.

##### What are the files included?
The files included are SI507_project_1.py, lab3_code.py, requirements.txt and README.md. These files are all in a folder called project_1.

The lab3_code.py contains logic that converts the three currencies (yuan, pound, dollar) into desired currency. There is also logic that allows users to deposit an amount to the a bank of choice. The logic will check if the bank accepts the type of currency that the user has. If the bank accepts the type of currency that the user wishes to deposit,  the bank will then add the user's deposit amount to the current amount in the bank.

In SI507_project_1.py displays information that was created in lab3_code.py. There are routes in this code that display different information. When the route ends with "/", we are that home page with text that reads "Just the home page, nothing interesting.". Similarly, when user inputs '/yuan/<amt>' and inserts a desired amount, the amount and currency name will be on display. This occurs because we have established methods in each currency class (Yuan, Pound, Dollar) in the lab3_code.py. Lastly, when user inputs '/bank/<name>/<currency>/<value>', a sentence that reads "Welcome to the (NAME) bank! NAME Bank holds the (CURRENCY) currency and currently holds (VALUE) of (CURRENCY)" will be displayed. This occurs because we have  established methods in the lab3_code.py to create this sentence. In lab3_code.py, we create this sentence by isolating variables we have created so that they can be used in the sentence.  

##### How do you run this project?
Download project_1 on your local computer.
requirements.txt will indicate all the dependencies required for this project. Open the terminal and download all the dependencies by typing pip install -r requirements.txt.

##### What is the final result?
The final result is displaying of information that was created in lab3_code.py. 
