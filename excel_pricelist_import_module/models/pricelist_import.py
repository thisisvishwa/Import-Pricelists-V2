```python
from odoo import models, fields

class PricelistImport(models.Model):
    _name = 'pricelist.import'
    _description = 'Pricelist Import'

    pricelist_id = fields.Char('Pricelist ID', required=True)
    name = fields.Char('Name', required=True)
    currency = fields.Char('Currency', required=True)
    product_category = fields.Char('Product Category', required=True)
    min_quantity = fields.Integer('Min. Quantity', required=True)
    start_date = fields.Date('Start Date', required=True)
    end_date = fields.Date('End Date', required=True)
    pricing_computation_method = fields.Char('Pricing Computation Method', required=True)

    def import_excel_file(self, file_path):
        # Import the xlrd library
        import xlrd

        # Open the workbook and select the first worksheet
        wb = xlrd.open_workbook(file_path)
        sheet = wb.sheet_by_index(0)

        # Read the data and store it in the database
        for row in range(1, sheet.nrows):
            values = {
                'pricelist_id': sheet.cell(row, 0).value,
                'name': sheet.cell(row, 1).value,
                'currency': sheet.cell(row, 2).value,
                'product_category': sheet.cell(row, 3).value,
                'min_quantity': int(sheet.cell(row, 4).value),
                'start_date': sheet.cell(row, 5).value,
                'end_date': sheet.cell(row, 6).value,
                'pricing_computation_method': sheet.cell(row, 7).value,
            }
            self.create(values)
```