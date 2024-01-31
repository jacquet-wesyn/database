from typing import TypedDict

types_int = int
types_varchar = str
types_longtext = str
types_datetime = str
types_char = str
types_json = str
types_tinyint = int
types_double = float
types_text = str

class TD_banner_message(TypedDict):
	id: types_int #int NOT NULL AUTO_INCREMENT,
	message: types_varchar #varchar(655) COLLATE utf8mb4_unicode_ci NOT NULL,
	type: types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	# PRIMARY KEY (`id`)

class TD_credit_note_status(TypedDict):
	code: types_varchar #varchar(3) COLLATE utf8mb4_unicode_ci NOT NULL,
	name: types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	# PRIMARY KEY (`code`)

class TD_credit_note_status_translations(TypedDict):
	id: types_int #int NOT NULL AUTO_INCREMENT,
	locale: types_varchar #varchar(8) COLLATE utf8mb4_unicode_ci NOT NULL,
	object_class: types_varchar #varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
	field: types_varchar #varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
	foreign_key: types_varchar #varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
	content: types_longtext #longtext COLLATE utf8mb4_unicode_ci,
	# PRIMARY KEY (`id`),
	# KEY `credit_note_status_translation_idx` (`locale`,`object_class`,`field`,`foreign_key`)

class TD_delivery_method(TypedDict):
	code: types_varchar #varchar(3) COLLATE utf8mb4_unicode_ci NOT NULL,
	name: types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	# PRIMARY KEY (`code`)

class TD_delivery_method_translations(TypedDict):
	id: types_int #int NOT NULL AUTO_INCREMENT,
	locale: types_varchar #varchar(8) COLLATE utf8mb4_unicode_ci NOT NULL,
	object_class: types_varchar #varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
	field: types_varchar #varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
	foreign_key: types_varchar #varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
	content: types_longtext #longtext COLLATE utf8mb4_unicode_ci,
	# PRIMARY KEY (`id`),
	# KEY `delivery_method_translation_idx` (`locale`,`object_class`,`field`,`foreign_key`)

class TD_doctrine_migration_versions(TypedDict):
	version: types_varchar #varchar(191) COLLATE utf8mb3_unicode_ci NOT NULL,
	executed_at: None | types_datetime #datetime DEFAULT NULL,
	execution_time: None | types_int #int DEFAULT NULL,
	# PRIMARY KEY (`version`)

class TD_ext_translations(TypedDict):
	id: types_int #int NOT NULL AUTO_INCREMENT,
	locale: types_varchar #varchar(8) COLLATE utf8mb4_unicode_ci NOT NULL,
	object_class: types_varchar #varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
	field: types_varchar #varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
	foreign_key: types_varchar #varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
	content: types_longtext #longtext COLLATE utf8mb4_unicode_ci,
	# PRIMARY KEY (`id`),
	# UNIQUE KEY `lookup_unique_idx` (`locale`,`object_class`,`field`,`foreign_key`),
	# KEY `translations_lookup_idx` (`locale`,`object_class`,`foreign_key`)

class TD_invoice_status(TypedDict):
	code: types_varchar #varchar(3) COLLATE utf8mb4_unicode_ci NOT NULL,
	name: types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	# PRIMARY KEY (`code`)

class TD_invoice_status_translations(TypedDict):
	id: types_int #int NOT NULL AUTO_INCREMENT,
	locale: types_varchar #varchar(8) COLLATE utf8mb4_unicode_ci NOT NULL,
	object_class: types_varchar #varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
	field: types_varchar #varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
	foreign_key: types_varchar #varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
	content: types_longtext #longtext COLLATE utf8mb4_unicode_ci,
	# PRIMARY KEY (`id`),
	# KEY `invoice_status_translation_idx` (`locale`,`object_class`,`field`,`foreign_key`)

class TD_legal_status(TypedDict):
	code: types_varchar #varchar(3) COLLATE utf8mb4_unicode_ci NOT NULL,
	name: types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	# PRIMARY KEY (`code`)

class TD_legal_status_translations(TypedDict):
	id: types_int #int NOT NULL AUTO_INCREMENT,
	locale: types_varchar #varchar(8) COLLATE utf8mb4_unicode_ci NOT NULL,
	object_class: types_varchar #varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
	field: types_varchar #varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
	foreign_key: types_varchar #varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
	content: types_longtext #longtext COLLATE utf8mb4_unicode_ci,
	# PRIMARY KEY (`id`),
	# KEY `legal_status_translation_idx` (`locale`,`object_class`,`field`,`foreign_key`)

class TD_quote_origin(TypedDict):
	code: types_varchar #varchar(3) COLLATE utf8mb4_unicode_ci NOT NULL,
	name: types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	# PRIMARY KEY (`code`)

