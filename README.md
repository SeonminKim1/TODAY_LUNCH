![image](https://user-images.githubusercontent.com/87006912/173308040-4a80baf8-b228-47a6-a4e9-46b026fdc164.png)
## ๐ ์ค๋์ ์ ์ฌ
- ํ๋ฃจ ์ผ์์ธ๋ผ, โ์ค๋ ์ ์ฌ ๋ญ ๋จน์ง?โ ๊ณ ๋ฏผํด ๋ณธ ์ฌ๋๋ค์ด ๊ณ ๋ฏผํ๋ ์ฌ๋๋ค์ ์ํด ๋ง๋ค์ด ๋ณด๋ ์น ์๋น์ค

## ๐ Introduction
- **์ฃผ์ ** : ์ ์ฌ ์ถ์ฒ ์น ์๋น์ค (for ์ง๋ฉ, ์ผ๋ฐ์ธ)
- **๊ธฐ๊ฐ** : 2022.06.03 (๊ธ) ~ 2022.06.13 (์)
- **Team** : ๊น์ ๋ฏผ ([Github](https://github.com/SeonminKim1)), ๊น๋ฏผ๊ธฐ ([Github](https://github.com/kmingky)), ๋ฐ์ฌํ ([Github](https://github.com/Aeius)), ํฉ์ ํ ([Github](https://github.com/hwangshinhye)) 

<hr>

## ๐ Project-Rules
#### Schedule Management : [Git Project Link](https://github.com/SeonminKim1/TODAY_LUNCH/projects/1), [๊ฐํธ์ฐจํธ Link](https://docs.google.com/spreadsheets/d/1_1Sx46dnKnI8_DLJQzAASMSr7u525RFjm2Iat0beU14/edit#gid=1212318893)
#### API Design : [Notion-link](https://www.notion.so/1b59a28804b9451d97d7b0145dc658f3?v=fb5a1b50406d43699b83a1d38aa2986c)
#### Branch Info
- main : LocalHost ์คํ branch
- publish : EC2 Hosting ์คํ Branch

#### Figma Mock-up
![image](https://user-images.githubusercontent.com/87006912/173303730-37dea9f0-4aad-4fa4-ac9d-248fc19766e1.png)

#### DB Modeling   
![image](https://user-images.githubusercontent.com/33525798/173334447-cbf70e34-82a3-47af-844a-0c6e4804c394.png)

<hr>

## ๐ Development-Stack
#### ๐ Frameworks, Libraries (ML) 
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![jQuery](https://img.shields.io/badge/jquery-%230769AD.svg?style=for-the-badge&logo=jquery&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white) 

#### ๐พ Databases, Hosting/Storage
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)      

#### ๐ Languages
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)    

#### ๐ป IDEs/Editors
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)    

<hr>

## ๐ Getting-Started

``` Run
$ pip install -r requirements.txt
$ python recommandtion/crawling.py  # Crawing Data
$ python auto_publish.py            # Data Migrations & Run Server
$ python auto_db_insert.py          # Insert Restaurant DB 

# publish branch version 
$ sh auto_delete_db.sh
$ sh auto_publish.sh
```

#### Crawling 
- ์๊ธฐ์ ํํ์ด์ง ์นดํ๊ณ ๋ฆฌ๋ณ ์์์  ๋ฐ์ดํฐ ํฌ๋กค๋ง (python crawling.py)
- ์์ฑ๋ restaurant_OO.csv ํ์ผ (OO ๋ถ๋ถ์ ์นดํ๊ณ ๋ฆฌ, 50๊ฐ์ ์์์  ์ ๋ณด ์ ์ฅ)๋ค ํฉ์ณ์ ์ต์ข restaurant.csv ์์ฑ

#### DB Migration & DB 
- (main Branch) ```python auto_publish.py``` ํ์ฌ migrations, migrate ์งํ
- (main Branch) ```python auto_db_insert.py``` ํ์ฌ ํฌ๋กค๋ง ๋ฐ์ดํฐ(restaurant.csv)๋ค DB์ ์ ์ฅ
- (publish branch) ```sh auto_delete_db.sh``` ํ์ฌ migrations, sqlite3 db ์ด๊ธฐํ
- (publish branch) ```sh auto_publish.sh``` ํ์ฌ DB Migrations ๋ฐ ํฌ๋กค๋ง ๋ฐ์ดํฐ(restaurant.csv) DB ์ ์ฅ

<hr>

## ๐ Structure
```
โโtoday_lunch
โโโ today_lunch         // project
โ   โโโ urls.py       
โ   โโโ settings.py     // setting
โ   โโโ ...
โโโ users               // app
โ   โโโ models.py       // DB Model - User
โ   โโโ views.py
โ   โโโ ...
โโโ restaurant          // app
โ   โโโ models.py       // DB Model - Restaurant, Category
โ   โโโ views.py
โ   โโโ ...
โโโ star                // app
โ   โโโ models.py       // DB Model - Star 
โ   โโโ views.py
โ   โโโ ...
โโโ mypage              // app
โ   โโโ models.py       // DB Model - Diary
โ   โโโ views.py
โ   โโโ ...
โโโ recommandation
โ   โโโ crawling.py     // Crawling
โ   โโโ db_uploader.py  // Restaurant data insert
โ   โโโ recommand.py    // User Based Recommandation
โ   โโโ restaurant.csv  // restaurant data
โโโ static 
โ   โโโ css/            // css
โ   โโโ img/            // images    
โโโ templates
โ   โโโ init/           // Init Page  
โ   โโโ users/          // Join, Login Page  
โ   โโโ main/           // Main Page  
โ   โโโ mypage/         // Profile Page  
โ   โโโ ...
โ
โโโ db.sqlite3          // DB  
โโโ manage.py           // ๋ฉ์ธ
โโโ auto_db_insert.py   
โโโ auto_publish.py
```

<hr>


## ๐ Development

#### User Page
- ์์ ํ์ด์ง ํ์๊ฐ์, ๋ก๊ทธ์ธ ํ์ด์ง ์ด๋
- ํ์๊ฐ์/๋ก๊ทธ์ธ ๊ธฐ๋ฅ
- ํ์๊ฐ์ vaildation
- ์นด์นด์ค์ง๋ API๋ฅผ ์ด์ฉํ ์ฃผ์ ๊ฒ์ ๊ธฐ๋ฅ

#### Nav Bar
- ํ์ด์ง ์ด๋(ํ, ํ์ ํ์ด์ง, ๋ง์ดํ์ด์ง, ๋ก๊ทธ์์)

#### Scoring Page
- **๋ก๊ทธ์ธ ํ ์ค์ฝ์ด๋ง ํ์ด์ง ์ด๋**
- **๋ก๊ทธ์ธ User ํ์  ์ด๋ ฅ ์๋ ์์์  5๊ฐ ์ถ๋ ฅ**
- **์์์  ๋ง๋ค ๋ณ 1๊ฐ ~ 5๊ฐ ์ ํํด์ ํ์  ๋ถ์ฌ ๋ฐ ์ ์ฅ**
  - '๋ณ์  ์ ์ฅํ๊ธฐ' ํด๋ฆญ ์ ํ์  ๋ถ์ฌํ ์์์ ๋ค๋ง ํ์  ๋ฑ๋ก๋จ
  - 'ํ๊ฐ ๊ทธ๋งํ๊ธฐ' ํด๋ฆญ ์ ๋ฉ์ธ ํ์ด์ง๋ก ์ด๋

#### Aside (Main Page, MyPage)
- **์ฌ์ฉ์ ์ ๋ณด(์ด๋ฆ, ์ฃผ์) ์ถ๋ ฅ**
- **์ถ์ฒ ์ปจํ์ธ  1) ์ค๋์ ์ถ์ฒ**
  - ์ด์  ํ์ ์ด ๊ฐ์ฅ ๋์๋ ์์์  1๊ฐ ์ถ์ฒ

#### Main Page
- **์ถ์ฒ ์ปจํ์ธ  2) '์ฌ์ฉ์๋๊ณผ ๊ฐ์ฅ ์ ์ฌํ OOO๋์ ์ถ์ฒ ์์์ ์๋๋ค!'**
  - User-Baed Filtering์ ์ด์ฉํ ๋์ ๊ฐ์ฅ ๋น์ทํ ์ ์ ์ top 5 ์์์  ์ถ๋ ฅ
  - OOO๋ ํด๋ฆญ ์ ์ ์ฌ๋ ํ์ค๋ฒ ์ถ๋ ฅ
- **์ถ์ฒ ์ปจํ์ธ  3) '์ ์ฌ ๋ญ ๋จน์ง? TOP 5'**
  - ์นดํ๊ณ ๋ฆฌ๋ณ ํ๊ท  ํ์ ์ด ๊ฐ์ฅ ๋์ ์์์  TOP 5 (์ ์ฒด, ํ์, ์ค์, ์ผ์, ์์)
