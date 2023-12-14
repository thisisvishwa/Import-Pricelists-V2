{
    "name": "excel_pricelist_import_module",
    "version": "1.0",
    "category": "Extra Tools",
    "summary": "Excel Pricelist Import Module for Odoo 16 CE",
    "sequence": 1,
    "author": "Your Company",
    "website": "http://www.yourcompany.com",
    "description": """
Excel Pricelist Import Module
=============================
This module provides a feature to import and update pricelists directly from Excel files. It supports both .xls and .xlsx formats and uses the xlrd Python library to read Excel files. The module also includes a sample Excel file demonstrating the required data format.
""",
    "depends": ["base", "product", "sale"],
    "data": [
        "views/import_view.xml",
        "data/sample_excel_file.xls"
    ],
    "demo": [],
    "installable": True,
    "auto_install": False,
    "application": True,
    "external_dependencies": {
        "python": ["xlrd"]
    }
}