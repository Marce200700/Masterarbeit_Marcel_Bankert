public class TMDBApi {
    private String apiKey;

    public TMDBApi(String apiKey) {
        this.apiKey = apiKey;
    }

    public List<Actor> getPopularActors() {
        // Implement the method to fetch popular actors from TMDB API
    }

    public List<Movie> getMoviesByActorId(int actorId) {
        // Implement the method to fetch movies by actor ID from TMDB API
    }
}