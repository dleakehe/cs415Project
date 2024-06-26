# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Characters(models.Model):
    characterid = models.AutoField(db_column='characterID', primary_key=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='class', max_length=30, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    race = models.CharField(max_length=30, blank=True, null=True)
    skill1 = models.CharField(max_length=30, blank=True, null=True)
    skill2 = models.CharField(max_length=30, blank=True, null=True)
    skill3 = models.CharField(max_length=30, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    level = models.IntegerField(blank=True, null=True)
    raceskill = models.CharField(max_length=30, blank=True, null=True)
    classskill = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Characters'


class Classskills(models.Model):
    cskills = models.AutoField(db_column='cSkills', primary_key=True)  # Field name made lowercase.
    skill = models.CharField(max_length=30, blank=True, null=True)
    roll = models.CharField(max_length=30, blank=True, null=True)
    skilltype = models.CharField(db_column='skillType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    magic = models.CharField(max_length=30, blank=True, null=True)
    classid = models.ForeignKey('Classes', models.DO_NOTHING, db_column='classID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClassSkills'


class Classes(models.Model):
    classid = models.AutoField(db_column='classID', primary_key=True)  # Field name made lowercase.
    classname = models.CharField(db_column='className', max_length=30, blank=True, null=True)  # Field name made lowercase.
    classbonus1 = models.CharField(db_column='classBonus1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    classbonus2 = models.CharField(db_column='classBonus2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    classbonus3 = models.CharField(db_column='classBonus3', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Classes'


class Raceskills(models.Model):
    rskill = models.AutoField(db_column='rSkill', primary_key=True)  # Field name made lowercase.
    skill = models.CharField(max_length=30, blank=True, null=True)
    roll = models.CharField(max_length=30, blank=True, null=True)
    skilltype = models.CharField(db_column='skillType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    magic = models.CharField(max_length=30, blank=True, null=True)
    raceid = models.ForeignKey('Races', models.DO_NOTHING, db_column='raceID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RaceSkills'


class Races(models.Model):
    raceid = models.AutoField(db_column='raceID', primary_key=True)  # Field name made lowercase.
    racename = models.CharField(db_column='raceName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    racebonus1 = models.CharField(db_column='raceBonus1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    racebonus2 = models.CharField(db_column='raceBonus2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    racebonus3 = models.CharField(db_column='raceBonus3', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Races'


class Skills(models.Model):
    skill_id = models.AutoField(primary_key=True)
    skill = models.CharField(max_length=30, blank=True, null=True)
    roll = models.CharField(max_length=30, blank=True, null=True)
    skilltype = models.CharField(db_column='skillType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    magic = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Skills'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=30, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    email = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    last_login = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
