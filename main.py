count_counties = 10
customers_per_country = 10

filled_quote_per_customer = 10
product_per_quotes = 100
total_quote_per_customer = 100

filled_invoice_per_customer = 10
product_per_invoices = 100
total_invoice_per_per_customer = 100

filled_credit_note_per_customer = 10
product_per_credit_notes = 100
total_credit_note_per_per_customer = 100

tax_codes = (1, 2, 3, 4, 5, 8, )

# imports and inits

from datetime import datetime
from math import floor
from typing import Any
from uuid import uuid4
import BCP47
import itertools
import tables

import pymysql
connection = pymysql.connect(
	host='host.docker.internal',
	port=3636,
	user='dktProApi',
	password='localDevPassword',
	database='dkt_pro_api',
	autocommit=False,
)

from random import SystemRandom
random = SystemRandom()

from json import load
from pathlib import Path
diceware: list[str] = list()
with open(Path(__file__).parent / 'diceware.json', mode='br') as file:
	diceware = load(file)

ProductIds = dict[int, dict[int, dict[int, str]]]


# single scalar generators

def types_varchar(length: int):
	return ' '.join(random.choices(diceware, k=3))[0:length]

def types_longtext():
	return types_varchar(420)

def types_datetime():
	minimum = int(datetime(1000, 1, 1).timestamp())
	maximum = int(datetime(2000, 1, 1).timestamp())
	timestamp = random.randrange(start=minimum, stop=maximum)
	return datetime.fromtimestamp(timestamp).isoformat(sep=' ', timespec='seconds')

def types_json():
	return '{}'

def types_double():
	return random.randint(1_00, 1_000_000_00) /100 #this is begging to get out of sync

def types_char(x: None|Any) -> str:
	if x is None:
		return None
	else:
		return x.get('id', None)

# single row generators

def random_country(
	config: None|tables.TD_country_config=None,
	front_office_user: None|tables.TD_front_office_user=None,
) -> tables.TD_country:
	return {
		'id': str(uuid4()),
		'config_id': types_char(config), #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
		'front_office_user_id': types_char(front_office_user), #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
		'name': types_varchar(255), #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
		'telephone': types_varchar(255), #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
		'address_number': types_varchar(15), #varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
		'address_street': types_varchar(255), #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
		'postcode': types_varchar(10), #varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
		'city': types_varchar(125), #varchar(125) COLLATE utf8mb4_unicode_ci NOT NULL,
		'contact_email': types_varchar(320), #varchar(320) COLLATE utf8mb4_unicode_ci NOT NULL,
		'enabled': 9, #tinyint(1) NOT NULL,
		'start_date': types_datetime(), #datetime DEFAULT NULL,
		'territory': types_json(), #json NOT NULL,
		'currency': types_varchar(3), #varchar(3) COLLATE utf8mb4_unicode_ci NOT NULL,
		'vat_number': types_varchar(20), #varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
		'created_at': types_datetime(), #datetime NOT NULL,
		'updated_at': types_datetime(), #datetime NOT NULL,
		'licence_end_date': types_datetime(), #datetime DEFAULT NULL,
	}

def random_country_vat(code: int, country: tables.TD_country) -> tables.TD_country_vat:
	rate = 0.0 if 8 == code else random.random()
	
	return {
		'id': str(uuid4()),
		'country_id': types_char(country), #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
		'code': code, #int NOT NULL,
		'rate': rate, #double NOT NULL,
	}

