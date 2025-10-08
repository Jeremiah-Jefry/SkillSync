function initializeSearch(containerSelector, itemSelector) {
    const searchInput = document.querySelector(`${containerSelector}-search`);
    if (!searchInput) return;

    searchInput.addEventListener('input', (e) => {
        const searchTerm = e.target.value.toLowerCase();
        const items = document.querySelectorAll(itemSelector);

        items.forEach(item => {
            const text = item.textContent.toLowerCase();
            if (text.includes(searchTerm)) {
                item.style.display = '';
            } else {
                item.style.display = 'none';
            }
        });
    });
}

// Initialize search when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    // Initialize search for skills
    initializeSearch('#skills', '.skill-item');
    // Initialize search for projects
    initializeSearch('#projects', '.project-item');
});