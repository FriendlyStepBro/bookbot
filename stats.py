def get_num_words(text):
    return len(text.split())

def symbol_count(text):
    results = {}
    for symbol in text.lower():
        if symbol in results:
            results[symbol] += 1
        else:
            results[symbol] = 1
    return results

def dictionary_to_list(dictionary):
    result = []
    for key, value in dictionary.items():  # Iterate over key-value pairs
        result.append((key, value))  # Add the key-value pair as a set
    result.sort(key=lambda item:  item[1], reverse=True)
    return result