# Generated by Django 4.0.5 on 2022-07-04 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_boxbachelor_meeting_image_meeting_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting',
            old_name='image',
            new_name='photo',
        ),
        migrations.AddField(
            model_name='meeting',
            name='Friday',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='Thursday',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='Wednesday',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='book_now',
            field=models.TextField(default='Book now'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meeting',
            name='link_facebbok',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='link_instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='link_linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='link_twitter',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='location',
            field=models.TextField(default='Popo city'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meeting',
            name='monday',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='saturday',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='sunday',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='tuesday',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='welcometext',
            name='mini_title',
            field=models.CharField(error_messages={'invalid': 'tu et b??te comment entre un carat??re laba'}, max_length=150),
        ),
    ]