- **๊ฐ ์์์ ๋ค์ '์์ธ๋ณด๊ธฐ'**
  - ๋ค์ด๋ฒ ์ง๋์ ํด๋น ์์์  ๊ฒ์ ๊ฒฐ๊ณผ ์ถ๋ ฅ

#### Mypage
- **์ ์ฌ์ผ์ง ์บ๋ฆฐ๋ ํํ ์ถ๋ ฅ**
- **์ ์ฌ์ผ์ง ๋ฑ๋ก**
  - ๋น ๋ ์ง ํธ๋ฒ ์ '๋ฑ๋ก'๋ฒํผ ์ถ๋ ฅ, ํด๋ฆญ์ ๋ชจ๋ฌ ์ถ๋ ฅ
- **์ ์ฌ์ผ์ง ๋ฑ๋ก ๋ชจ๋ฌ**
  - ์์์  ์ ํ (+ ๊ฒ์ ๊ฐ๋ฅ) 
  - ๋ณ์  ์ ํ (1 ~ 5)
  - ๋ฑ๋ก ๋ด์ฉ ๋ฐํ์ผ๋ก DB Update ๋ฐ ์ถ์ฒ ์๊ณ ๋ฆฌ์ฆ Upgrade
- **์ ์ฌ์ผ์ง ์์ /์ญ์ **
  - ๋ฑ๋ก๋ ์ ์ฌ์ผ์ง ๋ถ๋ถ ํด๋ฆญ์ ๋ชจ๋ฌ ์ฐฝ ์ถ๋ ฅ
  - ์์ /์ญ์  ๋ด์ฉ ๋ฐํ์ผ๋ก DB Update ๋ฐ ์ถ์ฒ ์๊ณ ๋ฆฌ์ฆ Upgrade
  - ์ญ์  ํด๋ฆญ์ ํด๋น ์ ์ฌ์ผ์ง ์ญ์ ๋จ

#### Publish and Storage Mount
- AWS EC2 ์ด์ฉํ ์ธ๋ถ Publish ๋ฐฐํฌ
- S3์ ์ ์  ์ด๋ฏธ์ง ํ์ผ๋ค ๊ด๋ฆฌ ๋ฐ EC2์ Mountํ์ฌ ๊ตฌํ

<hr>

## ๐ ์์ฐ ํ๋ฉด
#### ์ฒซํ๋ฉด, ํ์๊ฐ์, ๋ก๊ทธ์ธ ํ๋ฉด
![image](https://user-images.githubusercontent.com/33525798/173514356-84840d07-2425-4095-b9fa-07d50a19bc0d.png)

#### ํ๊ฐ ํ์ด์ง, ๋ฉ์ธ ํ์ด์ง
![image](https://user-images.githubusercontent.com/33525798/173514477-228b4897-bee0-491e-847c-5720d11a5eb4.png)

#### ๋ง์ดํ์ด์ง (์ ์ฌ์ผ์ง ๋ฑ๋ก, ์์ , ์ญ์ )
![image](https://user-images.githubusercontent.com/33525798/173514527-8e456009-0dcb-4e5d-890a-e476ef4331fb.png)

