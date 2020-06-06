# -*- coding: utf-8 -*-

{
    'name' : 'AFCC Sale Report',
    'version' : '13.0',
    'summary': 'AFCC Sale Report',
    'category': 'Sales',
    'author' : 'Magdy, TeleNoc',
    'description': """ AFCC Sale Report""",
    "license": "AGPL-3",
    'depends' : ['sale'],
    'data': [
        'wizard/wiz_periodical_report_view.xml',
        'views/periodical_report.xml',
        'views/report_periodical_sales.xml'
    ],
}
