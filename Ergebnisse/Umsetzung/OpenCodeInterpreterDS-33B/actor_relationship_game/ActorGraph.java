import java.util.HashMap;
import java.util.Map;

public class ActorGraph {
    private Map<String, Actor> actors;
    private Map<String, Movie> movies;

    public ActorGraph() {
        this.actors = new HashMap<>();
        this.movies = new HashMap<>();
    }

    public Map<String, Actor> getActors() {
        return actors;
    }

    public Map<String, Movie> getMovies() {
        return movies;
    }

    public void addActor(Actor actor) {
        actors.put(actor.getId(), actor);
    }

    public void addMovie(Movie movie) {
        movies.put(movie.getId(), movie);
    }
}