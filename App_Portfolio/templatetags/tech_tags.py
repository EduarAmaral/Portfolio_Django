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
        'github': 'logo-github',
        'python': 'python',
        'django': 'django-sigla',
        'SQL': 'SQL'
    }
    
    # Tenta encontrar o arquivo pelo nome mapeado
    file_name = name_mapping.get(tech_lower, tech_lower)
    
    # Caminho para o diretório de SVGs
    svg_dir = os.path.join(settings.STATIC_ROOT, 'Portfolio', 'SVG')
    
    # Verifica se o arquivo existe (apenas para debug, não afeta o funcionamento)
    svg_path = f'Portfolio/SVG/{file_name}.svg'
    
    # Retorna o caminho estático
    return static(svg_path)