# Generated by Django 4.1.6 on 2023-02-13 15:54
from django.core.management.sql import emit_post_migrate_signal
from django.db import migrations


def creer_groupes(apps, schema_migration):
    emit_post_migrate_signal(verbosity=1, interactive=False, db="default")
    Permission = apps.get_model("auth", "Permission")

    add_personnel = Permission.objects.get(codename="add_personnel")
    view_personnel = Permission.objects.get(codename="view_personnel")
    change_personnel = Permission.objects.get(codename="change_personnel")
    delete_personnel = Permission.objects.get(codename="delete_personnel")

    add_client = Permission.objects.get(codename="add_client")
    view_client = Permission.objects.get(codename="view_client")
    change_client = Permission.objects.get(codename="change_client")

    add_contrat = Permission.objects.get(codename="add_contrat")
    view_contrat = Permission.objects.get(codename="view_contrat")
    change_contrat = Permission.objects.get(codename="change_contrat")

    add_evenement = Permission.objects.get(codename="add_evenement")
    view_evenement = Permission.objects.get(codename="view_evenement")
    change_evenement = Permission.objects.get(codename="change_evenement")

    gestion_permissions = [add_personnel, view_personnel, change_personnel, delete_personnel,
                           view_client, change_client,
                           view_contrat, change_contrat,
                           view_evenement, change_evenement]

    vente_permissions = [add_client, view_client, change_client,
                         add_contrat, view_contrat, change_contrat,
                         add_evenement, view_evenement, change_evenement]

    support_permissions = [view_client, view_evenement, change_evenement]

    Group = apps.get_model("auth", "Group")

    gestion = Group(name="gestion")
    gestion.save()
    gestion.permissions.set(gestion_permissions)

    vente = Group(name="vente")
    vente.save()
    vente.permissions.set(vente_permissions)

    support = Group(name="support")
    support.save()
    support.permissions.set(support_permissions)

    Personnel = apps.get_model("connexion", "Personnel")
    for personne in Personnel.objects.all():
        if personne.equipe == "GESTION":
            gestion.user_set.add(personne)
        if personne.equipe == "VENTE":
            vente.user_set.add(personne)
        if personne.equipe == "SUPPORT":
            support.user_set.add(personne)


class Migration(migrations.Migration):

    dependencies = [
        ('connexion', '0002_remove_personnel_username_personnel_equipe_and_more'),
    ]

    operations = [
        migrations.RunPython(creer_groupes)
    ]