class TD_quote_origin_translations(TypedDict):
	id: types_int #int NOT NULL AUTO_INCREMENT,
	locale: types_varchar #varchar(8) COLLATE utf8mb4_unicode_ci NOT NULL,
	object_class: types_varchar #varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
	field: types_varchar #varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
	foreign_key: types_varchar #varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
	content: types_longtext #longtext COLLATE utf8mb4_unicode_ci,
	# PRIMARY KEY (`id`),
	# KEY `quote_origin_translation_idx` (`locale`,`object_class`,`field`,`foreign_key`)

class TD_quote_status(TypedDict):
	code: types_varchar #varchar(3) COLLATE utf8mb4_unicode_ci NOT NULL,
	name: types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	# PRIMARY KEY (`code`)

class TD_quote_status_translations(TypedDict):
	id: types_int #int NOT NULL AUTO_INCREMENT,
	locale: types_varchar #varchar(8) COLLATE utf8mb4_unicode_ci NOT NULL,
	object_class: types_varchar #varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
	field: types_varchar #varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
	foreign_key: types_varchar #varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
	content: types_longtext #longtext COLLATE utf8mb4_unicode_ci,
	# PRIMARY KEY (`id`),
	# KEY `quote_status_translation_idx` (`locale`,`object_class`,`field`,`foreign_key`)

class TD_user(TypedDict):
	id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	roles: types_json #json NOT NULL,
	discr: types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	name: types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	# PRIMARY KEY (`id`)

class TD_decathlon_user(TypedDict):
	id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	email: None | types_varchar #varchar(180) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	password: None | types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	enabled: types_tinyint #tinyint(1) NOT NULL,
	last_connection: None | types_datetime #datetime DEFAULT NULL,
	firstname: None | types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	lastname: None | types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	uid: None | types_varchar #varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	job_name: None | types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	site_name: None | types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	created_at: types_datetime #datetime NOT NULL,
	updated_at: types_datetime #datetime NOT NULL,
	createdBy: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	report_enabled: types_tinyint #tinyint(1) NOT NULL,
	# PRIMARY KEY (`id`),
	# UNIQUE KEY `UNIQ_5F49577BE7927C74` (`email`),
	# KEY `IDX_5F49577BD3564642` (`createdBy`),
	# CONSTRAINT `FK_5F49577BBF396750` FOREIGN KEY (`id`) REFERENCES `user` (`id`) ON DELETE CASCADE,
	# CONSTRAINT `FK_5F49577BD3564642` FOREIGN KEY (`createdBy`) REFERENCES `decathlon_user` (`id`) ON DELETE SET NULL

class TD_manage(TypedDict):
	employee_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	manager_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	# PRIMARY KEY (`employee_id`,`manager_id`),
	# KEY `IDX_2472AA4A8C03F15C` (`employee_id`),
	# KEY `IDX_2472AA4A783E3463` (`manager_id`),
	# CONSTRAINT `FK_2472AA4A783E3463` FOREIGN KEY (`manager_id`) REFERENCES `decathlon_user` (`id`),
	# CONSTRAINT `FK_2472AA4A8C03F15C` FOREIGN KEY (`employee_id`) REFERENCES `decathlon_user` (`id`)

class TD_user_connection_log(TypedDict):
	id: types_int #int NOT NULL AUTO_INCREMENT,
	user_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	date: types_datetime #datetime NOT NULL,
	device: None | types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	# PRIMARY KEY (`id`),
	# KEY `IDX_F8643FA6A76ED395` (`user_id`),
	# CONSTRAINT `FK_F8643FA6A76ED395` FOREIGN KEY (`user_id`) REFERENCES `decathlon_user` (`id`)

class TD_user_stats(TypedDict):
	id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	owner_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	calculation_date: types_datetime #datetime NOT NULL,
	quote_total_quantity: types_int #int NOT NULL,
	quote_total_value: types_double #double NOT NULL,
	invoice_total_quantity: types_int #int NOT NULL,
	invoice_total_value: types_double #double NOT NULL,
	credit_note_total_quantity: types_int #int NOT NULL,
	credit_note_total_value: types_double #double NOT NULL,
	# PRIMARY KEY (`id`),
	# KEY `IDX_B5859CF27E3C61F9` (`owner_id`),
	# CONSTRAINT `FK_B5859CF27E3C61F9` FOREIGN KEY (`owner_id`) REFERENCES `decathlon_user` (`id`)

class TD_banner_message_country(TypedDict):
	banner_message_id: types_int #int NOT NULL,
	country_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	# PRIMARY KEY (`banner_message_id`,`country_id`),
	# KEY `IDX_1074BDD3910F89C6` (`banner_message_id`),
	# KEY `IDX_1074BDD3F92F3E70` (`country_id`),
	# CONSTRAINT `FK_1074BDD3910F89C6` FOREIGN KEY (`banner_message_id`) REFERENCES `banner_message` (`id`) ON DELETE CASCADE,
	# CONSTRAINT `FK_1074BDD3F92F3E70` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`) ON DELETE CASCADE

