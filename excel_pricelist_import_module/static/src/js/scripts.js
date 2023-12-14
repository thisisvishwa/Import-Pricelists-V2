odoo.define('excel_pricelist_import_module.scripts', function (require) {
    "use strict";

    var core = require('web.core');
    var ajax = require('web.ajax');
    var Widget = require('web.Widget');

    var QWeb = core.qweb;
    var _t = core._t;

    var PricelistImportWidget = Widget.extend({
        template: 'excel_pricelist_import_module.ImportView',
        events: {
            'change .o_import_file': 'on_file_change',
            'click .o_import_button': 'on_import_button_click',
        },

        on_file_change: function (event) {
            var self = this;
            var file = event.target.files[0];
            var reader = new FileReader();

            reader.onload = function (event) {
                var data = event.target.result;
                self.preview_data(data);
            };

            reader.readAsText(file);
        },

        preview_data: function (data) {
            // TODO: Implement data preview functionality
        },

        on_import_button_click: function () {
            var self = this;
            var file_input = this.$('.o_import_file')[0];
            var file = file_input.files[0];

            var data = new FormData();
            data.append('file', file);

            ajax.post('/excel_pricelist_import_module/import', data).then(function (response) {
                if (response.error) {
                    self.display_error(response.error);
                } else {
                    self.display_success(response.message);
                }
            });
        },

        display_error: function (message) {
            this.$('.o_import_error').text(message).show();
        },

        display_success: function (message) {
            this.$('.o_import_success').text(message).show();
        },
    });

    core.action_registry.add('excel_pricelist_import_module', PricelistImportWidget);

    return PricelistImportWidget;
});