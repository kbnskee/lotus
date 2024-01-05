from django import template

register = template.Library()

from apps.teacher.models import(
    StudentWrittenWorkScores,
    PerformanceTaskScore,
    ParticipationScore,
    QuarterlyAssessmentScore
)

from apps.students.models import(
    StudentSubjectGrade
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