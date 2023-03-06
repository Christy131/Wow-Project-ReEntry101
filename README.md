# Wow-Project-ReEntry101

-Our project is a website to assist the formerly incarcerated to find resources and connect with others when re-entering into society. There will be a resources page with helpful links and information. Also a page where questions can be asked and answered by others.
=======


### 1. Create a Virtual Environment
- To create virtual environment, first you create your virtual environment in the main folder. Run:<br>

```$ python3 -m venv venv```


### 2. Run the Virtual Environment
- Run the following command:
    - For Windows:<br>
        ```venv/Scripts/activate```
    - For Mac:<br>
        ```source venv/bin/activate```

     -Your virtaul environment should be running in your terminal in 'venv' marker`<br>

    -To deactivate virtual enviroment:
       ```source venv/bin/deactivate```

### 3. Run Bootstrap
-Run the following commands in termminal:<br>
    ```pip3 install importlib-metadata```
    ```pip install django-bootstrap-v5```
    ```pip install django-bootstrap```

### 4. Install the requirements
 - In order for the program to run we need to make sure we have the required libraries to run the program, programs change and update all the time, by running the following command you will install the proper ones to run this program. <br>
    ```pip install -r requirements.txt```

### 5. How to run Django App
- Run your virtual environment <br>
```python3 manage.py runserver```

=======

## How program looks
In order to run the program, please in your **internet server** type: http://localhost:8000. The opening page looks like the following page:
![Homepage](./images/Screenshot%202023-01-12%20at%208.21.33%20PM.png)

From the Home page you can  you the Navigation Bar to navigate to the other pages in the site:
![Navigation](./images/nav%20bar.tiff)

If you you click on Send a Kite it will take you to the questions page. From here you can view all the questions that have been posted or post a question of your own.
![Questions](./images/Screenshot%202023-01-12%20at%208.43.05%20PM.png)
You can add a question by typing it in the Question field and clicking add:
![Post_Question](./images/Screenshot%202023-01-12%20at%208.46.33%20PM.png)
If you want to view a specfic question and comment or view the comments for that question you click the link for that question and it will take you to the comments page:
[!Comment_Page](./images/Screenshot%202023-01-12%20at%208.52.58%20PM.png)
From here you can Tag the question (like label):
[!Tag](./images/Screenshot%202023-01-12%20at%208.59.05%20PM.png)
You can also add a comment:
[!Comment](./images/Screenshot%202023-01-12%20at%208.59.34%20PM.png)
Or you can update or delete an exsisting comment:
[!updateDelete](./images/Screenshot%202023-01-12%20at%209.03.55%20PM.png)
If you update it will bring you to another page where you can update your comment:
[!update](./images/Screenshot%202023-01-12%20at%209.05.32%20PM.png)
Once you have successfully updated you will see a page letting you know it has updated and gives you the option to navigate back to home:
[Successful](./images/Screenshot%202023-01-12%20at%209.12.16%20PM.png)

From the Homepage you can also click on the resources page in the Navigation Bar and it will take you to the resources page:
[Resources](./images/Screenshot%202023-01-12%20at%209.15.00%20PM.png)

## Roadblocks we had along the way
-Redirecting back to home page
-Getting the Update fuction to work properly
-The many to many realtionship

## We plan on adding
-A search fuction using the question tags





# Group Members are : 
 Erick Nava: https://github.com/ErickNavaP <br>
 Christy Hayter: https://github.com/Christy131 <br>
 Mikayla Munn: https://github.com/MikaylaMunn
### Documentation
- https://code.visualstudio.com/docs/python/tutorial-django

- https://py-vscode.readthedocs.io/en/latest/files/venv.html



