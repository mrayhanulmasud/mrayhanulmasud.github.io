document.addEventListener('DOMContentLoaded', () => {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('nav ul li a');

    // Don't run script if there are no nav links
    if (navLinks.length === 0 || sections.length === 0) {
        return;
    }

    const onScroll = () => {
        let currentSection = '';

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            // 65px offset for the sticky nav height + a little extra
            if (pageYOffset >= sectionTop - 65) { 
                currentSection = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            // Check if the link's href matches the current section's ID
            if (link.getAttribute('href') === `#${currentSection}`) {
                link.classList.add('active');
            }
        });
    };

    window.addEventListener('scroll', onScroll);
    
    // Run once on load to set the initial state
    onScroll(); 
});