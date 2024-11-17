import java.util.List;

public class TMDBApi {
    private String apiKey;

    public TMDBApi(String apiKey) {
        this.apiKey = apiKey;
    }

    public List<Actor> getPopularActors() {
        // Implement logic to fetch popular actors from TMDB API
        // This could involve making an HTTP GET request to the TMDB API endpoint for popular actors
        // and parsing the response JSON to create Actor objects
        return null;
    }

    public List<Movie> getMoviesByActor(String actorId) {
        // Implement logic to fetch movies by actor from TMDB API
        // This could involve making an HTTP GET request to the TMDB API endpoint for movies by actor
        // and parsing the response JSON to create Movie objects
        return null;
    }
}