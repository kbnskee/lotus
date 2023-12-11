import os, sys
from pathlib import Path
from django.core.management.base import BaseCommand
from django.core.management import call_command
import openpyxl

from lotus.conf import BASE_DATA

from lotus.models import (
    User,
    App,
    Page,
    Group,
    GroupApp,
    GroupPage,
    UserGroup,
)

base_dir=BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


def importer():
    import pandas
    df=pandas.read_excel("predefined_data.xls")
    


class Command(BaseCommand):
    help = "kadari"

    def add_arguments(self, parser):
        parser.add_argument("arg", type=str)

    def handle(self, *args, **kwargs):
        _arg=kwargs['arg']

        if _arg=="info":
            self.__info()

        elif _arg=="init-app":
            self.__init_app()

        elif _arg=="clearbasedata":
            self.__clear_tables()

        elif _arg=="reset":
            self.__reset()

        elif _arg=="factoryreset":
            self.__factory_reset()

        elif _arg=="show-excel-models":
            self.__get_excel_models()
                
        elif _arg=="createsuperuser":
            self.__create_superuser()


    def __info(self):
        self.stdout.write(f"kadari 1.0")

    def __init_app(self):
        self.__delete_table_contents()
        self.__create_superuser()
        self.__create_superuser_group()
        self.__create_suuperuser_usergroup()
        self.__create_lotus_app()
        self.__create_lotus_pages()
        self.__upload_excel()

        
    
    def __reset(self):
        self.stdout.write("Exiting...")
        sys.exit()

    def __delete_table_contents(self):
        self.stdout.write("1. Deleting Table Contents...")
        User.objects.all().delete()
        App.objects.all().delete()
        Page.objects.all().delete()
        Group.objects.all().delete()
        
        self.stdout.write("1. Deleting Table Contents...OK!")

    def __create_superuser(self):
        self.stdout.write("2. Creating createsuperuser...")
        user=User(id=1,username="kadari")
        user.set_password("kadari")
        user.save()
        self.stdout.write("2. Creating createsuperuser...OK!")

    def __create_superuser_group(self):
        self.stdout.write("3. Createing Superuser Group...")
        group=Group(id=1,name="kadari")
        group.created_by=self.__get_superuser()
        group.save()
        self.stdout.write("3. Createing Superuser Group...OK!")

    def __get_superuser_group(self):
        return Group.objects.get(name="kadari")
    
    def __get_superuser(self):
        return User.objects.get(username="kadari")
    
    def __create_suuperuser_usergroup(self):
        self.stdout.write("4. creating createsuperuser...")
        user_group=UserGroup.objects.create(id=1,user=self.__get_superuser(),
                                            group=self.__get_superuser_group(),
                                            created_by=self.__get_superuser())
        user_group.save()
        self.stdout.write("4. creating createsuperuser... OK")



    def __create_lotus_app(self):
        self.stdout.write("5. Creating Lotus App...")
        App.objects.create(id=100,name="lotus",created_by_id=self.__get_superuser().id,is_enabled=True)
        self.stdout.write("5. Creating Lotus App... OK")
    

    def __get_lotus_app(self):
        return App.objects.get(id=100,name="lotus")

    
    def __create_lotus_pages(self):
        self.stdout.write("6. Creating Lotus Pages...")
        app=self.__get_lotus_app()
        Page.objects.create(id=str(app.id)+"001",app=app,path="lotus_app_list",name="lotus_app_list",is_enabled=True,created_by=self.__get_superuser())
        Page.objects.create(id=str(app.id)+"002",app=app,path="lotus_app_add",name="lotus_app_add",is_enabled=True,created_by=self.__get_superuser())
        Page.objects.create(id=str(app.id)+"003",app=app,path="lotus_app_details",name="lotus_app_details",is_enabled=True,created_by=self.__get_superuser())
        Page.objects.create(id=str(app.id)+"004",app=app,path="lotus_app_update",name="lotus_app_update",is_enabled=True,created_by=self.__get_superuser())
        Page.objects.create(id=str(app.id)+"005",app=app,path="lotus_app_delete",name="lotus_app_delete",is_enabled=True,created_by=self.__get_superuser())
        Page.objects.create(id=str(app.id)+"006",app=app,path="lotus_page_list",name="lotus_page_list",is_enabled=True,created_by=self.__get_superuser())
        Page.objects.create(id=str(app.id)+"007",app=app,path="lotus_page_add",name="lotus_page_add",is_enabled=True,created_by=self.__get_superuser())
        Page.objects.create(id=str(app.id)+"008",app=app,path="lotus_page_details",name="lotus_page_details",is_enabled=True,created_by=self.__get_superuser())
        Page.objects.create(id=str(app.id)+"009",app=app,path="lotus_page_update",name="lotus_page_update",is_enabled=True,created_by=self.__get_superuser())
        Page.objects.create(id=str(app.id)+"010",app=app,path="lotus_page_delete",name="lotus_page_delete",is_enabled=True,created_by=self.__get_superuser())
        Page.objects.create(id=str(app.id)+"011",app=app,path="lotus_group_list",name="lotus_group_list",is_enabled=True,created_by=self.__get_superuser())
        Page.objects.create(id=str(app.id)+"012",app=app,path="lotus_group_add",name="lotus_group_add",is_enabled=True,created_by=self.__get_superuser())
        Page.objects.create(id=str(app.id)+"013",app=app,path="lotus_group_details",name="lotus_group_details",is_enabled=True,created_by=self.__get_superuser())
        Page.objects.create(id=str(app.id)+"014",app=app,path="lotus_group_app_add",name="lotus_group_app_add",is_enabled=True,created_by=self.__get_superuser())
        Page.objects.create(id=str(app.id)+"015",app=app,path="lotus_group_page_add",name="lotus_group_page_add",is_enabled=True,created_by=self.__get_superuser())
        Page.objects.create(id=str(app.id)+"016",app=app,path="lotus_group_app_delete",name="lotus_group_app_delete",is_enabled=True,created_by=self.__get_superuser())
        Page.objects.create(id=str(app.id)+"017",app=app,path="lotus_group_update",name="lotus_group_update",is_enabled=True,created_by=self.__get_superuser())
        Page.objects.create(id=str(app.id)+"018",app=app,path="lotus_group_delete",name="lotus_group_delete",is_enabled=True,created_by=self.__get_superuser())
        Page.objects.create(id=str(app.id)+"019",app=app,path="lotus_user_list",name="lotus_user_list",is_enabled=True,created_by=self.__get_superuser())
        Page.objects.create(id=str(app.id)+"020",app=app,path="lotus_user_employee_details",name="lotus_user_employee_details",is_enabled=True,created_by=self.__get_superuser())
        Page.objects.create(id=str(app.id)+"021",app=app,path="lotus_user_student_details",name="lotus_user_student_details",is_enabled=True,created_by=self.__get_superuser())
        Page.objects.create(id=str(app.id)+"022",app=app,path="lotus_user_update",name="lotus_user_update",is_enabled=True,created_by=self.__get_superuser())
        Page.objects.create(id=str(app.id)+"023",app=app,path="lotus_user_delete",name="lotus_user_delete",is_enabled=True,created_by=self.__get_superuser())
        Page.objects.create(id=str(app.id)+"024",app=app,path="lotus_importer",name="lotus_importer",is_enabled=True,created_by=self.__get_superuser())
        Page.objects.create(id=str(app.id)+"025",app=app,path="lotus_404",name="lotus_404",is_enabled=True,created_by=self.__get_superuser())

        self.stdout.write("6. Creating Lotus Pages...OK!")


    def __upload_excel(self):
        self.stdout.write("7. Upload Excel...")
        excel_file_path = 'dio_predefined.xlsx'

        try:
            workbook = openpyxl.load_workbook(excel_file_path, read_only=True, data_only=True)

            # Loop through each sheet in the workbook
            for sheet in workbook.sheetnames:
                django_model = globals().get(sheet, None)
                print(f"django model: {django_model}")

                if django_model:
                    sheet_data = workbook[sheet]

                #     # Assuming the first row contains column headers
                    headers = [cell.value for cell in sheet_data[1]]

                #     # Loop through rows (excluding the header) and insert data into the corresponding model
                    for row in sheet_data.iter_rows(min_row=2, values_only=True):
                        data = dict(zip(headers, row))
                #         # Choose the model based on the sheet name
                        instance = django_model()

                #         # Set the instance fields based on the data from the row
                        for field, value in data.items():
                            setattr(instance, field, value)
                            self.stdout.write(str(instance) + str(value) + str(field))
                #         # Save the instance
                            instance.save()

                #     self.stdout.write(f'Data imported successfully from {sheet}.')
                # else:
                #     self.stdout.write(f'Model not found for sheet {sheet}. Check your models and sheet names.')

        except Exception as e:
            self.stdout.write(f'Error: {str(e)}')

        # Optionally, handle GET requests or provide a default response
        self.stdout.write("No action performed for GET request.")
        

    def __get_excel_models(self):
        excel_file_path = 'dio_predefined.xlsx'
        self.stdout.write("Generating List from dio_predefined.xlsx...")
        try:
            workbook = openpyxl.load_workbook(excel_file_path, read_only=True, data_only=True)
            for sheet in workbook.sheetnames:
                django_model = globals().get(sheet, None)
                self.stdout.write(f"django model: {django_model}")
            self.stdout.write("Generating List from dio_predefined.xlsx...OK!")
        except Exception as e:
            self.stdout.write(f'Error: {str(e)}...Exiting!')
            sys.exit()
        
    
    def __factory_reset(self):
        user_input = input("WARNING!!! This will reset the whole application. Are you sure you want to continue? Yes/No: ")
        if user_input.lower() == "no":
            self.stdout.write("Exiting...")
            sys.exit()
        elif user_input.lower() == "yes":
            final = input("Man, this is going to delete all your data! Are you sure? Yes/No: ")
            if final.lower()=="no":
                self.stdout.write("Exiting...")
                sys.exit()
            elif final.lower()=="yes":
                self.stdout.write("Okay then...")
                self.stdout.write("resetting...")
                User.objects.all().delete()
                App.objects.all().delete()
                Group.objects.all().delete()
                self.stdout.write("resetting...OK")
            else:
                self.stdout.write("Exiting...")
                sys.exit()
        else:
            self.stdout.write("Exiting...")
            sys.exit()
    
    

    def __clear_tables(self):
        answer=input(f"This command clears all Role, App, AppUser, Page, PageUser in your database. Do you want to continue? Yes or No. Default=Yes... ")
        if answer=="Yes" or not answer.strip():
            App.objects.all().delete()
            Page.objects.all().delete()
            Group.objects.all().delete()
            UserGroup.objects.all().delete()
            self.stdout.write(f"Clearing tables... Ok")
        else:
            self.stdout.write(f"loadbasedata... Cancelled")
            