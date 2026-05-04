from app.graph import build_graph

graph = build_graph()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        result = graph.invoke({"input": user_input})
        print("Bot:", result["output"])
        
        
        
        