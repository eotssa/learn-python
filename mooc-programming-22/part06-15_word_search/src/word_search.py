def find_words(search_term: str):
    results = []
 
    with open("words.txt") as file:
        # Tätä tarvitaan myöhemmin
        hakusana_ilman_tahtea = search_term.replace("*","")
 
        for word in file:
            word = word.replace("\n","")
            # Is there an asterisk?
            if "*" in search_term:
                # start or end?
                if search_term[0] == "*":
                    if word.endswith(hakusana_ilman_tahtea):
                        results.append(word)
                else:
                    if word.startswith(hakusana_ilman_tahtea):
                        results.append(word)
            # Is there a dot?
            elif "." in search_term:
                # same length?
                if len(search_term) == len(word):
                    found = True
                    for i in range(len(search_term)):
                        if search_term[i] != "." and search_term[i] != word[i]:
                            found = False
                            break
                    if found:
                        results.append(word)
            # No special characters, only whole word matches count
            else:
                if word == search_term:
                    results.append(word)
    return results