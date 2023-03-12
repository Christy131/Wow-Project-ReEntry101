# Wow-Project-ReEntry101

- Our project is a website to assist the formerly incarcerated to find resources and connect with others when re-entering into society. There will be a resources page with helpful links and information. Also a page where questions can be asked and answered by others.

## 1. Create a Virtual Environment

- To create virtual environment, first you create your virtual environment in the main folder. Run:

``` python3 -m venv venv```

## 2. Run the Virtual Environment

- Run the following command:
  - For Windows:
        ```venv/Scripts/activate```
  - For Mac:
        ```source venv/bin/activate```

     -Your virtaul environment should be running in your terminal in 'venv' marker`

    -To deactivate virtual enviroment:
       ```source venv/bin/deactivate```

### 3. Run Bootstrap

-Run the following commands in termminal:
    ```pip3 install importlib-metadata```
    ```pip install django-bootstrap-v5```
    ```pip install django-bootstrap```

### 4. Install the requirements

- In order for the program to run we need to make sure we have the required libraries to run the program, programs change and update all the time, by running the following command you will install the proper ones to run this program.
    ```pip install -r requirements.txt```

### 5. How to run Django App

- Run your virtual environment
```python3 manage.py runserver```

---

## Navigate the app

In order to run the program, please in your **internet server** type: <http://localhost:8000>. This is how the home page looks where one option is to click on the house. If you do click on the house it will take you to the resource page:
![Homepage](./ReEntry101_site/reentry_todo/static/images/screen%20shots%20for%20readme/Middle%20of%20Home%20Page%20-%20Need%20a%20Housing%20Unit.png)

From all pages you can click the Navigation Bar to navigate to the other pages in the site:
![Navigation](./ReEntry101_site/reentry_todo/static/images/screen%20shots%20for%20readme/Top%20of%20Home%20Page%20-%20Welcome%20Back.png)

When you click on the search bar you will be given the option to search ReEntry 101 for potential resources:
![SearchBar](./ReEntry101_site/reentry_todo/static/images/screen%20shots%20for%20readme/SearchBar.png)

If you search for a resource that doesn't exist on the site you will get an error message:
![SearchBarError](./ReEntry101_site/reentry_todo/static/images/screen%20shots%20for%20readme/SearchBar%20Error.png)

If you succesfully search for a resource that does exist, it will take you to that resource:
![SearchBarSuccessfulSearch](./ReEntry101_site/reentry_todo/static/images/screen%20shots%20for%20readme/SearchBAr%20Succesful%20Search.png)

If you you click on Send a Kite it will take you to the questions page. From here you can view all the questions that have been posted or post a question of your own.

![Questions](./ReEntry101_site/reentry_todo/static/images/screen%20shots%20for%20readme/Send%20a%20Kite%20-%20Ask%20Your%20Question.png)

If you want to view a specfic question and comment or view the comments for that question you click the link for that question and it will take you to the comments page:
![Comment_Page](./ReEntry101_site/reentry_todo/static/images/screen%20shots%20for%20readme/Send%20a%20Kite%20-%20View%20Comment.png)

Or you can update or delete an existing comment:
![updateDelete](./ReEntry101_site/reentry_todo/static/images/screen%20shots%20for%20readme/Send%20A%20Kite%20-%20Update%20and%20Delete.png)

If you update it will bring you to another page where you can update your comment and then once you have successfully updated you will see a page letting you know it has updated and gives you the option to navigate back to home:
![update](./ReEntry101_site/reentry_todo/static/images/screen%20shots%20for%20readme/Send%20A%20Kite%20-%20Update.png)

From the Homepage you can also click on the resources page in the Navigation Bar and it will take you to the resources page where you will have the option to choose available resources, for example, resource guide and it will toggle down:
![Resources](./ReEntry101_site/reentry_todo/static/images/screen%20shots%20for%20readme/Resorce%20Page%20-%20Resource%20Guides.png)

When you click the about us page you will read about the creators of ReEntry 101 and you will also see some of our sponsers:
![AboutUs](./ReEntry101_site/reentry_todo/static/images/screen%20shots%20for%20readme/About%20Us.png) 

In the About Us section at the bottom there is the option to contact us, where when submitted, one of will receive an email letting us know that you reached out:
![ContactUs](./ReEntry101_site/reentry_todo/static/images/screen%20shots%20for%20readme/AboutUS-%20Contact%20Us.png)

## Roadblocks we had along the way

-Redirecting back to home page
-Getting the Update fuction to work properly
-The many to many realtionship

## We plan on adding

-A search fuction using the question tags

## Group Members

- [Erick Nava](https://github.com/ErickNavaP)
- [Christy Hayter](https://github.com/Christy131)
- [Mikayla Munn](https://github.com/MikaylaMunn)

## Documentation

- [Django](https://code.visualstudio.com/docs/python/tutorial-django)

- [Venv](https://py-vscode.readthedocs.io/en/latest/files/venv.html)