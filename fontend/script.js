document.addEventListener('DOMContentLoaded', () => {
    const movieGrid = document.getElementById('movieGrid');
    const trendingSlider = document.getElementById('trendingSlider');
    const searchInput = document.getElementById('searchInput');
    const searchBtn = document.getElementById('searchBtn');
    const modal = document.getElementById('movieModal');
    const modalTitle = document.getElementById('modalTitle');
    const modalDescription = document.getElementById('modalDescription');
    const modalYear = document.getElementById('modalYear');
    const modalDownload = document.getElementById('modalDownload');
    const modalCloseBtn = document.querySelector('.close-btn');
    const modalDownloadBtn = document.getElementById('modalDownload');

    function displayMovies(movies, container) {
        container.innerHTML = '';
        movies.forEach(movie => {
            const movieCard = document.createElement('div');
            movieCard.className = 'movie-card';
            movieCard.innerHTML = `
                <img src="${movie.image_link}" alt="${movie.name}" class="movie-image">
                <div class="movie-info">
                    <h3>${movie.name}</h3>
                    <p>${movie.date}</p>
                </div>
            `;
            movieCard.onclick = () => showMovieDetails(movie);
            container.appendChild(movieCard);
        });
    }

    function showMovieDetails(movie) {
        modalTitle.textContent = movie.name;
        modalYear.textContent = `${movie.date}`;
        modalDescription.textContent = movie.description;
        modalImage.src = movie.image_link;
        modalImage.alt = `${movie.name} Poster`;
        
        modalDownloadBtn.onclick = () => {
            window.open(movie.download_link, '_blank');
        };
        
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden'; // Prevent scrolling when modal is open
    }

    modalCloseBtn.onclick = () => {
        modal.style.display = 'none';
        document.body.style.overflow = ''; // Re-enable scrolling
    };

    window.onclick = (event) => {
        if (event.target == modal) {
            modal.style.display = 'none';
            document.body.style.overflow = ''; // Re-enable scrolling
        }
    };

    function fetchMovies() {
        Promise.all([
            fetch('http://localhost:8000/trending').then(res => res.json()),
            fetch('http://localhost:8000/all').then(res => res.json())
        ]).then(([trending, all]) => {
            displayMovies(trending, trendingSlider);
            displayMovies(all, movieGrid);
        }).catch(error => {
            console.error("Failed to fetch data:", error);
        });
    }

    function searchMovies() {
        const query = searchInput.value.trim();
        if (query) {
            fetch(`http://localhost:8000/search?q=${encodeURIComponent(query)}`)
                .then(response => response.json())
                .then(movies => {
                    displayMovies(movies, movieGrid);
                })
                .catch(error => {
                    console.error("Failed to search movies:", error);
                    movieGrid.innerHTML = '<p style="color: #fff; text-align: center;">No movies found.</p>';
                });
        } else {
            fetchMovies();
        }
    }

    searchBtn.addEventListener('click', searchMovies);
    searchInput.addEventListener('keyup', event => {
        if (event.key === 'Enter') {
            searchMovies();
        }
    });

    fetchMovies();
}); 