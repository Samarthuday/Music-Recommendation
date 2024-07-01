document.addEventListener('DOMContentLoaded', function() {
    const heading = document.getElementById('heading-3d');
    const mainContent = document.getElementById('main-content');

    setTimeout(() => {
        heading.classList.add('hidden');
        mainContent.classList.remove('hidden');
    }, 3000); // Adjust the delay as needed (3 seconds in this case)
});
