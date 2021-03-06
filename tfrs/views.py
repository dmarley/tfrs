import json

from django.http import HttpResponse
from django.shortcuts import render

def dashboard(request):
    table_data = [
        {'transaction':{ 'fuelSupplier': 'BC EveryFuel', 'type': 'Sell', 'partner': 'BC AnyFuel', 'quantity': 15000, 'fairMarketValue': '$100', 'lastModified': '2015-04-01', 'effectiveDate': '2015-04-01', 'status': 'Draft', 'balance': 75000, 'compliance_period': '2016'}},
        {'transaction':{ 'fuelSupplier': 'BC EveryFuel', 'type': 'Buy', 'partner': 'BC AnyFuel', 'quantity': 5000, 'fairMarketValue': '$70', 'lastModified': '2016-12-15', 'effectiveDate': '2017-01-31', 'status': 'Balanced Updated', 'balance': 80000, 'compliance_period': '2016'}},
        {'transaction':{ 'fuelSupplier': 'BC EveryFuel', 'type': 'Sell', 'partner': 'BC AnyFuel', 'quantity': 75000, 'fairMarketValue': '$125', 'lastModified': '2017-04-04', 'effectiveDate': '2017-12-31', 'status': 'Offer', 'balance': 80000, 'compliance_period': '2016'}},
        {'transaction':{ 'fuelSupplier': 'BC EveryFuel', 'type': 'Sell', 'partner': 'BC AnyFuel', 'quantity': 7500, 'fairMarketValue': '$120', 'lastModified': '2017-02-28', 'effectiveDate': '2017-02-28', 'status': 'Balanced Updated', 'balance': 87500, 'compliance_period': '2016'}},
        {'transaction':{ 'fuelSupplier': 'BC EveryFuel', 'type': 'Buy', 'partner': 'BC AnyFuel', 'quantity': 1500, 'fairMarketValue': '$750', 'lastModified': '2017-03-20', 'effectiveDate': '2017-03-20', 'status': 'Balanced Updated', 'balance': 89000, 'compliance_period': '2016'}}
    ]
    notifications = [
        {'id': 1, 'subject': 'Credit Transfer Proposed', 'date': '2 dys ago', 'flagged': False, 'message': 'A credit transfer was proposed from exxon'},
        {'id': 2, 'subject': 'Credits Awarded - Fuel Supply', 'date': '3 wk ago', 'flagged': True, 'message': 'Credits have been awarded by Fuel Supply'},
        {'id': 3, 'subject': 'Credits Awarded - Part Three', 'date': '2 mos ago', 'flagged': False, 'message': 'Credits have been awarded by Part Three Agreement'}
    ]
    return render(request, 'dashboard.html', {
        'table_data': json.dumps(table_data),
        'notifications': notifications
    })

