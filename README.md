## Project Name : Voice Lie Detection System







![img](Miscellaneous/cover.jpg)

------

## SECTION 1 : EXECUTIVE SUMMARY / PAPER ABSTRACT

------
`    `Our project develops an advanced speech recognition-based polygraph system with the aim of providing an innovative alternative to the traditional polygraph for criminal investigations and other areas. The traditional methods, for example the polygraph, have been the subject of criticism on ethical grounds and with regard to their reliability. In view of this, we propose a voice-based polygraph model that uses machine learning to enhance detection accuracy. This provides a more transparent, non-intrusive and adaptable solution for detection. 
  
  `    `The project addresses the shortcomings of existing polygraph techniques, particularly in regard to data transparency, model interpretability and cross-domain applicability. They are achieved by integrating a range of machine learning models (including Random Forests, Support Vector Machines, KNN and others) and we utilise the soft-voting integration methods to enhance the reliability and accuracy of the predictions.  
    
`    `From a commercial perspective, the project's voice lie detector system has the potential for a wide range of applications in multiple fields, including criminal justice, corporate censorship and insurance claims. Our system can be offered on a per-use or subscription basis through a software-as-a-service (SaaS) cloud platform model, making it suitable for a variety of users, including law enforcement agencies, healthcare organisations, insurance companies, and corporate users. The system has been developed with the objective of meeting the specific needs of a range of enterprises. It could assist customers in making efficient judgments in different scenarios such as employee selection, internal vetting, and fraud detection. 



## SECTION 2 : CREDITS / PROJECT CONTRIBUTION



| Official Full Name | Student ID (MTech Applicable) | Work Items (Who Did What)                                    | Email (Optional)                                      |
| ------------------ | ----------------------------- | ------------------------------------------------------------ | ----------------------------------------------------- |
| Mohan Liu          | A0297443U                     | 1. The process of cleaning data, extracting features, training models (such as KNN and SVM), and evaluating models. <br>2. Develop integrated models and produce soft voting algorithms to integrate the most accurate algorithms, as well as prepare implementation documents.<br> 3. Contribute to the preparation(write and revise) of reports and the design of their layout. <br>4. Delegate tasks and monitor progress. | [e1351581@u.nus.edu](mailto:e1351581@u.nus.edu)       |
| Yuhao Zhou         | A1234567B                     | 1. Literature review- Web application front-end development <br>2. Part of web app back-end development <br>3. Server transmission testing<br> 4. Part of report writing <br>5.Demo recording | [zhouyuhao24@u.nus.edu](mailto:zhouyuhao24@u.nus.edu) |
| LiXin Zhang        | A0279544N                     | 1. Participate in system design discussions and draw system architecture diagrams <br>2. Participate in model design and write reports on model training part <br>3. Participate in report integration <br>4. Produce PowerPoint and video for system design section | [E1351682@u.nus.edu](mailto:E1351682@u.nus.edu)       |
| Zhiyuan Zhang      | A0297736J                     | 1. project reproduction, project Intro, data collection <br>2. model training <br>3.related report writing | [e1351874@u.nus.edu](mailto:e1351874@u.nus.edu)       |
| Wenyu Zhou         | A0294636R                     | 1.web application backend development <br>2. Writing Report <br>3.PPT creation | [e1348774@u.nus.edu](mailto:e1348774@u.nus.edu)       |

------

## SECTION 3 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO



[![BUSINESS and DEMO](Video/ISY500PRE（business and demo).mp4)

------

## SECTION 4 : USER GUIDE

`Refer to appendix <Installation & User Guide> in project report at Github Folder: ProjectReport`

Make sure all developer tools have been installed:

- npm
- Python3
- pip

### [ 1 ] To run the back-end server:

```
$ cd SystemCode/backend
$ pip install -r requirements.txt
$ cd myproject
$ python manage.py makemigrations api
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

### [ 2 ] To run the front-end server:

```
$ cd SystemCode/frontend
$ npm install
$ npm run dev
```

> **Go to URL using web browser** [http://127.0.0.1:4000](http://127.0.0.1:4000/)



## SECTION 5 : PROJECT REPORT / PAPER
