// Copyright (c) 2024, Dante Devenir and contributors
// For license information, please see license.txt

frappe.ui.form.on("VTigerCRM Sync", {
	setup(frm) {
		frm.toggle_display("section_sync_preview", false);
		console.log("Setup Step")
		frappe.realtime.on("vtigercrm_sync_refresh", ({ percentage, vtigercrm_sync }) => {		
			// Validar que el sync corresponda al documento actual
			if (vtigercrm_sync !== frm.doc.name) return;
			
			updateProgressBar(frm, percentage);
			//reloadDocument(frm);
		})
		frappe.realtime.on("vtigercrm_sync_error_log", ({ error_log, vtigercrm_sync }) => {
			if (vtigercrm_sync !== frm.doc.name) return;
			
			updateErrorLog(frm, error_log);
			//reloadDocument(frm);
		})
	},
	onload(frm) {
		if (frm.is_new()) {
			frm.toggle_display("section_sync_preview", false);
		}
	},
	refresh(frm) {
        frm.toggle_display("section_sync_preview", false);
        frm.trigger("update_primary_action");
    },
    onload_post_render(frm) {
		frm.trigger("update_primary_action");
	},
    update_primary_action(frm) {
		if (frm.is_dirty()) {
			frm.enable_save();
			return;
		}
		frm.disable_save();
		if (frm.doc.status !== "Success") {
			if (!frm.is_new()) {
				let label = frm.doc.status === "Pending" ? __("Start Sync") : __("Retry");
				frm.page.set_primary_action(label, () => frm.events.start_sync(frm));
			} else {
				frm.page.set_primary_action(__("Save"), () => frm.save());
			}
		}
	},
	start_sync(frm) {
		frm.toggle_display("section_sync_preview", true);
		frm.call({
			method: "form_start_sync",
			args: { vtigercrm_sync: frm.doc.name },
			btn: frm.page.btn_primary,
		}).then((r) => {
			if (r.message === true) {
				frm.disable_save();
			}
		});
	},
});

function updateErrorLog(frm, error_log) {
    const $wrapper = frm.get_field("sync_preview").$wrapper;
    $wrapper.empty();
    
    const $progress = $(`<div class="warning">`).appendTo($wrapper);

	$('<p class="text-danger">')
		.text(`${error_log}`)
		.appendTo($progress);
}

function updateProgressBar(frm, percentage) {
	const $wrapper = frm.get_field("sync_preview").$wrapper;
	$wrapper.empty();
	
	const $progress = $('<div class="progress">').appendTo($wrapper);
	$('<div class="progress-bar progress-bar-striped progress-bar-animated bg-primary">')
		.attr({
			'role': 'progressbar',
			'style': `width: ${percentage}%`,
			'aria-valuenow': percentage,
			'aria-valuemin': '0', 
			'aria-valuemax': '100'
		})
		.text(`${percentage}%`)
		.appendTo($progress);
}

function reloadDocument(frm) {
	frappe.model.with_doc("VTigerCRM Sync", frm.doc.name)
		.then(() => frm.reload_doc());
}
