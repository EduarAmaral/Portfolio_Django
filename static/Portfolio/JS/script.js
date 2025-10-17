var swiper = new Swiper(".mySwiper", {
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: "auto",
    coverflowEffect: {
      rotate: 50,
      stretch: 0,
      depth: 100,
      modifier: 1,
      slideShadows: true,
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
  });

// Lógica de identificação de ancora

document.addEventListener('DOMContentLoaded', function() {
    // Seleciona todos os links da navbar
    const navLinks = document.querySelectorAll('.navbar ul li a');
    const sections = document.querySelectorAll('section[id]');
    
    // Função para remover active de todos os links
    function removeActiveClasses() {
        navLinks.forEach(link => link.classList.remove('active'));
    }
    
    // Função para adicionar active ao link correspondente
    function addActiveClass(id) {
        const activeLink = document.querySelector(`.navbar ul li a[href="#${id}"]`);
        if (activeLink) {
            activeLink.classList.add('active');
        }
    }
    
    // Observer para detectar qual seção está visível
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                removeActiveClasses();
                addActiveClass(entry.target.id);
            }
        });
    }, {
        threshold: 0.6 // 60% da seção deve estar visível
    });
    
    // Observa todas as seções
    sections.forEach(section => {
        observer.observe(section);
    });
});

// Função para inicializar o menu toggle
function inicializarMenu() {
  const toggle = document.querySelector(".menu-toggle i");
  const nav = document.querySelector(".navbar");
  const btn = document.querySelector(".menu-toggle");

  if (!btn || !nav || !toggle) return;

  btn.addEventListener("click", () => {
    nav.classList.toggle("active");
    toggle.classList.toggle("fa-bars");
    toggle.classList.toggle("fa-xmark");
    btn.setAttribute("aria-expanded", nav.classList.contains("active") ? "true" : "false");
  });

  // Fecha o menu quando clica em um link
  nav.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      nav.classList.remove("active");
      toggle.classList.add("fa-bars");
      toggle.classList.remove("fa-xmark");
      btn.setAttribute("aria-expanded", "false");
    });
  });
}

// Inicializar o menu quando o DOM estiver carregado
document.addEventListener('DOMContentLoaded', inicializarMenu);
