

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grievance',
            old_name='description',
            new_name='message',
        ),
    ]
