public class Movie {
    private int id;
    private String title;
    private Set<Integer> actorIds;

    public Movie(int id, String title) {
        this.id = id;
        this.title = title;
        this.actorIds = new HashSet<>();
    }

    public int getId() {
        return id;
    }

    public String getTitle() {
        return title;
    }

    public Set<Integer> getActorIds() {
        return actorIds;
    }

    public void addActorId(int actorId) {
        actorIds.add(actorId);
    }
}