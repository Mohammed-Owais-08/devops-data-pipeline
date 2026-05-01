# 🚀 Production-Ready Data Pipeline with DevOps

## 📌 Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline built using Python and deployed with DevOps practices. The pipeline extracts real-time weather data from an API, processes it, and stores it in a database.

The project is containerized using Docker, automated using CI/CD pipelines, and deployed on AWS EC2.

---

## 🛠️ Tech Stack

* Python
* Docker
* GitHub Actions (CI/CD)
* AWS EC2
* REST APIs
* SQLite
* Linux

---

## ⚙️ Features

* Real-time data extraction from API
* Data transformation and storage
* Logging and error handling
* Dockerized for consistent deployment
* CI/CD pipeline for automation
* Cloud deployment on AWS EC2

---

## 📁 Project Structure

```
devops-data-pipeline/
│
├── app/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
│
├── logs/
├── Dockerfile
├── requirements.txt
└── .github/workflows/ci.yml
```

---

## ▶️ How to Run (Locally)

### 1. Clone the repo

```
git clone https://github.com/Mohammed-Owais-08/devops-data-pipeline.git
cd devops-data-pipeline
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Set API Key

```
set API_KEY=your_api_key
```

### 4. Run pipeline

```
python app/main.py
```

---

## 🐳 Run with Docker

### Build image

```
docker build -t pipeline-app .
```

### Run container

```
docker run --rm -e API_KEY=your_api_key pipeline-app
```

---

## 🔁 CI/CD Pipeline

* Implemented using GitHub Actions
* Automatically runs pipeline on every push
* Builds Docker image

---

## ☁️ AWS Deployment

* Deployed on AWS EC2
* Installed Docker and ran containerized pipeline

---

## 📊 Output

* Data stored in SQLite database (`weather.db`)
* Logs generated in `logs/pipeline.log`

---

## 🎯 Key Learnings

* Hands-on experience with Docker and containerization
* CI/CD pipeline automation using GitHub Actions
* Cloud deployment using AWS EC2
* Building scalable and automated data pipelines

---

## 👤 Author

**Mohammed Owais Siddibapa**
GitHub: https://github.com/Mohammed-Owais-08
