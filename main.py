from flask import (Flask, render_template, request, make_response)
import json
import models
import static


from models.models import Myentry



app = Flask('app')


@app.route('/')
def index():
  
  return render_template("index.html",)


@app.route('/add', methods=['POST','GET'])
def add():
  data = dict(request.form.items()) 
    
  return render_template("add.html")

@app.route('/events', methods=['POST'])
def events():
    models.initialize()
    events = models.models.Myentry.select()
    return render_template("Events.html", events = events)


    
@app.route('/blogs')
def blogs():
    models.models.initialize()
    blogs = models.models.Myentry.select()
    return render_template("list_entry.html", blogs = blogs)



@app.route('/blogs/view', methods=['POST', 'GET'])
def view():
 models.models.initialize()
 blogs_number = models.models.Myentry.select()
 objects = []
 for blog in blogs_number:
   blog_item ={

      'title': blog.title,
      'body': blog.body,
      
   }
   objects.append(blog_item)
    
 return render_template("edit.html",blogs=objects)


    
  

app.run(debug=True, host='0.0.0.0', port=8080)