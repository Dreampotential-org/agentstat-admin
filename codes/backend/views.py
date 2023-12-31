from django.shortcuts import render
from backend.utils import api_client
from datetime import datetime

import dateutil.relativedelta


def _make_date_filter(date_filter, start_date, end_date):
    now = datetime.strptime(
        datetime.strftime(datetime.now(), '%Y-%m-%d'), "%Y-%m-%d"
    )
    now = now + dateutil.relativedelta.relativedelta(days=1)

    if date_filter == 'last-7-days':
        days = 7
    elif date_filter == 'last-30-days':
        days = 30
    elif date_filter == 'this-month':
        days = datetime.now().day
    elif date_filter == 'last-month':
        start_date = datetime.strptime(
            str(datetime.now().year) + '-' +
            str(datetime.now().month - 1) + '-' + '01',
            '%Y-%m-%d'
        )
        start_date = datetime.strftime(start_date, '%Y-%m-%d')

        end_date = datetime.strptime(
            str(datetime.now().year) + '-' +
            str(datetime.now().month - 1) + '-' + '31',
            '%Y-%m-%d'
        )
        end_date = datetime.strftime(end_date, '%Y-%m-%d')
    elif date_filter == 'year-to-date':
        start_date = datetime.strptime(
            str(datetime.now().year) + '-' + '01' + '-' + '01', '%Y-%m-%d'
        )
        start_date = datetime.strftime(start_date, '%Y-%m-%d')

    elif date_filter == 'custom':
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

        start_date = datetime.strftime(start_date, '%Y-%m-%d')
        end_date = datetime.strftime(end_date, '%Y-%m-%d')

    if not start_date:
        start_date = now - dateutil.relativedelta.relativedelta(days=days)
        start_date = datetime.strftime(start_date, '%Y-%m-%d')

    if not end_date:
        end_date = datetime.strftime(now, '%Y-%m-%d')

    return start_date, end_date


def dashboard(request):
    date_filter = request.GET.get('date-filter', 'last-7-days')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if date_filter:
        start_date, end_date = _make_date_filter(
            date_filter, start_date, end_date)

    params = {}
    if start_date and end_date:
        params['start_date'] = start_date
        params['end_date'] = end_date

    val = api_client('/dashboard-report/', method='POST', params=params)

    context = {
        'date_filter': date_filter,
        'profile_count': val['profile_count'],
        'referral_count': val['referral_count'],
        'categories': val['categories'],
        'categories_keys': val['categories'].keys(),
        'categories_values': val['categories'].values(),
    }

    return render(request, 'dashboard.html', context)


def profile(request):
    data = api_client('/profiles/')
    return render(request, 'profiles.html', data)


def search_log(request):
    data = api_client('/search-log/')
    return render(request, 'search_log.html', data)

def manual_agents(request):
    return render(request, 'manual_agents.html')

def referrals(request):
    return render(request, 'referrals.html')


def messages(request):
    return render(request, 'messages.html')


def login(request):
    return render(request, 'login.html')


def admin(request):
    return render(request, 'administration.html')


def update_profile(request):
    return render(request, 'update_profile.html')


def settings(request):
    return render(request, 'settings.html')

def inbox(request):
    return render(request, 'inbox.html')
