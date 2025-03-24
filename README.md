# ISS Tracker and Notifier

## 📜 Overview

This Python script tracks the location of the International Space Station (ISS) and checks whether it is currently visible from your location. If the ISS is nearby and it is nighttime, the script sends an email notification, prompting you to look up.

## 🚀 Features

- Retrieves the current position of the ISS using the Open Notify API.

- Fetches sunrise and sunset times based on your location using the Sunrise-Sunset API.

- Determines if the ISS is close to your location.

- Checks if it is currently dark.

- Sends an email alert if the ISS is visible.

- Uses environment variables for sensitive credentials.

## 💻 Prerequisites

- Python 3.x

- requests library

- smtplib (built-in)

- dotenv library (for handling environment variables)

## ▶️ Installation

Clone the repository or download the script.

Install the required dependencies:

```pip install requests python-dotenv ```

Create a .env file in the same directory as the script and add the following variables:

```GMAIL_ADDRESS=your_email@gmail.com
GMAIL_PASSWORD=your_email_password
GMAIL_HOST_NAME=smtp.gmail.com
PORT=587
TIMEOUT=60
```
Modify MY_LAT and MY_LNG in the script to your actual latitude and longitude.

## 🕹 Usage

Run the script manually:

```python main.py```

For continuous execution, set up a cron job (Linux/macOS) or Task Scheduler (Windows) to run the script every 60 seconds.

## 🗝 API References

- ISS Position API

- Sunrise-Sunset API

- License

This project is open-source and available under the MIT License.

## 📌 Credits

This project is based on the 100 Days of Code: The Complete Python Pro Bootcamp by Angela Yu on Udemy.

