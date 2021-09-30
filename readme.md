# MelonRessie

## Table of Contents

*   [Description](#description)
*   [Tech Stack](#tech-stack)
*   [Features](#features)
*   [Running](#running)
*   [About the Developer](#developer)

## <a name="description"></a>Description
**MelonRessie** is a simple web app that allows users to schedule and keep track of their Melon Tasting reservations 🙂 🍉

## <a name="tech-stack"></a>Tech Stack
__Front End:__ Jinja2, HTML5, CSS <br/>
__Back End:__ Python, Flask, PostgreSQL, SQLAlchemy <br/>

## <a name="features"></a>Features

 -Schedule for a melon tasting
 -Track existing reservations
    ![User-Page](/static/img/user_page.png)


## <a name="setup"></a>Setup/Installation

To run MelonRessie on your local machine:

Clone repository:
```
$ git clone https://github.com/lisamqy/MelonRessie
```

Create and activate a virtual environment:
```
$ virtualenv env
$ source env/bin/activate
```

Install the dependencies:
```
$ pip3 install -r requirements.txt
```

```
$ createdb melon
$ python3 model.py
```

Run the app:

```
$ python3 server.py
```

You can now navigate to 'localhost:5000/' 

## <a name="developer"></a>About the Developer

Lisa Ma is a new software engineer excited to put her skills to the test and just learn and build stuff!
Learn more on her <a href="https://www.linkedin.com/in/lisa-ma77/">LinkedIn.</a>