class TD_billing_address(TypedDict):
	id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	customer_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	responsible_firstname: types_varchar #varchar(55) COLLATE utf8mb4_unicode_ci NOT NULL,
	responsible_lastname: types_varchar #varchar(55) COLLATE utf8mb4_unicode_ci NOT NULL,
	address: types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	additional_address: None | types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	postcode: types_varchar #varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
	city: types_varchar #varchar(55) COLLATE utf8mb4_unicode_ci NOT NULL,
	telephone: types_varchar #varchar(25) COLLATE utf8mb4_unicode_ci NOT NULL,
	pipedrive_person_id: None | types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	# PRIMARY KEY (`id`),
	# KEY `IDX_6660E4569395C3F3` (`customer_id`),
	# CONSTRAINT `FK_6660E4569395C3F3` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`)

class TD_country(TypedDict):
	id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	config_id: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	front_office_user_id: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	name: types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	telephone: types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	address_number: types_varchar #varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
	address_street: types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	postcode: types_varchar #varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
	city: types_varchar #varchar(125) COLLATE utf8mb4_unicode_ci NOT NULL,
	contact_email: types_varchar #varchar(320) COLLATE utf8mb4_unicode_ci NOT NULL,
	enabled: types_tinyint #tinyint(1) NOT NULL,
	start_date: None | types_datetime #datetime DEFAULT NULL,
	territory: types_json #json NOT NULL,
	currency: types_varchar #varchar(3) COLLATE utf8mb4_unicode_ci NOT NULL,
	vat_number: None | types_varchar #varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	created_at: types_datetime #datetime NOT NULL,
	updated_at: types_datetime #datetime NOT NULL,
	licence_end_date: None | types_datetime #datetime DEFAULT NULL,
	# PRIMARY KEY (`id`),
	# UNIQUE KEY `UNIQ_5373C96624DB0683` (`config_id`),
	# UNIQUE KEY `UNIQ_5373C96658328303` (`front_office_user_id`),
	# CONSTRAINT `FK_5373C96624DB0683` FOREIGN KEY (`config_id`) REFERENCES `country_config` (`id`),
	# CONSTRAINT `FK_5373C96658328303` FOREIGN KEY (`front_office_user_id`) REFERENCES `front_office_user` (`id`) ON DELETE SET NULL

class TD_country_config(TypedDict):
	id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	country_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	front_heading_picture_id: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	noreply_email: None | types_varchar #varchar(180) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	g_analytics_enabled: types_tinyint #tinyint(1) NOT NULL,
	g_analytics_id: None | types_varchar #varchar(25) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	terms: types_longtext #longtext COLLATE utf8mb4_unicode_ci,
	quote_footer_terms: types_longtext #longtext COLLATE utf8mb4_unicode_ci,
	shipping_cost_vat: None | types_double #double DEFAULT NULL,
	gift_card_vat: None | types_double #double DEFAULT NULL,
	days_until_quote_expired: types_int #int NOT NULL,
	invoice_legal_mentions: types_longtext #longtext COLLATE utf8mb4_unicode_ci,
	dkt_pro_front_available: types_tinyint #tinyint(1) NOT NULL,
	dkt_pro_front_domain: None | types_varchar #varchar(180) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	languages: types_json #json NOT NULL,
	pipedrive_api_key: types_longtext #longtext COLLATE utf8mb4_unicode_ci,
	pipedrive_enabled: types_tinyint #tinyint(1) NOT NULL,
	front_request_contact_activated: types_tinyint #tinyint(1) NOT NULL DEFAULT '0',
	front_maintenance_activated: types_tinyint #tinyint(1) NOT NULL DEFAULT '0',
	mail_service_dsn: None | types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	custom_product_vat: None | types_double #double DEFAULT NULL,
	use_marketplace_items: types_tinyint #tinyint(1) NOT NULL DEFAULT '1',
	default_business_unit: None | types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	business_units: None | types_json #json DEFAULT NULL,
	dkarticle_api_key: None | types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	store_locator_url: None | types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	pipedrive_pipeline_id: None | types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	pipedrive_default_deals_owner_id: None | types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	# PRIMARY KEY (`id`),
	# UNIQUE KEY `UNIQ_94F2C40FF92F3E70` (`country_id`),
	# UNIQUE KEY `UNIQ_94F2C40FD60DDE81` (`front_heading_picture_id`),
	# CONSTRAINT `FK_94F2C40FD60DDE81` FOREIGN KEY (`front_heading_picture_id`) REFERENCES `front_heading_picture` (`id`) ON DELETE SET NULL,
	# CONSTRAINT `FK_94F2C40FF92F3E70` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`) ON DELETE CASCADE

class TD_country_featured_product(TypedDict):
	id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	country_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	country_config_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	product_id: types_varchar #varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
	model_id: types_varchar #varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
	position: types_int #int NOT NULL,
	created_by: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	created_at: types_datetime #datetime NOT NULL,
	updated_at: types_datetime #datetime NOT NULL,
	sku_code: None | types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	# PRIMARY KEY (`id`),
	# KEY `IDX_EC28CA11F92F3E70` (`country_id`),
	# KEY `IDX_EC28CA11913803E3` (`country_config_id`),
	# KEY `IDX_EC28CA11DE12AB56` (`created_by`),
	# CONSTRAINT `FK_EC28CA11913803E3` FOREIGN KEY (`country_config_id`) REFERENCES `country_config` (`id`),
	# CONSTRAINT `FK_EC28CA11DE12AB56` FOREIGN KEY (`created_by`) REFERENCES `decathlon_user` (`id`) ON DELETE SET NULL,
	# CONSTRAINT `FK_EC28CA11F92F3E70` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`)

