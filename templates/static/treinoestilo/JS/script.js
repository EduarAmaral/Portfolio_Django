let header = document.getElementById('header')

window.addEventListener('scroll', () => {
    if (window.scrollY > 200) {
        header.style.background = '#191919'
    } else {
        header.style.background = 'transparent'
    }
});

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