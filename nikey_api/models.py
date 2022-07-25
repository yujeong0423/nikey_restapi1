# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AddressesAddresses(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'addresses_addresses'


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


class Clipboard(models.Model):
    cb_memo = models.CharField(max_length=200)
    cb_field = models.SmallIntegerField(db_column='cb_')  # Field renamed because it ended with '_'.
    th_user = models.SmallIntegerField()
    g_allow = models.IntegerField()
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid')

    class Meta:
        managed = False
        db_table = 'clipboard'


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


class Emoticon(models.Model):
    e_default = models.CharField(primary_key=True, max_length=10)
    rl_emoticon = models.ForeignKey('RecommendLearningData', models.DO_NOTHING, db_column='rl_emoticon')
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid')

    class Meta:
        managed = False
        db_table = 'emoticon'


class EmoticonRelationWord(models.Model):
    e_r_word = models.CharField(max_length=20)
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid')

    class Meta:
        managed = False
        db_table = 'emoticon_relation_word'


class KeyboardSetting(models.Model):
    kb_korea_form = models.IntegerField()
    kb_full_stop = models.IntegerField()
    kb_capital_letter = models.IntegerField()
    kb_double_consonant = models.IntegerField()
    kb_suggested_words = models.IntegerField()
    kb_typo_correction = models.IntegerField()
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid')

    class Meta:
        managed = False
        db_table = 'keyboard_setting'


class MyDictionary(models.Model):
    num = models.ForeignKey('NeologismDictionary', models.DO_NOTHING, db_column='num')
    md_bookmark = models.CharField(max_length=255, blank=True, null=True)
    md_save_date = models.DateField()
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid')

    class Meta:
        managed = False
        db_table = 'my_dictionary'


class NeologismDictionary(models.Model):
    num = models.IntegerField(primary_key=True)
    nd_word = models.CharField(max_length=40)
    nd_detail = models.CharField(max_length=265)

    class Meta:
        managed = False
        db_table = 'neologism_dictionary'


class NeologismDictionaryAssociatedWord(models.Model):
    num = models.OneToOneField(NeologismDictionary, models.DO_NOTHING, db_column='num', primary_key=True)
    nd_a_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'neologism_dictionary_associated_word'


class NeologismDictionaryBookmark(models.Model):
    num = models.OneToOneField(NeologismDictionary, models.DO_NOTHING, db_column='num', primary_key=True)
    nd_bookmark = models.IntegerField()
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid')

    class Meta:
        managed = False
        db_table = 'neologism_dictionary_bookmark'


class NeologismDictionaryExample(models.Model):
    num = models.OneToOneField(NeologismDictionary, models.DO_NOTHING, db_column='num', primary_key=True)
    nd_ex = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'neologism_dictionary_example'


class NeologismDictionarySearch(models.Model):
    num = models.OneToOneField(NeologismDictionary, models.DO_NOTHING, db_column='num', primary_key=True)
    nd_s_word = models.CharField(max_length=40, blank=True, null=True)
    nd_s_date = models.DateField()
    nd_word_frequency_data = models.IntegerField(blank=True, null=True)
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid')

    class Meta:
        managed = False
        db_table = 'neologism_dictionary_search'


class RecommendLearningData(models.Model):
    rl_text = models.CharField(max_length=255)
    rl_emoticon = models.CharField(primary_key=True, max_length=10)
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid')

    class Meta:
        managed = False
        db_table = 'recommend_learning_data'


class ThemeSetting(models.Model):
    th_dark = models.IntegerField()
    th_default = models.SmallIntegerField()
    th_user = models.SmallIntegerField()
    g_allow = models.IntegerField()
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid')

    class Meta:
        managed = False
        db_table = 'theme_setting'


class ToolSetting(models.Model):
    t_cb_icon = models.IntegerField()
    t_kb_setting = models.IntegerField()
    t_spell_check = models.IntegerField()
    t_nd = models.IntegerField()
    t_allow = models.IntegerField()
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid')

    class Meta:
        managed = False
        db_table = 'tool_setting'


class User(models.Model):
    uid = models.IntegerField(primary_key=True)
    uname = models.CharField(max_length=20)
    password = models.CharField(max_length=65)
    ubirth = models.DateField()
    usex = models.CharField(max_length=20)
    uemail = models.CharField(max_length=40)
    uphone = models.CharField(max_length=20)
    admin = models.IntegerField()
    acc_allow = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'
