
const URIEL_KEY = 'ed8ace910f5c3b9654153126f564caa2';
const URL_PELICULASDB = 'https://api.themoviedb.org/3';
let div_root = document.getElementById("root");

const load = () => {
    div_root.innerHTML = `
        <div class="container text-center">
            <h1 class="mb-4">¿Qué quieres ver hoy?</h1>
            <input type="text" id="searchBar" class="form-control mb-3" placeholder="Buscar película..." onkeyup="filtraerpeliculas()">
            <div id="carousel" class="d-flex overflow-hidden position-relative" style="height: 300px;">
                <button class="btn btn-dark position-absolute top-50 start-0 translate-middle-y" onclick="scrollCarousel(-1)">←</button>
                <div id="moviesContainer" class="d-flex gap-3 overflow-auto flex-nowrap align-items-center px-5" style="scroll-behavior: smooth;"></div>
                <button class="btn btn-dark position-absolute top-50 end-0 translate-middle-y" onclick="scrollCarousel(1)">→</button>
            </div>
            <div id="show" class="mt-4"></div>
            <div class="position-absolute bottom-0 end-0 m-3" id="total"></div>
        </div>
    `;
};

const datos = (response) => {
    let total = document.getElementById("total");
    total.innerText = `Total de películas: ${response.total_results}`;

    const moviesContainer = document.getElementById("moviesContainer");
    moviesContainer.innerHTML = "";

    response.results.forEach(({ id, title, poster_path }) => {
        const poster = `https://image.tmdb.org/t/p/w200${poster_path}`;
        const movieCard = `
            <div class="movie-card text-center" onclick="verpelicula(${id})" style="cursor: pointer; width: 150px;">
                <div class="movie-poster">
                    <img src="${poster}" alt="${title}" class="w-100 rounded shadow">
                </div>
                <div class="movie-title mt-2">${title}</div>
            </div>
        `;
        moviesContainer.innerHTML += movieCard;
    });
    console.log(response);
};

const peliculasss = () => {
    fetch(`${URL_PELICULASDB}/movie/popular?api_key=${URIEL_KEY}&language=es-ES&page=1`)
        .then((response) => response.json())
        .then((response) => {
            datos(response);
            allMovies = response.results; 
        });
};

let allMovies = [];

const filtraerpeliculas = () => {
    const query = document.getElementById("searchBar").value.toLowerCase();
    const filteredMovies = allMovies.filter(movie =>
        movie.title.toLowerCase().includes(query)
    );
    datos({ results: filteredMovies, total_results: filteredMovies.length });
};

const dataMovie = (response) => {
    let show = document.getElementById("show");
    show.innerHTML = "";

    const { title, overview, poster_path, genres, release_date } = response;
    const poster = `https://image.tmdb.org/t/p/w300${poster_path}`;
    const genreNames = genres.map((genre) => genre.name).join(', ');

    show.innerHTML = `
        <div class="card animated-card mx-auto" style="width: 18rem;">
          <img src="${poster}" class="card-img-top" alt="${title}">
          <div class="card-body">
            <h5 class="card-title">${title}</h5>
            <p class="card-text"><strong>Géneros:</strong> ${genreNames}</p>
            <p class="card-text"><strong>Fecha de estreno:</strong> ${release_date}</p>
            <p class="card-text">${overview}</p>
          </div>
        </div>
    `;
    console.log(response);
};

const verpelicula = (id) => {
    fetch(`${URL_PELICULASDB}/movie/${id}?api_key=${URIEL_KEY}&language=es-ES`)
        .then((response) => response.json())
        .then((response) => dataMovie(response));
};

const scrollCarousel = (direction) => {
    const container = document.getElementById("moviesContainer");
    const scrollAmount = direction * 300;
    container.scrollBy({ left: scrollAmount, behavior: 'smooth' });
};


const style = document.createElement('style');
style.innerHTML = `
    #carousel {
        background: linear-gradient(45deg, #000, #333);
        border-radius: 10px;
        padding: 10px 0;
    }
    .movie-card {
        transition: transform 0.3s ease-in-out;
    }
    .movie-card:hover {
        transform: scale(1.1);
    }
    .animated-card {
        animation: slideIn 0.5s ease-out;
    }
    @keyframes slideIn {
        from {
            transform: translateY(-100%);
            opacity: 0;
        }
        to {
            transform: translateY(0);
            opacity: 1;
        }

	.movie-title {
    		color: #ff6347;
	}
    }
`;
document.head.appendChild(style);

window.onload = () => {
    load();
    peliculasss();
};

