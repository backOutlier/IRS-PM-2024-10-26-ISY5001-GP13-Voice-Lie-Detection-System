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



[![BUSINESS and DEMO](Video/ISY500PRE（business and demo).mp4)](https://youtu.be/vqprQnLd8X0)]  
<rb>
[![System and Tech]([Video/ISY5001-Project-Pre(tech and system).mp4)](https://youtu.be/WfFMWGkmkG8)]

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
PROJECT REPORT	1<br>
1. Executive Summary	3<br>
2. Introduction	4<br>
  2.1 Project Background	4<br>
  2.2 Project Significance	5<br>
    2.2.1 Current limitations	5<br>
    2.2.2 Proposed Solution and Innovations	6<br>
  2.3 Project Content	8<br>
    2.3.1 Project Scope	8<br>
    2.3.1 Project Challenges	9<br>
  2.4 Business Plan	10<br>
    2.4.1 Business Value	10<br>
    2.4.2 Company Vision and Mission	10<br>
    2.4.3 Products and Services	11<br>
    2.4.4 Market Analysis	11<br>
    2.4.5 Business Model	12<br>
  2.5 Project Objective	12<br>
    2.5.1 Base Line Setting	12<br>
    2.5.1 Web Application Setting	13<br>
3. Literature Review	14<br>
  3.1 Relevant Research	14<br>
  3.2 Key Findings	16<br>
  3.3 Methodologies	16<br>
4. System Design	17<br>
  4.1 Architecture Overview	17<br>
  4.2 System Components	18<br>
    4.2.1 User Interface Module	19<br>
    4.2.2 Data Processing Module	19<br>
    4.2.3 Knowledge base Module	20<br>
    4.2.4 Reasoning engine Module	21<br>
    4.2.5 Explainability Module	22<br>
    4.2.6 External interface Module	23<br>
  4.3 Reasoning Techniques and Algorithms	23<br>
5. Data Collection and Preparation	25<br>
  5.1 Data Sources	25<br>
  5.2 Challenges in Data Collection	26<br>
  5.3 Preprocessing Techniques	27<br>
    5.3.1 Video Data Retrieval Process	27<br>
    5.3.2 Video Data Convert Process	28<br>
    5.3.3 Feature Extracted	29<br>
6. Implementation	31<br>
  6.1 Platform and Tools	31<br>
  6.2 Methods and Technologies	32<br>
    6.2.1 Random Forest	32<br>
    6.2.2 Support Vector Machine	34<br>
    6.2.3 K-Nearest Neighbors	35<br>
    6.2.4 Deep Neural Networks	37<br>
7. Results and Progress	38<br>
  7.1Preliminary Results from Reasoning Engine	38<br>
  7.2 Performance Metrics Visualizations	38<br>
    7.2.1 Soft Voting Integration Model_A	38<br>
    7.2.2 Soft Voting Integration Model_B	40
  7.3 Comparison with Existing Lie Detection Techniques	41<br>
8 Web Application Development	43<br>
  8.1 Initiation	43<br>
  8.2 Front-End Development	43<br>
    8.2.1 Tools	43<br>
    8.2.2Application Design	44<br>
  8.3 Back-End Development	44<br>
    8.3.1 System Architecture	44<br>
    8.3.2 Database Design	45<br>
    8.3.3 Api Design	45<br>
9. Challenges and Future Work	48<br>
  9.1 Obstacles in System Development	48<br>
    9.1.1 Limitation of Data and Features	48<br>
    9.1.2 Problem for the accuracy and generation of reasoning engine	48<br>
  9.2 Strategies to Overcome Identified Challenges	49<br>
    9.2.1 Methods to solve limitation of Data and Features	49<br>
    9.2.2 Methods to solve problem for the accuracy and generation	49<br>
  9.3 Additional Features to be Implemented 	49<br>
References	51
