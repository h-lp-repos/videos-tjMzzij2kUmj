import json
import argparse

def stub_generator(prompt):
    return "This is a stub answer for prompt: " + prompt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, default="generate_output.json")
    args = parser.parse_args()

    data = json.load(open(args.input))
    results = []
    for item in data:
        prompt = item["query"] + " Docs: " + ", ".join(map(str, item.get("retrieved_doc_ids", [])))
        ans = stub_generator(prompt)
        results.append({"query": item["query"], "generated_answer": ans})
    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Generated answers saved to {args.output}")

if __name__ == "__main__":
    main()
