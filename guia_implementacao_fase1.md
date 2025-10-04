# Guia de Implementação: Fase 1 do Portfólio Django

Este guia apresenta um passo a passo didático com exemplos práticos para implementar a Fase 1 do projeto de portfólio.

## 1. Refatoração da Estrutura Django

### Class-Based Views (CBVs) - Antes e Depois

**ANTES (Function-Based View):**
```python
# App_Portfolio/views.py
from django.shortcuts import render

def Portfolio(request):
    return render(request, 'Portfolio.html')
```

**DEPOIS (Class-Based View):**
```python
# App_Portfolio/views.py
from django.views.generic import TemplateView

class PortfolioView(TemplateView):
    template_name = 'portfolio/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tecnologias'] = ['Django', 'Python', 'HTML5', 'CSS3']
        return context
```

**Como verificar se concluiu:** Crie uma view de teste que exiba dados dinâmicos (lista de tecnologias) e confirme que aparecem corretamente no template.

### Sistema de Templates com Herança - Antes e Depois

**ANTES (Template monolítico):**
```html
<!-- Portfolio.html -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Eduardo Amaral - Portfolio</title>
    <link rel="stylesheet" href="{% static 'file/CSS/style.css' %}">
</head>
<body>
    <header><!-- Todo o código do cabeçalho --></header>
    <main><!-- Conteúdo específico --></main>
    <footer><!-- Todo o código do rodapé --></footer>
</body>
</html>
```

**DEPOIS (Sistema de templates):**
```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Eduardo Amaral{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/main.css' %}">
    {% block extra_css %}{% endblock %}
</head>
<body>
    <header><!-- Cabeçalho comum --></header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer><!-- Rodapé comum --></footer>
    {% block extra_js %}{% endblock %}
</body>
</html>

<!-- templates/portfolio/home.html -->
{% extends 'base.html' %}

{% block title %}Eduardo Amaral - Portfolio{% endblock %}

{% block content %}
    <!-- Apenas o conteúdo específico da página -->
    <section class="hero">
        <h1>Eduardo Amaral</h1>
        <p>Desenvolvedor Django</p>
    </section>
{% endblock %}
```

**Como verificar se concluiu:** Crie uma segunda página que estenda base.html e confirme que o cabeçalho e rodapé são idênticos em ambas as páginas.

## 2. Organização Modular de Apps

**ANTES (Estrutura atual):**
```
Portfolio_Django/
  ├── App_Portfolio/  # App com funcionalidades misturadas
  └── cadastro/       # App com propósito não claro
```

**DEPOIS (Estrutura modular):**
```
Portfolio_Django/
  ├── core/           # Funcionalidades centrais, templates base
  ├── portfolio/      # Exibição de projetos e habilidades
  ├── blog/           # Funcionalidade futura para blog
  └── contact/        # Sistema de contato
```

**Como implementar:**
1. Crie novos apps com `python manage.py startapp nome_do_app`
2. Mova views, templates e models relacionados para cada app
3. Atualize INSTALLED_APPS no settings.py:
   ```python
   INSTALLED_APPS = [
       # Django apps
       'django.contrib.admin',
       # ...
       
       # Apps locais
       'core.apps.CoreConfig',
       'portfolio.apps.PortfolioConfig',
       'contact.apps.ContactConfig',
   ]
   ```

**Como verificar se concluiu:** Cada app deve ter seu próprio arquivo urls.py e suas próprias pastas de templates, com responsabilidades bem definidas.

## 3. Unificação de CSS - Antes e Depois

**ANTES (CSS espalhado):**
```css
/* style.css */
body { font-family: Arial; }
.header { background: blue; }

/* estilo.css */
body { font-family: Helvetica; } /* Conflito! */
.projeto { margin: 10px; }
```

**DEPOIS (CSS unificado com variáveis):**
```css
/* main.css */
:root {
  --primary-color: #3498db;
  --secondary-color: #2ecc71;
  --text-color: #333;
  --font-heading: 'Roboto', sans-serif;
  --font-body: 'Open Sans', sans-serif;
}

/* Base */
body {
  font-family: var(--font-body);
  color: var(--text-color);
}

/* Componentes */
.header {
  background: var(--primary-color);
}

.projeto-card {
  margin: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}
```

**Como verificar se concluiu:** Todas as páginas devem carregar apenas um arquivo CSS principal, e alterando uma variável CSS (como --primary-color), todas as instâncias dessa cor devem mudar simultaneamente.

## 4. Layout Responsivo - Antes e Depois

**ANTES (Layout fixo):**
```css
.container {
  width: 960px;
  margin: 0 auto;
}

.projeto {
  width: 300px;
  float: left;
}
```

**DEPOIS (Layout responsivo):**
```css
.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.projetos-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.projeto-card {
  flex: 1 1 300px;
  min-width: 0; /* Evita overflow */
}

/* Media queries */
@media (max-width: 768px) {
  .container {
    padding: 0 15px;
  }
  
  .projeto-card {
    flex-basis: 100%;
  }
}
```

**Como verificar se concluiu:** Teste o site em diferentes larguras (320px, 768px, 1024px, 1440px) e confirme que todos os elementos se ajustam adequadamente sem quebrar o layout.

## Métricas de Conclusão para Cada Etapa

1. **Refatoração para CBVs:**
   - Todas as views convertidas para classes
   - Testes com dados dinâmicos funcionando
   - URLs atualizadas para apontar para as novas views

2. **Sistema de Templates:**
   - Template base.html criado com blocos apropriados
   - Todas as páginas estendendo o template base
   - Nenhuma duplicação de código HTML entre páginas

3. **Organização Modular:**
   - Apps criados com responsabilidades bem definidas
   - Arquivos movidos para os apps corretos
   - Cada app com sua própria estrutura de templates/static

4. **CSS Unificado:**
   - Um único arquivo CSS principal
   - Variáveis CSS implementadas para cores e tamanhos
   - Zero conflitos de estilo entre componentes

5. **Layout Responsivo:**
   - Flexbox/Grid implementado para layouts
   - Media queries para todos os breakpoints principais
   - Teste em DevTools com diferentes tamanhos de tela

## Recursos Recomendados

- [Django Docs](https://docs.djangoproject.com/en/4.2/)
- [Django CBVs Guide](https://ccbv.co.uk/)
- [MDN Responsive Design](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design)
- [CSS-Tricks Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [Django for Professionals](https://djangoforprofessionals.com/)