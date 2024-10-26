## SECTION 1 : PROJECT TITLE



## Singapore Housing & Deveoplment Board - BTO Recommender System



[![img](https://github.com/backOutlier/IRS-PM-2024-10-26-ISY5001-GP13-Voice-Lie-Detection-System/raw/main/SystemCode/clips/static/hdb-bto.png)](https://github.com/backOutlier/IRS-PM-2024-10-26-ISY5001-GP13-Voice-Lie-Detection-System/blob/main/SystemCode/clips/static/hdb-bto.png)

------

## SECTION 2 : EXECUTIVE SUMMARY / PAPER ABSTRACT



Singapore ranks amongst countries with the highest population density in the world. In a bid to have firm control over long term urban planning, the Singapore government came up with the “Built to Order” (abbreviated BTO) initiative back in 2001. These are new Housing Development Board (HDB) flats tightly controlled by their eligibility and quantity released every year. In more recent years, the modern BTO scheme in Singapore requires a waiting period of 3-4 years, and is generally targeted at young Singaporean couples looking to purchase their first property and set up a family. Nationality and income ceilings are some of the broad filters that determine one’s eligibility for the highly sought after projects.

Our team, comprising of 6 young Singaporeans, all hope to be property owners one day. Many of our peers opt for BTO flats due to their affordability, existence of financial aid from the government, as well as their resale value. However, there often exists a knowledge gap for these young couples during the decision making process and they end up making potentially regretful decisions. We would like to bridge this knowledge gap, and have hence chosen to base our project on creating a recommender system for BTO flats, utilizing the data from recent launches in Tampines, Eunos, Sengkang and Punggol.

Using the techniques imparted to us in lectures, our group first set out to build a sizeable knowledge base via conducting an interview and administering a survey. While building the system, we utilized tools such as Java to scrape real time data from HDB website and transform it into a database, CLIPS to synthesize the rule based reasoning process, and Python to integrate it into an easy to use UI for the everyday user. To add icing on the cake, we even hosted the system on a website so that the everyday user can access it through the click of a link.

Our team had an amazing time working on this project, and hope to share our insights with everyone. Despite a focus on BTO flats, we would recommend it for everybody interested in understanding property market trends for residence or investment purposes. There truly are a wide array of factors behind the decision to invest in a property, and we only wish there was more time to work on the scope and scale of the project.

------

## SECTION 3 : CREDITS / PROJECT CONTRIBUTION



| Official Full Name | Student ID (MTech Applicable) | Work Items (Who Did What)                                    | Email (Optional)                                      |
| ------------------ | ----------------------------- | ------------------------------------------------------------ | ----------------------------------------------------- |
| Mohan Liu          | A0297443U                     | 1. The process of cleaning data, extracting features, training models (such as KNN and SVM), and evaluating models. 2. Develop integrated models and produce soft voting algorithms to integrate the most accurate algorithms, as well as prepare implementation documents. 3. Contribute to the preparation of reports and the design of their layout. 4. Delegate tasks and monitor progress. | [e1351581@u.nus.edu](mailto:e1351581@u.nus.edu)       |
| Yuhao Zhou         | A1234567B                     | 1. Literature review- Web application front-end development 2. Part of web app back-end development 3. Server transmission testing 4. Part of report writing 5.Demo recording | [zhouyuhao24@u.nus.edu](mailto:zhouyuhao24@u.nus.edu) |
| LiXin Zhang        | A0279544N                     | 1. Participate in system design discussions and draw system architecture diagrams 2. Participate in model design and write reports on model training part 3. Participate in report integration 4. Produce PowerPoint and video for system design section | [E1351682@u.nus.edu](mailto:E1351682@u.nus.edu)       |
| Zhiyuan Zhang      | A0297736J                     | 1. project reproduction, project Intro, data collection 2. model training 3.related report writing | [e1351874@u.nus.edu](mailto:e1351874@u.nus.edu)       |
| Wenyu Zhou         | A0294636R                     | 1.web application backend development 2. Writing Report 3.PPT creation | [e1348774@u.nus.edu](mailto:e1348774@u.nus.edu)       |

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