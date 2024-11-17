import java.io.*;
import java.util.Map;

public class ActorGraphUtil {
    public static void serializeActorGraph(ActorGraph actorGraph, String fileName) {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(fileName))) {
            oos.writeObject(actorGraph);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static ActorGraph deserializeActorGraph(String fileName) {
        ActorGraph actorGraph = null;
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(fileName))) {
            actorGraph = (ActorGraph) ois.readObject();
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
        return actorGraph;
    }

    public static void writeActorNames(ActorGraph actorGraph, String fileName) {
        try (PrintWriter writer = new PrintWriter(new FileWriter(fileName))) {
            for (Map.Entry<String, Actor> entry : actorGraph.getActors().entrySet()) {
                writer.println(entry.getValue().getName());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}