class TD_country_stats(TypedDict):
	id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	country_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	calculation_date: types_datetime #datetime NOT NULL,
	total_quotes: types_int #int NOT NULL,
	total_invoices: types_int #int NOT NULL,
	total_credit_notes: types_int #int NOT NULL,
	avg_quote_per_customer: types_double #double NOT NULL,
	avg_invoice_per_customer: types_double #double NOT NULL,
	total_customers: types_int #int NOT NULL,
	ratio_quote_invoice: types_double #double NOT NULL,
	avg_quote_amount: types_double #double NOT NULL,
	avg_invoice_amount: types_double #double NOT NULL,
	avg_credit_note_amount: types_double #double NOT NULL,
	total_decath_store_delivery: types_int #int NOT NULL,
	# PRIMARY KEY (`id`),
	# KEY `IDX_F0A77240F92F3E70` (`country_id`),
	# CONSTRAINT `FK_F0A77240F92F3E70` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`)

class TD_country_vat(TypedDict):
	id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	country_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	code: types_int #int NOT NULL,
	rate: types_double #double NOT NULL,
	# PRIMARY KEY (`id`),
	# KEY `IDX_BF9B14A2F92F3E70` (`country_id`),
	# CONSTRAINT `FK_BF9B14A2F92F3E70` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`) ON DELETE CASCADE

class TD_credit_note(TypedDict):
	id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	invoice_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	country_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	status_code: None | types_varchar #varchar(3) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	created_by: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	number: types_varchar #varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
	reason: None | types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	amount: types_double #double NOT NULL,
	created_at: types_datetime #datetime NOT NULL,
	updated_at: types_datetime #datetime NOT NULL,
	billing_address_id: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	assigned_to: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	business_unit: None | types_varchar #varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	# PRIMARY KEY (`id`),
	# KEY `IDX_C87F45292989F1FD` (`invoice_id`),
	# KEY `IDX_C87F4529F92F3E70` (`country_id`),
	# KEY `IDX_C87F45294F139D0C` (`status_code`),
	# KEY `IDX_C87F4529DE12AB56` (`created_by`),
	# KEY `IDX_C87F452979D0C0E4` (`billing_address_id`),
	# KEY `IDX_C87F452989EEAF91` (`assigned_to`),
	# CONSTRAINT `FK_C87F45292989F1FD` FOREIGN KEY (`invoice_id`) REFERENCES `invoice` (`id`),
	# CONSTRAINT `FK_C87F45294F139D0C` FOREIGN KEY (`status_code`) REFERENCES `credit_note_status` (`code`),
	# CONSTRAINT `FK_C87F452979D0C0E4` FOREIGN KEY (`billing_address_id`) REFERENCES `billing_address` (`id`),
	# CONSTRAINT `FK_C87F452989EEAF91` FOREIGN KEY (`assigned_to`) REFERENCES `decathlon_user` (`id`) ON DELETE SET NULL,
	# CONSTRAINT `FK_C87F4529DE12AB56` FOREIGN KEY (`created_by`) REFERENCES `decathlon_user` (`id`) ON DELETE SET NULL,
	# CONSTRAINT `FK_C87F4529F92F3E70` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`)

class TD_custom_product(TypedDict):
	id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	created_by: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	country_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	invoice_id: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	quote_id: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	name: types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	description: None | types_varchar #varchar(2048) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	vat: types_double #double NOT NULL,
	unit_reduc_rate: None | types_double #double DEFAULT NULL,
	price: types_double #double NOT NULL,
	quantity: types_int #int NOT NULL,
	created_at: types_datetime #datetime NOT NULL,
	updated_at: types_datetime #datetime NOT NULL,
	customer_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	credit_note_id: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	# PRIMARY KEY (`id`),
	# KEY `IDX_D4136D60DE12AB56` (`created_by`),
	# KEY `IDX_D4136D60F92F3E70` (`country_id`),
	# KEY `IDX_D4136D602989F1FD` (`invoice_id`),
	# KEY `IDX_D4136D60DB805178` (`quote_id`),
	# KEY `IDX_D4136D609395C3F3` (`customer_id`),
	# KEY `IDX_D4136D601C696F7A` (`credit_note_id`),
	# CONSTRAINT `FK_D4136D601C696F7A` FOREIGN KEY (`credit_note_id`) REFERENCES `credit_note` (`id`),
	# CONSTRAINT `FK_D4136D602989F1FD` FOREIGN KEY (`invoice_id`) REFERENCES `invoice` (`id`),
	# CONSTRAINT `FK_D4136D609395C3F3` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`),
	# CONSTRAINT `FK_D4136D60DB805178` FOREIGN KEY (`quote_id`) REFERENCES `quote` (`id`),
	# CONSTRAINT `FK_D4136D60DE12AB56` FOREIGN KEY (`created_by`) REFERENCES `decathlon_user` (`id`) ON DELETE SET NULL,
	# CONSTRAINT `FK_D4136D60F92F3E70` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`)

