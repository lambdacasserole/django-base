# Django Base Template
Basic Django project for a simple website.

I'm presenting here a clean (-ish) starting point for a website written in Python on Django. This is the stripped-down and skeletonised version of my old personal website which was a cool experiment in Django but otherwise pretty unimpressive. I've since moved on.

![GitHub Logo](https://raw.githubusercontent.com/lambdacasserole/django-base/master/screenshot.png)

## Prerequisites
You'll need to have Python 2 and Django installed and configured for this to work. The [Python](https://www.python.org/downloads/) and [Django](https://docs.djangoproject.com/en/1.9/topics/install/) websites have some pretty good tutorials on this. Once you've done that you can proceed.

You'll also need [Node.js](https://nodejs.org/en/) and [npm](https://www.npmjs.com/) installed and working.

## Configuration
A couple of files need changing to get the site working for you.

1. Copy `sensitive.py.dist` and rename it to `sensitive.py`. Fill in the fields according to their descriptions and save.
2. Locate `blog.coffee` and fill in the `blogId` and `apiKey` fields to get your blog working.

## Building
Clone the project down and open the folder in your favourite editor. It's a JetBrains PyCharm project but you can use whichever paid/free software takes your fancy. 

First, install the npm packages necessary to build and run the website. Run the following in your terminal in the project root directory:

```
npm install
```

This will install [Bower](https://bower.io/) which will allow you to install the assets the website requires (Bootstrap, jQuery etc.) using the command:

```
bower install
```

Gulp will also have been installed. This will compile the [Less](http://lesscss.org/) and [CoffeeScript](http://coffeescript.org/) into CSS and JavaScript ready for production. Do this using the command:

```
gulp
```

This command will need running again every time you make a change to a Less or CoffeeScript file. If you're working on them, run `gulp watch` in a terminal to watch for file changes and compile accordingly.

Now run the following command in a terminal (make sure the Python directory is in your PATH):

```
python manage.py runserver
```

Then navigate to `http://localhost:8000/` to see the site up and running!

## Limitations

I'm not a web designer. The site isn't going to bring a tear to your eye with its beauty. 
