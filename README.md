# 🔴 Redlogs

Redlogs is a lightweight Python application that fetches and displays Reddit account information such as total karma, number of posts, and more — just by using your Reddit username and password.

> ⚠️ Your credentials are stored locally and used only for authentication via Reddit's secure API (using PRAW). No information is sent to third-party servers.

---

## 🚀 Features

- View your Reddit account details
- Real-time Karma and post count tracking
- Environment-variable based security

---

## 🛠️ Setup

### 1. Clone this repository

```bash
  git clone https://github.com/darkstarexist/Redlogs.git
  cd Redlogs
```

### 2. Install Required Dependencies

```bash
  pip install -r requirements.txt
```

### 3. Configure .env file
## Go to Reddit's app creation page

```bash
  https://www.reddit.com/prefs/apps
```

## Click on "Create App" and fill in the required fields:

## name: Your app's name (e.g., "Redlogs").

## App type: Select "script" for the type of app.

## description: A brief description of your app.

## about URL: Leave it blank or put a URL if you have one.

## redirect URI: Use http://localhost:8000 for testing purposes.

## permissions: Select "read" and any other permissions your app might need.

##Once created, you'll get the following credentials:

#Client ID: Found just under the webapp's name.

#Client Secret: A unique string found on the app page.

### Configure Environment Variables
```bash
  REDDIT_CLIENT_ID='your_client_id_here'
  REDDIT_CLIENT_SECRET='your_client_secret_here'
  REDDIT_USERNAME='your_reddit_username_here'
  REDDIT_PASSWORD='your_reddit_password_here'

```

### Run the app in cmd
```bash
  python redlogs.py
```



