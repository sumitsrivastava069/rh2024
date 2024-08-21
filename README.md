# Hello World App with Streamlit and FastAPI

This project demonstrates a simple Hello World application using Streamlit for the frontend and FastAPI for the backend, containerized with Docker Compose.

## Project Structure
```
root/ 
── backend/  
    ── app/  
        ── init.py 
            └── main.py  
    ── Dockerfile 
    └── requirements.txt 
── frontend/  
    ── Dockerfile     
    ── app.py 
    └── requirements.txt 
── docker-compose.yml 
── README.md
```

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. Clone this repository:
git clone https://github.com/yourusername/hello-world-app.git cd hello-world-app


2. Build and run the containers:
docker-compose up --build


3. Access the application:
- Frontend (Streamlit): http://localhost:8501
- Backend (FastAPI): http://localhost:80

## Usage

1. Open the Streamlit frontend in your web browser.
2. Click the "Get Greeting" button to fetch a greeting from the FastAPI backend.

## Components

### Backend (FastAPI)

- Located in the `backend/` directory
- Provides a simple API endpoint that returns a greeting
- Runs on port 80 inside the container

### Frontend (Streamlit)

- Located in the `frontend/` directory
- Provides a user interface with a button to fetch the greeting from the backend
- Runs on port 8501

## Docker Configuration

The project uses Docker Compose to manage two services:

1. `backend`: FastAPI application
2. `frontend`: Streamlit application

The `docker-compose.yml` file in the root directory defines these services and their configurations.

## Development

To modify the application:

1. Backend: Edit `backend/app/main.py`
2. Frontend: Edit `frontend/app.py`

After making changes, rebuild and restart the containers:

docker-compose up --build


## License

[MIT License](https://opensource.org/licenses/MIT)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
