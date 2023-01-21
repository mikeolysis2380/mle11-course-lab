<p align = "center" draggable=”false” ><img src="https://user-images.githubusercontent.com/37101144/161836199-fdb0219d-0361-4988-bf26-48b0fad160a3.png"
     width="200px"
     height="auto"/>
</p>

# <h1 align="center" id="heading">FastAPI Web App with Hugging Face Transformers</h1>

# Creating a Simple Web App with FastAPI!

Make sure you've completed the `hugging_face_tutorial.ipynb` notebook before you move on to these steps.

You'll notice that in this folder, we don't have a whole lot. Just a single directory called `app` with an `app.py` and a `model` directory with our saved model. 

Let's check out the `app.py` file. 

## PART 3: Creating a Simple Web App with FastAPI

### 3.1: Running the Web App


Let's take a look at the `app.py` file.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
```

Right now, there's not a lot going on - but let's try and run it! From the terminal, run the following command (making sure you're in the `app` directory which contains the `app.py` file)

```bash
uvicorn app:app --reload
```

You should see something like this:

```bash
INFO:     Will watch for changes in these directories: ['<PATH TO YOUR DIRECTORY>']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [5676] using StatReload
INFO:     Started server process [5678]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

If you CTRL+click on the link, you should see the following in your browser:

```json
{"message": "Hello World"}
```

### 3.2: Adding a GET request


Let's add a GET request to our web app. We'll add a new function called `ping` that will return a simple message. 

```python
@app.get("/ping")
def ping():
    return {"message": "pong"}
```

Now, if you go back to your browser and append `/ping` to the end of the URL, you should see the following:

```json
{"message": "pong"}
```

You'll notice that you don't have to restart the server to see the changes. This is because we added the `--reload` flag when we ran the server. This will automatically restart the server when you make changes to the code, this is a very useful feature when you're developing your web app!

Let's look at each part of this function and see what's going on.

```python
@app.get("/ping")
```

This is a [decorator](https://www.datacamp.com/tutorial/decorators-python) that tells FastAPI that this function is a GET request! With FastAPI, it is as simple as that!

```python
def ping():
    return {"message": "pong"}
```

This is the function that will be executed when the GET request is made. It simply returns a JSON object with a message of "pong". Thanks to the hard work of the FastAPI team, we don't have to worry about converting this to JSON - it's done for us!

### 3.3: Adding a POST request

Let's add a POST request to our web app. We'll add a new function called `echo` that will take in a string and return it back to us. 

```python
@app.post("/echo")
def echo(message: str):
    return {"message": message}
```

Now, if you go back to your browser and append `/echo` to the end of the URL, you should see the following:

```json
{"detail":"Method Not Allowed"}
```

This is because we haven't specified any data to send to the server. We need to send a POST request with some data in order to get a response. Thankfully, FastAPI has a built-in UI that we can use to test our web app. It's called "Swagger UI" and it's available at [localhost:8000/docs](http://localhost:8000/docs).

Now you can try your POST request by clicking on the endpoint (it should be a big green button with the endpoint name "echo" on it) and then clicking on the "Try it out" button!

Let's do a quick check-in of the whole Python file to make sure we're all on the same page.

<details>
<summary>app.py file up to this pointl</summary>

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/echo")
def echo(message: str):
    return {"message": message}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
```
</details>

### 3.4 Pydantic Models

You'll notice that we have a `message` parameter in our `echo` function. This is a string that we're expecting to be sent to the server. 

```python
def echo(message: str):
    return {"message": message}
```

Now imagine we wanted to send more than just a string to our server. Or maybe we wanted to send a string and a name. Or maybe we wanted to send a list of strings!

We could do this by adding more parameters to our function, but this would get very messy very quickly. 

```python
def echo(message: str, name: str):
    return {"message": message, "name": name}
```

Instead, we can use a Pydantic model to define the data we're expecting to receive. 

```python
from pydantic import BaseModel

class TextToTranslate(BaseModel):
    input_text: str
```

Now, we can use this model as a parameter in our function. 

```python
def echo(text_to_translate: TextToTranslate):
    return {"message": text_to_translate.input_text}
```

Notice that we're no longer passing in a string, but instead we're passing in an instance of our `TextToTranslate` class, which has a single attribute called `input_text`.

Now, if we go back to our Swagger UI and try out our POST request, we'll see that we can send a JSON object with a single attribute called `input_text` and it will be returned to us.

```json
{
  "input_text": "Hello World"
}
```

```json
{
  "message": "Hello World"
}
```

Make sure to add this to your `app.py` file!

<details><summary>app.py file with Pydantic model</summary>

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextToTranslate(BaseModel):
    input_text: str

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/echo")
def echo(text_to_translate: TextToTranslate):
    return {"message": text_to_translate.input_text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
```
</details>

### 3.5: Adding our local pipeline to the web app

Now that we have a basic grasp of how FastAPI works, let's add our local pipeline to our web app! 

First things first, we want to load this pipeline only once when the server starts up. We don't want to load it every time a request is made, because that would be very slow. 

```python
from fastapi import FastAPI
from pydantic import BaseModel

pipeline = # complete this line with the code to load the pipeline from the local files (path to model directory for 

app = FastAPI()
```

### 3.6: Adding a POST request to translate using our pipeline

Now that we have our pipeline loaded, we can add a new POST request to our web app that will use our pipeline to translate the text we send to it!

Go ahead and work with your partner to add this new POST request to your web app and test it out using the Swagger UI!

### 3.7: Batch Translation with a POST request

Now that we have a POST request that can translate a single string, let's add a new POST request that can translate a list of strings!

We don't want to mess with our main app, so we'll want to make a new branch for this new feature. 

You can use the following command to create a new branch called `batch-translation`.

```bash
git checkout -b batch-translation
```

Now that we're on our new branch, we can add our new feature!

1. Add a new pydantic model called `TextsToTranslate` that has a single attribute called `input_texts` that is a list of strings.
2. Add a new POST request to your web app that takes in a `TextsToTranslate` object and returns a list of translated strings.
3. Test out your new POST request using the Swagger UI!

### 3.8: Merging our new feature into the main branch

Now that we've added our new feature, we want to merge it into the main branch.

We'll want to: 

1. Stage and commit our changes
2. Push our new branch with the changes to our remote repository (your personal GitHub repo)
3. Create a pull request to merge our new branch into the main branch
4. Merge the pull request

### Conclusion

If you've made it this far, great! You've successfully created a web app that can translate text using a pipeline that you've gotten from the Hugging Face Hub!





