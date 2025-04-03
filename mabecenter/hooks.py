app_name = "mabecenter"
app_title = "Mabecenter"
app_publisher = "Dante Devenir"
app_description = "Test app customize"
app_email = "dantedevenir@outlook.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "mabecenter",
# 		"logo": "/assets/mabecenter/logo.png",
# 		"title": "Mabecenter",
# 		"route": "/mabecenter",
# 		"has_permission": "mabecenter.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mabecenter/css/mabecenter.css"
# app_include_js = "/assets/mabecenter/js/mabecenter.js"

# include js, css files in header of web template
# web_include_css = "/assets/mabecenter/css/mabecenter.css"
# web_include_js = "/assets/mabecenter/js/mabecenter.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "mabecenter/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "mabecenter/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "mabecenter.utils.jinja_methods",
# 	"filters": "mabecenter.utils.jinja_filters"
# }

# Installation
# ------------


# after_install = "mabecenter.install.after_install"
before_install = "mabecenter.installer.before_install"

after_migrate = "mabecenter.installer.before_install"

# setup wizard
setup_wizard_requires = "assets/mabecenter/js/setup_wizard.js"
#setup_wizard_stages = "mabecenter.setup.setup_wizard.setup_wizard.get_setup_stages"

# import fixtures
fixtures = [
    # export all records from the Category table
    # "Patient",
	"Client Script",
    "Server Script",
    # "Contact"
    # export only those records that match the filters from the Role table
    #{"dt": "Role", "filters": [["role_name", "like", "Admin%"]]},
]

# Uninstallation
# ------------

# before_uninstall = "mabecenter.uninstall.before_uninstall"
# after_uninstall = "mabecenter.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "mabecenter.utils.before_app_install"
# after_app_install = "mabecenter.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "mabecenter.utils.before_app_uninstall"
# after_app_uninstall = "mabecenter.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mabecenter.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

doc_events = {
    "Contact": {
        "validate": "mabecenter.overrides.contact.validate_contact"
    }
}

# Scheduled Tasks
# ---------------

scheduler_events = {
    # frappe.email.queue.flush every 60 seconds
    "cron": {
        "*/60 * * * *": [
            "frappe.email.queue.flush"
        ]
    },
}

# Testing
# -------

# before_tests = "mabecenter.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "mabecenter.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "mabecenter.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["mabecenter.utils.before_request"]
# after_request = ["mabecenter.utils.after_request"]

# Job Events
# ----------
# before_job = ["mabecenter.utils.before_job"]
# after_job = ["mabecenter.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"mabecenter.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

website_route_rules = [
    {"from_route": "/dashboard/<path:app_path>", "to_route": "dashboard"}
]
