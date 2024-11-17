public class TMDBApi {
    private static final String API_KEY = System.getenv("TMDB_API_KEY");
    private static final String BASE_URL = "https://api.themoviedb.org/3";

    public List<Actor> getPopularActors(int numActors) {
        List<Actor> popularActors = new ArrayList<>();
        String url = BASE_URL + "/person/popular?api_key=" + API_KEY + "&language=en-US&page=1";
        try {
            String response = sendGetRequest(url);
            JSONObject json = new JSONObject(response);
            JSONArray results = json.getJSONArray("results");
            for (int i = 0; i < numActors && i < results.length(); i++) {
                JSONObject actorJson = results.getJSONObject(i);
                int actorId = actorJson.getInt("id");
                String actorName = actorJson.getString("name");
                popularActors.add(new Actor(actorId, actorName));
            }
        } catch (IOException | JSONException e) {
            e.printStackTrace();
        }
        return popularActors;
    }

    public List<Movie> getMoviesByActorId(int actorId) {
        List<Movie> movies = new ArrayList<>();
        String url = BASE_URL + "/person/" + actorId + "/movie_credits?api_key=" + API_KEY + "&language=en-US";
        try {
            String response = sendGetRequest(url);
            JSONObject json = new JSONObject(response);
            JSONArray cast = json.getJSONArray("cast");
            for (int i = 0; i < cast.length(); i++) {
                JSONObject movieJson = cast.getJSONObject(i);
                int movieId = movieJson.getInt("id");
                String movieTitle = movieJson.getString("title");
                movies.add(new Movie(movieId, movieTitle));
            }
        } catch (IOException | JSONException e) {
            e.printStackTrace();
        }
        return movies;
    }

    private String sendGetRequest(String url) throws IOException {
        HttpURLConnection connection = (HttpURLConnection) new URL(url).openConnection();
        connection.setRequestMethod("GET");
        connection.setRequestProperty("Content-Type", "application/json");
        connection.setConnectTimeout(5000);
        connection.setReadTimeout(5000);

        int status = connection.getResponseCode();
        if (status != 200) {
            throw new IOException("Failed to fetch data from TMDB API. Status code: " + status);
        }

        BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
        String inputLine;
        StringBuilder response = new StringBuilder();
        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();

        return response.toString();
    }
}