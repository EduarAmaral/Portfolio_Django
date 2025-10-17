from django import template
from django.templatetags.static import static
import os
from django.conf import settings

register = template.Library()

@register.simple_tag
def tech_icon(tech_name):
    tech_lower = tech_name.lower()
    
    # Mapeamento de nomes alternativos para arquivos
    name_mapping = {
        'javascript': 'js',
        'html5': 'html',
        'css3': 'css',
        'html': 'html',
        'css': 'css',
        'github': 'logo-github',
        'python': 'python',
        'django': 'django-sigla',
        'sql': 'SQL'
    }
    
    # Tenta encontrar o arquivo pelo nome mapeado
    file_name = name_mapping.get(tech_lower, tech_lower)
    
    # Lista de arquivos SVG disponíveis
    available_svgs = [
        'css', 'django-sigla', 'django', 'html', 'js', 'logo-github',
        'logo-insta', 'logo-linkedin', 'node', 'python', 'react',
        'Excel', 'MYSQL', 'SQL'
    ]
    
    # Verifica se o arquivo existe na lista, se não usa fallback
    if file_name not in available_svgs:
        file_name = 'node'
    
    svg_path = f'Portfolio/SVG/{file_name}.svg'
    # Retorna o caminho estático
    return static(svg_path)