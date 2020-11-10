from django.shortcut import render, redirect
from .models import Post
from django.utils import timezone
from django.contrib.auth.decoration import login_required

@login_required