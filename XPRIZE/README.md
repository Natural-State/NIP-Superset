# XPrize Superset Deployment 

## 1. Docker 

### 1.1 What is Docker? 

Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications. 

### 1.2 Installing Docker Desktop

Docker Desktop is an easy-to-install application for your Mac, Windows or Linux environment that enables you to build and share containerized applications and microservices. 

Why install Docker?

We are installing docker because to run any Docker command on the terminal, such as running an application, it will not be possible without Docker Desktop installed. 

Here is the link to install Docker Desktop: [installation](https://docs.docker.com/desktop/).

Pick the right installation for your local computer or laptop.

Once installed, sign up for an account with Docker Desktop. You can use your personal or work email.

### 1.3 The Natural State Superset Visualization Platform

The Natural State Impact Portal (NIP) Superset repository contains the dashboard visualization platfrom known as [Superset](https://github.com/apache/superset). It is a dashboard for creating Business Intelligence (BI) visualizations. 

To have the NIP Superset in your local machine, open VS Code and in the terminal, type: 

```
git clone https://github.com/Natural-State/NIP-Superset.git

```

This will clone the up-to-date NIP Superset into your local machine.

The branch `3.1.1` will be downloaded by default. 

Create a new branch based on the `dev` branch which is used for active development by running this: 

```
git checkout -b <name-of-your-branch> origin/dev
```

Ensure you are in the right branch by running:

```
git branch

```

Let's say you have named your branch as `xprize` or something, you will instantiate the Superset dashboard using: 

```
docker compose up

```

This should create a list of logs. Besides the logs, a new widget should show up asking you to go to a specific port path in your browser. Otherwise, just go to this port on your browser:

```
localhost:8088
```

or

```
http://127.0.0.1:8088/login/
```

Login using the Azure email provided by your data administrator.

#### Troubleshooting

If unable to login, some additional instructions will be provided by your data administrator. ie. the `env` file might need to be changed to something else. 


## 2. Converting Comma Separated Files (CSVs) to Sqlite Database

### 2.1 What is an Sqlite Database?

SQLite is a lightweight relational database systems favoured for its light, simplicity and no-administration required features.

### 2.2 Convert csv files to sqlite database

Attached to this folder is a python file called `cd_to_db_converter.py`. 

It has two functions:

1. `create_database`

2. `read_table_from_db`


1. `create_database`

The purpose of this function is to convert your csv file(s) to a SQLite database. It only needs three parameters: 

- path to your csv files, 
- desired path to your database and,
- desired name of the database  

The function does the heavy lifting of conversion from csv to sqlite database for you.


















