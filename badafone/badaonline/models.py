# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

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

class CallTable(models.Model):
	caller = models.OneToOneField('SimCard', models.DO_NOTHING, db_column='caller', primary_key=True)
	callee = models.ForeignKey('SimCard', models.DO_NOTHING, db_column='callee')
	start_time = models.TimeField()
	end_time = models.TimeField()
	caller_tower = models.ForeignKey('Tower', models.DO_NOTHING, db_column='caller_tower')
	callee_tower = models.ForeignKey('Tower', models.DO_NOTHING, db_column='callee_tower')
	
	class Meta:
		managed = False
		unique_together = (('caller', 'start_time'),)

class Customer(models.Model):
	customer_id = models.IntegerField(db_column='customer_ID', primary_key=True)  # Field name made lowercase.
	phone_number = models.ForeignKey('SimCard', models.DO_NOTHING, db_column='phone_number')
	aadhaar = models.BigIntegerField()
	username = models.CharField(max_length=100)
	birthdate = models.DateField()
	
	class Meta:
		db_table = 'customer'


class Employee(models.Model):
	employee_id = models.IntegerField(db_column='employee_ID', primary_key=True)  # Field name made lowercase.
	employee_name = models.CharField(max_length=100)
	aadhaar = models.BigIntegerField()
	e_mail = models.CharField(max_length=100)
	date_of_joining = models.DateField()
	
	class Meta:
		db_table = 'employee'

class Plan(models.Model):
	plan_id = models.IntegerField(db_column='plan_ID', primary_key=True)  # Field name made lowercase.
	name = models.CharField(max_length=50)
	validity = models.IntegerField()
	price = models.DecimalField(max_digits=5, decimal_places=2)
	
	class Meta:
		db_table = 'plan'

class PlanCalling(models.Model):
	plan = models.OneToOneField(Plan, models.DO_NOTHING, db_column='plan_ID',
	                            primary_key=True, related_name='%(class)s_fk_planid_plan')  # Field name made lowercase.
	price = models.ForeignKey(Plan, models.DO_NOTHING, db_column='price', related_name='%(class)s_fk_price_plan')
	name = models.ForeignKey(Plan, models.DO_NOTHING, db_column='name', related_name='%(class)s_fk_name_plan')
	l_minutes = models.IntegerField()
	s_minutes = models.IntegerField()
	i_minutes = models.IntegerField()
	calls = models.IntegerField()
	sms = models.IntegerField()
	validity = models.ForeignKey(Plan, models.DO_NOTHING, db_column='validity', blank=True, null=True,
	                             related_name='%(class)s_validity')
	
	class Meta:
		db_table = 'plan_calling'

class PlanData(models.Model):
	plan = models.OneToOneField(Plan, models.DO_NOTHING, db_column='plan_ID',
	                            primary_key=True)  # Field name made lowercase.
	price = models.ForeignKey(Plan, models.DO_NOTHING, db_column='price', related_name='fk_price_plan')
	validity = models.ForeignKey(Plan, models.DO_NOTHING, db_column='validity')
	name = models.ForeignKey(Plan, models.DO_NOTHING, db_column='name')
	data_limit = models.DecimalField(max_digits=5, decimal_places=2)
	speed = models.IntegerField()
	data_after_limit = models.DecimalField(max_digits=5, decimal_places=2)
	speed_after_limit = models.IntegerField()
	
	class Meta:
		db_table = 'plan_data'

class SimCard(models.Model):
	phone_number = models.BigIntegerField(primary_key=True)
	activated = models.IntegerField()
	date_of_activation = models.DateField()
	home_tower = models.ForeignKey('Tower', models.DO_NOTHING, db_column='home_tower', blank=True, null=True,
	                               related_name='fk_hometower_simcard')
	current_tower = models.ForeignKey('Tower', models.DO_NOTHING, db_column='current_tower', blank=True, null=True,
	                                  related_name='fk_currtower_simcard')
	roaming = models.IntegerField()
	
	class Meta:
		db_table = 'sim_card'

class Sms(models.Model):
	sender = models.OneToOneField(SimCard, models.DO_NOTHING, db_column='sender', primary_key=True,
	                              related_name='fk_sender_simcard')
	send_time = models.TimeField()
	receiver = models.ForeignKey(SimCard, models.DO_NOTHING, db_column='receiver', blank=True, null=True,
	                             related_name='fk_receiver_simcard')
	read = models.IntegerField(blank=True, null=True)
	sms_content = models.CharField(max_length=500, blank=True, null=True)
	
	class Meta:
		db_table = 'sms'
		unique_together = (('sender', 'send_time'),)

class Subscription(models.Model):
	phone_number = models.ForeignKey(SimCard, models.DO_NOTHING, db_column='phone_number')
	plan = models.ForeignKey(Plan, models.DO_NOTHING, db_column='plan_ID')  # Field name made lowercase.
	
	class Meta:
		db_table = 'subscription'
		unique_together = (('phone_number', 'plan'),)

class SupportTicket(models.Model):
	ticket_id = models.IntegerField(db_column='ticket_ID', primary_key=True)  # Field name made lowercase.
	customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='customer_ID')  # Field name made lowercase.
	content = models.CharField(max_length=500, blank=True, null=True)
	category = models.CharField(max_length=19)
	closed = models.IntegerField()
	employee = models.ForeignKey(Employee, models.DO_NOTHING, db_column='employee_ID', blank=True,
	                             null=True)  # Field name made lowercase.
	
	class Meta:
		db_table = 'support_ticket'

class Tower(models.Model):
	tower_id = models.IntegerField(db_column='tower_ID', primary_key=True)  # Field name made lowercase.
	city = models.CharField(max_length=40)
	
	class Meta:
		db_table = 'tower'

class Transaction(models.Model):
	phone_number = models.OneToOneField(SimCard, models.DO_NOTHING, db_column='phone_number', primary_key=True)
	plan = models.ForeignKey(Plan, models.DO_NOTHING, db_column='plan_ID')  # Field name made lowercase.
	purchase_time = models.DateField()
	
	class Meta:
		db_table = 'transaction'
		unique_together = (('phone_number', 'purchase_time'),)

class UsageCalling(models.Model):
	phone_number = models.ForeignKey(SimCard, models.DO_NOTHING, db_column='phone_number')
	plan = models.OneToOneField(PlanCalling, models.DO_NOTHING, db_column='plan_ID',
	                            primary_key=True)  # Field name made lowercase.
	l_minutes = models.IntegerField()
	s_minutes = models.IntegerField()
	i_minutes = models.IntegerField()
	calls = models.IntegerField()
	sms = models.IntegerField(db_column='SMS')  # Field name made lowercase.
	start_date = models.DateField()
	
	class Meta:
		db_table = 'usage_calling'
		unique_together = (('plan', 'phone_number'),)

class UsageData(models.Model):
	phone_number = models.OneToOneField(SimCard, models.DO_NOTHING, db_column='phone_number', primary_key=True)
	plan = models.ForeignKey(PlanData, models.DO_NOTHING, db_column='plan_ID')  # Field name made lowercase.
	data_used = models.DecimalField(max_digits=5, decimal_places=2)
	start_date = models.DateField()
	
	class Meta:
		db_table = 'usage_data'
		unique_together = (('phone_number', 'plan'),)

class Wallet(models.Model):
	phone_number = models.ForeignKey(SimCard, models.DO_NOTHING, db_column='phone_number')
	payment_method = models.CharField(max_length=11)
	balance = models.IntegerField()
	
	class Meta:
		db_table = 'wallet'
