from flask import Flask, render_template, request
import openai
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html', author="")


@app.route('/generate', methods=['POST'])
def generate():
    title = request.form['title']
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

    # Return the generated paper to the user
    return render_template('result.html', title=title, author=author, problemStatement=problemStatement, proposedSl=proposedSl, abstract=abstract, intro=intro, literature=literature, conclusion=conclusion, ack=ack, result=result)


if __name__ == '__main__':
    app.run(port=8000, debug=True)


# import openai
# openai.api_key = "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"
# completion = openai.ChatCompletion. create(
#     model="gpt-3.5-turbo", messages=[{"role": "system", "content": "Write a technical review paper titled 'smart parking system' by vrushabh that completed. It should be in proper format"}])
# paper = completion.choices[0].message.content
# print(paper)
