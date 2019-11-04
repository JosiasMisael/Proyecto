# Generated by Django 2.2.6 on 2019-11-04 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['-nombre'], 'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterModelOptions(
            name='pais',
            options={'ordering': ['-nombre'], 'verbose_name': 'Pais', 'verbose_name_plural': 'Paises'},
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='created',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='Pais',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='encargado',
        ),
        migrations.RemoveField(
            model_name='pais',
            name='created',
        ),
        migrations.AddField(
            model_name='autor',
            name='Pais',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proyecto.Pais'),
        ),
        migrations.AddField(
            model_name='autor',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='libro',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proyecto.Categoria'),
        ),
        migrations.AddField(
            model_name='libro',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='imagen'),
        ),
        migrations.AddField(
            model_name='libro',
            name='publicacion',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Autor')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Libro')),
            ],
        ),
        migrations.AddField(
            model_name='libro',
            name='autor',
            field=models.ManyToManyField(through='proyecto.Asignacion', to='proyecto.Autor'),
        ),
    ]