from lotus.models import User, ActivityLog

def filter(app,page,created_by,created_date):
    list=ActivityLog.objects.filter(
        app=app,
        page=page,
        created_by=created_by,
        created_date=created_date
    )
    return list

create = lambda page,remarks,user : ActivityLog.objects.create(page=page,remarks=remarks,created_by=user)
filter_by_app = lambda app : ActivityLog.objects.filter(app=app)
filter_by_page = lambda page : ActivityLog.objects.filter(page=page)
filter_by_creator = lambda creator : ActivityLog.objects.filter(created_by=creator)
filter_by_date = lambda date : ActivityLog.objects.filter(created_date=date)

get = lambda id : ActivityLog.objects.get(id=id)