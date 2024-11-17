import java.util.HashSet;
import java.util.Set;

public class Actor {
    private String id;
    private String name;
    private Set<String> movies;

    public Actor(String id, String name) {
        this.id = id;
        this.name = name;
        this.movies = new HashSet<>();
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public Set<String> getMovies() {
        return movies;
    }

    public void addMovie(String movieId) {
        movies.add(movieId);
    }
}