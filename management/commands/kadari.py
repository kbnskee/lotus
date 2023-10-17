import os
from pathlib import Path
from django.core.management.base import BaseCommand
from django.core.management import call_command

from lotus.conf import BASE_DATA

from lotus.models import (
    User,
    App,
    Page,
    Group,
    AppGroup,
    PageGroup,
    UserGroup,
)

base_dir=BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

class Command(BaseCommand):
    help = "kadari"

    def add_arguments(self, parser):
        parser.add_argument("arg", type=str)

    def handle(self, *args, **kwargs):
        _arg=kwargs['arg']
        if _arg=="info":
            self.stdout.write(f"kadari 1.0")

        elif _arg=="clearbasedata":
            self.clear_tables()

        elif _arg=="updatebasedata":
            self.stdout.write("Initializing updatebasedata...")
            for list in BASE_DATA:
                call_command('loaddata',os.path.join(base_dir,list.replace(".","/")))
                self.stdout.write(f"loading {list}... OK")
            self.stdout.write("updatebasedata... OK")
        elif _arg=="loadbasedata":
            self.stdout.write("Initializing loadbasedata...")
            self.clear_tables()    
            
            for list in BASE_DATA:
                call_command('loaddata',os.path.join(base_dir,list.replace(".","/")))
                self.stdout.write(f"loading {list}... OK")
            
            user=User(username="kadari")
            user.set_password("kadari")
            user.save()

            user_instance=User.objects.get(username="kadari")
            group_instance=Group.objects.get(name="superuser")
            self.stdout.write("creating Group... OK")
            
            user_group=UserGroup.objects.create(user=user_instance,group=group_instance)
            user_group.save()
            self.stdout.write("creating UserGroup... OK")

            apps=App.objects.filter()
            for app in apps:
                AppGroup.objects.create(group=group_instance,app=app)
                self.stdout.write(f"creating AppGroup {app}... OK")
            pages=Page.objects.filter()
            for page in pages:
                PageGroup.objects.create(group=group_instance,page=page)
                self.stdout.write(f"creating PageGroup {page}... OK")

            self.stdout.write("loadbasedata... OK")
        else:    
            user=User.objects.filter(username=_arg)
            if user.exists():
                self.stdout.write(f"Initializing KADARI APPLICATION. This may take a few minutes to complete...")

                self.stdout.write(f"KADARI APPLICATION COMPLETE. ")
            else:
                self.stdout.write(f"Invalid action for init-kadari and {_arg}. This action will be reported.")

    def clear_tables(self):
        answer=input(f"This command clears all Role, App, AppUser, Page, PageUser in your database. Do you want to continue? Yes or No. Default=Yes... ")
        if answer=="Yes" or not answer.strip():
            App.objects.all().delete()
            Page.objects.all().delete()
            Group.objects.all().delete()
            AppGroup.objects.all().delete()
            PageGroup.objects.all().delete()
            UserGroup.objects.all().delete()
            self.stdout.write(f"Clearing tables... Ok")
        else:
            self.stdout.write(f"loadbasedata... Cancelled")
            