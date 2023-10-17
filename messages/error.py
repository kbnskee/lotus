from django.contrib import messages

def invalid_password():
    return "Invalid Username and or Password. Please try again!"


def alert(error,message):
    return {'error':error,'message':message}

