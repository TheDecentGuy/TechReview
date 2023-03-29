# from flask import Flask, render_template, request
# import openai
# app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('home.html', author="")


# @app.route('/generate', methods=['POST'])
# def generate():
#     title = request.form['title']
#     author = request.form['author']
#     problemStatement = request.form['problem']
#     proposedSl = request.form['solution']
#     result = request.form['result']

#     # Generate the technical review paper using OpenAI API
#     prompt = "Write a example of technical review paper titled " + \
#         title + " by "+author+"."

#     prompt = str(prompt)

#     openai.api_key = "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"

#     completion = openai.ChatCompletion. create(
#         model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Abstract based on "+title}])
#     abstract = completion.choices[0].message.content

#     completion = openai.ChatCompletion. create(
#         model="gpt-3.5-turbo", messages=[{"role": "user", "content": "write Introduction on "+title}])
#     intro = completion.choices[0].message.content

#     completion = openai.ChatCompletion. create(
#         model="gpt-3.5-turbo", messages=[{"role": "user", "content": "write Literature Survey on "+title}])
#     literature = completion.choices[0].message.content

#     completion = openai.ChatCompletion. create(
#         model="gpt-3.5-turbo", messages=[{"role": "user", "content": "write Conclusion on "+title}])
#     conclusion = completion.choices[0].message.content

#     completion = openai.ChatCompletion. create(
#         model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Acknowledgement Based on "+proposedSl}])
#     ack = completion.choices[0].message.content

#     # Return the generated paper to the user
#     return render_template('result.html', title=title, author=author, problemStatement=problemStatement, proposedSl=proposedSl, abstract=abstract, intro=intro, literature=literature, conclusion=conclusion, ack=ack, result=result)


# if __name__ == '__main__':
#     app.run(port=8000, debug=True)


# # import openai
# # openai.api_key = "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"
# # completion = openai.ChatCompletion. create(
# #     model="gpt-3.5-turbo", messages=[{"role": "system", "content": "Write a technical review paper titled 'smart parking system' by vrushabh that completed. It should be in proper format"}])
# # paper = completion.choices[0].message.content
# # print(paper)


from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.shared import Inches, Pt

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
title = document.add_heading('Title of the Paper', 0)
title.alignment = 1  # center align

# Add authors
p = document.add_paragraph()
p.alignment = 1  # center align
p.add_run('Author 1').bold = True
p.add_run(', Author 2, and Author 3')

# Set the text as two columns
section = document.sections[0]
section.left_margin = Inches(0.7)
section.right_margin = Inches(0.7)
cols = section._sectPr.xpath('./w:cols')[0]
cols.set(qn('w:num'), '1')

# Add the abstract and keywords
document.add_heading('Abstract', 1)
abstract_para = document.add_paragraph('This is the abstract of the paper.')
abstract_para.paragraph_format.left_indent = Inches(0.5)
abstract_para.paragraph_format.right_indent = Inches(0.5)
abstract_para.paragraph_format.first_line_indent = Inches(-0.25)

document.add_heading('Index Terms', 2)
keywords_para = document.add_paragraph('Keyword 1, Keyword 2, Keyword 3')
keywords_para.paragraph_format.left_indent = Inches(0.5)
keywords_para.paragraph_format.right_indent = Inches(0.5)

# Add the introduction
document.add_heading('I. Introduction', 1)
document.add_paragraph('This is the introduction of the paper.')

# Add a figure at the top of a column

# Save the document
document.save('demo.docx')
