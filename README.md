# Crop Disease Identification System

This project is a web application designed to identify crop diseases from leaf images and provide relevant information through an AI chatbot. It uses YOLO for image inference and LangChain for the chatbot functionality.

## Features

* **Disease Detection** : Upload a leaf image to identify crop diseases using YOLO.
* **AI Chatbot** : Ask questions about the detected diseases, powered by LangChain and ChatGroq.
* **Interactive UI** : User-friendly interface built with React.

---

## Project Structure

```plaintext
.
├── backend/                # Backend server and AI processing logic
│   ├── app.py              # Flask API for handling image uploads and chatbot queries
│   ├── chat.py             # Chatbot logic using LangChain and plant disease information
│   ├── inference.py        # YOLO inference for disease detection
│   ├── best.pt             # YOLO model weights
│   ├── yolotrain.ipynb     # Notebook for YOLO model training
├── frontend/               # Frontend React application
│   ├── public/             # Static files
│   │   ├── index.html      # Main HTML file
│   ├── src/                # React components and logic
│   │   ├── App.js          # Main React component
│   │   ├── App.css         # Styles for the application
├── README.md               # Documentation (this file)
```

---

## Backend Components

### 1. **chat.py**

* Implements a chatbot to guide users about crop diseases.
* Uses **LangChain** with the ChatGroq model for natural language understanding.
* Contains a dictionary (`class_info_dict`) with detailed information about healthy and diseased leaves.

Key Functionality:

```python
def chatbot(info, history, message):
    # Generates chatbot responses using the LangChain library
```

### 2. **inference.py**

* Handles disease detection using a YOLO model (`best.pt`).
* Outputs detected classes and visualizes bounding boxes on the image.

Key Functionality:

```python
def inference(image):
    # Performs YOLO inference and returns processed image and detected classes
```

### 3. **app.py**

* Flask server to connect the backend with the frontend.
* Two main endpoints:
  * `/upload`: Accepts leaf images, detects diseases, and returns results.
  * `/chat`: Processes user queries based on detected diseases.

---

## Frontend Components

### 1. **App.js**

* The main React component for the frontend.
* Provides the following features:
  * Image upload and preview.
  * Disease detection using the `/upload` backend endpoint.
  * Chat functionality using the `/chat` backend endpoint.
  * Displays processed image and detected labels.

---

## Installation

### Prerequisites

* Python 3.8+
* Node.js and npm

### Backend Setup

1. Navigate to the `backend/` directory.
2. Create a `.env` file with the following content:
   ```plaintext
   GROQ_API_KEY=<your-groq-api-key>
   ```
3. Install dependencies:
   ```bash
   pip install flask flask-cors opencv-python numpy langchain-groq ultralytics python-dotenv
   ```
4. Run the server:
   ```bash
   python app.py
   ```

### Frontend Setup

1. Navigate to the `frontend/` directory.
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```

---

## Usage

1. Start the backend and frontend servers.
2. Open the React app in your browser (typically at `http://localhost:5000`).
3. Upload a leaf image and process it to detect diseases.
4. Use the chatbot to ask questions about the detected diseases.

---

## Technologies Used

* **Backend** :
  * Flask
  * YOLO (Ultralytics)
  * LangChain + ChatGroq
* **Frontend** :
  * React.js
  * Bootstrap (for styling)

---

## Future Enhancements

* Add more robust error handling.
* Improve chatbot's conversational capabilities.
* Expand the dataset for YOLO training to include more crop diseases.
