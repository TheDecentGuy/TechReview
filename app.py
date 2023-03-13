# from flask import Flask, render_template, request
# import openai
# app = Flask(__name__)
# openai.api_key = "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"


# @app.route('/')
# def index():
#     return render_template('home.html')


# @app.route('/generate', methods=['POST'])
# def generate():
#     title = request.form['title']
#     author = request.form['author']
#     result = request.form['result']

#     # Generate the technical review paper using OpenAI API
#     prompt = "Write a technical review paper titled '{title}' by {author} that {result}."
#     response = openai.Completion.create(
#         engine="davinci",
#         prompt=prompt,
#         temperature=0.5,
#         max_tokens=1024,
#         n_top=1,
#         stop=None,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
#     paper = response['choices'][0]['text']
#     # print(response.choices[0].text)

#     # Return the generated paper to the user
#     return render_template('result.html', paper=paper)


# if __name__ == '__main__':
#     app.run(debug=True)


import openai
openai.api_key = "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"
completion = openai.ChatCompletion. create(
    model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Write a technical review paper titled 'smart parking system' by vrushabh that completed. It should be in proper format"}])
print(completion.choices[0].message.content)
