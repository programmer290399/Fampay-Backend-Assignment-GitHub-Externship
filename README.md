# Fampay-Backend-Assignment-GitHub-Externship

## Problem Statement:
<details>
  <summary>Click to expand!</summary>

### Basic Requirements:

- [x] Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.

- [x] A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.

- [x] It should be scalable and optimized.

### Bonus Points:

- [x] Add support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.

- [ ] Make a dashboard to view the stored videos with filters and sorting options (optional)

### Instructions:
* You are free to choose any search query, for example: official, cricket, football etc. (choose something that has high frequency of video uploads)
* Try and keep your commit messages clean, and leave comments explaining what you are doing wherever it makes sense.
* Also try and use meaningful variable/function names, and maintain indentation and code style.
* Submission should have a README file containing instructions to run the server and test the API.
* Submission should be done on GitHub Externship Portal.


### Reference:
* [YouTube data v3 API](https://developers.google.com/youtube/v3/getting-started)
* [Search API reference](https://developers.google.com/youtube/v3/docs/search/list)
* To fetch the latest videos you need to specify these: ```type=video, order=date, publishedAfter=<SOME_DATE_TIME>```
Without publishedAfter, it will give you cached results which will be too old
</details>


## How it Works

![img](https://github.com/programmer290399/Fampay-Backend-Assignment-GitHub-Externship/raw/docker-branch/images/main-architecture.png)

* When a client requests data from django, using our REST API, we read the DB for latest data and send back a paginated JSON response.
* In the background, in django we have scheduled a periodic task which is send to Redis and Celery can read that task from it.
* Celery goes and asynchronously hits the YouTube Data API to fetch new videos released after the last hit. 
* The response received is stored by celery in the DB. 

## How to Setup:

### Using Docker (Recommended):

```bash
  # Clone the repository
  $ git clone git@github.com:programmer290399/Fampay-Backend-Assignment-GitHub-Externship.git
  $ cd Fampay-Backend-Assignment-GitHub-Externship/
  # Checkout to docker branch
  $ git checkout docker-branch
  # Change permission on entrypoint.sh
  $ chmod  775 Fampay_Backend_Assignment/entrypoint.sh
  # Spin up the container, after adding appropriate API key 
  # Related information in the docker-compose.yml
  $ docker-compose up -d --build
  # The server should be up on port 8000, API usage same as shown below 
  ```

* Incase you have problems running due to ports and stuff already in use, try running the script `docker_fresh_start.sh`, be careful while using it as it will kill and remove all other containers as well and thus might lead to loss of your work.


* You can watch logs of `celery`, `redis` & `celery-beat` by using the following command:
  ```bash
  $ docker-compose logs -f '<service name here>'
  ```
### Using Source:


  ```bash
  # Clone the repository
  $ git clone git@github.com:programmer290399/Fampay-Backend-Assignment-GitHub-Externship.git
  $ cd Fampay-Backend-Assignment-GitHub-Externship/
  # Create a virtual env and install python dependencies
  $ python3.7 -m venv .venv 
  $ . .venv/bin/activate
  $ pip install -r requirements.txt 
  # Install Redis:
  # ---------------------------------------------------------
  # Run the next command only if using Debain based Distro: 
  $ sudo apt install redis-server 
  # Run the next command only if using Arch based Distro 
  $ sudo pacman -S redis
  # Run this command only if using a Mac
  $ brew install redis
  # ---------------------------------------------------------
  # Start redis server
  $ redis-server
  # In a new terminal tab/window navigate to the same path as before and
  # run the django server using the same env
  $ cd Fampay_Backend_Assignment/
  # BEFORE RUNNING THE FOLLOWING TWO COMMANDS
  # Place the .env file on the same level as manage.py
  # With the following syntax:
  # NUM_KEYS=<Number of keys you want to use>
  # API_KEY_1=<Your First API Key>
  # API_KEY_2=<Your Second API Key>
  # Ans so on, add all your keys in it.
  $ python manage.py migrate
  $ python manage.py runserver
  # Similarly in the same working directory as above run the following 
  # two commands in separate terminal/tabs
  $ celery -A Fampay_Backend_Assignment worker --loglevel=info
  $ celery -A Fampay_Backend_Assignment beat -l info
  ```
* Visit http://localhost:8000/videos/?page=1 in your browser to see the API response.
* You can configure the following things as per requirement from [settings.py](Fampay_Backend_Assignment/Fampay_Backend_Assignment/settings.py):
  - **`SEARCH_QUERY`:** This can be used to alter the search query
  - **`MAX_RESULTS`:** The max number of results you wish to fetch from youtube
  - **`CHECK_INTV`:** Interval at which we poll the YouTube API in minutes
  - **`REST_FRAMEWORK.PAGE_SIZE`:** The size of the paginated response 

