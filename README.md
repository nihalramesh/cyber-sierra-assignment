# AI Data Explorer

An interactive, AI-powered web application that allows users to upload datasets, explore their structure, and ask natural language questions using OpenAI via PandasAI.

---

## Features

- Upload `.csv`, `.xls`, and `.xlsx` files
- Preview top N rows from selected files
- Ask questions in plain English about your data
- Maintain a session-based history of past queries
- Reuse previous questions with one click
- Provide feedback on the usefulness of AI responses

---

## Tech Stack

| Layer        | Technology        |
|--------------|-------------------|
| Frontend     | Streamlit         |
| Backend      | Python, Pandas, OpenPyXL |
| AI Engine    | PandasAI + OpenAI |

## Thought Process
The app was developed with the following goals:

    - Enable interactive exploration of structured data with minimal friction

    - Allow users to derive insights through natural language without writing code

    - Maintain simplicity in UI while enabling stateful features like prompt history and feedback

    - Use modular and widely adopted libraries to ensure clarity and maintainability

    - PandasAI provides an abstraction over raw dataframes that enables natural language-to-code translation. This allowed for a streamlined and maintainable architecture without writing a custom parser or query engine.

## Security Consideration
Security was incorporated into design and development decisions throughout:

    - File Upload Restrictions: Only .csv, .xls, and .xlsx files are accepted.

    - In-Memory Handling: Uploaded files are not persisted to disk or server — they are handled entirely in memory.

    - Error Isolation: All file parsing and AI processing is wrapped in exception handling to protect the UI from crashes.

    - Prompt Injection Risk Mitigation: PandasAI handles internal validation of prompts. Additional constraints can be added for production.

    - Secrets Management: The OpenAI API key is excluded from version control and should be stored in a .env file or secrets manager in production environments.

    - Session-Based State: Feedback and prompt history are stored only in Streamlit session state and not persisted or shared externally.
