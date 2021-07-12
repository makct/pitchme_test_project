from dataclasses import asdict

from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_list_or_404, redirect, render
from django.urls import reverse

from .dataclasses import SearchParams
from .forms import LoginForm, RegisterForm, SearchForm
from .models import Event, UserSearchHistory


def index(request: HttpRequest) -> HttpResponse:
    events = get_list_or_404(Event)

    return render(request, "events/index.html", {"events": events})


def register(response) -> HttpResponse:
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse("events:login"))

    else:
        form = RegisterForm()

    return render(response, "events/register.html", {"form": form})


def user_login(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd["username"], password=cd["password"])
            if user is None:
                return HttpResponse("Invalid login")
            if not user.is_active:
                return HttpResponse("Disabled account")
            login(request, user)
            return HttpResponseRedirect(reverse("events:home"))
    else:
        form = LoginForm()
    return render(request, "events/login.html", {"form": form})


def user_logout(request: HttpRequest) -> HttpResponse:
    logout(request)

    return redirect("/")


def home_page(request) -> HttpResponse:
    if request.user.is_authenticated:
        search_records = UserSearchHistory.objects.filter(
            username=request.user.username
        )
        return render(
            request, "events/homepage.html", {"search_records": search_records}
        )

    return HttpResponseRedirect(reverse("events:login"))


def search_result(
    request: HttpRequest, search_params: SearchParams = None
) -> HttpResponse:
    matched_events = []

    if search_params:
        events_filtered_by_city = Event.objects.filter(
            city__name__exact=search_params.city
        )
        matched_events = events_filtered_by_city.filter(
            eventtopic__topic__name__exact=search_params.topic
        )
        if search_params.start_interval and search_params.end_interval:
            matched_events = matched_events.filter(
                start_date__range=[
                    search_params.start_interval,
                    search_params.end_interval,
                ]
            )

    history_record = UserSearchHistory(
        username=request.user.username,
        city=search_params.city,
        start_interval=search_params.start_interval,
        end_interval=search_params.end_interval,
        topic=search_params.topic,
    )
    history_record.save()

    return render(
        request,
        "events/search_result.html",
        {"events": matched_events, "search_params": asdict(search_params)},
    )


def search(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            search_params = SearchParams(
                city=data["city"],
                start_interval=data["start_interval"],
                end_interval=data["end_interval"],
                topic=data["topic"],
            )
            return search_result(request, search_params)
    else:
        form = SearchForm()

    return render(request, "events/search_page.html", {"form": form})


def repeat_search_request(request: HttpRequest, history_log_id: int):
    log_record = UserSearchHistory.objects.get(id=history_log_id)
    search_params = SearchParams(
        city=log_record.city,
        start_interval=log_record.start_interval,
        end_interval=log_record.end_interval,
        topic=log_record.topic,
    )
    return search_result(request, search_params)
