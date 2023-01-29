# mchacks

MCHacks Hackathon Submission.

This application is an extension to the Raddish website. It adds an option to let an AI make the decision for your next meal. This AI is trained with a dataset and uses and API to manage all information, such as database queries and http requests.

## Description

Raw-Dish uses Java for its powerfull JavaFX Framework. Once a questionnaire is submitted an api request is made and the AI makes a decision based on the information provided. It will then store all the data into a database for developement purposes. Once the AI finds an answer it responses to the client with information on a restaurant and a dish. The REST API is build with python using Flask.

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

Romullus
Constance Prevot https://www.linkedin.com/in/constance-prevot/ 
Richard Badir https://www.linkedin.com/in/richard-badir-199b44234/ 
Andrew Dagher https://www.linkedin.com/in/aniss-chalah-606774203/


## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