class TD_customer(TypedDict):
	id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	legalstatus_code: None | types_varchar #varchar(3) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	country_id: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	company_name: None | types_varchar #varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	email: None | types_varchar #varchar(180) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	loyalty_card_number: None | types_varchar #varchar(15) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	vat_number: None | types_varchar #varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	internal_ref: None | types_varchar #varchar(25) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	created_at: types_datetime #datetime NOT NULL,
	updated_at: types_datetime #datetime NOT NULL,
	created_by: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	pipedrive_organization_id: None | types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	data_policy_optin_date: None | types_datetime #datetime DEFAULT NULL,
	receive_emails_optin_date: None | types_datetime #datetime DEFAULT NULL,
	block_overall_email_date: None | types_datetime #datetime DEFAULT NULL,
	block_commercial_email_date: None | types_datetime #datetime DEFAULT NULL,
	creation_email_send_date: None | types_datetime #datetime DEFAULT NULL,
	internal_message: types_longtext #longtext COLLATE utf8mb4_unicode_ci,
	terms_and_conditions_optin_date: None | types_datetime #datetime DEFAULT NULL,
	# PRIMARY KEY (`id`),
	# KEY `IDX_81398E0930D8C529` (`legalstatus_code`),
	# KEY `IDX_81398E09F92F3E70` (`country_id`),
	# KEY `IDX_81398E09DE12AB56` (`created_by`),
	# CONSTRAINT `FK_81398E0930D8C529` FOREIGN KEY (`legalstatus_code`) REFERENCES `legal_status` (`code`),
	# CONSTRAINT `FK_81398E09DE12AB56` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`) ON DELETE SET NULL,
	# CONSTRAINT `FK_81398E09F92F3E70` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`)

class TD_customer_stats(TypedDict):
	id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	owner_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	calculation_date: types_datetime #datetime NOT NULL,
	quote_total_quantity: types_int #int NOT NULL,
	quote_total_value: types_double #double NOT NULL,
	invoice_total_quantity: types_int #int NOT NULL,
	invoice_total_value: types_double #double NOT NULL,
	credit_note_total_quantity: types_int #int NOT NULL,
	credit_note_total_value: types_double #double NOT NULL,
	# PRIMARY KEY (`id`),
	# KEY `IDX_997212917E3C61F9` (`owner_id`),
	# CONSTRAINT `FK_997212917E3C61F9` FOREIGN KEY (`owner_id`) REFERENCES `customer` (`id`)

class TD_decath_store(TypedDict):
	id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	country_id: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	store_id: types_varchar #varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
	name: types_varchar #varchar(125) COLLATE utf8mb4_unicode_ci NOT NULL,
	enabled: None | types_tinyint #tinyint(1) DEFAULT NULL,
	phone: None | types_varchar #varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	address: None | types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	postal_code: None | types_varchar #varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	city: None | types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	country_territory: types_json #json NOT NULL,
	facebook_url: None | types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	do_order: None | types_tinyint #tinyint(1) DEFAULT NULL,
	click_and_collect: None | types_tinyint #tinyint(1) DEFAULT NULL,
	created_by: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	created_at: types_datetime #datetime NOT NULL,
	updated_at: types_datetime #datetime NOT NULL,
	# PRIMARY KEY (`id`),
	# KEY `IDX_54240956F92F3E70` (`country_id`),
	# KEY `IDX_54240956DE12AB56` (`created_by`),
	# CONSTRAINT `FK_54240956DE12AB56` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`) ON DELETE SET NULL,
	# CONSTRAINT `FK_54240956F92F3E70` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`)

class TD_delivery_address(TypedDict):
	id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	customer_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	address: types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	additional_address: None | types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	postcode: types_varchar #varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
	city: types_varchar #varchar(55) COLLATE utf8mb4_unicode_ci NOT NULL,
	# PRIMARY KEY (`id`),
	# KEY `IDX_750D05F9395C3F3` (`customer_id`),
	# CONSTRAINT `FK_750D05F9395C3F3` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`)

class TD_front_heading_picture(TypedDict):
	id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	config_id: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	file_path: None | types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	# PRIMARY KEY (`id`),
	# UNIQUE KEY `UNIQ_F01A281B24DB0683` (`config_id`),
	# CONSTRAINT `FK_F01A281B24DB0683` FOREIGN KEY (`config_id`) REFERENCES `country_config` (`id`)

class TD_front_office_user(TypedDict):
	id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	country_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	api_key: types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	# PRIMARY KEY (`id`),
	# UNIQUE KEY `UNIQ_2B51C4D0F92F3E70` (`country_id`),
	# CONSTRAINT `FK_2B51C4D0BF396750` FOREIGN KEY (`id`) REFERENCES `user` (`id`) ON DELETE CASCADE,
	# CONSTRAINT `FK_2B51C4D0F92F3E70` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`)

