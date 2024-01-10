import java.util.*;

class ConsoleDisplayController{
    private ArrayList<String> result;
    
    public void setContent (ArrayList<String>msg){
        this.result = msg;
    }
    
    public void display(){
        System.out.print(result.toString());
    }
}

class LengthAsStrategy{
    private Integer lengthChar;
    
    public void setLengthOfChar(Integer len){
        this.lengthChar = len;
    }
    
    public boolean invoke(String item){
        if(item.length()<lengthChar){
            return true;
        }
        return false;
    }
}

class StringListFilterController{
    LengthAsStrategy predicate = new LengthAsStrategy();
    public ArrayList<String> filter(ArrayList<String> strlist){
        ArrayList<String> filteredArr = new ArrayList<>();
        predicate.setLengthOfChar(6);
        for(String word:strlist){
            if(predicate.invoke(word))filteredArr.add(word);
        }
        return filteredArr;
    }
}

public class Main{
    public static void main(String args[]){
        ArrayList<String> arr = new ArrayList<>();
        
        arr.add("one");
        arr.add("two");
        arr.add("three");
        StringListFilterController stringListFilterControllerObj = new StringListFilterController();
        ArrayList<String> filteredArray = stringListFilterControllerObj.filter(arr);
      
        ConsoleDisplayController consoleDisplayControllerObj = new ConsoleDisplayController();
        consoleDisplayControllerObj.setContent(filteredArray);
        consoleDisplayControllerObj.display();
        
    }
}
