def topic_explainer(abstract):
    return f"Summary: This paper discusses the main topic of '{abstract[:60]}...' (auto-summarized)."

def literature_finder(abstract):
    return (
        "Suggested Related Literature:\n"
        "- Paper A: Advances in the Main Topic\n"
        "- Paper B: Recent Trends and Challenges\n"
        "- Paper C: State of the Art Approaches"
    )

def gap_analyzer(abstract):
    return (
        "Identified Research Gaps:\n"
        "- Lack of focus on emerging methods\n"
        "- Limited discussion on applications in specific domains\n\n"
        "Suggested Paper Outline:\n"
        "1. Introduction\n2. Related Work\n3. Proposed Method\n4. Experiments or Discussion\n5. Conclusion\n6. Future Work"
    )

if __name__ == "__main__":
    user_abstract = input("Paste your research paper abstract: ")
    print("\n--- Topic Explainer ---")
    print(topic_explainer(user_abstract))
    print("\n--- Literature Finder ---")
    print(literature_finder(user_abstract))
    print("\n--- Gap Analyzer ---")
    print(gap_analyzer(user_abstract))
