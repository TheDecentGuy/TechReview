from flask import Flask, render_template, request
import openai
app = Flask(__name__)
openai.api_key = "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"


@app.route('/')
def index():
    return render_template('home.html', author="king")


@app.route('/generate', methods=['POST'])
def generate():
    title = request.form['title']
    author = request.form['author']
    result = request.form['result']

    # Generate the technical review paper using OpenAI API
    prompt = "Write a example of technical review paper titled " + \
        title + " by "+author+"."

    prompt = str(prompt)

    openai.api_key = "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"

    completion = openai.ChatCompletion. create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt+". It should be in proper IEEE format."}])
    paper = completion.choices[0].message.content

    # Return the generated paper to the user
    return render_template('result.html', paper=paper, prompt=prompt)


if __name__ == '__main__':
    app.run(debug=True)


# import openai
# openai.api_key = "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"
# completion = openai.ChatCompletion. create(
#     model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Write a technical review paper titled 'smart parking system' by vrushabh that completed. It should be in proper format"}])
# paper = completion.choices[0].message.content
# print(paper)