def account_activity(request):
    table_data = [
        {'transaction':{ 'fuelSupplier': 'BC EveryFuel', 'type': 'Sell', 'partner': 'BC AnyFuel', 'quantity': 25000, 'fairMarketValue': '$250', 'lastModified': '2017-01-15', 'effectiveDate': '2017-05-31', 'status': 'Rejected', 'balance': 50000, 'compliance_period': '2016'}},
        {'transaction':{ 'fuelSupplier': 'BC EveryFuel', 'type': 'Buy', 'partner': 'BC AnyFuel', 'quantity': 5000, 'fairMarketValue': '$50', 'lastModified': '2016-11-21', 'effectiveDate': '2016-12-25', 'status': 'Cancelled', 'balance': 50000, 'compliance_period': '2016'}},
        {'transaction':{ 'fuelSupplier': 'BC EveryFuel', 'type': 'Award from Fuel Supply', 'partner': 'BC Gov', 'quantity': 25000, 'fairMarketValue': '$75', 'lastModified': '2016-10-31', 'effectiveDate': '2016-10-31', 'status': 'Balanced Updated', 'balance': 75000, 'compliance_period': '2016'}},
        {'transaction':{ 'fuelSupplier': 'BC EveryFuel', 'type': 'Award from Pt3 Agrmt', 'partner': 'BC Gov', 'quantity': 15000, 'fairMarketValue': '$75', 'lastModified': '2017-03-31', 'effectiveDate': '2017-04-21', 'status': 'Approved', 'balance': 75000, 'compliance_period': '2016'}},
        {'transaction':{ 'fuelSupplier': 'BC EveryFuel', 'type': 'Buy', 'partner': 'BC AnyFuel', 'quantity': 5500, 'fairMarketValue': '$70', 'lastModified': '2017-02-15', 'effectiveDate': '2017-12-24', 'status': 'Pending', 'balance': 75000, 'compliance_period': '2016'}},
        {'transaction':{ 'fuelSupplier': 'BC EveryFuel', 'type': 'Sell', 'partner': 'BC AnyFuel', 'quantity': 5000, 'fairMarketValue': '$90', 'lastModified': '2017-04-04', 'effectiveDate': '2017-11-11', 'status': 'Proposed', 'balance': 75000, 'compliance_period': '2016'}},
        {'transaction':{ 'fuelSupplier': 'BC EveryFuel', 'type': 'Sell', 'partner': 'BC AnyFuel', 'quantity': 15000, 'fairMarketValue': '$100', 'lastModified': '2015-04-01', 'effectiveDate': '2015-04-01', 'status': 'Draft', 'balance': 75000, 'compliance_period': '2016'}},
        {'transaction':{ 'fuelSupplier': 'BC EveryFuel', 'type': 'Buy', 'partner': 'BC AnyFuel', 'quantity': 5000, 'fairMarketValue': '$70', 'lastModified': '2016-12-15', 'effectiveDate': '2017-01-31', 'status': 'Balanced Updated', 'balance': 80000, 'compliance_period': '2016'}},
        {'transaction':{ 'fuelSupplier': 'BC EveryFuel', 'type': 'Sell', 'partner': 'BC AnyFuel', 'quantity': 75000, 'fairMarketValue': '$125', 'lastModified': '2017-04-04', 'effectiveDate': '2017-12-31', 'status': 'Offer', 'balance': 80000, 'compliance_period': '2016'}},
        {'transaction':{ 'fuelSupplier': 'BC EveryFuel', 'type': 'Sell', 'partner': 'BC AnyFuel', 'quantity': 7500, 'fairMarketValue': '$120', 'lastModified': '2017-02-28', 'effectiveDate': '2017-02-28', 'status': 'Balanced Updated', 'balance': 87500, 'compliance_period': '2016'}},
        {'transaction':{ 'fuelSupplier': 'BC EveryFuel', 'type': 'Buy', 'partner': 'BC AnyFuel', 'quantity': 1500, 'fairMarketValue': '$750', 'lastModified': '2017-03-20', 'effectiveDate': '2017-03-20', 'status': 'Balanced Updated', 'balance': 89000, 'compliance_period': '2016'}}
    ]
    return render(request, 'account-activity.html', {'table_data': json.dumps(table_data)})

def new_transaction(request):
    return render(request, 'new-transaction.html', {})

def transaction_summary(request):
    transaction = {
        'partner': 'BC AnyFuel',
        'partner_adddress': '1234 Douglas Road, V3G 6N1, Victoria, BC',
        'type': 'Buy',
        'quantity': 5000,
        'fair_market_value': '$70',
        'total_value': '$35,000',
        'compliance_period': '2016',
        'effective_date': '2017-01-31'
    }
    return render(request, 'transaction-summary.html', {'transaction': transaction})

def settings(request):
    return render(request, 'settings.html', {})

def notifications(request):
    notifications = [
        {'id': 1, 'subject': 'Credit Transfer Proposed', 'date': '2015-05-30', 'flagged': False, 'message': 'A credit transfer was proposed from exxon'},
        {'id': 2, 'subject': 'Credits Awarded - Fuel Supply', 'date': '2016-01-15', 'flagged': True, 'message': 'Credits have been awarded by Fuel Supply'},
        {'id': 3, 'subject': 'Credits Awarded - Part Three', 'date': '2017-02-15', 'flagged': False, 'message': 'Credits have been awarded by Part Three Agreement'}
    ]
    return render(request, 'notifications.html', {'notifications': notifications})
