public class helloworld implements Hello{
    @Override
    public void Hello(){
        System.out.print("Hello ");
    }
    @Override
    public void World(){
        System.out.println("world!");
    }
    public static void main(String[] args) {
        helloworld Helloworld = new helloworld();
        Helloworld.Hello();
        Helloworld.World();
    }
}
interface Hello{
    void Hello();
    void World();
}