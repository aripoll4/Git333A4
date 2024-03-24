#!/usr/bin/env python

#----------------------------------------------------
# cmv.py
# Authors: Author: Wangari Karani, Alfred Ripoll               
#----------------------------------------------------

import sys
import sqlite3
import contextlib
import textwrap

DATABASE_URL = 'file:reg.sqlite?mode=ro'

class Query:
    def __init__(self, query_type, dept, number, area, title, classid):
        self._dept = dept
        self._number = number
        self._area = area
        self._title = title
        self._classid = classid
    
    def get_dept(self):
        return self._dept

    def get_number(self):
        return self._number

    def get_area(self):
        return self._area

    def get_title(self):
        return self._title
    
    def get_classid(self):
        return self._classid

    @staticmethod
    def a1reg(query_type, dept, num, area, title):
        try:
            with sqlite3.connect(DATABASE_URL, isolation_level=None, uri=True) as connection:
                with contextlib.closing(connection.cursor()) as cursor:
                    class_info = []
                    stmt_str = "SELECT classid, dept, coursenum, area, title"
                    stmt_str += " FROM classes, courses, crosslistings"
                    stmt_str += " WHERE classes.courseid = courses.courseid"
                    stmt_str += " AND classes.courseid = crosslistings.courseid"

                    if dept != None:
                        dept = '%' + dept.replace("%", "/%").replace("_", "/_").lower() + '%'
                        stmt_str += " AND crosslistings.dept LIKE ? "
                        class_info.append(dept)
                    if num != None:
                        num = '%' + num.replace("%", "/%").replace("_", "/_").lower() + '%'
                        stmt_str += " AND crosslistings.coursenum LIKE ? "
                        class_info.append(num)
                    if area != None:
                        area = '%' + area.replace("%", "/%").replace("_", "/_").lower() + '%'
                        stmt_str += " AND courses.area LIKE ?"
                        class_info.append(area)
                    if title != None:
                        title = '%' + title.replace("%", "/%").replace("_", "/_").lower() + '%'
                        stmt_str += " AND courses.title LIKE ? "
                        class_info.append(title)

                    if dept == None and num == None and area == None and title == None:
                        stmt_str += " ORDER by dept, coursenum, classid"
                    else:
                        stmt_str += " ESCAPE '/' ORDER by dept, coursenum, classid"

                    cursor.execute(stmt_str, class_info)
                    row = cursor.fetchone()
                    overviews = []

                    while row != None:
                        # Call another class function here
                        queryadd =  '%5s %4s %6s %4s %s' % (row[0], row[1], row[2], row[3], row[4])
                        overviews.append(queryadd)
                        row = cursor.fetchone()
                    return overviews

        except Exception as ex:
            print(ex, file=sys.stderr)
        sys.exit(1)

    #----------------------------------------------------------------------

    @staticmethod
    def a1regdetails(query_type, classid):
        assert query_type == "getDetails"
        try:
            with sqlite3.connect(DATABASE_URL, isolation_level=None,uri=True) as connection:
                with contextlib.closing(connection.cursor()) as cursor:
                    stmt_str = "SELECT classid, classes.courseid, days, starttime, endtime, bldg, roomnum,"
                    stmt_str += " dept, coursenum, area, title, descrip, prereqs, coursesprofs.profid, profname"
                    stmt_str += " FROM classes, courses, crosslistings, coursesprofs, profs"
                    stmt_str += " WHERE classes.courseid = courses.courseid"
                    stmt_str += " AND classes.courseid = crosslistings.courseid"
                    stmt_str += " AND crosslistings.courseid = coursesprofs.courseid"
                    stmt_str += " AND coursesprofs.profid = profs.profid"
                    stmt_str += " AND classid = ?"

                    cursor.execute(stmt_str, [classid])
                    row = cursor.fetchone()
                    details = ""
                    while row != None:
                        wrapper = textwrap.TextWrapper(width = 72)
                        description = wrapper.wrap(text = str(row[11]))
                        details = 'Course Id: ' + str(row[1]) + '\n' + '\n'

                        details += 'Days: ' + str(row[2]) + '\n'
                        details += 'Start Time: ' + str(row[3]) + '\n'
                        details += 'End Time: ' + str(row[4]) + '\n'
                        details += 'Building: ' + str(row[5]) + '\n'
                        details += 'Room: ' + str(row[6]) + '\n' + '\n'

                        details += 'Dept and Number: ' + str(row[7]) + ' ' + str(row[8]) + '\n' + '\n'

                        details += 'Area: ' + str(row[9]) + '\n' + '\n'

                        details += 'Title: ' + str(row[10]) + '\n' + '\n'

                        details += 'Description: '
                        for line in description:
                            details += line
                        details += '\n' + '\n'

                        details += 'Prerequisites: ' + str(row[12]) + '\n' + '\n'

                        details += 'Professor: ' + str(row[14]) + '\n'

                        row = cursor.fetchone()

                        return details
                    
                    else:
                        err_str = "This class does not exist"
                        print(err_str, file=sys.stderr)
                        return False, err_str 
                    

        except Exception as ex:
            print(ex, file=sys.stderr)
            sys.exit(1)
