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

    public Actor getActor(int actorId) {
        return actors.get(actorId);
    }

    public Movie getMovie(int movieId) {
        return movies.get(movieId);
    }
}