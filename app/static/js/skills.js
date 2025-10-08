// Skill subcategories mapping
const skillSubcategories = {
    'programming_languages': [
        'Python', 'JavaScript', 'Java', 'C++', 'C#', 'Ruby', 'PHP', 'Go', 'Rust', 'Swift',
        'TypeScript', 'Kotlin', 'Other'
    ],
    'web_technologies': [
        'HTML/CSS', 'JavaScript', 'TypeScript', 'WebSocket', 'WebAssembly', 'Progressive Web Apps',
        'Web Components', 'Web Security', 'Web Performance', 'Web Accessibility', 'Other'
    ],
    'frameworks_libraries': [
        'React', 'Angular', 'Vue.js', 'Django', 'Flask', 'Spring', 'Express.js', 'Laravel',
        'ASP.NET', 'Ruby on Rails', 'Other'
    ],
    'databases': [
        'MySQL', 'PostgreSQL', 'MongoDB', 'Redis', 'SQLite', 'Oracle', 'Microsoft SQL Server',
        'Cassandra', 'Neo4j', 'Other'
    ],
    'cloud_services': [
        'AWS', 'Google Cloud', 'Azure', 'Heroku', 'DigitalOcean', 'Firebase',
        'Cloudflare', 'Vercel', 'Netlify', 'Other'
    ],
    'devops_tools': [
        'Git', 'Docker', 'Kubernetes', 'Jenkins', 'Travis CI', 'CircleCI', 'Ansible',
        'Terraform', 'Prometheus', 'Other'
    ],
    'mobile_development': [
        'iOS Development', 'Android Development', 'React Native', 'Flutter', 'Xamarin',
        'Ionic', 'Progressive Web Apps', 'Other'
    ],
    'design_multimedia': [
        'UI Design', 'UX Design', 'Graphic Design', 'Motion Graphics', 'Video Editing',
        'Sound Design', 'Photography', 'Other'
    ],
    'ai_ml': [
        'Machine Learning', 'Deep Learning', 'Natural Language Processing', 'Computer Vision',
        'Data Science', 'Neural Networks', 'Other'
    ],
    'security': [
        'Network Security', 'Web Security', 'Cryptography', 'Authentication',
        'Penetration Testing', 'Security Auditing', 'Other'
    ],
    'soft_skills': [
        'Communication', 'Leadership', 'Problem Solving', 'Team Collaboration',
        'Time Management', 'Project Management', 'Other'
    ],
    'other': ['Other']
};

// Update subcategories when primary category changes
document.addEventListener('DOMContentLoaded', () => {
    const categorySelect = document.querySelector('select#category');
    const subcategorySelect = document.querySelector('select#subcategory');
    
    if (categorySelect && subcategorySelect) {
        categorySelect.addEventListener('change', (e) => {
            const category = e.target.value;
            const subcategories = skillSubcategories[category] || [];
            
            // Clear current options
            subcategorySelect.innerHTML = '<option value="">Select a subcategory</option>';
            
            // Add new options
            subcategories.forEach(subcat => {
                const option = document.createElement('option');
                option.value = subcat.toLowerCase().replace(/\s+/g, '_');
                option.textContent = subcat;
                subcategorySelect.appendChild(option);
            });
        });
        
        // Trigger initial population of subcategories
        categorySelect.dispatchEvent(new Event('change'));
    }
});