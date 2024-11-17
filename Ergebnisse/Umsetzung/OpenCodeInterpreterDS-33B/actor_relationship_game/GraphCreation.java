import java.util.List;

public class GraphCreation {
    private TMDBApi tmdbApi;

    public GraphCreation(String apiKey) {
        this.tmdbApi = new TMDBApi(apiKey);
    }

    public ActorGraph createActorGraph() {
        ActorGraph actorGraph = new ActorGraph();
        List<Actor> popularActors = tmdbApi.getPopularActors();
        for (Actor actor : popularActors) {
            actorGraph.addActor(actor);
            List<Movie> actorMovies = tmdbApi.getMoviesByActor(actor.getId());
            for (Movie movie : actorMovies) {
                actorGraph.addMovie(movie);
                actor.addMovie(movie.getId());
                movie.addActor(actor.getId());
            }
        }
        return actorGraph;
    }
}