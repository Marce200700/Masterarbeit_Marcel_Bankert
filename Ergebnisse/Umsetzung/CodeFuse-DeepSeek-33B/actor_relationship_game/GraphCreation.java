public class GraphCreation {
    private TMDBApi tmdbApi;

    public GraphCreation(TMDBApi tmdbApi) {
        this.tmdbApi = tmdbApi;
    }

    public ActorGraph createGraph(int numActors) {
        ActorGraph actorGraph = new ActorGraph();
        List<Actor> popularActors = tmdbApi.getPopularActors(numActors);

        for (Actor actor : popularActors) {
            actorGraph.addActor(actor);
            List<Movie> movies = tmdbApi.getMoviesByActorId(actor.getId());
            for (Movie movie : movies) {
                if (!actorGraph.getMovies().containsKey(movie.getId())) {
                    actorGraph.addMovie(movie);
                }
                actorGraph.getMovie(movie.getId()).addActor(actor.getId());
                actorGraph.getActor(actor.getId()).addMovie(movie.getId());
            }
        }

        return actorGraph;
    }
}