class TD_front_request_contact(TypedDict):
	id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	country_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	content: types_text #text COLLATE utf8mb4_unicode_ci NOT NULL,
	from_email: types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	notification_sent: types_tinyint #tinyint(1) NOT NULL,
	telephone: types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	quote_number: None | types_varchar #varchar(15) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	company_name: types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	# PRIMARY KEY (`id`),
	# KEY `IDX_E7738291F92F3E70` (`country_id`),
	# CONSTRAINT `FK_E7738291F92F3E70` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`)

class TD_gift_card(TypedDict):
	id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	created_by: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	country_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	quote_id: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	invoice_id: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	number: types_varchar #varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
	quantity: types_int #int NOT NULL,
	description: None | types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	amount: types_double #double NOT NULL,
	price: types_double #double NOT NULL,
	vat: types_double #double NOT NULL,
	unit_reduc_rate: types_double #double NOT NULL,
	created_at: types_datetime #datetime NOT NULL,
	updated_at: types_datetime #datetime NOT NULL,
	customer_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	credit_note_id: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	# PRIMARY KEY (`id`),
	# KEY `IDX_E4696A8EDE12AB56` (`created_by`),
	# KEY `IDX_E4696A8EF92F3E70` (`country_id`),
	# KEY `IDX_E4696A8EDB805178` (`quote_id`),
	# KEY `IDX_E4696A8E2989F1FD` (`invoice_id`),
	# KEY `IDX_E4696A8E9395C3F3` (`customer_id`),
	# KEY `IDX_E4696A8E1C696F7A` (`credit_note_id`),
	# CONSTRAINT `FK_E4696A8E1C696F7A` FOREIGN KEY (`credit_note_id`) REFERENCES `credit_note` (`id`),
	# CONSTRAINT `FK_E4696A8E2989F1FD` FOREIGN KEY (`invoice_id`) REFERENCES `invoice` (`id`),
	# CONSTRAINT `FK_E4696A8E9395C3F3` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`),
	# CONSTRAINT `FK_E4696A8EDB805178` FOREIGN KEY (`quote_id`) REFERENCES `quote` (`id`),
	# CONSTRAINT `FK_E4696A8EDE12AB56` FOREIGN KEY (`created_by`) REFERENCES `decathlon_user` (`id`) ON DELETE SET NULL,
	# CONSTRAINT `FK_E4696A8EF92F3E70` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`)

class TD_invoice(TypedDict):
	id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	country_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	quote_id: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	delivery_method_code: types_varchar #varchar(3) COLLATE utf8mb4_unicode_ci NOT NULL,
	billing_address_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	delivery_address_id: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	customer_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	created_by: None | types_char #char(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	status_code: None | types_varchar #varchar(3) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	shipping_cost_id: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	delivery_decath_store_id: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	number: types_varchar #varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
	additional_note: types_longtext #longtext COLLATE utf8mb4_unicode_ci,
	amount: types_double #double NOT NULL,
	created_at: types_datetime #datetime NOT NULL,
	updated_at: types_datetime #datetime NOT NULL,
	discount: None | types_double #double DEFAULT NULL,
	assigned_to: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	business_unit: None | types_varchar #varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	# PRIMARY KEY (`id`),
	# UNIQUE KEY `UNIQ_90651744DB805178` (`quote_id`),
	# KEY `IDX_90651744F92F3E70` (`country_id`),
	# KEY `IDX_9065174457DCEBA8` (`delivery_method_code`),
	# KEY `IDX_9065174479D0C0E4` (`billing_address_id`),
	# KEY `IDX_90651744EBF23851` (`delivery_address_id`),
	# KEY `IDX_906517449395C3F3` (`customer_id`),
	# KEY `IDX_90651744DE12AB56` (`created_by`),
	# KEY `IDX_906517444F139D0C` (`status_code`),
	# KEY `IDX_90651744FBF783BB` (`shipping_cost_id`),
	# KEY `IDX_906517445577E8D3` (`delivery_decath_store_id`),
	# KEY `IDX_9065174489EEAF91` (`assigned_to`),
	# CONSTRAINT `FK_906517444F139D0C` FOREIGN KEY (`status_code`) REFERENCES `invoice_status` (`code`),
	# CONSTRAINT `FK_906517445577E8D3` FOREIGN KEY (`delivery_decath_store_id`) REFERENCES `decath_store` (`id`),
	# CONSTRAINT `FK_9065174457DCEBA8` FOREIGN KEY (`delivery_method_code`) REFERENCES `delivery_method` (`code`),
	# CONSTRAINT `FK_9065174479D0C0E4` FOREIGN KEY (`billing_address_id`) REFERENCES `billing_address` (`id`),
	# CONSTRAINT `FK_9065174489EEAF91` FOREIGN KEY (`assigned_to`) REFERENCES `decathlon_user` (`id`) ON DELETE SET NULL,
	# CONSTRAINT `FK_906517449395C3F3` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`),
	# CONSTRAINT `FK_90651744DB805178` FOREIGN KEY (`quote_id`) REFERENCES `quote` (`id`),
	# CONSTRAINT `FK_90651744DE12AB56` FOREIGN KEY (`created_by`) REFERENCES `decathlon_user` (`id`) ON DELETE SET NULL,
	# CONSTRAINT `FK_90651744EBF23851` FOREIGN KEY (`delivery_address_id`) REFERENCES `delivery_address` (`id`) ON DELETE SET NULL,
	# CONSTRAINT `FK_90651744F92F3E70` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`),
	# CONSTRAINT `FK_90651744FBF783BB` FOREIGN KEY (`shipping_cost_id`) REFERENCES `shipping_cost` (`id`)

