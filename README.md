# Using Django

## How is this Project different than Flask (or Node) application. What role are the '''urls.py''' and '''views.py''' files responsible for?
    Django is a full-stack framework, whereas Flask is a micro and lightweight web framework. In comparison to Node JS, which is used with JavaScript, you would need to have a undersatnding of asynchronous programming, including Node's native methods and architecture. Node is slightly more difficult for beginners because of some complex concepts.

## Why do we use 2 separate '''urls.py''' files? How do they interact
    Inside the root folder, the '''urls.py''' file is used as the "table of the contents' while the other '''urls.py''' file inside the app connects to that file and use the url connected to that. 

## When is it desirable to split our code over multiple apps? Why would we want to do so?
   It's desirable to split our code over multiple apps when we have multiple features inside a larger project. This way we can structure our code so its easier to read.
