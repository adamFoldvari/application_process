import consol_functions
import querys
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/')
def menu():
    links = ['/mentors', '/all-school', '/mentors-by-country', '/contacts', '/applicants', '/applicants-and-mentors']
    query_names = ['Mentors', 'All school', 'Mentors by country', 'Contacts', 'Applicants', 'Applicants and mentors']
    return render_template('menu.html', links=links, query_names=query_names)


@app.route('/mentors')
def mentors():
    query_result, query_header = querys.mentors_query()
    return render_template('query_result.html', query_result=query_result, query_header=query_header)


if __name__ == '__main__':
    app.run(debug=True)