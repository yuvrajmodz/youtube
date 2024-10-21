from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os

app = Flask(__name__)

@app.route('/youtube-title', methods=['GET'])
def get_youtube_title():
    # Set up Chrome WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode (without GUI)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Open YouTube
        driver.get("https://youtube.com")
        
        # Get the title of the page
        title = driver.title
        
        # Return title in JSON format
        return jsonify({"title": title})
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        driver.quit()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5003))
    app.run(host='0.0.0.0', port=port, debug=True)