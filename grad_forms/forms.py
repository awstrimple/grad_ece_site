from django import forms

class BasePos(forms.Form):
    student_first_name = forms.CharField()
    student_last_name = forms.CharField()
    advisor_first_name = forms.CharField()
    advisor_last_name = forms.CharField()


class CourseForm(forms.Form):
    course_number = forms.CharField()
    course_title = forms.CharField()
    course_grade = forms.CharField()
    course_semester = forms.CharField()


class MSPoSCoursework(BasePos):
    pass
