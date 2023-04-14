from flask import Flask, render_template, request
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.shared import Inches, Pt
from docx.enum.section import WD_ORIENT

import openai
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form')
def form():
    return render_template('form.html', author="")


@app.route('/generate', methods=['POST'])
def generate():
    pTitle = request.form['title']
    author = request.form['author']
    problemStatement = request.form['problem']
    proposedSl = request.form['solution']
    result = request.form['result']

    # Generate the technical review paper using OpenAI API
    prompt = "Write a example of technical review paper titled " + \
        pTitle + " by "+author+"."

    print(prompt)
    prompt = str(prompt)

    openai.api_key = "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"

    completion = openai.ChatCompletion. create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Abstract based on "+pTitle}])
    abstract = completion.choices[0].message.content

    completion = openai.ChatCompletion. create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": "write Introduction on "+pTitle}])
    intro = completion.choices[0].message.content

    completion = openai.ChatCompletion. create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": "write Literature Survey on "+pTitle}])
    literature = completion.choices[0].message.content

    completion = openai.ChatCompletion. create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": "write Conclusion on "+pTitle}])
    conclusion = completion.choices[0].message.content

    completion = openai.ChatCompletion. create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Acknowledgement Based on "+proposedSl}])
    ack = completion.choices[0].message.content

    completion = openai.ChatCompletion. create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Only single Reference Based on "+pTitle}])
    ref1 = completion.choices[0].message.content

    completion = openai.ChatCompletion. create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Only single Reference different than "+ref1+"Based on "+pTitle}])
    ref2 = completion.choices[0].message.content

    completion = openai.ChatCompletion. create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Only single Reference different than "+ref1+","+ref2+"Based on "+pTitle}])
    ref3 = completion.choices[0].message.content

    completion = openai.ChatCompletion. create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Keywords Related "+pTitle}])
    keywords = completion.choices[0].message.content

    document = Document('static/IEEE.docx')  # Open the document

    # Access the title paragraph and change its text
    title_paragraph = document.paragraphs[0]
    title_paragraph.text = pTitle

    title_paragraph = document.paragraphs[1]
    title_paragraph.text = author

    title_paragraph = document.paragraphs[5]
    title_paragraph.text = "Abstract- "+abstract

    title_paragraph = document.paragraphs[6]
    title_paragraph.text = 'Keywords- '+keywords

    title_paragraph = document.paragraphs[8]
    title_paragraph.text = intro

    title_paragraph = document.paragraphs[10]
    title_paragraph.text = literature

    title_paragraph = document.paragraphs[12]
    title_paragraph.text = problemStatement

    title_paragraph = document.paragraphs[14]
    title_paragraph.text = proposedSl

    title_paragraph = document.paragraphs[16]
    title_paragraph.text = result

    title_paragraph = document.paragraphs[18]
    title_paragraph.text = conclusion

    title_paragraph = document.paragraphs[20]
    title_paragraph.text = ack

    title_paragraph = document.paragraphs[22]
    title_paragraph.text = ref1

    title_paragraph = document.paragraphs[23]
    title_paragraph.text = ref2

    title_paragraph = document.paragraphs[24]
    title_paragraph.text = ref3

    document.save('static/output.docx')  # Save the modified document

    # Return the generated paper to the user
    return render_template('result.html', pTitle=pTitle, author=author, problemStatement=problemStatement, proposedSl=proposedSl, abstract=abstract, intro=intro, literature=literature, conclusion=conclusion, ack=ack, result=result, ref1=ref1, ref2=ref2, ref3=ref3)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
