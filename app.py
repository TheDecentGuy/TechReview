from flask import Flask, render_template, request
import openai
app = Flask(__name__)
# openai.api_key = "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"


@app.route('/')
def index():
    return render_template('home.html', author="vrushabh")


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
        model="gpt-3.5-turbo", messages=[{"role": "system", "content": "write abstract on "+title}])
    abstract = completion.choices[0].message.content

    completion = openai.ChatCompletion. create(
        model="gpt-3.5-turbo", messages=[{"role": "system", "content": "write introduction on "+title}])
    intro = completion.choices[0].message.content

    completion = openai.ChatCompletion. create(
        model="gpt-3.5-turbo", messages=[{"role": "system", "content": "write related work on "+title}])
    work = completion.choices[0].message.content

    completion = openai.ChatCompletion. create(
        model="gpt-3.5-turbo", messages=[{"role": "system", "content": "write Proposed Methodology on "+title}])
    methodology = completion.choices[0].message.content

    completion = openai.ChatCompletion. create(
        model="gpt-3.5-turbo", messages=[{"role": "system", "content": "write conclusion on "+title}])
    conclusion = completion.choices[0].message.content

    completion = openai.ChatCompletion. create(
        model="gpt-3.5-turbo", messages=[{"role": "system", "content": "write analysis on "+title}])
    anlysis = completion.choices[0].message.content

    # Return the generated paper to the user
    return render_template('result.html', title=title, author=author, abstract=abstract, result=result, intro=intro, work=work, methodology=methodology, prompt=prompt, conclusion=conclusion)


if __name__ == '__main__':
    app.run(debug=True)


# import openai
# openai.api_key = "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"
# completion = openai.ChatCompletion. create(
#     model="gpt-3.5-turbo", messages=[{"role": "system", "content": "Write a technical review paper titled 'smart parking system' by vrushabh that completed. It should be in proper format"}])
# paper = completion.choices[0].message.content
# print(paper)
