#Create a prog of displaying questions to users like kbc
name=input("Enter your name=")
print(f"Welcome our brain testing calub Mr {name} \n!!")
questions = [
    "1. What is the worst-case time complexity of Quick Sort?",
    "2. Which data structure is used to implement recursion?",
    "3. Which algorithm finds the shortest path with non-negative edge weights?",
    "4. Which normal form removes transitive dependency?",
    "5. Which sorting algorithm guarantees O(n log n) worst-case complexity?",
    "6. Which data structure is commonly used to implement a priority queue?",
    "7. What does ACID stand for in DBMS?",
    "8. Which tree traversal gives sorted elements in a Binary Search Tree?",
    "9. What is the average-case time complexity of searching in a hash table?",
    "10. Which of the following is an NP-complete problem?"
]
options = [
    ["A) O(n)", "B) O(log n)", "C) O(n²)", "D) O(n log n)"],
    ["A) Queue", "B) Stack", "C) Heap", "D) Graph"],
    ["A) BFS", "B) DFS", "C) Dijkstra", "D) Prim"],
    ["A) 1NF", "B) 2NF", "C) 3NF", "D) 4NF"],
    ["A) Quick Sort", "B) Bubble Sort", "C) Merge Sort", "D) Selection Sort"],
    ["A) Stack", "B) Queue", "C) Heap", "D) Array"],
    ["A) Atomicity, Consistency, Isolation, Durability",
     "B) Accuracy, Control, Integrity, Data",
     "C) Access, Consistency, Isolation, Data",
     "D) Atomicity, Control, Integrity, Durability"],
    ["A) Preorder", "B) Postorder", "C) Inorder", "D) Level Order"],
    ["A) O(1)", "B) O(log n)", "C) O(n)", "D) O(n log n)"],
    ["A) Binary Search", "B) Sorting",
     "C) Travelling Salesman Decision Problem",
     "D) Finding Maximum"]
]
le=len(questions)
answers = [
    "C",
    "B",
    "C",
    "C",
    "C",
    "C",
    "A",
    "C",
    "A",
    "C"
]
score=0
for i in range(len(questions)):
    print(questions[i],"\n",options[i])
    ans=input("Ans=").upper()
    if(ans==answers[i]):
        score=score+1
print(f"Mr {name}, your score is {score}/{le}")
