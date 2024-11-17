import java.util.HashSet;
import java.util.Set;

public class Movie {
    private String id;
    private String title;
    private Set<String> actors;

    public Movie(String id, String title) {
        this.id = id;
        this.title = title;
        this.actors = new HashSet<>();
    }

    public String getId() {
        return id;
    }

    public String getTitle() {
        return title;
    }

    public Set<String> getActors() {
        return actors;
    }

    public void addActor(String actorId) {
        actors.add(actorId);
    }
}