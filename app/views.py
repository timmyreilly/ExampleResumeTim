"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime


    
def base(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/base.html',
        context_instance = RequestContext(request,
            {
                'title': 'Tim Reilly Resume',
                'left_header': 'Tim Reilly',
                'header_right_one': 'Little Album',
                'header_right_two': 'About',
                'header_right_three': 'Contact',
                
                'main': 'This is me!',
                'secondary': 'Play Ultimate, Code, and Work for Microsoft',
                'tertiary': 'Let\'s hang out at DjangoCon',
                
                'portfolio_main': 'Little Album',
                
                'about_main': 'About',
                
                'contact_main': 'Say Hi',    
                'email': 'Tim.Reilly@microsoft.com',
                'twitter': '@timmyreilly',
                'number': '503-314-3771',
                
                'year': datetime.now().year,
            })
    )


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Microsoft Code Challege',
            'year':datetime.now().year,
        })
    )

def anotherpage(request):
    assert isinstance(request, HttpRequest)
    return render(
        request, 
        'app/anotherpage.html',
        context_instance = RequestContext(request, 
            {
                'name': 'Timothy',
                'twitter': '@timmyreilly',
                'year': datetime.now().year,
            })
    )