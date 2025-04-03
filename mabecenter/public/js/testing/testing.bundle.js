import { createApp } from "vue";
import App from "./App.vue";


class Testing {
	constructor({ page, wrapper }) {
		this.$wrapper = $(wrapper);
		this.page = page;

		this.init();
	}

	init() {
		this.setup_page_actions();
		this.setup_app();
	}

	setup_page_actions() {
		// setup page actions
		this.primary_btn = this.page.set_primary_action(__("Print Message"), () =>
	  frappe.msgprint("Hello My Page!")
		);
	}

	setup_app() {
		// create a vue instance
		let app = createApp(App);
		// mount the app
		this.$testing = app.mount(this.$wrapper.get(0));
	}
}

frappe.provide("frappe.ui");
frappe.ui.Testing = Testing;
export default Testing;