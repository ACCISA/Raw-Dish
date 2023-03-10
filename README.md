# Raw-Dish

MCHacks Hackathon Submission.

This application is an extension to the Raddish website. It adds an option to let an AI make the decision for your next meal. This AI is trained with a dataset and uses and API to manage all information, such as database queries and http requests.

<img src="https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/002/360/528/datas/gallery.jpg" align="right"
     alt="Size Limit logo by Anton Lovchikov" width="459" height="257">
     
## Description

Raw-Dish uses Java for its powerfull JavaFX Framework. Once a questionnaire is submitted an api request is made and the AI makes a decision based on the information provided. It will then store all the data into a database for developement purposes. Once the AI finds an answer it responses to the client with information on a restaurant and a dish. The REST API is build with python using Flask.

## Demo
![alt text](https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/002/360/910/datas/gallery.jpg)
![alt text](https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/002/360/909/datas/gallery.jpg)
![alt text](https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/002/362/479/datas/gallery.png)
![alt text](https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/002/361/070/datas/gallery.jpg)
![alt text](https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/002/361/817/datas/gallery.jpg)




## Getting Started

### Dependencies

JFoenix - Download Here: https://github.com/sshahine/JFoenix
org.json - Download Here: https://jar-download.com/artifacts/org.json

### Installing
Add VM Options to IDE: 
```
--add-opens=java.base/java.lang.reflect=com.jfoenix 
```
JDK:
```
open JDK 19
```
### Executing program

* How to run the program

*Run the API:
In a venv run the routes.py. This will train the AI Model.
```
py routes.py
```
Once the API is running you can run the project in your IDE.


## Help

Any advise for common problems or issues.
```
JFoenix Version: 9.0.10
Org.JSON: json.jar (20220924)
```

## Authors

Aniss Chalah https://www.linkedin.com/in/aniss-chalah-606774203/
Constance Prevot https://www.linkedin.com/in/constance-prevot/ 
Richard Badir https://www.linkedin.com/in/richard-badir-199b44234/ 
Andrew Dagher https://www.linkedin.com/in/aniss-chalah-606774203/

