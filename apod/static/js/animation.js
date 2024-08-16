document.addEventListener('alpine:init', () => {
    Alpine.store('animations', {
        fadeIn(el) {
            el.style.transition = 'opacity 0.5s ease-in-out';
            el.style.opacity = 0;
            setTimeout(() => {
                el.style.opacity = 1;
            }, 50);
        },
        slideIn(el) {
            el.style.transition = 'transform 0.5s ease-in-out';
            el.style.transform = 'translateX(-20px)';
            setTimeout(() => {
                el.style.transform = 'translateY(0)';
            }, 50);
        }
    });
});