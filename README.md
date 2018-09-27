## Community Incident Management Console

This project is for the Call For Code Contest

- WILDFIRES are a global emergency and when they affect housing and industry, the firefighter system can collapse quickly. In recent years we have gone from fires of thousands of hectares to tens of thousands, and especially we have begun to see fires burning beyond 5 km/h in a sustained way. Fire extinguishing capacity does not exceed 1.2 km/h.  In Europe between 2017 and 2018, forest fires have caused more civil mortality than the whole terrorist problem.
Extinction systems need to focus on the fire strategy but often most of the resources are lost defending people and assets. Self-protection becomes a priority to ensure that the emergency system can maintain the response to the source of the problem, the fire.

- Self-protection means being able to guarantee the safety of people in a fire environment without losing resources assuming the responsibility to execute it. Technology is needed to be able to evaluate and guide evacuations in a dynamic way. Especially, we need IT systems to advise about the evacuation conditions versus conditions of confinement in real time.
Emergency services have been operating so far with a culture of values based on the priorities of lives, material goods and the environment. We need to add now a culture of tactical value where first it manages the value of no collapse to be able to guarantee that we always have capacity to answer. In this step, self-protection and guidance advice is key.
Let’s save our house, let’s save the world with a solution called Community Incident Management Console (CIMC). This tool will make it easier for the communities:

    * Identify the key points to protect their houses
    * Measure the risk of fire and fire load
    * In case of fire, calculate if the house is in the hot area
    *	Help to decide to evacuate or confine  and the best house to confine
    *	Count the people on the hot area

- How CIMC works – Main capabilities:

    1. Prevention with fire load indicators and self-protection recommendations by house
    2. Early Detection with fire-detection alerts
    3. Making decision advice recollecting information on real time from Google Maps to calculate the time to arrive to a secure area and from Twitter to calculate the sentiment in the evacuation road
    4. Fire management to provide number of people in the hot area and searching the most valuable data to improve forest fire-fighting strategies.

- Technologies – This solution uses:

    1. IBM Watson Studio to create and manage cognitive models to gather insight of data
    2. IBM Watson Machine Learning to train, deploy and publish cognitive models
    3. IBM Cloud Object Storage to store data sets, trained cognitive models and training results
    4. Apache Spark service to execute Machine Learning workload
    5. Db2 Warehouse on Cloud to store the feedback data for batch predictions
    6. SQL Database to store the data
    7. Natural Language processing to analyze social network inputs.
    8. Google Maps Api to get information about the evacuation route


![schema](doc_images/Schema.jpg)

You can find all documentation about this project in the directory [all_documents](all_documents)



