
#!/usr/bin/env python

#----------------------------------------------------
# webversion1.py
# Authors: Author: Wangari Karani, Alfred Ripoll               
#----------------------------------------------------

import flask
import dbquery

app = flask.Flask(__name__, template_folder='.')

@app.route('/', methods = ['GET'])
@app.route('/course_search', methods = ['GET'])
def course_search():
    dept = flask.request.args.get("dept")
    if dept is None:
        dept = ""
    num = flask.request.args.get("num")
    if num is None:
        num = ""
    area = flask.request.args.get("area")
    if area is None:
        area = ""
    title = flask.request.args.get("title")
    if title is None:
        title = ""

    # Error Handling
    success, courses = dbquery.DBQuery.a1reg(dept, num, area, title)
    if success != True:
        error_msg = "A server error occured. Please contact the system administrator."
        html_code =  flask.render_template("errorpage.html", error_msg = error_msg)
        response = flask.make_response(html_code)
        return response

    html_code = flask.render_template("classsearch.html", 
        prev_dept = dept, prev_num = num, prev_area = area, prev_title = title, courses = courses)
    response = flask.make_response(html_code)
    response.set_cookie('prev_dept', prev_dept, 'prev_num', prev_num, 'prev_area', prev_area, 'prev_title', prev_title)
    return response
    
@app.route("/course_details", methods = ['GET'])
def course_details():
    classid = flask.request.args.get("classid")

    if classid == "" or classid is None:
        error_msg = "Missing classid"
        html_code = flask.render_template("errorpage.html", error_msg = error_msg)
        response = flask.make_response(html_code)
        return response

    try:
        isinstance(int(classid), int)
    except:
        error_msg = "Non-integer classid"
        html_code = flask.render_template("errorpage.html", error_msg = error_msg)
        response = flask.make_response(html_code)
        return response
    
    prev_classid = classid
    success, course_detail = dbquery.DBQuery.a1regdetails(classid)
    if success != True:
        if course_detail == "Non-existing classid":
            error_msg = "no class with classid " + classid + " exists"
        else:
            error_msg = "A server error occured. Please contact the system administrator."
        html_code = flask.render_template("errorpage.html", error_msg = error_msg)
        response = flask.make_response(html_code)
        return response
        
    html_code = flask.render_template("classdetails.html", classid = classid, course_detail = course_detail)
    response = flask.make_response(html_code)
    response.set_cookie('prev_classid', prev_classid)
    return response
