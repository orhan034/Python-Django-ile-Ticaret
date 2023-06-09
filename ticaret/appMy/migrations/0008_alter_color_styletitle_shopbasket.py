# Generated by Django 4.1.5 on 2023-03-17 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appMy', '0007_color_styletitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='styletitle',
            field=models.CharField(max_length=50, null=True, verbose_name='Renk class'),
        ),
        migrations.CreateModel(
            name='Shopbasket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_all', models.FloatField(default=0, verbose_name='Toplam Fiyat')),
                ('count', models.IntegerField(default=0, verbose_name='Adet')),
                ('product_letter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.sizeletter', verbose_name='Ürün Giysi')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
    ]
