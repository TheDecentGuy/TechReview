from flask import Flask, render_template, request
from docx import Document
from flask import send_file
from docx2pdf import convert

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
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": "write only Abstract based on "+pTitle}])
    abstract = completion.choices[0].message.content

    completion = openai.ChatCompletion. create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": "write only Introduction on "+pTitle}])
    intro = completion.choices[0].message.content

    completion = openai.ChatCompletion. create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": "References Based on "+pTitle+".List it in square parentheses numbering."}])
    ref1 = completion.choices[0].message.content

    completion = openai.ChatCompletion. create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Write a detailed literature survey on the "+pTitle+" , according to "+ref1+". Include square parentheses numbering in the literature survey based on the provided reference"}])
    literature = completion.choices[0].message.content

    completion = openai.ChatCompletion. create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": "write Conclusion on "+pTitle}])
    conclusion = completion.choices[0].message.content

    # completion = openai.ChatCompletion. create(
    #     model="gpt-3.5-turbo", messages=[{"role": "user", "content": "example of basics Acknowledgement as student wroking on mini project Based on "+pTitle}])
    # ack = completion.choices[0].message.content

    # completion = openai.ChatCompletion. create(
    #     model="gpt-3.5-turbo", messages=[{"role": "user", "content": "single Reference Based on "+pTitle}])
    # ref2 = completion.choices[0].message.content

    # completion = openai.ChatCompletion. create(
    #     model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Only single Reference different than "+ref1+","+ref2+"Based on "+pTitle}])
    # ref3 = completion.choices[0].message.content

    completion = openai.ChatCompletion. create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": "10 Keywords Related in single line comma format "+pTitle}])
    keywords = completion.choices[0].message.content

    document = Document('IEEE.docx')  # Open the document

    # Access the title paragraph and change its text
    title_paragraph = document.paragraphs[0]
    title_paragraph.text = pTitle.upper()

    title_paragraph = document.paragraphs[1]
    title_paragraph.text = author.title()

    title_paragraph = document.paragraphs[5]
    title_paragraph.text = "Abstract- "+abstract

    title_paragraph = document.paragraphs[6]
    title_paragraph.text = 'Keywords- '+keywords.title()

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
    title_paragraph.text = "I would like to express my heartfelt gratitude to all the individuals who have contributed and made this mini project of "+pTitle.title()+" a success. First and foremost, I would like to extend my deepest appreciation to my mentor, (mentor’s name), for their invaluable support, guidance, and encouragement throughout the entire duration of this project. Without their guidance, I would not have been able to accomplish this project in a timely and efficient manner. Furthermore, I would like to thank(name of team members) for their hard work and dedication in completing this project. Their inputs and insights have been extremely beneficial in enhancing the overall quality of the project. Last but not least, I would like to express my sincere thanks to the management of the institute(name of the institution) for providing us with all the necessary resources, including space, equipment, and software, and for believing in our potential to complete this project. Once again, I offer my heartfelt thanks to all who have contributed to the successful completion of this mini-project, and I hope that it will prove to be beneficial for the development of the "+pTitle.title()+"."

    title_paragraph = document.paragraphs[22]
    title_paragraph.text = ref1

    document.save('static/output.docx')  # Save the modified document
    convert('static/output.docx', 'static/output.pdf')

    # Return the generated paper to the user
    return render_template('result.html', pTitle=pTitle, author=author, problemStatement=problemStatement, proposedSl=proposedSl, abstract=abstract, intro=intro, literature=literature, conclusion=conclusion, result=result)


@app.route('/download')
def download():
    document = Document()
    # Add content to the document here
    return send_file('static/output.docx', as_attachment=True)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
