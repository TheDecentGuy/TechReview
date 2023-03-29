from flask import Flask, render_template, request
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.shared import Inches, Pt
import openai
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html', author="")


@app.route('/generate', methods=['POST'])
def generate():
    pTitle = request.form['title']
    author = request.form['author']
    problemStatement = request.form['problem']
    proposedSl = request.form['solution']
    result = request.form['result']

    # Generate the technical review paper using OpenAI API
    prompt = "Write a example of technical review paper titled " + \
        title + " by "+author+"."

    prompt = str(prompt)

    openai.api_key = "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"

    completion = openai.ChatCompletion. create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Abstract based on "+title}])
    abstract = completion.choices[0].message.content

    completion = openai.ChatCompletion. create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": "write Introduction on "+title}])
    intro = completion.choices[0].message.content

    completion = openai.ChatCompletion. create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": "write Literature Survey on "+title}])
    literature = completion.choices[0].message.content

    completion = openai.ChatCompletion. create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": "write Conclusion on "+title}])
    conclusion = completion.choices[0].message.content

    completion = openai.ChatCompletion. create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Acknowledgement Based on "+proposedSl}])
    ack = completion.choices[0].message.content

    document = Document()

    # Set the page margins
    sections = document.sections
    for section in sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)

    # Set the font
    style = document.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(10)

    # Add a title
    title = document.add_heading(title, 0)
    title.alignment = 1  # center align

    # Add authors
    p = document.add_paragraph()
    p.alignment = 1  # center align
    p.add_run(author).bold = True
    p.add_run(', Author 2, and Author 3')

    # Set the text as two columns
    section = document.sections[0]
    section.left_margin = Inches(0.7)
    section.right_margin = Inches(0.7)
    cols = section._sectPr.xpath('./w:cols')[0]
    cols.set(qn('w:num'), '2')

    # Add the abstract and keywords
    document.add_heading('Abstract', 1)
    abstract_para = document.add_paragraph(abstract)
    abstract_para.paragraph_format.left_indent = Inches(0.5)
    abstract_para.paragraph_format.right_indent = Inches(0.5)
    abstract_para.paragraph_format.first_line_indent = Inches(-0.25)

    document.add_heading('Index Terms', 2)
    keywords_para = document.add_paragraph('Keyword 1, Keyword 2, Keyword 3')
    keywords_para.paragraph_format.left_indent = Inches(0.5)
    keywords_para.paragraph_format.right_indent = Inches(0.5)

    # Add the introduction
    document.add_heading('I. Introduction', 1)
    document.add_paragraph(intro)

# Add a figure at the top of a column

# Save the document
    document.save('static/demo.docx')

    # Return the generated paper to the user
    return render_template('result.html', pTitle=pTitle, author=author, problemStatement=problemStatement, proposedSl=proposedSl, abstract=abstract, intro=intro, literature=literature, conclusion=conclusion, ack=ack, result=result)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
