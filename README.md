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
oc new-app command to deploy both the application on openshift.
