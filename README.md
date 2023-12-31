# Daisies Django Project
This is a webpage for the fictional band Daisies

## How to Build and Run
1. Install dependancies using 'pip install -r requirements.txt'.
2. Set up your virtual enviroment
3. Run migrations: 'python manage.py migrate'.
4. Start the development server: 'python manage.py runserver'.

## Using Docker
- If you prefer Docker:
1. Build the Docker image: 'docker build -t band .'
2. Run the Docker container: 'docker run -p 8000:8000 band'.

## Access the Daisies Website

1. Open your web browser and go to 'http://localhost:8000/'.
2. Register yourself to access the band's content.
3. After registration, you'll be redirected to the login page.
4. Log in with your registered credentials.
5. You'll then be directed to the homepage of the Daisies website.

## Once logged in, you can:

- View band members
- Explore the albums
- Discover the songs and new releases

## Important info
- Ensure you have Python and Django installed.
- Do not commit sensitive information like passwords.