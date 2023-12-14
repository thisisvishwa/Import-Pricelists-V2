# Odoo 16 CE Excel Pricelist Import Module

## Introduction

This module provides a feature to import and update pricelists directly from Excel files in Odoo 16 Community Edition (CE). It is designed to simplify and expedite the process of pricelist management, eliminating the need for manual data entry and reducing errors.

## Features

- **Excel File Import**: Supports both .xls and .xlsx formats.
- **xlrd Library Dependency**: Utilizes the `xlrd` Python library to read Excel files.
- **Sample Excel File**: Includes a sample Excel file illustrating the required format and layout for successful import.
- **Field Import Support**: Compatible with various pricelist-related fields.

## Installation

1. Download or clone this repository to your Odoo addons directory.
2. Restart the Odoo server.
3. Go to Apps menu and click on 'Update Apps List'.
4. Remove the 'Apps' filter and search for 'excel_pricelist_import_module'.
5. Click on 'Install' to install the module.

## Usage

1. Go to the Pricelist Import page.
2. Click on 'Upload' and select your Excel file, or drag and drop the file into the upload area.
3. The system will validate the format and structure of the Excel file.
4. Preview the data to be imported and make necessary adjustments.
5. Click on 'Import' to finalize the import.

## Dependencies

This module depends on the `xlrd` Python library. Make sure to install it in your Python environment before installing the module. You can do this by running `pip install -r requirements.txt`.

## Sample Excel File

A sample Excel file is included in the module at `data/sample_excel_file.xls`. Use this file as a reference for the required data format.

## Documentation

For more detailed user and technical documentation, including screenshots and step-by-step guides, please refer to the official documentation.

## License

This module adheres to the licensing terms of Odoo CE.