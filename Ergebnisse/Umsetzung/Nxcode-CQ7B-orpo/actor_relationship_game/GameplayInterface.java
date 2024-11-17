import java.util.*;

public class GameplayInterface {
    public static void main(String[] args) {
        String graphPath = args[0];
        String actorPath = args[1];
        String filePath = args[2];

        ActorGraph actorGraph = ActorGraphUtil.deserializeActorGraph(graphPath);
        List<Actor> actors = readActorsFromFile(actorPath);

        for (int i = 0; i < actors.size(); i++) {
            for (int j = i + 1; j < actors.size(); j++) {
                Actor actor1 = actors.get(i);
                Actor actor2 = actors.get(j);
                List<Actor> path = findConnectionPath(actorGraph, actor1, actor2);
                if (path != null) {
                    System.out.println("Connection between " + actor1.getName() + " and " + actor2.getName() + ":");
                    System.out.println("Connection Number: " + (path.size() - 1));
                    System.out.println("Connection Path: " + path.stream().map(Actor::getName).collect(Collectors.joining(" -> ")));
                    System.out.println();
                }
            }
        }

        ActorGraphUtil.writeActorsToFile(actors, filePath);
    }

    private static List<Actor> readActorsFromFile(String filePath) {
        List<Actor> actors = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                actors.add(new Actor(-1, line));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return actors;
    }

    private static List<Actor> findConnectionPath(ActorGraph actorGraph, Actor actor1, Actor actor2) {
        Set<Actor> visited = new HashSet<>();
        Queue<List<Actor>> queue = new LinkedList<>();
        queue.offer(Arrays.asList(actor1));

        while (!queue.isEmpty()) {
            List<Actor> currentPath = queue.poll();
            Actor lastActor = currentPath.get(currentPath.size() - 1);

            if (lastActor.equals(actor2)) {
                return currentPath;
            }

            for (Actor neighbor : actorGraph.getNeighbors(lastActor)) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    List<Actor> newPath = new ArrayList<>(currentPath);
                    newPath.add(neighbor);
                    queue.offer(newPath);
                }
            }
        }

        return null;
    }
}