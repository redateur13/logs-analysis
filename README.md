# Logs Analysis 
 **by ٌReda Zerrougui**


 ## Project  Description:

This is the third project for the Udacity Full Stack Nanodegree Program called "Logs Analysis".


### The Task
You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.
The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.
The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

The Task is to create a reporting tool that prints out reports (in plain text) based on the data in the database.
This reporting tool is a Python program using the psycopg2 module to connect to the database (newsdata.sql)



 ## Project contents

Within the download you'll find the following files:

```
logs-analysis.zip/
│
├── logs-analysis.py
│
├── report.txt
│   
└── README.md
```
## Requirements

* [VirtualBox](https://www.virtualbox.org/)
* [Vagrant](https://www.vagrantup.com/)
* [Python3](https://www.python.org/)
* [psycopg2](http://initd.org/psycopg/docs/install.html) `pip3 install psycopg2`
* [Bash terminal(for windows machine)](https://git-scm.com/downloads)

## Installation


1. Install Python3 , VirtualBox and Vagrant


2. Clone or download the Vagrant VM configuration file from [fullstack-nanodegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm)

3. Clone Or download this repository to your desktop Paste `log-analyser.py` from this project into the vagrant/ sub-directory

4. Download the newsdata [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) Unzip the file and put the file newsdata.sql into vagrant diretory.

## Steps to run this project

1. Open terminal and go to the folder where you saved the fullstack repository then : 
`cd vagrant`.

2. Launch Vagrant to set up the virtual machine and then log into the virtual machine.:
`vagrant up`
`vagrant ssh`

3. move to root of repository in vagrant :
`cd /vagrant`

4. Set up the database then load and connect to the database:
`psql -d news -f newsdata.sql`

5. Finally run `python3 logs-analysis.py` to see the query results.

## The expected program output is as the following :

1.What are the most popular three articles of all time?

* Candidate is jerk, alleges rival - 338647 views

* Bears love berries, alleges bear - 253801 views

* Bad things gone, say good people - 170098 views



2.Who are the most popular article authors of all time?

* Ursula La Multa - 507594 views
* Rudolf von Treppenwitz - 423457 views

* Anonymous Contributor - 170098 views

* Markoff Chaney - 84557 views



3.On which days did more than 1% of requests lead to errors?

* July 17, 2016 - 2.26% errors


 ## Licence

The MIT License ([MIT](https://choosealicense.com/licenses/mit/#))
Copyright (c) [2018] [Reda Zerrougui]