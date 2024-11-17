import java.io.*;
import java.util.*;

public class ActorGraphUtil {
    public static void serializeActorGraph(ActorGraph actorGraph, String filePath) {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(filePath))) {
            oos.writeObject(actorGraph);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static ActorGraph deserializeActorGraph(String filePath) {
        ActorGraph actorGraph = null;
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(filePath))) {
            actorGraph = (ActorGraph) ois.readObject();
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
        return actorGraph;
    }

    public static void writeActorsToFile(List<Actor> actors, String filePath) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath))) {
            for (Actor actor : actors) {
                writer.write(actor.getName() + "\n");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}