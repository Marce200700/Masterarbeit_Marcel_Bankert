public class Actor {
    private int id;
    private String name;
    private Set<Integer> movieIds;

    public Actor(int id, String name) {
        this.id = id;
        this.name = name;
        this.movieIds = new HashSet<>();
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public Set<Integer> getMovieIds() {
        return movieIds;
    }

    public void addMovieId(int movieId) {
        movieIds.add(movieId);
    }
}