🛡️ Event-B TestGen: Smart Contract Analysis

Automated Test Case Generation Tool from Event-B models for Smart Contract verification.

📖 Introduction

Event-B TestGen is a lightweight web-based tool designed to help developers and testers analyze Event-B models (commonly used in Smart Contracts). This tool automatically parses model files (.bum, .xml) and generates verification scenarios (Test Cases), covering both successful executions (PASS) and condition violations (FAIL/REVERT).

This project aims to minimize manual test writing efforts and ensure comprehensive coverage of Guard conditions within Smart Contracts.

✨ Key Features

📂 Model Import: Supports importing Event-B model files (.bum or .xml) directly from your local machine.

🔍 Structural Analysis: Automatically extracts and visualizes:

Variables

Invariants

Events & Guard Conditions

⚡ Automated Test Generation:

PASS Case: Validates the successful execution flow when all Guards are satisfied.

FAIL Case: Automatically generates scenarios that violate specific Guards (verifying the contract's rejection/revert logic).

📊 Visual Statistics: Dashboard displaying Test Case count, Transition Coverage, and Guard distribution.

💾 Data Export: Exports the complete Test Suite to .json format (compressed in .zip) for integration with further testing workflows.

🚀 Demo

![](./assets/demo.png)

🛠️ Tech Stack

The project is built entirely on the Client-side (Frontend), requiring no Backend server:

Core: HTML5, JavaScript (ES6+).

UI/UX: Tailwind CSS (Modern, Responsive Design).

Icons: FontAwesome 6.

Libraries:

JSZip: For packaging and exporting reports.

DOMParser: For parsing Event-B XML structures.

⚙️ Installation & Usage

Since this is a Static Web App, no complex environment setup (like Node.js or Python) is required.

How to Run

Clone this repository:

git clone [https://yumingcaca.github.io/TestGen/]

Open the index.html file in any modern web browser (Chrome, Edge, Firefox, etc.).

User Guide

Click the "Import .BUM" button at the top right corner.

Select an Event-B model file (.bum or .xml) from your computer.

Click "Generate Tests" to analyze the model and generate scenarios.

Review the generated Test Cases in the right-hand panel.

Click "Export Results" to download the test report as a .zip file.

📂 Project Structure

eventb-testgen/
├── index.html          # Main application file (UI + Logic)
├── README.md           # Project documentation
└── assets/             # Assets directory
    └── demo.png        # Screenshot for README


🤝 Contributing

Contributions are always welcome! If you find any bugs or want to improve the test generation algorithm:

Fork the project.

Create your feature branch (git checkout -b feature/NewFeature).

Commit your changes (git commit -m 'Add some NewFeature').

Push to the branch (git push origin feature/NewFeature).

Open a Pull Request.

📝 License

This project is licensed under the MIT License.

Developed for Smart Contract Verification Course.