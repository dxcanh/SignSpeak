# SignSpeak - Gesture Recognition for Sign Language Conversion

SignSpeak is an innovative application that uses machine learning and computer vision techniques to translate sign language gestures into text. This tool is designed to break down communication barriers for the hearing-impaired community by allowing individuals who do not know sign language to understand it in text form. The app also offers real-time video calling and gesture recognition to help foster inclusivity and social integration.

## Table of Contents
- [System Configuration](#system-configuration)
- [Technologies Used](#technologies-used)
- [Main Technologies of the Application](#main-technologies-of-the-application)
- [System Workflow](#system-workflow)
- [Development Story](#development-story)
- [Technical Aspects](#technical-aspects)
- [Security](#security)
- [Social Impact](#social-impact)
- [Future Improvements](#future-improvements)

## System Configuration

**Frontend:**
- **JavaScript:** Controls user interface and dynamic behaviors.
- **HTML:** Provides structure and markup for the web page.
- **CSS:** Styles and layouts the web page.
- **MediaPipe API (JavaScript Version):** Hand gesture recognition.
- **WebRTC:** Video calling implementation.
- **JSON:** Data exchange format between client and server.

**Backend:**
- **Flask:** Web framework to provide API services.
- **Socket.io:** Real-time communication and messaging.
- **Firebase:** User authentication and database.
- **Pyrebase:** Firebase integration with Python.
- **Docker:** Application deployment and containerization.

## Technologies Used

- **RTC (Real-Time Communication):** Video calling using WebRTC.
- **Gesture Recognition (MediaPipe API):** Using hand and pose landmarks for gesture recognition.
- **Server Communication (JSON):** Sending data to the server for gesture processing.
- **Message Transmission (Socket.io):** Real-time message updates.
- **Database Connection (Firebase, Pyrebase):** Storing user data and maintaining session states.
- **App Deployment (Docker):** Containerizing the application for easy deployment.
- **Machine Learning (TensorFlow):** Training and running gesture recognition models.

## Main Technologies of the Application

- **LSTM (Long Short-Term Memory):** Converts complex sign language gestures into textual output.
- **Random Forest:** Identifies individual letters in the sign language alphabet.

## System Workflow

### Step 1: User Setup
After logging in, users can create a waiting room, invite other users to their room, and activate gesture recognition.

### Step 2: Data Transmission
Gesture coordinates (hand and pose landmarks) are detected and transmitted in JSON format via the MediaPipe API for web. The client sends these coordinates to the server for processing.

### Step 3: Gesture Recognition
The server receives the request and temporarily stores the data. The server processes up to 20 requests for complex movements and uses this data as input for the LSTM model, which recognizes gestures and returns the corresponding text. The result is sent back to all users in the current room via Socket.io.

## Development Story

### 1. Context of the Application
SignSpeak was created to bridge the communication gap for individuals with hearing impairments. As sign language speakers often struggle to communicate with those who don’t understand it, this app aims to convert sign language gestures into text, helping to make communication more inclusive and accessible for everyone.

### 2. Challenges Encountered
The major challenge was finding a suitable AI model to recognize complex sign language gestures. Sign language is not just a form of body language but consists of a series of movements that convey meaning. We decided to use the **LSTM model** due to its ability to process sequential data, although training it with two-dimensional data was a significant hurdle. We invested time in collecting data and training the model to overcome this challenge.

Despite these difficulties, I learned a lot through the process and feel I have grown as a developer through persistence and continuous learning.

### 3. Key Notes:
- **Technical Aspects:**
  The AI model LSTM specializes in natural language processing by combining past and present data to make predictions. By leveraging Google’s Mediapipe library, we extract key coordinates (hand and pose landmarks) from the user’s webcam feed and use these as inputs for our 2D array-based model, enabling us to make predictions based on action sequences in short video clips.

- **Security:**
  - **Privacy of User Images:** The Mediapipe tool identifies the coordinates of hand joints and body points in each frame on the user's device. Only the relevant coordinates are sent to the server, ensuring that no personal image data is exposed.
  - **Real-Time Video Calls:** Video calls are made using WebRTC with end-to-end encryption, ensuring secure communication.
  - **User Registration and Login:** The app uses Firebase Authentication for user registration with minimal data requirements (email and username), ensuring that the user’s identity and account are securely managed.

- **Social Impact:**
  - **Communication Facilitation:** The app enables the hearing-impaired to communicate seamlessly with non-sign-language speakers.
  - **Information Accessibility:** Information is made accessible to the deaf and hard-of-hearing through sign language translation, promoting equality.
  - **Education Support:** Implementing the system in classrooms or public information booths will allow students with hearing impairments to participate more actively in education and social environments. It can also serve as a tool to learn sign language.
  
## Future Improvements

### 1. Challenges
Given the vast vocabulary used in communication, teaching a person to perform all the corresponding sign language gestures in front of a camera requires significant time. To address this challenge, we plan to add a feature where users can teach the system new gestures.

### 2. Improvements
We aim to enhance the app further by adding a user guide for first-time users and integrating a forum feature where users can share and learn about sign language gestures.

---

For more details, please refer to the accompanying diagrams and visual aids provided in the repository.

Feel free to contribute to the project or report issues via the GitHub repository!

---

Thank you for exploring SignSpeak! Together, we can help expand the world we see.