class TD_pipedrive_custom_field(TypedDict):
	key: types_varchar #varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
	config_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	name: types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	type: types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	id: types_int #int NOT NULL AUTO_INCREMENT,
	# PRIMARY KEY (`id`),
	# KEY `IDX_5914506124DB0683` (`config_id`),
	# CONSTRAINT `FK_5914506124DB0683` FOREIGN KEY (`config_id`) REFERENCES `country_config` (`id`)

class TD_product(TypedDict):
	id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	quote_id: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	invoice_id: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	display_name: types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	product_id: types_varchar #varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
	model_id: types_varchar #varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
	sku_id: types_varchar #varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
	sku_price: types_double #double NOT NULL,
	price_overwrite: None | types_double #double DEFAULT NULL,
	tax_code: types_int #int NOT NULL DEFAULT '8',
	quantity: types_int #int NOT NULL,
	additional_note: None | types_varchar #varchar(455) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	unit_reduc_rate: None | types_double #double DEFAULT NULL,
	position: types_int #int NOT NULL DEFAULT '0',
	picture_url: None | types_varchar #varchar(2048) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	sku_name: None | types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	created_at: types_datetime #datetime NOT NULL,
	updated_at: types_datetime #datetime NOT NULL,
	credit_note_id: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	audience_locale: None | types_varchar #varchar(5) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	taxes: types_json #json NOT NULL,
	dk_article_id: None | types_varchar #varchar(64) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	# PRIMARY KEY (`id`),
	# KEY `IDX_D34A04ADDB805178` (`quote_id`),
	# KEY `IDX_D34A04AD2989F1FD` (`invoice_id`),
	# KEY `IDX_D34A04AD1C696F7A` (`credit_note_id`),
	# CONSTRAINT `FK_D34A04AD1C696F7A` FOREIGN KEY (`credit_note_id`) REFERENCES `credit_note` (`id`),
	# CONSTRAINT `FK_D34A04AD2989F1FD` FOREIGN KEY (`invoice_id`) REFERENCES `invoice` (`id`),
	# CONSTRAINT `FK_D34A04ADDB805178` FOREIGN KEY (`quote_id`) REFERENCES `quote` (`id`)

class TD_product_stats(TypedDict):
	id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	country_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	sku_id: types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	model_id: types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	product_id: types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	display_name: types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	quote_total_quantity: types_int #int NOT NULL,
	quote_total_value: types_double #double NOT NULL,
	invoice_total_quantity: types_int #int NOT NULL,
	invoice_total_value: types_double #double NOT NULL,
	credit_note_total_quantity: types_int #int NOT NULL,
	credit_note_total_value: types_double #double NOT NULL,
	calculation_date: types_datetime #datetime NOT NULL,
	sku_name: None | types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	# PRIMARY KEY (`id`),
	# KEY `IDX_F61B1CF6F92F3E70` (`country_id`),
	# CONSTRAINT `FK_F61B1CF6F92F3E70` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`)

