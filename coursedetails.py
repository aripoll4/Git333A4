class CourseDetails:
    def __init__(self, crsid, days, sttime, endtime, bldg, rm, depts_crsnum, area, title, descrip, prereqs, profs):
        self._crsid = crsid
        self._days = days
        self._sttime = sttime
        self._endtime = endtime
        self._bldg = bldg
        self._rm = rm
        self._depts_crsnum = depts_crsnum
        self._descrip = descrip
        self._area = area
        self._title = title
        self._prereqs = prereqs
        self._profs = profs
    
    def get_crsid(self):
        return self._crsid
    
    def get_days(self):
        return self._days

    def get_sttime(self):
        return self._sttime

    def get_endtime(self):
        return self._endtime

    def get_bldg(self):
        return self._bldg

    def get_rm(self):
        return self._rm
    
    def get_depts_crsnum(self):
        return self._depts_crsnum

    def get_descrip(self):
        return self._descrip
    
    def get_area(self):
        return self._area
    
    def get_title(self):
        return self._title

    def get_prereqs(self):
        return self._prereqs
    
    def get_profs(self):
        return self._profs