### Table of Contents
* [Summary](#summary)
* [Requirements](#requirements)
* [Schema](#schema)
* [Environment Configuration](#configuration)
* [Database Configuration](#configuration_database)
* [Watson ML Services Configuration](#configuration_watson)
* [Natural Language Processing Configuration](#configuration_language)
* [Weather Channel Configuration](#configuration_weather)
* [Google Maps Configuration](#configuration_maps)
* [Run](#run)
* [Debug](#debug)

<a name="summary"></a>
# Summary

The CIMC solution is based on two web applications:

* https://cimc.eu-gb.mybluemix.net
     - User Community Incident Management
     - Oriented to the users of the community in order to introduce the features of their houses and get information about evacuation recommendations, fire risk, etc.


*	https://cimc.eu-gb.mybluemix.net/cimc
     - Community Incident Management Console
     - Oriented to give information to the community about the fire load and fire risk of the different houses in a community

The application was coded in python using the flask framework.

In order to create the app we used the ibm cloud templates in the cloud foundry section.

It was respected the structure of the project as created by ibm cloud but all the logic and presentation parts were modified.


The logic part is in the directory:  `\cimc\server\routes`


This part is referred to all the code needed in order to creates the different routes of the web applications and to give them all the logic

The presentation part is in the directory: `\cimc\public`

For the presentation part was used html, flask, css and javascript

There’s a database procedures and tables made to simplify the code of the app

<a name="requirements"></a>
# Requirements
## Local Development Tools Setup (optional)

- If you don't already have it, install [Python](https://www.python.org/downloads/)

## IBM Cloud development tools setup (optional)

1. Install [Docker](http://docker.io) on your machine.
    * Optional: Install [IBM Cloud Developer Tools](https://github.com/IBM-Cloud/ibm-cloud-developer-tools) to build, run, and deploy using IDT
```bash
# Install needed dependencies:
idt install
# Build the docker image for your app:
idt build
# Run the app locally through docker:
idt run
# Deploy your app to IBM Cloud using Cloud Foundry:
idt deploy
# Deploy your app to IBM Cloud using Kubernetes:
idt deploy --target container
```
2. Install the [IBM Cloud CLI](https://console.ng.bluemix.net/docs/cli/index.html)
3. Install the plugin with: `bx plugin install dev -r bluemix`


<a name="configuration"></a>
# Configuration

The project contains IBM Cloud specific files that are used to deploy the application as part of an IBM Cloud DevOps flow. The `.bluemix` directory contains files used to define the IBM Cloud toolchain and pipeline for your application. The `manifest.yml` file specifies the name of your application in IBM Cloud, the timeout value during deployment, and which services to bind to.

Credentials are either taken from the VCAP_SERVICES environment variable if in IBM Cloud, or from a config file if running locally.

<a name='configuration_database'></a>
# Database Configuration

You can use the database you want for the project, we recommend you to use the Compose for MySQL service in IBM Cloud.

In case you want to create the database in IBM Cloud, you have to follow the next steps:

1. Select from the Catalog the Compose MySQL component

![database1](doc_images/database1.jpg)

2. Create the Database

![database2](doc_images/database2.jpg)

3. Create the credentials

![database3](doc_images/database3.jpg)

4. Copy the credentials

![database3](doc_images/database4.jpg)

5. Introduce the credentials in the file [configbbdd.py](server/routes/configbbdd.py)

Here you have an example:

`config = {
    'user': 'admin',
    'password': 'OQTFVYYAEKIXATFF',
    'host': 'sl-eu-lon-2-portal.9.dblayer.com',
    'port': 28398,
    'database': 'name_database',
}`

5. In the database you created run the script [database.sql](database/database.sql) using a graphical tool for working with MySQL servers and databases (for example: MySQL Workbench)


<a name='configuration_watson'></a>
# Watson ML Services Configuration

As part of the CIMC solution, the application calculates several risk factors that helps to reinforce the idea of self-awareness and are intended to be used for assessment as an aid to decision making. This section describes how to setup cognitive services using IBM Watson in IBM Cloud: Predict Fire Risk based on home and surroundings configuration, on Weather Channel data and Fire Load with Watson Studio Machine Learning

On the basis of the provided data-sets, included in the solution as examples, Machine Learning service on IBM Cloud can be trained a model, - supervised machine learning- and be used for predicting either
* a real number – regression problem type- : Fire Risk based on Home and Surroundings Configuration and Fire Load,
* or a category - multiclass classification problem type -: Fire Risk based on Weather Channel data.

## Flow

* Use Watson Studio to add data assets and services (Watson Machine Learning instance and Apache Spark instance).
* Create the Machine Learning Model in Watson Machine Learning.
* Deploy Model as a Web Service.
* Gather credentials of your Watson Machine Learning Service and data from your Model Deployment.
* Call the Watson ML scoring endpoint (REST API) to make predictions from application

## Included components

* Watson Studio
* Machine Learning
* Apache Spark

## Prerequisites
* Download the files in the [datasets](datasets/) directory in CSV format.

## Steps

### A. Create Watson Studio services with IBM Cloud
* On Watson Studio choose New project and pick Data Science.
* Name the project and select your object storage.
* Choose + Add to project -> Data asset and add the data you downloaded in Prerequisites.
* Under the Settings tab -> Associated Services choose + Add service -> Watson and select Machine Learning. Either choose an Existing ML Service or create a New one.
* Under the Settings tab -> Associated Services choose + Add service -> Spark. Either choose an Existing Spark Service or create a New one.
* Under the Assets tab -> Models choose + New Watson Machine Learning model. Pick a name, the default Select model type of Model builder, and Automatic for "Prepare my data...".
* For Select Data choose.csv file you added. When finished click Next.
* For Select a Technique -> Column value to predict (Label Col) choose value to be predicted (last column in all files)
* For Feature columns choose the features: (rest of the columns, except HOME_ID)
* For a Technique choose Linear Regression or Multiclass Classification, depending on the type of problem, and Click Next.
* The model will train, and then Save the model.
* Once you've created the model, go to Deployments and click +add Deployment. Name it, keep the default Web service, and click Save. Leave this page open for the next step...

### B. Get the credentials
* If you haven't left it open from the previous step, from the Watson Studio project page, under the Assets tab, double click the Watson Machine Learning model you created earlier. Go to the Deployments tab and double click to open it. Copy and paste the Deployment ID and Model ID values
* Go to the Implementation tab and copy the Scoring End-point at the top. You will use this as SCORING_URL in either the IBM Cloud Runtime Environment Variable.
* On your Watson Studio project page, got to the Services tab on the top menu bar, and navigate to the Watson Machine Learning service you created earlier. Double-click the service, go to Service Credentials -> View Credentials.

### C. Include the new credentials in the project

Edit the file [credentials_cimc](server/routes/credentials_cimc.py) and modify all the credentials (name, password, urls and call). The code is commented to oriented you.

Here you have examples for the credentials you have to modify:

* Credentias to calculate the fire probability based on house features

`homerisk_credentials={
"url": "https://eu-gb.ml.cloud.ibm.com",
"username": "e4d0dd99-89dj-4051-8835-9de369cd6462",
"password": "014b669d-395e-4b86-8a48-00123ae8e32c",
"call": 'https://eu-gb.ml.cloud.ibm.com/v3/wml_instances/e4d0dd99-89dj-4051-8835-9de369cd6462/deployments/4f45d47d-0276-43ae-8805-dcc91bbd0cda/online'
}`

* Credentials for fire load service created in Watson

`fireload_credentials={
"url": "https://eu-gb.ml.cloud.ibm.com",
"username": "e4d0dd99-89dj-4051-8835-9de369cd6462",
"password": "014b669d-395e-4b86-8a48-00123ae8e32c",
"call": "https://eu-gb.ml.cloud.ibm.com/v3/wml_instances/aed51460-2eac-4edc-91b3-c8b3a238febb/deployments/32e50cd2-4f52-4be2-8d8a-a1f5cdecbed7/online"
}`

* Credentials to calculate the fire probability based on weather parameters

`fireprobability_credentials={
"url": "https://eu-gb.ml.cloud.ibm.com",
"username": "e4d0dd99-89dj-4051-8835-9de369cd6462",
"password": "014b669d-395e-4b86-8a48-00123ae8e32c",
"call": 'https://eu-gb.ml.cloud.ibm.com/v3/wml_instances/aed51460-2eac-4edc-91b3-c8b3a238febb/deployments/9cfae045-233d-44af-864c-e13dc9877e01/online'
}`


<a name='configuration_language'></a>
# Natural Language Processing Configuration

1. Select from the Catalog the service

![language1](doc_images/language1.jpg)

2. Create the Service

![language2](doc_images/language2.jpg)

3. Copy the credentials

![language3](doc_images/language3.jpg)

4. Introduce the credentials in the file [credentials_cimc](server/routes/credentials_cimc.py)

Here you have an example:

`natural_language_understanding = NaturalLanguageUnderstandingV1(
    username='3f619c43-9aec-4817-a67b-2d44f7db2622',
    password='6uXcMzAXtEov',
    version='2018-03-19')`


<a name="configuration_weather"></a>
# Weather Channel Configuration

1. Select from the Catalog the service

![weather1](doc_images/weather1.jpg)

2. Create the Service

![weather2](doc_images/weather2.jpg)

3. Create the credentials

![weather3](doc_images/weather3.jpg)

![weather3](doc_images/weather4.jpg)

3. Copy the credentials

![weather4](doc_images/weather5.jpg)

4. Introduce the credentials in the file [credentials_cimc](server/routes/credentials_cimc.py)

Here you have an example:

`weather_credentials={
"username": "8b355826-006c-41ac-83b7-2a6c29b03816",
"password": "80ufr7kH9C"
}`

<a name="configuration_maps"></a>
# Google Maps Configuration
It's important you introduce your google maps credentials in order to integrate with this service.

You'll have to create a directions api in the google maps for developers and get the credential of the service.

1. Go to the [Google Cloud Platform Console](https://console.cloud.google.com/project/_/apiui/apis/enabled)
2. Click the Select a project button, then select the same project you set up for the Maps JavaScript API and click Open.
3. From the list of APIs on the Dashboard, look for Directions API.
4. If you see the API in the list, you’re all set. If the API is not listed, enable it:
5. At the top of the page, select ENABLE API to display the Library tab. Alternatively, from the left side menu, select Library.
6. Search for Directions API, then select it from the results list.
7. Select ENABLE. When the process finishes, Directions API appears in the list of APIs on the Dashboard.
8. Create a credential for this service in case you don't have
9. Copy the credential key

10. Edit the file [credentials_cimc](server/routes/credentials_cimc.py) and modify the key_googlemaps credential, for example:

`key_googlemaps='AIzaDke8ywEB4bGOgD8UAsAD93v9BCQ4PYErSyU'`

11. Edit the file [map_google.html](public/map_google.html) and change the line src introducing your key in googlemaps in the URL, for example:

`src="https://maps.googleapis.com/maps/api/js?key=AIzaDke8ywEB4bGOgD8UAsAD93v9BCQ4PYErSyU&callback=initMap">`


<a name="run"></a>
# Run
## Using IBM Cloud development CLI
The IBM Cloud development plugin makes it easy to compile and run your application if you do not have all of the tools installed on your computer yet. Your application will be compiled with Docker containers. To compile and run your app, run:

```bash
bx dev build
bx dev run
```


## Using your local development environment


Running flask applications has been simplified with a `manage.py` file to avoid dealing with configuring environment variables to run your app.

## Usage
```bash
python manage.py subcommand [ipaddress]
```

## Subcommands
`manage.py` offers a variety of different run commands to match the proper situation:
* `start`: starts a server in a production setting using `gunicorn`.
* `runserver`: starts a native flask development server. This includes backend reloading upon file saves and the Werkzeug stack-trace debugger for diagnosing runtime failures in-browser.
* `livereload`: starts a development server via the `livereload` package. This includes backend reloading as well as dynamic frontend browser reloading. The Werkzeug stack-trace debugger will be disabled, so this is only recommended when working on frontend development.
* `debug`: starts a native flask development server, but with the native reloader/tracer disabled. This leaves the debug port exposed to be attached to an IDE (such as PyCharm's `Attach to Local Process`)

There are also a few utility commands:
* `build`: compiles `.py` files within the project directory into `.pyc` files
* `test`: runs all unit tests inside of the project's `test` directory


## Endpoints

Your application is running at: `http://localhost:3000/` in your browser.

- Health endpoint: `/health`



<a name="debug"></a>
# Debug

## Using IBM Cloud development CLI
To build and debug your app, run:
```bash
bx dev build --debug
bx dev debug
```
## Using your local development environment
There are two different options for debugging a `flask` project:
1. Run `python manage.py runserver` to start a native flask development server. This comes with the Werkzeug stack-trace debugger, which will present runtime failure stack-traces in-browser with the ability to inspect objects at any point in the trace. For more information, see [Werkzeug documentation](http://werkzeug.pocoo.org/).
2. Run `python manage.py debug` to run a flask development server with debug exposed, but the native debugger/reloader turned off. This grants access for an IDE to attach itself to the process (i.e. in PyCharm, use `Run` -> `Attach to Local Process`)
