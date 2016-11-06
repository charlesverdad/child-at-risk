
#DocuMe

This project is an attempt from scratch to solve the [child-at-risk challenge](https://indigitous.org/hack/challenges/childatrisk).

This is a solution from one of the two child-at-risk teams from Manila during #Hack 2016 event.

You may read our 3-min pitch script in `pitch.txt`. Our deck can be found [here](https://docs.google.com/presentation/d/1VPLmvjHi8JovfF9gjZs4y8sWLChc173QgEfq0Aqkzs0/edit?usp=sharinge)

#Setup

###Pre-requisites
1. Git
2. Python 2.7.x
3. pip

###Setup
1. Clone The repo. From the terminal/command line:
`git clone https://github.com/zine2hamster/child-at-risk.git`
(You may want to fork the project in github and clone from your repo instead)
2. Install requirements. Navigate to folder and run:
`pip install -r requirements.txt`
or
`python -m pip install -r requirements.txt`
3. Run the server using:
`python manage.py runserver`

#Progress
There is still very little progress for this. We started porting some database models into the backend but it turns out there's still a lot of normalization and designing to be done.

For the frontend, it is currently implemented in the `interface_html` branch. Switch to it using git and then run the server to view it. The frontend was just implemented from an already existing template so a lot of things still need to be delted. It currently only contains the children grid and profile.