# Flask Information Retrieval System

This Flask-based Information Retrieval System allows users to query a collection of political documents using a Boolean Retrieval model. The system employs a term-document matrix to efficiently process and retrieve relevant documents based on user queries.

## Features
- **Document Viewer:** Explore individual political documents by navigating to the `/document/<int:doc_id>` endpoint.
- **Boolean Query Support:** Submit queries using 'and', 'or', and 'not' operators for effective retrieval.
- **Term-Document Matrix:** Utilizes a pre-built term-document matrix to optimize document retrieval.

## Getting Started
1. Clone this repository: `git clone [https://github.com/fenil210/Information-Retrieval-System-for-Political-Document-using-Flask]'
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

## install flask
![install flask](https://github.com/fenil210/Information-Retrieval-System-for-Political-Document-using-Flask/assets/121050723/914912bd-a1e7-4c7d-afec-3d8bbd2c114b)

## select python interpreter as python dot exe from venv
![select python interpreter as python dot exe from venv](https://github.com/fenil210/Information-Retrieval-System-for-Political-Document-using-Flask/assets/121050723/8d2f837f-9c52-4bc9-84ba-1602b49280dd)

## run app
![run flask](https://github.com/fenil210/Information-Retrieval-System-for-Political-Document-using-Flask/assets/121050723/cb21cba7-2024-4fde-b18d-401668689a65)

## main input screen
![output](https://github.com/fenil210/Information-Retrieval-System-for-Political-Document-using-Flask/assets/121050723/5c2a6ec6-7855-4f9b-b465-7ea0e234db93)

## output query
![query app](https://github.com/fenil210/Information-Retrieval-System-for-Political-Document-using-Flask/assets/121050723/738326e0-c34a-4c4d-9343-e584f9c71d48)

## result of retrieved document 2
![result ss](https://github.com/fenil210/Information-Retrieval-System-for-Political-Document-using-Flask/assets/121050723/9a120345-d9aa-46c1-808d-e25ad360dcea)


## Example Query
```python
# Example query to retrieve documents containing both 'politics' and 'election':
query_result = ask_query('politics and election', term_doc_matrix)
