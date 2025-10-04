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
        
    # Verifica se o arquivo existe, se não usaará fallback com node.svg
    svg_path = f'Portfolio/SVG/{file_name}.svg'
    svg_absolute_path = os.path.join(settings.STATIC_ROOT or '', svg_path)

    if not os.path.exists(svg_absolute_path):
        svg_path = 'Portfolio/SVG/node.svg'
    # Retorna o caminho estático
    return static(svg_path)