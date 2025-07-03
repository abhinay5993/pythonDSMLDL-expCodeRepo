"""Experiments of List - Muteable data structure"""
mutLst = []
print("\nEnter List items : ");
print("\nType 'exit' to stop passing inputs..");
count=0;
while True:
      temp=input(f"\nEnter the {count+1} item : ");
      mutLst.append(temp);
      if mutLst[count]=='Exit' or mutLst[count]=='exit':
                                                  print("\nLast Items removed : ",mutLst.pop());
                                                  break;
      count=count+1;

print("\nUpdated Items of List : ",mutLst);
print("\nNumber of Items persent into List : ",len(mutLst));
numList=[45,30,-0.44435,39.45,-5.004];
print("\nNew Extended list : ",mutLst.extend(numList)," data items : ",mutLst);
print("\nLatest updated size/length of list : ",len(mutLst));
print("\nList reversal with slicing : ",mutLst[::-1]);
print("\nList reversal with slicing with 3-steps : ",mutLst[2:8:3]);
print("\nShowing list after clearning ",mutLst.clear()," updated listed items : ",mutLst);
