if __name__ == "__main__":
    dict = {
        "hello": "cześć",
        "world": "świat",
        "cruel": "okrutny",
        "university": "uniwersytet",
        "laptop": "laptop",
    }

    print(dict)
    dict["apple"] = "jabłko"
    print(dict)
    print(dict["hello"], dict["cruel"], dict["world"], "!")

    for k, v in dict.items():
        print(k, "->", v)
