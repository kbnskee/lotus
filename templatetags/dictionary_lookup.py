from django import template
from apps.adviserms.models import AdviserStudentAttendance
from apps.principal.models import SchoolDaysInMonth

register = template.Library()




@register.filter(name='month_lookup')
def month_lookup(lst, args):
    for item in lst:
        if item.month == args:
            return item.days
    return 0

@register.filter(name='get_month_days')
def get_month_days(lst, args):
    for item in lst:
        if item.month == args:
            return int(item.days)
    return 0

@register.filter(name='get_student_absent')
def get_student_absent(stud, month):
    if AdviserStudentAttendance.objects.filter(student_id = stud, month_id = month).exists():
        absent = AdviserStudentAttendance.objects.get(student_id = stud, month_id = month)
        absent = absent.number_of_absent
    else:
        return 0
    return int(absent)

@register.filter(name='get_student_late')
def get_student_late(stud, month):
    if AdviserStudentAttendance.objects.filter(student_id = stud, month_id = month).exists():
        absent = AdviserStudentAttendance.objects.get(student_id = stud, month_id = month)
        absent = absent.number_of_late
    else:
        return 0
    return int(absent)


@register.filter(name='get_total_absent')
def get_total_absent(stud, month):
    late_to_absent = int(get_student_late(stud, month)/3)
    absent = get_student_absent(stud, month)
    total = late_to_absent + absent
    return int(total)

@register.filter(name='get_present')
def get_present(days, absent):
    total = days - absent
    return int(total)
