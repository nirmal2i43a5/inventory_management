import os
import csv
from io import StringIO
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Product, ProductBulkUpload

@receiver(post_save, sender=StudentBulkUpload)
def create_bulk_student(sender, created, instance, *args, **kwargs):
  if created:
    opened = StringIO(instance.csv_file.read().decode())
    reading = csv.DictReader(opened, delimiter=',')
    students = []
    for row in reading:
      if 'registration_number' in row and row['registration_number']:
        reg = row['registration_number']
        lastname = row['lastname'] if 'lastname' in row and row['lastname'] else ''
        firstname = row['firstname'] if 'firstname' in row and row['firstname'] else ''
        gender = (row['gender']).lower(
        ) if 'gender' in row and row['gender'] else ''
        phone = row['parent_number'] if 'parent_number' in row and row['parent_number'] else ''
        address = row['address'] if 'address' in row and row['address'] else ''
        current_class = row['current_class'] if 'current_class' in row and row['current_class'] else ''
        if current_class:
          theclass, kind = StudentClass.objects.get_or_create(name=current_class)

        check = Student.objects.filter(registration_number=reg).exists()
        if not check:
          students.append(
            Student(
                registration_number=reg,
                lastname=lastname,
                firstname=firstname,
                gender=gender,
                current_class=theclass,
                parent_mobile_number=phone,
                address=address,
                current_status='active'
            )
          )

    Student.objects.bulk_create(students)
    instance.csv_file.close()
    instance.delete()


def _delete_file(path):
   """ Deletes file from filesystem. """
   if os.path.isfile(path):
       os.remove(path)

@receiver(post_delete, sender=StudentBulkUpload)
def delete_csv_file(sender, instance, *args, **kwargs):
  if instance.csv_file:
    _delete_file(instance.csv_file.path)


@receiver(post_delete, sender=Student)
def delete_passport_on_delete(sender, instance, *args, **kwargs):
  if instance.passport:
    _delete_file(instance.passport.path)