def random_user() -> tables.TD_user:
	return {
		'id': str(uuid4()),
		'roles': types_json(), #json NOT NULL,
		'discr': 'user', #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
		'name': types_varchar(255), #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	}	

def random_customer(
	country: None|tables.TD_country=None,
	created_by: None|tables.TD_user=None,
) -> tables.TD_customer:
	return {
		'id': str(uuid4()),
		'legalstatus_code': None, #varchar(3) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
		'country_id': types_char(country), #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
		'company_name': types_varchar(250), #varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
		'email': types_varchar(180), #varchar(180) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
		'loyalty_card_number': types_varchar(15), #varchar(15) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
		'vat_number': types_varchar(20), #varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
		'internal_ref': types_varchar(25), #varchar(25) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
		'created_at': types_datetime(), #datetime NOT NULL,
		'updated_at': types_datetime(), #datetime NOT NULL,
		'created_by': types_char(created_by), #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
		'pipedrive_organization_id': types_varchar(255), #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
		'data_policy_optin_date': types_datetime(), #datetime DEFAULT NULL,
		'receive_emails_optin_date': types_datetime(), #datetime DEFAULT NULL,
		'block_overall_email_date': types_datetime(), #datetime DEFAULT NULL,
		'block_commercial_email_date': types_datetime(), #datetime DEFAULT NULL,
		'creation_email_send_date': types_datetime(), #datetime DEFAULT NULL,
		'internal_message': types_longtext(), #longtext COLLATE utf8mb4_unicode_ci,
		'terms_and_conditions_optin_date': types_datetime(), #datetime DEFAULT NULL,
	}

def random_billing_address(
	customer: tables.TD_customer,
) -> tables.TD_billing_address:
	return {
		'id': str(uuid4()),
		'customer_id': types_char(customer), #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
		'responsible_firstname': types_varchar(55), #varchar(55) COLLATE utf8mb4_unicode_ci NOT NULL,
		'responsible_lastname': types_varchar(55), #varchar(55) COLLATE utf8mb4_unicode_ci NOT NULL,
		'address': types_varchar(255), #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
		'additional_address': types_varchar(255), #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
		'postcode': types_varchar(20), #varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
		'city': types_varchar(55), #varchar(55) COLLATE utf8mb4_unicode_ci NOT NULL,
		'telephone': types_varchar(25), #varchar(25) COLLATE utf8mb4_unicode_ci NOT NULL,
		'pipedrive_person_id': types_varchar(255), #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	}

def random_quote(
	customer: tables.TD_customer,
	billing_address: tables.TD_billing_address,
	country: tables.TD_country,
	delivery_address: None|tables.TD_delivery_address=None,
	created_by: None|tables.TD_user=None,
	shipping_cost: None|tables.TD_shipping_cost=None,
	delivery_decath_store: None|tables.TD_decath_store=None,
	assigned_to: None|tables.TD_decathlon_user=None,
) -> tables.TD_quote:
	status_code = random.choice(('CAN', 'DON', 'DRA', 'EXP', 'ISS', 'NEW', 'PEN', 'PRO', 'THB', ))
	
	return {
		'id': str(uuid4()),
		'customer_id': types_char(customer), #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
		'billing_address_id': types_char(billing_address), #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
		'delivery_address_id': types_char(delivery_address), #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
		'country_id': types_char(country), #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
		'delivery_method_code': 'MAG', #varchar(3) COLLATE utf8mb4_unicode_ci NOT NULL,
		'created_by': types_char(created_by), #char(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
		'origin_code': None, #varchar(3) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
		'status_code': status_code, #varchar(3) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
		'shipping_cost_id': types_char(shipping_cost), #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
		'delivery_decath_store_id': types_char(delivery_decath_store), #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
		'number': types_varchar(15), #varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
		'additional_note': types_longtext(), #longtext COLLATE utf8mb4_unicode_ci,
		'amount': types_double(), #double NOT NULL,
		'created_at': types_datetime(), #datetime NOT NULL,
		'updated_at': types_datetime(), #datetime NOT NULL,
		'pipedrive_deal_id': types_varchar(255), #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
		'discount': None, #double DEFAULT NULL,
		'assigned_to': types_char(assigned_to), #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
		'business_unit': types_varchar(16), #varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	}

def random_invoice(
	country: tables.TD_country,
	billing_address: tables.TD_billing_address,
	customer: tables.TD_customer,
	quote: None|tables.TD_quote=None,
	delivery_address: None|tables.TD_delivery_address=None,
	created_by: None|tables.TD_decathlon_user=None,
	shipping_cost: None|tables.TD_shipping_cost=None,
	delivery_decath_store: None|tables.TD_decath_store=None,
	assigned_to: None|tables.TD_decathlon_user=None,
) -> tables.TD_invoice:
	status_code = random.choice(('CAN', 'PAI', 'PEA', 'THB', ))
	
	return {
		'id': str(uuid4()),
		'country_id': types_char(country), #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
		'quote_id': types_char(quote), #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
		'delivery_method_code': 'MAG', #varchar(3) COLLATE utf8mb4_unicode_ci NOT NULL,
		'billing_address_id': types_char(billing_address), #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
		'delivery_address_id': types_char(delivery_address), #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
		'customer_id': types_char(customer), #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
		'created_by': types_char(created_by), #char(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
		'status_code': status_code, #varchar(3) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
		'shipping_cost_id': types_char(shipping_cost), #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
		'delivery_decath_store_id': types_char(delivery_decath_store), #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
		'number': types_varchar(15), #varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
		'additional_note': types_longtext(), #longtext COLLATE utf8mb4_unicode_ci,
		'amount': types_double(), #double NOT NULL,
		'created_at': types_datetime(), #datetime NOT NULL,
		'updated_at': types_datetime(), #datetime NOT NULL,
		'discount': None, #double DEFAULT NULL,
		'assigned_to': types_char(assigned_to), #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
		'business_unit': types_varchar(16), #varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	}

def random_credit_note(
	invoice: tables.TD_invoice,
	country: tables.TD_country,
	created_by: None|tables.TD_decathlon_user=None,
	billing_address: None|tables.TD_billing_address=None,
	assigned_to: None|tables.TD_decathlon_user=None,
) -> tables.TD_credit_note:
	status_code = random.choice(('CAN', 'ISS', 'PEN', 'SEN', ))
	
	return {
		'id': str(uuid4()),
		'invoice_id': types_char(invoice), #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
		'country_id': types_char(country), #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
		'status_code': status_code, #varchar(3) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
		'created_by': types_char(created_by), #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
		'number': types_varchar(15), #varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
		'reason': None, #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
		'amount': types_double(), #double NOT NULL,
		'created_at': types_datetime(), #datetime NOT NULL,
		'updated_at': types_datetime(), #datetime NOT NULL,
		'billing_address_id': types_char(billing_address), #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
		'assigned_to': types_char(assigned_to), #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
		'business_unit': None, #varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	}

def random_product(
	product_ids: ProductIds,
	position: int,
	quote: None|tables.TD_quote=None,
	invoice: None|tables.TD_invoice=None,
	credit_note: None|tables.TD_credit_note=None,
) -> tables.TD_product:
	sku_price = random.randint(1_00, 1_000_00) /100
	price_overwrite = random.randint(1_00, 1_000_00) /100
	if random.randint(0, 6) < 1: price_overwrite = None
	tax_code = random.choice(tax_codes)
	quantity = random.randint(1, 1_000)
	unit_reduc_rate = random.random()
	if random.randint(0, 6) < 1: unit_reduc_rate = 0.0
	if random.randint(0, 6) < 1: price_overwrite = None
	
	product_id = random.choice(tuple(product_ids.keys()))
	model_id = random.choice(tuple(product_ids[product_id].keys()))
	sku_id = random.choice(tuple(product_ids[product_id][model_id].keys()))
	display_name = product_ids[product_id][model_id][sku_id][0:250]
	
	return {
		'id': str(uuid4()),
		'quote_id': types_char(quote), #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
		'invoice_id': types_char(invoice), #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
		'display_name': display_name, #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
		'product_id': str(product_id), #varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
		'model_id': str(model_id), #varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
		'sku_id': str(sku_id), #varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
		'sku_price': sku_price, #double NOT NULL,
		'price_overwrite': price_overwrite, #double DEFAULT NULL,
		'tax_code': tax_code, #int NOT NULL DEFAULT '8',
		'quantity': quantity, #int NOT NULL,
		'additional_note': types_varchar(455), #varchar(455) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
		'unit_reduc_rate': unit_reduc_rate, #double DEFAULT NULL,
		'position': position, #int NOT NULL DEFAULT '0',
		'picture_url': types_varchar(2048), #varchar(2048) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
		'sku_name': types_varchar(255), #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
		'created_at': types_datetime(), #datetime NOT NULL,
		'updated_at': types_datetime(), #datetime NOT NULL,
		'credit_note_id': types_char(credit_note), #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
		'audience_locale': types_varchar(5), #varchar(5) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
		'taxes': '{}', #json NOT NULL,
		'dk_article_id': types_varchar(64), #varchar(64) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	}

# utils

def make_query(cursor, tbl_name, table):
	print(f'''INSERT INTO `{tbl_name}` {len(table)}''', end='…', flush=True)
	
	col_names = ", ".join(
		f"""`{key}`"""
		for key in table[0].keys()
	)
	
	value_list = ", ".join(
		"%s"
		for _key in table[0].keys()
	)
	
	cursor.executemany(
		f"""INSERT INTO `{tbl_name}` ({col_names}) VALUES ({value_list})""",
		(tuple(row.values()) for row in table)
	)
	
	print('\033[D ', flush=True)

def make_product_ids() -> ProductIds:
	products = (
		(
			count_counties
			* customers_per_country
			* filled_quote_per_customer
			* product_per_quotes
		)
		+ (
			count_counties
			* customers_per_country
			* filled_invoice_per_customer
			* product_per_invoices
		)
		+ (
			count_counties
			* customers_per_country
			* filled_credit_note_per_customer
			* product_per_credit_notes
		)
	)
	
	fanout = 10
	print(f'''{fanout=}''')

	sku_ids = itertools.batched(random.sample(range(1_000_000, 2_000_000), fanout *fanout *fanout), fanout)
	model_ids = itertools.batched(random.sample(range(3_000_000, 4_000_000), fanout *fanout), fanout)
	product_ids = itertools.batched(random.sample(range(5_000_000, 6_000_000), (fanout-1)), (fanout-1))
	
	return {
		product_id: {
			model_id: {
				sku_id: ' '.join(random.sample(diceware, random.randint(6, 12)))
				for sku_id in next(sku_ids)
			}
			for model_id in next(model_ids)
		}
		for product_id in next(product_ids)
	}

with connection:
	with connection.cursor() as cursor:
		# this TRUNCATE too much and i am not rebuilding the tables that get shunted
		cursor.execute('''SHOW TABLES''')
		statements = list(f'''TRUNCATE `{table}`''' for (table, ) in cursor.fetchall())
		
		statements = [
			'TRUNCATE `country`',
			'TRUNCATE `country_vat`',
			'TRUNCATE `user`',
			'TRUNCATE `customer`',
			'TRUNCATE `billing_address`',
			'TRUNCATE `quote`',
			'TRUNCATE `invoice`',
			'TRUNCATE `credit_note`',
			'TRUNCATE `product`',
			
			'TRUNCATE `country_stats`',
			'TRUNCATE `customer_stats`',
			'TRUNCATE `product_stats`',
			'TRUNCATE `user_stats`',
		]
		statements.reverse()
		
		cursor.execute('SET foreign_key_checks = 0')
		
		had_error = True
		while had_error:
			had_error = False
			for statement in statements:
				try:
					print(statement, end='…', flush=True)
					cursor.execute(statement)
					print('\033[D ', flush=True)
				except:
					had_error = True
					raise
		
		cursor.execute('SET foreign_key_checks = 1')
	connection.commit()
	
	print("TRUNCATE done", flush=True)
	
	countries: list[tables.TD_country] = list()
	country_vats: list[tables.TD_country_vat] = list()
	users: list[tables.TD_user] = list()
	customers: list[tables.TD_customer] = list()
	billing_addresses: list[tables.TD_billing_address] = list()
	quotes: list[tables.TD_quote] = list()
	invoices: list[tables.TD_invoice] = list()
	credit_notes: list[tables.TD_credit_note] = list()
	products: list[tables.TD_product] = list()
	
	product_ids = make_product_ids()
	
	for tag in random.sample(BCP47.tags, k=count_counties):
		country = random_country()
		countries.append(country)
		
		for tax_code in tax_codes:
			country_vat = random_country_vat(code=tax_code, country=country)
			country_vats.append(country_vat)
		
		for index in range(customers_per_country):
			user = random_user()
			users.append(user)
		
		copy_users = list(users)
		random.shuffle(copy_users)
		random_users = itertools.cycle(copy_users)
		
		for index in range(customers_per_country):
			customer = random_customer(country=country, created_by=next(random_users))
			customers.append(customer)
			
			billing_address = random_billing_address(customer=customer)
			billing_addresses.append(billing_address)
			
			# quotes
			for index in range(filled_quote_per_customer):
				quote = random_quote(customer=customer, billing_address=billing_address, country=country)
				quotes.append(quote)
				
				for index in range(product_per_quotes):
					product = random_product(product_ids, position=index, quote=quote, invoice=None, credit_note=None)
					products.append(product)
			
			for index in range(filled_quote_per_customer, total_quote_per_customer):
				quote = random_quote(customer=customer, billing_address=billing_address, country=country)
				quotes.append(quote)
			
			# invoices
			for index in range(filled_invoice_per_customer):
				invoice = random_invoice(customer=customer, billing_address=billing_address, country=country)
				invoices.append(invoice)
				
				for index in range(product_per_invoices):
					product = random_product(product_ids, position=index, quote=None, invoice=invoice, credit_note=None)
					products.append(product)
			
			for index in range(filled_invoice_per_customer, total_invoice_per_per_customer):
				invoice = random_invoice(customer=customer, billing_address=billing_address, country=country)
				invoices.append(invoice)
			
			
			# credit_notes
			copy_invoices = list(invoices)
			random.shuffle(copy_invoices)
			random_invoices = itertools.cycle(copy_invoices)
			
			for index in range(filled_credit_note_per_customer):
				credit_note = random_credit_note(invoice=next(random_invoices), country=country)
				credit_notes.append(credit_note)
				
				for index in range(product_per_credit_notes):
					product = random_product(product_ids, position=index, quote=None, invoice=None, credit_note=credit_note)
					products.append(product)
			
			for index in range(filled_credit_note_per_customer, total_credit_note_per_per_customer):
				credit_note = random_credit_note(invoice=next(random_invoices), country=country)
				credit_notes.append(credit_note)
	
	with connection.cursor() as cursor:
		make_query(cursor, 'country', countries)
		make_query(cursor, 'country_vat', country_vats)
		make_query(cursor, 'user', users)
		make_query(cursor, 'customer', customers)
		make_query(cursor, 'billing_address', billing_addresses)
		make_query(cursor, 'quote', quotes)
		make_query(cursor, 'invoice', invoices)
		make_query(cursor, 'credit_note', credit_notes)
		make_query(cursor, 'product', products)
	
	connection.commit()
	print(connection.get_autocommit())
