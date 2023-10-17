import datetime


def id_generator(roleid, firstname, id):
    dio = "d" + str(roleid) + str(ord(firstname[0])+99)+ "-" + str(id)+str(datetime.datetime.now().day+99)
    return (dio)

def employee_id_generator(school_id, role_id, id):
    current_datetime = datetime.datetime.now()
    school_id=str(school_id)
    role_id=str(role_id)
    id=str(id)
    dio=str(current_datetime.year % 100)+"-"+str(school_id.zfill(2))+str(role_id.zfill(2))+"-"  +str(id.zfill(4))
    print(dio)
    return dio