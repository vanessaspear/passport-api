Passport
------
<img width="610" alt="Screenshot 2023-03-23 at 4 57 22 PM" src="https://user-images.githubusercontent.com/112430942/227373858-c8c6765b-64ec-4f38-a00f-0b6ba0396d93.png">

### Application Overview

Do you love to travel? Passport is meant for you! Passport is a full stack application designed for people who want to plan and document their trips.  Whether you're headed home for the holidays or headed to Munich for Oktoberfest, Passport is your partner in travel. 

### Features
- Users can create new trips and add itineraries, a packing list, and trip notes 
- Users can see an interactive map of all the places they visited during their travels
- Users can add Passport "stamps" (photos, journal entries, products) from their trips for lasting memories 
- Users can switch viewports without impacting their app experience through the use of responsive design
  
### Technologies Used

#### Backend Technologies

<img alt="Python" src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"><img alt="Django" src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green"><img alt="Django REST" src="https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white"><img alt="SQLite" src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white"><img alt="Leaflet" src="https://img.shields.io/badge/Leaflet-199900?style=for-the-badge&logo=Leaflet&logoColor=white"><img alt="GIT" src="https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white"><img alt="Github" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"><img alt="VScode" src="https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white">

#### Frontend Technologies

<img alt="Javascript" src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E"><img alt="React" src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB"><img alt="HTML5" src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"><img alt="CSS" src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"><img alt="Bootstrap" src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white"><img alt="GIT" src="https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white"><img alt="Github" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"><img alt="VScode" src="https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white"><img alt="Miro" src="https://img.shields.io/badge/Miro-F7C922?style=for-the-badge&logo=Miro&logoColor=050036"><img alt="" src="">

In the planning stages, I used DB Diagram to create an entity relationship diagram and Miro to create a wireframe.  Both documents helped with solution design and were referenced throughout my work building out this app.  I also used a Github project board to create issues and manage work.

* [Passport ERD](https://dbdiagram.io/d/6406090c296d97641d85cc8e)

* [Passport Wireframe](https://miro.com/app/board/uXjVPhQbM4U=/?share_link_id=955298799066)

* [Passport Agile Project Board](https://github.com/users/vanessaspear/projects/1/views/1)
            
### Running the Application

**Required dependencies:** 
- Python
- Django
- React + React-DOM
- NPM
- Leaflet
- Bootstrap
- Pillow

Navigate to your workspace directory. 

Run the following command in terminal to setup the server:

```
git clone git@github.com:vanessaspear/passport-api.git
cd passport-api
python manage.py runserver
```

Seed the database: 
- Run the following commands in terminal
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py loaddata users tokens types trips trip_reasons trip_notes stamp_photos reasons packing_list itinerary_categories itineraries categories
```

Run the following command in terminal to setup the client:

```
git clone git@github.com:vanessaspear/passport-client.git
cd passport-client
npm start
```

You should now be able to sign in to the application. 

To demo the app, register as a new user with an email and password or use the below login credentials.
```
username/email: jjones@travel.com
password: globetrotter
```

Author
------

Vanessa Spear 

[<img alt="Github" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white">](https://github.com/vanessaspear)[<img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">](https://www.linkedin.com/in/vanessavspear/)
