import java.io.*;
import java.util.*;

public class GraphCreation {
    public static void main(String[] args) {
        String filePath = args[0];

        ActorGraph actorGraph = new ActorGraph();
        List<Actor> actors = new ArrayList<>();

        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] parts = line.split(",");
                int actorId = Integer.parseInt(parts[0]);
                String actorName = parts[1];
                Actor actor = new Actor(actorId, actorName);
                actorGraph.addActor(actor);
                actors.add(actor);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        for (Actor actor : actors) {
            String url = "https://api.themoviedb.org/3/person/" + actor.getId() + "/movie_credits?api_key=" + System.getenv("TMDB_API_KEY");
            // Fetch movie data and add to actor's movieIds
            // ...
        }

        for (Actor actor : actors) {
            for (int movieId : actor.getMovieIds()) {
                Movie movie = new Movie(movieId, "");
                actorGraph.addMovie(movie);
                for (int neighborId : movie.getActorIds()) {
                    if (neighborId != actor.getId()) {
                        Actor neighbor = actorGraph.getActor(neighborId);
                        if (neighbor != null) {
                            neighbor.addMovieId(movieId);
                        }
                    }
                }
            }
        }

        ActorGraphUtil.serializeActorGraph(actorGraph, filePath);
    }
}