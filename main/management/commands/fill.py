from django.core.management import BaseCommand

from main.models import Student


class Command(BaseCommand):

    def handle(self, *args, **options):
        student_list = [
            {'last_name': 'Иванов', 'first_name': 'Иван'},
            {'last_name': 'Петров', 'first_name': 'Петр'},
            {'last_name': 'Семенов', 'first_name': 'Семен'},
            {'last_name': 'Александров', 'first_name': 'Александр'}
        ]

        # for student_item in student_list:
        #     Student.objects.create(**student_item)

        students_to_create = []
        for student_item in student_list:
            students_to_create.append(
                Student(**student_item)
            )

        Student.objects.bulk_create(students_to_create)
