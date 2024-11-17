import java.util.*;

public class ActorGraph {
    private Map<Integer, Actor> actors;
    private Map<Integer, Movie> movies;

    public ActorGraph() {
        this.actors = new HashMap<>();
        this.movies = new HashMap<>();
    }

    public void addActor(Actor actor) {
        actors.put(actor.getId(), actor);
    }

    public void addMovie(Movie movie) {
        movies.put(movie.getId(), movie);
    }

    public Actor getActor(int id) {
        return actors.get(id);
    }

    public Movie getMovie(int id) {
        return movies.get(id);
    }

    public Set<Actor> getNeighbors(Actor actor) {
        Set<Actor> neighbors = new HashSet<>();
        for (int movieId : actor.getMovieIds()) {
            Movie movie = movies.get(movieId);
            for (int neighborId : movie.getActorIds()) {
                if (neighborId != actor.getId()) {
                    neighbors.add(actors.get(neighborId));
                }
            }
        }
        return neighbors;
    }
}