class TD_quote(TypedDict):
	id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	customer_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	billing_address_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	delivery_address_id: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	country_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	delivery_method_code: types_varchar #varchar(3) COLLATE utf8mb4_unicode_ci NOT NULL,
	created_by: None | types_char #char(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	origin_code: None | types_varchar #varchar(3) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	status_code: None | types_varchar #varchar(3) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	shipping_cost_id: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	delivery_decath_store_id: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	number: types_varchar #varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
	additional_note: types_longtext #longtext COLLATE utf8mb4_unicode_ci,
	amount: types_double #double NOT NULL,
	created_at: types_datetime #datetime NOT NULL,
	updated_at: types_datetime #datetime NOT NULL,
	pipedrive_deal_id: None | types_varchar #varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	discount: None | types_double #double DEFAULT NULL,
	assigned_to: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	business_unit: None | types_varchar #varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	# PRIMARY KEY (`id`),
	# KEY `IDX_6B71CBF49395C3F3` (`customer_id`),
	# KEY `IDX_6B71CBF479D0C0E4` (`billing_address_id`),
	# KEY `IDX_6B71CBF4EBF23851` (`delivery_address_id`),
	# KEY `IDX_6B71CBF4F92F3E70` (`country_id`),
	# KEY `IDX_6B71CBF457DCEBA8` (`delivery_method_code`),
	# KEY `IDX_6B71CBF4DE12AB56` (`created_by`),
	# KEY `IDX_6B71CBF4B03BC868` (`origin_code`),
	# KEY `IDX_6B71CBF44F139D0C` (`status_code`),
	# KEY `IDX_6B71CBF4FBF783BB` (`shipping_cost_id`),
	# KEY `IDX_6B71CBF45577E8D3` (`delivery_decath_store_id`),
	# KEY `IDX_6B71CBF489EEAF91` (`assigned_to`),
	# CONSTRAINT `FK_6B71CBF44F139D0C` FOREIGN KEY (`status_code`) REFERENCES `quote_status` (`code`),
	# CONSTRAINT `FK_6B71CBF45577E8D3` FOREIGN KEY (`delivery_decath_store_id`) REFERENCES `decath_store` (`id`),
	# CONSTRAINT `FK_6B71CBF457DCEBA8` FOREIGN KEY (`delivery_method_code`) REFERENCES `delivery_method` (`code`),
	# CONSTRAINT `FK_6B71CBF479D0C0E4` FOREIGN KEY (`billing_address_id`) REFERENCES `billing_address` (`id`),
	# CONSTRAINT `FK_6B71CBF489EEAF91` FOREIGN KEY (`assigned_to`) REFERENCES `decathlon_user` (`id`) ON DELETE SET NULL,
	# CONSTRAINT `FK_6B71CBF49395C3F3` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`),
	# CONSTRAINT `FK_6B71CBF4B03BC868` FOREIGN KEY (`origin_code`) REFERENCES `quote_origin` (`code`) ON DELETE SET NULL,
	# CONSTRAINT `FK_6B71CBF4DE12AB56` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`) ON DELETE SET NULL,
	# CONSTRAINT `FK_6B71CBF4EBF23851` FOREIGN KEY (`delivery_address_id`) REFERENCES `delivery_address` (`id`) ON DELETE SET NULL,
	# CONSTRAINT `FK_6B71CBF4F92F3E70` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`),
	# CONSTRAINT `FK_6B71CBF4FBF783BB` FOREIGN KEY (`shipping_cost_id`) REFERENCES `shipping_cost` (`id`)

class TD_shipping_cost(TypedDict):
	id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	country_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	name: types_varchar #varchar(125) COLLATE utf8mb4_unicode_ci NOT NULL,
	price: types_double #double NOT NULL,
	only_once: types_tinyint #tinyint(1) NOT NULL,
	enabled: types_tinyint #tinyint(1) NOT NULL DEFAULT '1',
	vat: types_double #double NOT NULL,
	created_at: types_datetime #datetime NOT NULL,
	updated_at: types_datetime #datetime NOT NULL,
	createdBy: None | types_char #char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '(DC2Type:uuid)',
	# PRIMARY KEY (`id`),
	# KEY `IDX_899A02FEF92F3E70` (`country_id`),
	# KEY `IDX_899A02FED3564642` (`createdBy`),
	# CONSTRAINT `FK_899A02FED3564642` FOREIGN KEY (`createdBy`) REFERENCES `decathlon_user` (`id`) ON DELETE SET NULL,
	# CONSTRAINT `FK_899A02FEF92F3E70` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`)

class TD_users_countries(TypedDict):
	decathlon_user_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	country_id: types_char #char(36) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '(DC2Type:uuid)',
	# PRIMARY KEY (`decathlon_user_id`,`country_id`),
	# KEY `IDX_3B1B914CF92F3E70` (`country_id`),
	# KEY `IDX_3B1B914CC41F7079` (`decathlon_user_id`),
	# CONSTRAINT `FK_3B1B914CC41F7079` FOREIGN KEY (`decathlon_user_id`) REFERENCES `decathlon_user` (`id`) ON DELETE CASCADE,
	# CONSTRAINT `FK_3B1B914CF92F3E70` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`) ON DELETE CASCADE

TD_any = TD_banner_message|TD_credit_note_status|TD_credit_note_status_translations|TD_delivery_method|TD_delivery_method_translations|TD_doctrine_migration_versions|TD_ext_translations|TD_invoice_status|TD_invoice_status_translations|TD_legal_status|TD_legal_status_translations|TD_quote_origin|TD_quote_origin_translations|TD_quote_status|TD_quote_status_translations|TD_user|TD_decathlon_user|TD_manage|TD_user_connection_log|TD_user_stats|TD_banner_message_country|TD_billing_address|TD_country|TD_country_config|TD_country_featured_product|TD_country_stats|TD_country_vat|TD_credit_note|TD_custom_product|TD_customer|TD_customer_stats|TD_decath_store|TD_delivery_address|TD_front_heading_picture|TD_front_office_user|TD_front_request_contact|TD_gift_card|TD_invoice|TD_pipedrive_custom_field|TD_product|TD_product_stats|TD_quote|TD_shipping_cost|TD_users_countries
