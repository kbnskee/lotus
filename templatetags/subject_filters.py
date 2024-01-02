from django import template
from apps.students.models import StudentSubjectGrade
from apps.subjectms.models import SubSubject
from apps.sectionms.models import SectionSubjects
from django.db.models import Sum

register = template.Library()




@register.filter(name='q1_subject_grades')
def q1_subject_grades(student, subject):
    if StudentSubjectGrade.objects.filter(student=student, subject=subject, quarter=1).exists():
        grade = StudentSubjectGrade.objects.get(student=student, subject=subject, quarter=1).final_grade
    else:
        grade = "N/A"
    return grade


@register.filter(name='q1_subject_grades_mother')
def q1_subject_grades_mother(student, subject):
    sub_subjects = SubSubject.objects.filter(parent_subject=subject)
    child_subjects = SectionSubjects.objects.filter(sub_subject__in=sub_subjects)
    grades = StudentSubjectGrade.objects.filter(student=student, subject__in=child_subjects, quarter = 1)
    computed_grade = 0
    if grades.exists():
        for gr in grades:
            print(gr.final_grade)
            print(gr.subject.sub_subject.subject_impact)
            computed_grade += (gr.final_grade * gr.subject.sub_subject.subject_impact)/100
        return computed_grade
    else:
        return "N/A"
    
@register.filter(name='q2_subject_grades')
def q2_subject_grades(student, subject):
    if StudentSubjectGrade.objects.filter(student=student, subject=subject, quarter=2).exists():
        grade = StudentSubjectGrade.objects.get(student=student, subject=subject, quarter=2).final_grade
    else:
        grade = "N/A"
    return grade

@register.filter(name='q2_subject_grades_mother')
def q2_subject_grades_mother(student, subject):
    sub_subjects = SubSubject.objects.filter(parent_subject=subject)
    child_subjects = SectionSubjects.objects.filter(sub_subject__in=sub_subjects)
    grades = StudentSubjectGrade.objects.filter(student=student, subject__in=child_subjects, quarter = 2)
    computed_grade = 0
    if grades.exists():
        for gr in grades:
            print(gr.final_grade)
            print(gr.subject.sub_subject.subject_impact)
            computed_grade += (gr.final_grade * gr.subject.sub_subject.subject_impact)/100
        return computed_grade
    else:
        return "N/A"
    
@register.filter(name='q3_subject_grades')
def q3_subject_grades(student, subject):
    if StudentSubjectGrade.objects.filter(student=student, subject=subject, quarter=3).exists():
        grade = StudentSubjectGrade.objects.get(student=student, subject=subject, quarter=3).final_grade
    else:
        grade = "N/A"
    return grade

@register.filter(name='q3_subject_grades_mother')
def q3_subject_grades_mother(student, subject):
    sub_subjects = SubSubject.objects.filter(parent_subject=subject)
    child_subjects = SectionSubjects.objects.filter(sub_subject__in=sub_subjects)
    grades = StudentSubjectGrade.objects.filter(student=student, subject__in=child_subjects, quarter = 3)
    computed_grade = 0
    if grades.exists():
        for gr in grades:
            print(gr.final_grade)
            print(gr.subject.sub_subject.subject_impact)
            computed_grade += (gr.final_grade * gr.subject.sub_subject.subject_impact)/100
        return computed_grade
    else:
        return "N/A"
    
    
@register.filter(name='q4_subject_grades')
def q4_subject_grades(student, subject):
    if StudentSubjectGrade.objects.filter(student=student, subject=subject, quarter=4).exists():
        grade = StudentSubjectGrade.objects.get(student=student, subject=subject, quarter=4).final_grade
    else:
        grade = "N/A"
    return grade

@register.filter(name='q4_subject_grades_mother')
def q4_subject_grades_mother(student, subject):
    sub_subjects = SubSubject.objects.filter(parent_subject=subject)
    child_subjects = SectionSubjects.objects.filter(sub_subject__in=sub_subjects)
    grades = StudentSubjectGrade.objects.filter(student=student, subject__in=child_subjects, quarter = 4)
    computed_grade = 0
    if grades.exists():
        for gr in grades:
            print(gr.final_grade)
            print(gr.subject.sub_subject.subject_impact)
            computed_grade += (gr.final_grade * gr.subject.sub_subject.subject_impact)/100
        return computed_grade
    else:
        return "N/A"
    