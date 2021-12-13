# Generated by Django 3.2.8 on 2021-12-11 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255, unique=True)),
                ('lieu', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('dureeTotale', models.DurationField()),
                ('dureeEnCour', models.DurationField()),
                ('dureeQuotidienne', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('expediteur', models.IntegerField()),
                ('destinataire', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('fonction', models.CharField(max_length=255)),
                ('statut', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('mdp', models.CharField(max_length=255)),
                ('photo', models.ImageField(null=True, upload_to='')),
                ('dateEnregistrement', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Professeur',
            fields=[
                ('personne_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Connection.personne')),
            ],
            bases=('Connection.personne',),
        ),
        migrations.CreateModel(
            name='Horaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joursDeCours', models.DateField()),
                ('heureDeDebut', models.TimeField()),
                ('specificite', models.CharField(max_length=255)),
                ('aEuLieu', models.BooleanField(default=False)),
                ('remarque', models.CharField(max_length=255)),
                ('formations', models.ManyToManyField(blank=True, related_name='horaires', to='Connection.Formation')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Connection.matiere')),
            ],
        ),
        migrations.AddField(
            model_name='formation',
            name='personnes',
            field=models.ManyToManyField(blank=True, related_name='formations', to='Connection.Personne'),
        ),
        migrations.AddField(
            model_name='formation',
            name='responsable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Connection.personne'),
        ),
        migrations.AddField(
            model_name='matiere',
            name='professeur',
            field=models.ManyToManyField(related_name='matieres', to='Connection.Professeur'),
        ),
    ]
