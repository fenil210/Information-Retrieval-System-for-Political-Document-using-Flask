from flask import Flask, render_template, request
import os
import re 
app = Flask(__name__)


def get_document_content(doc_id):
    file_path = f'{doc_id}.txt'
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def term_doc_matrix():
    term_doc_matrix = {}
    for i in range(1, 11):
        with open(f'{i}.txt', 'r') as file:
            words = re.findall(r'\w+', file.read().lower())
            for word in words:
                if word not in term_doc_matrix:
                    term_doc_matrix[word] = [0] * 10
                term_doc_matrix[word][i - 1] = 1
    return term_doc_matrix

term_doc_matrix = term_doc_matrix()

def ask_query(query, term_doc_matrix):
    query_words = re.findall(r'\w+', query.lower())
    result = [1] * 10
    operator = 'and'
    for element in query_words:
        if element in ['and', 'or', 'not']:
            operator = element
        else:
            term_vector = term_doc_matrix.get(element, [0] * 10)
            if operator == 'and':
                result = [a and b for a, b in zip(result, term_vector)]
            elif operator == 'or':
                result = [a or b for a, b in zip(result, term_vector)]
            elif operator == 'not':
                result = [a and not b for a, b in zip(result, term_vector)]
    return [i + 1 for i, x in enumerate(result) if x == 1]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    user_query = request.form['query']
    result = ask_query(user_query, term_doc_matrix)
    return render_template('result.html', query=user_query, result=result)

@app.route('/document/<int:doc_id>')
def view_document(doc_id):
    content = get_document_content(doc_id)
    sorted_content = '\n'.join(sorted(content.split()))
    return render_template('document.html', doc_id=doc_id, content=sorted_content)

if __name__ == '__main__':
    app.run(debug=True)