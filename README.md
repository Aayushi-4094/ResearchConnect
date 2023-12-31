﻿# ResearchConnect - Automated Research Paper Updates


ResearchConnect is a web application designed to automate the process of fetching and delivering relevant research papers to users based on their interests. This project was inspired by a passion for research papers and a desire to gain experience in web development. The goal is to provide users with a personalized and convenient way to stay up-to-date with the latest research in their chosen fields.

## Getting Started

To set up ResearchConnect on your local machine, follow these steps:

### Prerequisites

- Python 3.7 or higher installed on your system.
- pip package manager installed to manage Python dependencies.

### Installation

1. Clone this GitHub repository to your local machine:

```bash
git clone https://github.com/your-username/research-connect.git
cd research-connect
```

2. Set up a virtual environment to isolate project dependencies:

```bash
python -m venv venv
source venv/bin/activate      # On Windows, use `venv\Scripts\activate`
```

3. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### Database Setup

1. Make sure you have a PostgreSQL database installed and running.

2. Open `config.py` and update the `SQLALCHEMY_DATABASE_URI` to match your database connection settings:

```python
SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/research_connect_db'
```

3. Create the database tables using SQLAlchemy migrations:

```bash
flask db init
flask db migrate
flask db upgrade
```

### API and Email Configuration

1. Register for an API key from [Research Papers API](https://researchpapers.io/) and update `api_key` in `config.py`:

```python
API_KEY = 'your-api-key-here'
```

2. To enable email updates for users, configure the email service settings in `config.py`:

```python
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'your-email@example.com'
MAIL_PASSWORD = 'your-email-password'
```

### Running the Application

1. Start the application using Flask:

```bash
flask run
```

2. The application will be accessible at `http://localhost:5000` in your web browser.

### Usage

1. Access the ResearchConnect application through your web browser.

2. Register as a new user by filling out the registration form with your full name, email, and research topic preferences.

3. Submit the form to receive weekly email updates containing relevant research papers based on your interests.

## Contributions and Feedback

Contributions and feedback are welcome! If you encounter any issues or have suggestions for improvements, please create a GitHub issue or submit a pull request.

We hope ResearchConnect enhances your research experience and keeps you informed of the latest advancements in your field. Happy researching!
