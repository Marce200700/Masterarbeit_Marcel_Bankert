import java.io.*;
import java.net.*;
import java.util.*;

public class TMDBApi {
    public static String fetchActorData(int actorId) {
        String apiKey = System.getenv("TMDB_API_KEY");
        String url = "https://api.themoviedb.org/3/person/" + actorId + "?api_key=" + apiKey;
        // Fetch actor data and return as a string
        // ...
    }

    public static String fetchPopularActors() {
        String apiKey = System.getenv("TMDB_API_KEY");
        String url = "https://api.themoviedb.org/3/person/popular?api_key=" + apiKey;
        // Fetch popular actors data and return as a string
        // ...
    }
}