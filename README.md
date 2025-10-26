# 🧠 Flask Feedback Portal — Serverless CI/CD on AWS 🚀

A **cloud-native feedback portal** built with Flask and deployed on **AWS Lambda** using a fully automated **CI/CD pipeline** powered by **CodePipeline**, **CodeBuild**, and **S3**.  This project demonstrates a production-grade **serverless architecture** where every code commit triggers an automated build and deployment to Lambda.

---

## 🏗️ Architecture Overview

### **Workflow**
1. Code is pushed to **GitHub**
2. **AWS CodePipeline** detects the change and triggers:
   - **AWS CodeBuild** to install dependencies and package the Flask app
   - **AWS Lambda** update via deployment script
3. The updated Lambda function is accessible via a **Function URL**

---

## 🧩 Services Used

| Layer        | AWS Service   | Purpose                                        |
|---------------|---------------|------------------------------------------------|
| **Source**    | GitHub        | Repository trigger for CodePipeline            |
| **Build**     | CodeBuild     | Build and package the Flask application        |
| **Deploy**    | Lambda        | Serverless hosting for the Flask backend       |
| **Storage**   | S3            | Stores build artifacts and static files        |
| **CI/CD**     | CodePipeline  | Automates the build and deployment workflow    |

---

## 🗂️ Project Structure
aws-cicd-flask-feedback-portal/
├── app.py # Flask application entry point
├── requirements.txt # Python dependencies
├── buildspec.yml # CodeBuild build configuration
├── templates/ # HTML templates


---

## ⚙️ CI/CD Pipeline Setup

### **Step 1: Create IAM Roles**

- **CodePipeline role** → Full access to CodeBuild, Lambda, S3
- **CodeBuild role** → Access to S3, Lambda

---

### **Step 2: Connect GitHub Repository**

- In **CodePipeline**, choose **GitHub (Version 2)** as the source provider  
- Select your repository and branch (e.g., `main`)

---

### **Step 3: Define Build Process (`buildspec.yml`)**

```yaml
version: 0.2

phases:
  install:
    runtime-versions:
      python: 3.9
    commands:
      - echo "Installing dependencies..."
      - pip install -r requirements.txt -t .
  build:
    commands:
      - echo "Packaging application..."
artifacts:
  files:
    - '**/*'
```
---
### **Step 4: Lambda Deployment & Accessing the Application**

- CodePipeline automatically updates your Lambda.
- Once the deployment succeeds, open your Lambda Function URL in the browser.

---
### **Screenshots**

- GitHub Connection
  
<img width="1000" height="400" alt="github-connection" src="https://github.com/user-attachments/assets/db70a811-a427-47f5-b4df-337359a4b641" />

- CodeBuild Creations, History, IAM Roles
  
<img width="1000" height="400" alt="code-build" src="https://github.com/user-attachments/assets/8e88cf10-f88d-4ccc-9c37-f0c9250574cc" />
<img width="1000" height="400" alt="codebuild-history" src="https://github.com/user-attachments/assets/91fe08c3-7970-440e-ab89-2842b7a6d9d0" />
<img width="1000" height="400" alt="codebuild-IAM-Role" src="https://github.com/user-attachments/assets/b9f58be4-2a7b-4c9d-be24-e78281317d90" />

- CodePipeline Success, History, Logs

<img width="1000" height="400" alt="codepipeline-sucess" src="https://github.com/user-attachments/assets/d83fb61d-f29b-48e5-bbab-9f1edb4f94ce" />
<img width="1000" height="400" alt="codepipeline-history" src="https://github.com/user-attachments/assets/37d52823-8e8c-4eb5-903b-44d1a554c8bd" />
<img width="1000" height="400" alt="codepipeline-logs" src="https://github.com/user-attachments/assets/5e387370-abeb-4a87-8dc0-b2c0213e962f" />

- Lambda

<img width="1000" height="400" alt="lambda" src="https://github.com/user-attachments/assets/b5d2feef-c7c9-473c-a41d-316007856233" />

- s3 Bucket

<img width="1000" height="400" alt="s3-codepipeline" src="https://github.com/user-attachments/assets/e8a2d0d1-d8cd-404b-972f-9d3da526e9de" />

---

### **Learning Outcomes**

- Implemented a real-time CI/CD pipeline using AWS-native services
- Deployed Flask apps as serverless functions
- Automated build, test, and deploy workflows end-to-end
- Integrated GitHub with AWS CodePipeline
