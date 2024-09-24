# CAPTCHA Solver Script

## Overview

This project contains a Python script that automates the solving of CAPTCHA images from a specific website using a combination of web scraping, image processing, and Optical Character Recognition (OCR). The script utilizes Selenium for browser automation, BeautifulSoup for HTML parsing, OpenCV for image processing, and Tesseract for OCR.

### Features:
- **Web Scraping**: Automates interaction with a website to retrieve CAPTCHA images.
- **Image Processing**: Cleans and processes CAPTCHA images to enhance text recognition accuracy.
- **Optical Character Recognition**: Uses Tesseract OCR to extract text from the processed CAPTCHA images.
- **CAPTCHA Submission**: Automatically submits the extracted CAPTCHA text to the website.
- **Success Rate Testing**: Can test the success rate of CAPTCHA solving over multiple attempts.

## Requirements

To run the script, the following Python libraries and dependencies are required:

- `selenium`: For automating the browser interaction.
- `beautifulsoup4`: For parsing HTML content.
- `webdriver_manager`: To manage and automate the ChromeDriver installation.
- `opencv-python` (`cv2`): For image processing.
- `numpy`: For handling image data.
- `pytesseract`: For extracting text from images using Tesseract OCR.
- `Pillow` (`PIL`): For image handling.
- `tesseract`: OCR engine (needs to be installed on your system).
  
Install the required packages using:

```bash
pip install selenium beautifulsoup4 webdriver_manager opencv-python numpy pytesseract Pillow
