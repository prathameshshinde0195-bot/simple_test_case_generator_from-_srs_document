# Simple Test Case Generator from SRS Document

## 📌 Project Overview

The **Simple Test Case Generator from SRS Document** is a Python-based tool that automatically generates software test cases from a Software Requirements Specification (SRS) document.

This project helps testers and developers quickly derive structured test cases from requirement documents, reducing manual effort and improving test coverage.

The system reads an SRS document (PDF or text-based input), analyzes the content, and produces a structured list of possible test cases that can be used during software testing.

---

## 🎯 Objectives

* Automate the process of generating test cases from requirement documents.
* Reduce manual test case writing time.
* Improve consistency and coverage in software testing.
* Provide a simple interface for uploading requirement documents and generating test cases.

---

## 🛠️ Technologies Used

* **Python**
* **Flask** (Backend Web Framework)
* **HTML / CSS / JavaScript** (Frontend)
* **PDF Processing Libraries**
* **Natural Language Processing (NLP)** concepts for extracting requirements

---

## ⚙️ How the Project Works

1. The user uploads an SRS document (PDF format).
2. The system extracts text from the document.
3. The extracted requirements are processed and analyzed.
4. The application generates relevant test cases.
5. The generated test cases are displayed or exported as a file.

---

## 📂 Project Structure

```
project-root
│
├── backend
│   ├── app.py
│   ├── parser.py
│   └── testcases.pdf
│
├── frontend
│   ├── index.html
│   ├── styles.css
│   └── script.js
│
└── README.md
```

**Backend**

* Handles document processing
* Extracts requirement text
* Generates test cases

**Frontend**

* Provides the user interface
* Allows users to upload SRS documents
* Displays generated test cases

---

## ▶️ How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/prathameshshinde0195-bot/simple_test_case_generator_from-_srs_document.git
```

### 2. Navigate to the project directory

```
cd simple_test_case_generator_from-_srs_document
```

### 3. Install required dependencies

```
pip install -r requirements.txt
```

### 4. Run the application

```
python app.py
```

### 5. Open the application in your browser

```
http://localhost:5000
```

---

## 📊 Features

* Upload SRS documents
* Extract requirements automatically
* Generate structured test cases
* Simple and user-friendly interface
* Reduces manual testing effort

---

## 🚀 Future Improvements

* Advanced NLP-based requirement analysis
* Support for multiple document formats (DOCX, TXT)
* Export test cases to Excel or CSV
* AI-based intelligent test case generation
* Integration with test management tools

---

## 👨‍💻 Author

**Prathamesh Shinde**

If you found this project useful, feel free to ⭐ the repository.
