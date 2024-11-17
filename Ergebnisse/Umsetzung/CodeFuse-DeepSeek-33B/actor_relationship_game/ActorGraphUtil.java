public class ActorGraphUtil {
    public static void serializeActorGraph(ActorGraph actorGraph, String filePath) {
        try (FileOutputStream fileOut = new FileOutputStream(filePath);
             ObjectOutputStream out = new ObjectOutputStream(fileOut)) {
            out.writeObject(actorGraph);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static ActorGraph deserializeActorGraph(String filePath) {
        ActorGraph actorGraph = null;
        try (FileInputStream fileIn = new FileInputStream(filePath);
             ObjectInputStream in = new ObjectInputStream(fileIn)) {
            actorGraph = (ActorGraph) in.readObject();
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
        return actorGraph;
    }

    public static void writeActorNamesToFile(ActorGraph actorGraph, String filePath) {
        try (PrintWriter writer = new PrintWriter(new FileWriter(filePath))) {
            for (Actor actor : actorGraph.getActors().values()) {
                writer.println(actor.getName());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}