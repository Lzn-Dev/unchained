""" Module Views """
from django.shortcuts import render


def home(request):
    """Route 'Home'"""
    return render(request, "home.html")
