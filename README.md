# MedicalBot
Genai project for Medical Chatbot

# How to run?
### STEP 01: Create Repository in github and clone repository in local system

Create a new repository in the GitHub

Create a new folder `GenAI_Projects` in the local system.

Change the directory to the `GenAI_Projects`

```bash
cd  GenAI_Projects
```

Clone the repository

```bash
git clone  <repo from https://github.com/>
```
### STEP 02: Create a conda environment after opening the repository

```bash
conda create --prefix ./venv python=3.10 -y
```

```bash
conda activate <venv_path>
```


### STEP 03: install the requirements
```bash
pip install -r requirements.txt
```


### STEP 04- create a project folder structure

create a `template.py` file for creating project folder structure

```bash
python template.py
```

### STEP 05- Commit the changes to the github repository

To push the changes to github

Create `Personal Access Token(PAT)` in the GitHub account

Github ==> Settings ==> Developer Settings ==> Personal Access Tokens ==> Tokens(classic)
create the Token with scopes like "repo, user, and workflow"
Note the Token



```bash
git config --list
git config --global --list
git config --global user.name "<github-username>"
git config --global user.email "<github-user_email>"
git add .
git commit -m "project structure is added"
git push origin main
```

If it asks for the login into `github` then login with passkey and provide the `PAT`

### STEP 06: Create a `.env` file in the root directory and add your Pinecone,Google & Groq credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
GROQ_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
GOOGLE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```



```bash
# run the following command to store embeddings to pinecone
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up localhost:
```


### Techstack Used:

- Python
- LangChain
- Flask
- GROQ
- Pinecone


# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 970547337635.dkr.ecr.ap-south-1.amazonaws.com/medicalchatbot

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
   - AWS_DEFAULT_REGION
   - ECR_REPO
   - PINECONE_API_KEY
   - GROQ_API_KEY

    

