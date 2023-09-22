# AI Piping Hiring

Collection of take home assignments for candidates 

- [Backend L2](backend-L2.md) 
# FastAPI-React-Test-task

 Create a simple FastAPI application that serves an endpoint to recommend three things to do in a given country during a specific season by consulting the OpenAI API and implemented frontend using the React.

# Stack
- FastAPI
- Python3.9
- Node-14
- React

## Table of Contents
  - [Prerequisites](#prerequisites)
  - [Configuration](#configuration)
  - [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

### Here is the structure of the project in which there are two main directories backend and frontend, 
1. Backend folder contain all the backend files and modules - api, tests, utils
a. api - To keep API data like routes, views.
b. tests - For the test cases for the API.
c. Utils - To keep common functions
2. Frontend - I used redux for managing the states for the API, contaning the components, redux, Utils folders/ directories
a. Public - Keep the public things
b. Components - To keep logic of the components like app, home
c. Redux - To store action types and serivces, reducer
```
.
├── backend
│   ├── api
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── views.py
│   ├── Dockerfile
│   ├── __init__.py
│   ├── main.py
│   ├── requirements.txt
│   ├── tests
│   │   ├── __init__.py
│   │   └── test_views.py
│   └── utils
│       ├── __init__.py
│       └── utils.py
├── backend-L2.md
├── docker-compose.yml
├── frontend
│   ├── Dockerfile
│   ├── package.json
│   ├── public
│   │   ├── favicon.ico
│   │   ├── index.html
│   │   ├── logo192.png
│   │   ├── logo512.png
│   │   ├── manifest.json
│   │   └── robots.txt
│   ├── README.md
│   └── src
│       ├── components
│       │   └── views
│       │       ├── app
│       │       │   ├── App.css
│       │       │   ├── App.js
│       │       │   └── App.test.js
│       │       └── home
│       │           ├── index.jsx
│       │           ├── travelInput.jsx
│       │           └── travelOutput.jsx
│       ├── Global.js
│       ├── index.css
│       ├── index.js
│       ├── logo.svg
│       ├── redux
│       │   ├── actions
│       │   │   ├── ActionTypes.js
│       │   │   └── TravelAction.js
│       │   └── reducers
│       │       ├── index.js
│       │       └── TravelReducer.js
│       ├── reportWebVitals.js
│       ├── setupTests.js
│       ├── store.js
│       └── Utils
│           └── Utils.js
└── README.md
```

### Prerequisites

List the software and tools that need to be installed before running the Docker Compose file. Provide links to installation instructions if necessary.

- Docker: [Installation Guide](https://docs.docker.com/get-docker/)
- Docker Compose: [Installation Guide](https://docs.docker.com/compose/install/)

### Configuration

Contains the ChatGPT environment variables that override the variables set in the /etc/environment file.

Here is a sample `.env` file with key-value pairs:

```plaintext
open_ai_key=your_open_ai_key
```

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/PoojaGupta0/FastAPI-React-Test-task#fastapi-react-test-task
   ```

2. Checkout to this below branch:

   ```bash
   git checkout main
   ```

3. Build Docker images for the services defined in your Docker Compose configuration:

   ```bash
   sudo docker-compose build
   ```

4. Start docker containers:

   ```bash
   sudo docker-compose up -d
   ```

# Additional Info

Frontend is running on `http://localhost:3000/`

for checking backend API - `http://localhost:8000/docs`
   

