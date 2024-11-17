public class GameplayInterface {
    private ActorGraph actorGraph;

    public GameplayInterface(ActorGraph actorGraph) {
        this.actorGraph = actorGraph;
    }

    public void findConnections(String actor1, String actor2, String filePath) {
        try (PrintWriter writer = new PrintWriter(new FileWriter(filePath))) {
            int actor1Id = findActorIdByName(actor1);
            int actor2Id = findActorIdByName(actor2);

            if (actor1Id == -1 || actor2Id == -1) {
                writer.println("Actor not found.");
                return;
            }

            List<Integer> path = findShortestPath(actor1Id, actor2Id);
            if (path.isEmpty()) {
                writer.println("No connection found.");
                return;
            }

            writer.println("Connection Number: " + (path.size() - 1));
            writer.println("Connection Path:");
            for (int i = 0; i < path.size() - 1; i++) {
                Actor actor = actorGraph.getActor(path.get(i));
                Movie movie = actorGraph.getMovie(path.get(i + 1));
                writer.println(actor.getName() + " - " + movie.getTitle() + " - " + actorGraph.getActor(path.get(i + 1)).getName());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private int findActorIdByName(String name) {
        for (Actor actor : actorGraph.getActors().values()) {
            if (actor.getName().equals(name)) {
                return actor.getId();
            }
        }
        return -1;
    }

    private List<Integer> findShortestPath(int actor1Id, int actor2Id) {
        Map<Integer, Integer> parent = new HashMap<>();
        Queue<Integer> queue = new LinkedList<>();
        queue.add(actor1Id);
        parent.put(actor1Id, -1);

        while (!queue.isEmpty()) {
            int currentActorId = queue.poll();
            if (currentActorId == actor2Id) {
                break;
            }

            for (int movieId : actorGraph.getMovieIdsByActorId(currentActorId)) {
                for (int nextActorId : actorGraph.getActorIdsByMovieId(movieId)) {
                    if (!parent.containsKey(nextActorId)) {
                        queue.add(nextActorId);
                        parent.put(nextActorId, currentActorId);
                    }
                }
            }
        }

        List<Integer> path = new ArrayList<>();
        int currentActorId = actor2Id;
        while (currentActorId != -1) {
            path.add(currentActorId);
            currentActorId = parent.get(currentActorId);
        }
        Collections.reverse(path);
        return path;
    }
}