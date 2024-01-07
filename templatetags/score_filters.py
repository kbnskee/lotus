from django import template

register = template.Library()

from apps.teacher.models import(
    StudentWrittenWorkScores,
    PerformanceTaskScore,
    ParticipationScore,
    QuarterlyAssessmentScore
)

from apps.students.models import(
    StudentSubjectGrade,
    StudentSubject
)

@register.filter(name='get_ww_score')
def get_ww_score(stud, act):
    if act:
        if StudentWrittenWorkScores.objects.filter(student_name = stud, activity_info = act).exists():
            score = StudentWrittenWorkScores.objects.get(student_name = stud, activity_info = act)
            print(score.score)
            return score.score
        else:
            return "N/A"
    else:
        return "N/A"
    
@register.filter(name='get_pt_score')
def get_pt_score(stud, act):
    if act:
        if PerformanceTaskScore.objects.filter(student_name = stud, activity_info = act).exists():
            score = PerformanceTaskScore.objects.get(student_name = stud, activity_info = act)
            return score.score
        else:
            return "N/A"
    else:
        return "N/A"

@register.filter(name='get_pa_score')
def get_pa_score(stud, act):
    if act:
        if ParticipationScore.objects.filter(student_name = stud, activity_info = act).exists():
            score = ParticipationScore.objects.get(student_name = stud, activity_info = act)
            return score.score
        else:
            return "N/A"
    else:
        return "N/A"
    
@register.filter(name='get_qa_score')
def get_qa_score(stud, act):
    if act:
        if QuarterlyAssessmentScore.objects.filter(student_name = stud, activity_info = act).exists():
            score = QuarterlyAssessmentScore.objects.get(student_name = stud, activity_info = act)
            return score.score
        else:
            return "N/A"
    else:
        return "N/A"
    
@register.filter(name='get_final_grade')
def get_final_grade(stud, grades):
    if grades:
        if grades.filter(student = stud).exists():
            score = grades.get(student = stud)
            return score.final_grade
        else:
            return 70
    else:
        return 70
    
@register.filter(name='get_activity_total')
def get_activity_total(activity):
    if activity:
        total = 0
        for act in activity:
            total = total + act.total_score
        return total
    else:
        return 0
    
@register.filter(name='get_subject_grade_q1')
def get_subject_grade_q1(stud, subj):
    
    if StudentSubjectGrade.objects.filter(student = stud, subject = subj, quarter = 1).exists():
        final_grade = StudentSubjectGrade.objects.get(student = stud, subject = subj, quarter = 1)
        return final_grade.final_grade
    else:
        return "N/A"
    
@register.filter(name='get_subject_grade_q2')
def get_subject_grade_q2(stud, subj):
    if StudentSubjectGrade.objects.filter(student = stud, subject = subj, quarter = 2).exists():
        final_grade = StudentSubjectGrade.objects.get(student = stud, subject = subj, quarter = 2)
        return final_grade.final_grade
    else:
        return "N/A"
    
@register.filter(name='get_subject_grade_q3')
def get_subject_grade_q3(stud, subj):
    
    if StudentSubjectGrade.objects.filter(student = stud, subject = subj, quarter = 3).exists():
        final_grade = StudentSubjectGrade.objects.get(student = stud, subject = subj, quarter = 3)
        return final_grade.final_grade
    else:
        return "N/A"
    
@register.filter(name='get_subject_grade_q4')
def get_subject_grade_q4(stud, subj):
    
    if StudentSubjectGrade.objects.filter(student = stud, subject = subj, quarter = 4).exists():
        final_grade = StudentSubjectGrade.objects.get(student = stud, subject = subj, quarter = 4)
        return final_grade.final_grade
    else:
        return "N/A"
    


@register.filter(name='get_mapeh_grade')
def get_mapeh_grade(stud, quarter):
    grade = 0
    if StudentSubjectGrade.objects.filter(student = stud, subject__subject__type_id = 7, quarter = quarter).exists():
        subject = StudentSubjectGrade.objects.filter(student = stud, subject__subject__type_id = 7, quarter = quarter)
        for m in subject:
            grade = grade + ((m.final_grade * m.subject.subject.subject_impact)/100)
    return grade

@register.filter(name='get_tle_grade')
def get_tle_grade(stud, quarter):
    grade = 0
    if StudentSubjectGrade.objects.filter(student = stud, subject__subject__type_id = 4, quarter = quarter).exists():
        subject = StudentSubjectGrade.objects.filter(student = stud, subject__subject__type_id = 4, quarter = quarter)
        for m in subject:
            grade = grade + ((m.final_grade * m.subject.subject.subject_impact)/100)
    return grade

@register.filter(name='get_specialize_grade')
def get_specialize_grade(stud, quarter):
    if StudentSubjectGrade.objects.filter(student = stud, subject__subject__type_id = 1, quarter = quarter).exists():
        subject = StudentSubjectGrade.objects.get(student = stud, subject__subject__type_id = 1, quarter = quarter)
        return subject.final_grade
    else:
        return 0

@register.filter(name='get_final_grade_average')
def get_final_grade_average(stud, subj):
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    if get_subject_grade_q1(stud, subj) != "N/A":
        q1 = get_subject_grade_q1(stud, subj)
    if get_subject_grade_q2(stud, subj) != "N/A":
        q2 = get_subject_grade_q1(stud, subj)
    if get_subject_grade_q3(stud, subj) != "N/A":
        q3 = get_subject_grade_q1(stud, subj)
    if get_subject_grade_q4(stud, subj) != "N/A":
        q4 = get_subject_grade_q1(stud, subj)

    f_grade = (q1+q2+q3+q4)/4
    return f_grade

@register.filter(name='get_mapeh_final_average')
def get_mapeh_final_average(stud):
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    q1 = get_mapeh_grade(stud, 1)
    q2 = get_mapeh_grade(stud, 2)
    q3 = get_mapeh_grade(stud, 3)
    q4 = get_mapeh_grade(stud, 4)

    f_grade = (q1+q2+q3+q4)/4
    return f_grade

@register.filter(name='get_tle_final_average')
def get_tle_final_average(stud):
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    q1 = get_tle_grade(stud, 1)
    q2 = get_tle_grade(stud, 2)
    q3 = get_tle_grade(stud, 3)
    q4 = get_tle_grade(stud, 4)

    f_grade = (q1+q2+q3+q4)/4
    return f_grade


@register.filter(name='get_student_core_subjects')
def get_student_core_subjects(stud):
    return StudentSubject.objects.filter(student = stud, subject__subject__type_id = 2)

@register.filter(name='get_student_mapeh_subjects')
def get_student_mapeh_subjects(stud):
    return StudentSubject.objects.filter(student = stud, subject__subject__type_id = 7)

@register.filter(name='get_student_tle_subjects')
def get_student_tle_subjects(stud):
    return StudentSubject.objects.filter(student = stud, subject__subject__type_id = 4)

@register.filter(name='get_student_specialize_subjects')
def get_student_specialize_subjects(stud):
    return StudentSubject.objects.filter(student = stud, subject__subject__type_id = 1)
