# Generated by Django 3.2.6 on 2021-08-28 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ERC721',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tokenId', models.CharField(max_length=200)),
                ('metadataURI', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RecordLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=200)),
                ('state', models.CharField(choices=[('DRAFT', 'Draft'), ('MINTED', 'Minted'), ('PUBLISHED', 'Published')], max_length=200)),
                ('audio_hash', models.CharField(max_length=200)),
                ('fingerprint', models.BinaryField()),
                ('recordlabel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rlp_records.recordlabel')),
                ('token', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rlp_records.erc721')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('recordlabel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rlp_records.recordlabel')),
            ],
        ),
    ]
