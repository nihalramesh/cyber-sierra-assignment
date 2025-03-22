# AI Data Explorer

An interactive, AI-powered web application that allows users to upload datasets, explore their structure, and ask natural language questions using OpenAI via PandasAI.

---

## Features

* Upload `.csv`, `.xls`, and `.xlsx` files
* Preview top N rows from selected files
* Ask questions in plain English about your data
* Maintain a session-based history of past queries
* Reuse previous questions with one click
* Provide feedback on the usefulness of AI responses

---

## Tech Stack

| Layer     | Technology               |
|-----------|---------------------------|
| Frontend  | Streamlit                 |
| Backend   | Python, Pandas, OpenPyXL  |
| AI Engine | PandasAI + OpenAI         |

---

## Thought Process

The app was developed with the following goals:

* Enable interactive exploration of structured data with minimal friction
* Allow users to derive insights through natural language without writing code
* Maintain simplicity in the UI while enabling stateful features like prompt history and feedback
* Use modular and widely adopted libraries to ensure clarity and maintainability

PandasAI provides an abstraction over raw DataFrames that enables natural language-to-code translation. This allowed for a streamlined and maintainable architecture without writing a custom parser or query engine.

---

## Security Considerations

Security was incorporated into design and development decisions throughout the application:

* **File Upload Restrictions**: Only `.csv`, `.xls`, and `.xlsx` files are accepted.
* **In-Memory Handling**: Uploaded files are not persisted to disk or server — they are handled entirely in memory during session runtime.
* **Error Isolation**: All file parsing and AI processing is wrapped in exception handling to prevent crashes from malformed files or unexpected inputs.
* **Prompt Injection Risk Mitigation**: While PandasAI includes internal sanitization, future iterations could add custom validation layers to limit prompt scope.
* **Secrets Management**: The OpenAI API key is excluded from version control and loaded from a `.env` file. A `.env.example` is provided to guide setup.
* **Session-Based State**: Prompt history and feedback are stored only in the local Streamlit session state and are not persisted or shared externally.

---

## Setting Up the Project

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-data-explorer.git
cd ai-data-explorer
```

### 2. Set up the virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the environment variable

```bash
cp .env.example .env
```

Then add your OpenAI API key inside .env

```ini
OPENAI_API_KEY=your-openai-api-key-here
```

### 5. Run the Application

```bash
streamlit run app.py
```