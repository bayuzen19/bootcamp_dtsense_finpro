<<<<<<< HEAD
# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
=======
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
>>>>>>> 14f224b9f5010fd509a269137699818c98b04bef
