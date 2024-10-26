## SECTION 1 : Voice Lie Detection System







[![img](https://github.com/backOutlier/IRS-PM-2024-10-26-ISY5001-GP13-Voice-Lie-Detection-System/raw/main/SystemCode/clips/static/hdb-bto.png)](https://github.com/backOutlier/IRS-PM-2024-10-26-ISY5001-GP13-Voice-Lie-Detection-System/blob/main/SystemCode/clips/static/hdb-bto.png)

------

## SECTION 2 : EXECUTIVE SUMMARY / PAPER ABSTRACT

------
`    `This project develops an advanced speech recognition-based polygraph system with the objective of providing an innovative alternative to the traditional polygraph for criminal investigations. The traditional methods, for example the polygraph, have been the subject of criticism on ethical grounds and with regard to their reliability. In view of this, we propose a voice-based polygraph model that uses machine learning to enhance detection accuracy. This provides a more transparent, non-intrusive and adaptable solution for detection.
`    `The project addresses the shortcomings of existing polygraph techniques, particularly in regard to data transparency, model interpretability and cross-domain applicability. This is achieved by integrating a range of machine learning models (including Random Forests, Support Vector Machines, KNN and others) and utilising a soft-voting integration system to enhance the reliability and accuracy of the predictions.  
`    `From a commercial perspective, the project's voice lie detector system has the potential for a wide range of applications in multiple fields, including criminal justice, corporate censorship and insurance claims. The system can be offered on a per-use or subscription basis through a software-as-a-service (SaaS) cloud platform model, making it suitable for a variety of users, including law enforcement agencies, healthcare organisations, insurance companies, and corporate users. Furthermore, the system can be customised to meet the specific needs of individual enterprises, providing customers with proprietary models and tools to facilitate efficient truthfulness judgments in scenarios such as employee selection, internal vetting, and fraud detection.  
`    `The system offers substantial enhancements in both accuracy and user experience when compared to traditional lie detection methods, achieving 95% accuracy on specific data sets. The system's non-intrusive, highly interpretable and well-designed user interfaces enable it to stand out in a wide range of markets, with particular leadership in areas such as justice, healthcare and corporate security, where demand is growing.


## SECTION 3 : CREDITS / PROJECT CONTRIBUTION



| Official Full Name | Student ID (MTech Applicable) | Work Items (Who Did What)                                    | Email (Optional)                                      |
| ------------------ | ----------------------------- | ------------------------------------------------------------ | ----------------------------------------------------- |
| Mohan Liu          | A0297443U                     | 1. The process of cleaning data, extracting features, training models (such as KNN and SVM), and evaluating models. <br>2. Develop integrated models and produce soft voting algorithms to integrate the most accurate algorithms, as well as prepare implementation documents.<br> 3. Contribute to the preparation of reports and the design of their layout. 4. Delegate tasks and monitor progress. | [e1351581@u.nus.edu](mailto:e1351581@u.nus.edu)       |
| Yuhao Zhou         | A1234567B                     | 1. Literature review- Web application front-end development <br>2. Part of web app back-end development <br>3. Server transmission testing<br> 4. Part of report writing <br>5.Demo recording | [zhouyuhao24@u.nus.edu](mailto:zhouyuhao24@u.nus.edu) |
| LiXin Zhang        | A0279544N                     | 1. Participate in system design discussions and draw system architecture diagrams <br>2. Participate in model design and write reports on model training part <br>3. Participate in report integration 4. Produce PowerPoint and video for system design section | [E1351682@u.nus.edu](mailto:E1351682@u.nus.edu)       |
| Zhiyuan Zhang      | A0297736J                     | 1. project reproduction, project Intro, data collection <br>2. model training <br>3.related report writing | [e1351874@u.nus.edu](mailto:e1351874@u.nus.edu)       |
| Wenyu Zhou         | A0294636R                     | 1.web application backend development <br>2. Writing Report 3.PPT creation | [e1348774@u.nus.edu](mailto:e1348774@u.nus.edu)       |

------

## SECTION 4 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO



[![Sudoku AI Solver](https://camo.githubusercontent.com/14852e31ac6dc17ae28b33c4a7ffcd609239aaa8261051f5c48eb8ce0ef75da1/687474703a2f2f696d672e796f75747562652e636f6d2f76692f2d4169594c556a50366f382f302e6a7067)](https://youtu.be/-AiYLUjP6o8)

------

## SECTION 5 : USER GUIDE

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



## SECTION 6 : PROJECT REPORT / PAPER
