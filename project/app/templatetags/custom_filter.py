from django import template
from bs4 import BeautifulSoup
import re


register = template.Library()

@register.filter
def text_only(value):
    soup = BeautifulSoup(value, "html.parser")

    for img in soup.find_all('img'):
        img.decompose()
    
    text_content = soup.get_text()
    if len(text_content) >= 200:
        text_content = text_content[:200] + '...'
    return text_content

@register.filter(name='get_img_src')
def get_img_src(value):
    match = re.search(r'<img [^>]*src="([^"]+)', value)
    if match:
        return match.group(1)
    return ''