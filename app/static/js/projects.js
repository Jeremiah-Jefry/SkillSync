document.addEventListener('DOMContentLoaded', () => {
    const projectsContainer = document.querySelector('.projects-grid');
    const sortSelect = document.querySelector('#sort-projects');
    const techFilterInput = document.querySelector('#filter-tech');
    const projectItems = Array.from(document.querySelectorAll('.project-item'));

    if (!projectsContainer || !projectItems.length) return;

    // Create sort select if it doesn't exist
    if (!sortSelect) {
        const select = document.createElement('select');
        select.id = 'sort-projects';
        select.className = 'px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent';
        select.innerHTML = `
            <option value="newest">Newest First</option>
            <option value="oldest">Oldest First</option>
            <option value="name-asc">Name (A-Z)</option>
            <option value="name-desc">Name (Z-A)</option>
        `;
        projectsContainer.parentElement.insertBefore(select, projectsContainer);
    }

    // Create tech filter if it doesn't exist
    if (!techFilterInput) {
        const input = document.createElement('input');
        input.id = 'filter-tech';
        input.type = 'text';
        input.placeholder = 'Filter by technology...';
        input.className = 'px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent ml-4';
        document.querySelector('#sort-projects').insertAdjacentElement('afterend', input);
    }

    // Sorting function
    function sortProjects(order) {
        const projects = Array.from(projectsContainer.children);
        projects.sort((a, b) => {
            switch (order) {
                case 'newest':
                    return new Date(b.dataset.date) - new Date(a.dataset.date);
                case 'oldest':
                    return new Date(a.dataset.date) - new Date(b.dataset.date);
                case 'name-asc':
                    return a.dataset.title.localeCompare(b.dataset.title);
                case 'name-desc':
                    return b.dataset.title.localeCompare(a.dataset.title);
                default:
                    return 0;
            }
        });
        projectsContainer.innerHTML = '';
        projects.forEach(project => projectsContainer.appendChild(project));
    }

    // Filtering function
    function filterProjects(techFilter) {
        projectItems.forEach(project => {
            const techStack = project.dataset.techStack.toLowerCase();
            const shouldShow = !techFilter || techStack.includes(techFilter.toLowerCase());
            project.style.display = shouldShow ? '' : 'none';
        });
    }

    // Event listeners
    document.querySelector('#sort-projects').addEventListener('change', (e) => {
        sortProjects(e.target.value);
    });

    document.querySelector('#filter-tech').addEventListener('input', (e) => {
        filterProjects(e.target.value);
    });

    // Initial sort
    sortProjects('newest');
});