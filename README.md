# Flask Information Retrieval System

This Flask-based Information Retrieval System allows users to query a collection of political documents using a Boolean Retrieval model. The system employs a term-document matrix to efficiently process and retrieve relevant documents based on user queries.

## Features
- **Document Viewer:** Explore individual political documents by navigating to the `/document/<int:doc_id>` endpoint.
- **Boolean Query Support:** Submit queries using 'and', 'or', and 'not' operators for effective retrieval.
- **Term-Document Matrix:** Utilizes a pre-built term-document matrix to optimize document retrieval.

## Getting Started
1. Clone this repository: `git clone [<repo-url>](https://github.com/fenil210/Information-Retrieval-System-for-Political-Document-using-Flask)`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the Flask application: `python app.py`
4. Access the application in your browser: `http://localhost:5000`

## Usage
1. Visit the home page (`/`) to access the query interface.
2. Submit queries using 'and', 'or', and 'not' operators.
3. View the retrieved documents and explore individual document contents.

## File Structure
- `app.py`: Main Flask application.
- `templates/`: HTML templates for rendering pages.
  - `index.html`: Home page template.
  - `result.html`: Query result page template.
  - `document.html`: Document view page template.
- `static/`: Static files (e.g., CSS, JavaScript).

## Example Query
```python
# Example query to retrieve documents containing both 'politics' and 'election':
query_result = ask_query('politics and election', term_doc_matrix)
