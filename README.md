# Cosmic Canvas: NASA APOD Explorer
Cosmic Canvas is a unique web application that brings the wonders of space directly to users through NASA's Astronomy Picture of the Day (APOD) API. The project's distinctiveness lies in its combination of educational content, visual appeal, and interactive features:

1. Dynamic content fetching from NASA's APOD API.
2. Local storage of APOD data to reduce API calls and enable offline viewing.
3. Interactive timeline feature for exploring past APODs.
4. Smooth animations and transitions using JavaScript and CSS.
5. Responsive design that works seamlessly on both desktop and mobile devices.

## How to run the application
To run the application, follow these steps:
1. Clone the repository using `git clone https://github.com/[your_username]/final_project.git`
2. Navigate to the project directory using `cd cosmic_canvas`
3. Create and activate the virtual environment using:
```
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate\`
```
4. Install the required packages using `pip install -r requirements.txt`
5. Set up your NASA API Key:
-  Obtain key from (https://api.nasa.gov/)
-  Create a .env file in the project root and add: `NASA_API_KEY=your_api_key_here`
6. Apply migrations
    `python manage.py migrate`
7. Run the development server
    `python manage.py runserver`
8. Access the application at (http://localhost:8000)

You can access the live webapp by <a href="https://corporate-ardyce-ohmitek-8a95df29.koyeb.app" style="display: inline-block; padding: 10px 20px; font-size: 16px; color: #fff; background-color: #007bff; border-radius: 5px; text-decoration: none;">Clicking Me!</a>