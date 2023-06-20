# Final Project System Architecture

## Team Members

- Agustín Soto
- Benjamin Rodriguez
- Jaime Torres

## Project Description

This project aims to develop a system architecture for a desktop application using Tkinter that allows users to upload files to Google Drive and monitor generated files, storing the metadata in MongoDB. The application will provide features such as file selection, upload to Google Drive, and tracking metadata in a database.

## System Architecture Overview

The system architecture is designed to be modular, scalable, and secure. It consists of several components that work together to provide the desired functionality. Here is an overview of the key components:

1. **Desktop Application**: This is the front-end component that the users interact with. It is developed using Tkinter, a Python GUI toolkit, and provides a user-friendly interface for file selection and upload. It communicates with the back-end via RESTful APIs.

2. **Web Server**: The web server hosts the back-end services and serves the client application. It handles incoming requests, manages sessions, and serves static assets. Flask, a lightweight web framework, can be used for this purpose.

3. **Authentication Service**: This component handles user authentication and authorization with Google Drive. It securely stores user credentials, verifies login requests, and manages authentication tokens. The Google Drive API provides authentication mechanisms and OAuth2 integration.

4. **Google Drive Integration**: The application integrates with the Google Drive API to upload files. It utilizes the appropriate API endpoints for file upload and management. The authentication service securely handles user authentication to authorize API requests.

5. **MongoDB Database**: The system relies on MongoDB, a NoSQL database, to store metadata related to the uploaded files. It stores information such as file names, sizes, upload timestamps, and any additional relevant metadata. PyMongo, a Python driver for MongoDB, can be used for database interactions.

6. **Monitoring Service**: This service monitors the file system for generated files and extracts metadata. It communicates with the desktop application or listens for file system events. When a file is generated, it extracts relevant metadata and stores it in the MongoDB database.

## Deployment and Infrastructure

The system architecture can be deployed on desktop machines. However, if there is a need for centralized access or additional functionalities, the following considerations can be made:

- **Cloud Storage**: Instead of direct integration with Google Drive, the application can utilize cloud storage services like Amazon S3 or Google Cloud Storage. This would involve integrating with their APIs and storing metadata in their respective databases.

- **Backend Hosting**: If there is a need to host the backend services in the cloud, platforms like AWS or Google Cloud Platform can be used. This would involve containerizing the services and deploying them on cloud infrastructure like Amazon EC2 or Google Compute Engine.

- **Scaling and Load Balancing**: If the application experiences high traffic or requires scaling, load balancers can be used to distribute requests across multiple instances of the web server. Tools like Kubernetes can also be used for container orchestration and scaling.

- **Database Hosting**: MongoDB can be hosted in the cloud using services like MongoDB Atlas or AWS DocumentDB. This provides managed database hosting, automated backups, and scaling capabilities.

## Conclusion

The proposed system architecture provides a modular and scalable foundation for building a Tkinter desktop application that uploads files to Google Drive and monitors generated files, storing metadata in MongoDB. By utilizing Tkinter, Flask, Google Drive API, and MongoDB, the application can provide a user-friendly interface, secure authentication, file upload capabilities, and metadata tracking. Specific technologies and services can be chosen based on project requirements and team preferences.
